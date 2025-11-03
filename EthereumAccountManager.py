# 作者：顾涛
# 创建时间：2025/11/3
# time: 2025/10/1611:56

from web3 import Web3
import json
import os
import getpass
from datetime import datetime
from eth_account import Account


class EthereumAccountManager:
    def __init__(self, rpc_url="http://127.0.0.1:8545", datadir="/Users/gutao/web3_project/myChain/data"):
        self.rpc_url = rpc_url
        self.datadir = datadir
        self.keystore_dir = os.path.join(datadir, "keystore")
        self.w3 = None
        self.connect_to_node()

    def connect_to_node(self):
        """连接到Geth节点"""
        try:
            self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
            if self.w3.is_connected():
                print(f"✓ 成功连接到 Geth 节点: {self.rpc_url}")
                print(f"当前区块: {self.w3.eth.block_number}")
                print(f"节点信息: {self.w3.client_version}")
            else:
                print("✗ 无法连接到 Geth 节点")
                return False
        except Exception as e:
            print(f"✗ 连接失败: {e}")
            return False
        return True

    def create_account(self, password=None):
        """创建新的以太坊账户"""
        try:
            # 生成新账户
            account = self.w3.eth.account.create()

            print("\n=== 新账户创建成功 ===")
            print(f"地址: {account.address}")
            print(f"私钥: {account.key.hex()}")

            # 如果提供了密码，创建加密的keystore
            if password:
                encrypted = account.encrypt(password)

                # 确保keystore目录存在
                os.makedirs(self.keystore_dir, exist_ok=True)

                # 生成标准文件名
                timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S.%fZ')[:-3] + 'Z'
                filename = f"UTC--{timestamp}--{account.address[2:]}"
                filepath = os.path.join(self.keystore_dir, filename)

                # 保存keystore文件
                with open(filepath, 'w') as f:
                    json.dump(encrypted, f, indent=2)

                print(f"✓ Keystore 文件已保存: {filepath}")

            return account

        except Exception as e:
            print(f"✗ 创建账户失败: {e}")
            return None

    def list_accounts(self):
        """列出所有账户及其余额"""
        try:
            # 从keystore目录读取账户
            accounts_from_files = []
            if os.path.exists(self.keystore_dir):
                for filename in os.listdir(self.keystore_dir):
                    if filename.startswith("UTC--"):
                        address = "0x" + filename.split("--")[2]
                        checksum_address = Web3.to_checksum_address(address)
                        accounts_from_files.append(checksum_address)

            print("\n=== 本地账户列表 ===")
            for i, addr in enumerate(accounts_from_files):
                try:
                    balance_wei = self.w3.eth.get_balance(addr)
                    balance_eth = self.w3.from_wei(balance_wei, 'ether')
                    print(f"{i + 1}. {addr}")
                    print(f"   余额: {balance_eth} ETH")
                    print(f"   交易数: {self.w3.eth.get_transaction_count(addr)}")
                except Exception as e:
                    print(f"{i + 1}. {addr} [查询失败: {e}]")

            return accounts_from_files

        except Exception as e:
            print(f"✗ 获取账户列表失败: {e}")
            return []

    def get_account_balance(self, address):
        """获取指定账户余额"""
        try:
            balance_wei = self.w3.eth.get_balance(address)
            balance_eth = self.w3.from_wei(balance_wei, 'ether')
            print(f"账户 {address}:")
            print(f"  余额: {balance_eth} ETH")
            print(f"  余额(Wei): {balance_wei}")
            return balance_eth
        except Exception as e:
            print(f"✗ 获取余额失败: {e}")
            return 0

    def send_transaction(self, from_address, to_address, amount_eth, private_key=None):
        """发送交易"""
        try:
            # 转换金额
            amount_wei = self.w3.to_wei(amount_eth, 'ether')

            # 获取nonce
            nonce = self.w3.eth.get_transaction_count(from_address)

            # 获取gas价格
            gas_price = self.w3.eth.gas_price

            # 构建交易
            transaction = {
                'to': to_address,
                'value': amount_wei,
                'gas': 21000,  # 标准转账gas limit
                'gasPrice': gas_price,
                'nonce': nonce,
                'chainId': 12345  # 你的私有链ID
            }

            # 如果有私钥，直接签名
            if private_key:
                signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key)
                tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            else:
                # 如果没有私钥，尝试使用节点解锁的账户
                transaction['from'] = from_address
                tx_hash = self.w3.eth.send_transaction(transaction)

            print(f"✓ 交易已发送，哈希: {tx_hash.hex()}")

            # 等待交易确认
            print("等待交易确认...")
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)

            if receipt.status == 1:
                print("✓ 交易确认成功!")
                print(f"区块: {receipt.blockNumber}")
                print(f"Gas 使用量: {receipt.gasUsed}")
            else:
                print("✗ 交易失败!")

            return receipt

        except Exception as e:
            print(f"✗ 发送交易失败: {e}")
            return None

    def get_node_info(self):
        """获取节点信息"""
        try:
            print("\n=== 节点信息 ===")
            print(f"当前区块: {self.w3.eth.block_number}")
            print(f"Gas 价格: {self.w3.from_wei(self.w3.eth.gas_price, 'gwei')} Gwei")
            print(f"同步状态: {self.w3.eth.syncing}")
            print(f"对等节点数: {self.w3.net.peer_count}")

            # 尝试获取最新区块信息
            latest_block = self.w3.eth.get_block('latest')
            print(f"最新区块时间: {datetime.fromtimestamp(latest_block.timestamp)}")

        except Exception as e:
            print(f"获取节点信息失败: {e}")

    def import_private_key(self, private_key, password=None):
        """导入私钥"""
        try:
            # 从私钥创建账户
            account = self.w3.eth.account.from_key(private_key)
            print(f"导入账户: {account.address}")

            # 如果提供了密码，保存keystore
            if password:
                encrypted = account.encrypt(password)
                os.makedirs(self.keystore_dir, exist_ok=True)

                timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S.%fZ')[:-3] + 'Z'
                filename = f"UTC--{timestamp}--{account.address[2:]}"
                filepath = os.path.join(self.keystore_dir, filename)

                with open(filepath, 'w') as f:
                    json.dump(encrypted, f, indent=2)

                print(f"✓ Keystore 文件已保存: {filepath}")

            return account

        except Exception as e:
            print(f"✗ 导入私钥失败: {e}")
            return None


    def exportPrivateKeyByPublicKey(self, target_address, password):
        """
            在密钥库目录中查找指定地址并解密私钥

            参数:
                keystore_dir: 密钥库目录路径
                target_address: 目标以太坊地址
                password: 密码（开发者模式通常为空）
            """

        # 标准化目标地址格式
        target_address = target_address.lower().replace('0x', '')
        print(f"🔍 寻找地址: 0x{target_address}")
        print(f"📁 密钥库目录: {self.keystore_dir }")

        if not os.path.exists(self.keystore_dir ):
            print(f"❌ 密钥库目录不存在: {self.keystore_dir }")
            return None

        # 列出所有密钥库文件
        keystore_files = [f for f in os.listdir(self.keystore_dir )]
        print(f"找到 {len(keystore_files)} 个密钥库文件")

        for filename in keystore_files:
            file_path = os.path.join(self.keystore_dir , filename)

            # 方法1: 从文件名中提取地址
            file_address = filename.split('--')[-1].replace('.json', '').lower()

            # 方法2: 从文件内容中提取地址
            try:
                with open(file_path, 'r') as f:
                    keystore_data = json.load(f)
                content_address = keystore_data.get('address', '').lower().replace('0x', '')
            except:
                content_address = ""

            # 检查是否匹配目标地址
            if target_address in [file_address, content_address]:
                print(f"✅ 找到匹配的密钥库文件: {filename}")
                return self.decrypt_keystore_file(file_path, password)

        print(f"❌ 未找到地址 0x{target_address} 对应的密钥库文件")
        return None

    def decrypt_keystore_file(selt,file_path, password=""):
        """解密单个密钥库文件"""
        try:
            with open(file_path, 'r') as f:
                keystore = json.load(f)

            print("🔓 尝试解密...")

            # 尝试使用空密码（开发者模式）
            private_key_bytes = Account.decrypt(keystore, password)
            private_key_hex = private_key_bytes.hex()

            # 验证私钥
            account = Account.from_key(private_key_hex)
            print(f"✅ 解密成功!")
            print(f"📬 账户地址: {account.address}")
            print(f"🔑 私钥: 0x{private_key_hex}")

            return f"0x{private_key_hex}"

        except Exception as e:
            print(f"❌ 解密失败: {e}")

            # 如果空密码失败，尝试常见测试密码
            test_passwords = ["", "password", "1234", "test"]
            for test_pwd in test_passwords:
                if test_pwd == password:  # 跳过已尝试的密码
                    continue
                try:
                    private_key_bytes = Account.decrypt(keystore, test_pwd)
                    private_key_hex = private_key_bytes.hex()
                    account = Account.from_key(private_key_hex)
                    print(f"✅ 使用密码 '{test_pwd}' 解密成功!")
                    print(f"🔑 私钥: 0x{private_key_hex}")
                    return f"0x{private_key_hex}"
                except:
                    continue

            print("💡 提示: 尝试手动输入密码")
            return None

    def decrypt_keystore_directory(self, password=""):
        """解密整个密钥库目录"""
        print(f"🔐 解密密钥库目录: {self.keystore_dir}")
        print("=" * 60)

        if not os.path.exists(self.keystore_dir):
            print(f"❌ 目录不存在: {self.keystore_dir}")
            return {}

        private_keys = {}

        # 遍历所有密钥库文件
        for filename in os.listdir(self.keystore_dir):
            file_path = os.path.join(self.keystore_dir, filename)
            print(f"处理文件: {filename}")

            try:
                # 读取密钥库文件
                with open(file_path, 'r') as f:
                    keystore = json.load(f)

                # 获取地址
                address = keystore.get('address', '')
                if not address:
                    # 有些版本地址在文件名中
                    address = filename.split('--')[-1]

                # 尝试解密（开发者模式通常空密码）
                private_key_bytes = Account.decrypt(keystore, password)
                private_key_hex = private_key_bytes.hex()

                # 验证地址
                account = Account.from_key(private_key_hex)
                real_address = Web3.to_checksum_address(address)

                if account.address.lower() == real_address.lower():
                    private_keys[address] = private_key_hex
                    print(f"✅ 成功解密: {account.address}")
                    print(f"   私钥: 0x{private_key_hex}")
                else:
                    print(f"⚠️  地址不匹配: {account.address}")

            except Exception as e:
                print(f"❌ 解密失败: {e}")

            print("-" * 40)

        return private_keys



def main():
    # 初始化账户管理器
    manager = EthereumAccountManager()

    if not manager.w3:
        print("请确保Geth节点正在运行，然后重试")
        return

    while True:
        print("\n" + "=" * 50)
        print("         以太坊账户管理器 (PoS 版本)")
        print("=" * 50)
        print("1. 创建新账户")
        print("2. 列出所有账户及余额")
        print("3. 查询账户余额")
        print("4. 发送测试交易")
        print("5. 导入私钥")
        print("6. 查看节点信息")
        print("7. 查看指定账户私钥")
        print("8. 查看是有账户的私钥")
        print("0. 退出")
        print("-" * 50)

        try:
            choice = input("请选择操作 [0-9]: ").strip()

            if choice == '1':
                print("\n创建新账户:")
                password = getpass.getpass("输入密码 (可选，直接回车跳过): ")
                if password == '':
                    password = None
                manager.create_account(password)
            elif choice == '2':
                manager.list_accounts()

            elif choice == '3':
                address = input("输入要查询的地址: ").strip()
                if Web3.is_address(address):
                    manager.get_account_balance(address)
                else:
                    print("无效的地址格式")
            elif choice == '4':
                print("\n发送测试交易:")
                from_addr = input("发送方地址: ").strip()
                to_addr = input("接收方地址: ").strip()
                amount = input("金额 (ETH): ").strip()

                if Web3.is_address(from_addr) and Web3.is_address(to_addr):
                    try:
                        amount_float = float(amount)
                        # 询问是否使用私钥签名
                        use_private_key = input("使用私钥签名? (y/N): ").strip().lower()
                        private_key = None
                        if use_private_key == 'y':
                            private_key = getpass.getpass("输入私钥: ")

                        manager.send_transaction(from_addr, to_addr, amount_float, private_key)
                    except ValueError:
                        print("无效的金额格式")
                else:
                    print("无效的地址格式")

            elif choice == '5':
                print("\n导入私钥:")
                private_key = getpass.getpass("输入私钥: ")
                password = getpass.getpass("输入密码 (可选，直接回车跳过): ")
                if password == '':
                    password = None
                manager.import_private_key(private_key, password)

            elif choice == '6':
                manager.get_node_info()

            elif choice == '7':
                print("\n输入需要查询的公钥:")
                private_key = getpass.getpass("输入公钥: ")
                if private_key == '':
                    print("\n输入为空,请重试输入！")
                else:
                    manager.exportPrivateKeyByPublicKey(private_key, "123456")
            elif choice == '8':
                manager.decrypt_keystore_directory("123456")

            elif choice == '0':
                print("退出程序")
                break
            else:
                print("无效选择，请重新输入")

        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            break
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    # 检查依赖
    try:
        import web3
    except ImportError:
        print("请先安装 web3.py: pip install web3")
        exit(1)

    main()

    # address = "0x7AdFDB5074704165265C6B443Ec3A64591F05b24"
    #
    # # 转换为校验和地址
    # checksum_address = Web3.to_checksum_address(address)
    # print(checksum_address)