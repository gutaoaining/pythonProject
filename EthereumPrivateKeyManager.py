# 作者：顾涛
# 创建时间：2025/11/3
import json
import os
from eth_account import Account
from web3 import Web3


def find_and_decrypt_keystore(keystore_dir, target_address, password=""):
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
    print(f"📁 密钥库目录: {keystore_dir}")

    if not os.path.exists(keystore_dir):
        print(f"❌ 密钥库目录不存在: {keystore_dir}")
        return None

    # 列出所有密钥库文件
    keystore_files = [f for f in os.listdir(keystore_dir)]
    print(f"找到 {len(keystore_files)} 个密钥库文件")

    for filename in keystore_files:
        file_path = os.path.join(keystore_dir, filename)

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
            return decrypt_keystore_file(file_path, password)

    print(f"❌ 未找到地址 0x{target_address} 对应的密钥库文件")
    return None


def decrypt_keystore_directory(keystore_dir, password=""):
    """解密整个密钥库目录"""
    print(f"🔐 解密密钥库目录: {keystore_dir}")
    print("=" * 60)

    if not os.path.exists(keystore_dir):
        print(f"❌ 目录不存在: {keystore_dir}")
        return {}

    private_keys = {}

    # 遍历所有密钥库文件
    for filename in os.listdir(keystore_dir):
        file_path = os.path.join(keystore_dir, filename)
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

def decrypt_keystore_file(file_path, password=""):
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


def backup_all_private_keys(keystore_dir, output_file="private_keys_backup.json"):
    """备份所有账户的私钥"""
    private_keys = {}

    for filename in os.listdir(keystore_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(keystore_dir, filename)

            # 从文件名获取地址
            address = "0x" + filename.split('--')[-1].replace('.json', '')

            print(f"处理: {address}")

            # 尝试解密（先试空密码，再试常见密码）
            private_key = None
            for password in ["", "password", "1234", "test"]:
                try:
                    with open(file_path, 'r') as f:
                        keystore = json.load(f)
                    private_key_bytes = Account.decrypt(keystore, password)
                    private_key = "0x" + private_key_bytes.hex()

                    # 验证
                    account = Account.from_key(private_key)
                    if account.address.lower() == address.lower():
                        print(f"  ✅ 解密成功 (密码: '{password}')")
                        break
                    else:
                        private_key = None
                except:
                    continue

            if private_key:
                private_keys[address] = private_key
            else:
                print(f"  ❌ 解密失败")

    # 保存到文件
    with open(output_file, 'w') as f:
        json.dump(private_keys, f, indent=2)

    print(f"\n💾 已备份 {len(private_keys)} 个私钥到: {output_file}")
    return private_keys


# 使用示例
if __name__ == "__main__":
    keystore_dir = "/Users/gutao/web3_project/myChain/data/keystore"
    decrypt_keystore_directory(keystore_dir,"123456")
    # target_address = "5fFdea11673c3f86096F83814B38125793c9F336"
    #
    # print("=" * 60)
    # print("🔐 以太坊私钥提取工具")
    # print("=" * 60)
    #
    # # 提取指定地址的私钥
    # private_key = find_and_decrypt_keystore(keystore_dir, target_address, "123456")
    #
    # if private_key:
    #     print(f"\n🎉 成功获取私钥!")
    #     print(f"私钥: {private_key}")
    #
    #     # 验证私钥
    #     from web3 import Web3
    #
    #     account = Web3().eth.account.from_key(private_key)
    #     print(f"验证地址: {account.address}")
    # else:
    #     print(f"\n😞 未能获取私钥")
    #
    #     # 尝试备份所有账户
    #     print("\n" + "=" * 60)
    #     print("🔄 尝试备份所有账户...")
    #     all_keys = backup_all_private_keys(keystore_dir)
    #
    #     if target_address.lower() in [addr.lower() for addr in all_keys.keys()]:
    #         print(f"\n✅ 在备份中找到目标地址!")
    #         for addr, key in all_keys.items():
    #             if addr.lower() == target_address.lower():
    #                 print(f"私钥: {key}")