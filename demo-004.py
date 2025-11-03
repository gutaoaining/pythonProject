# 作者：顾涛
# 创建时间：2025/1/26
price = float(input("请输入本次的购买商品总价格："))
flag = input("你是会员么？")
if flag == 'Y':
    if price >= 200:
        print("本次打75折! 打完折扣价格为：", price * 0.75)
    elif 200 > price >= 100:
        print("本次打8折！打完折扣价格为：", price * 0.8)
    elif 0 < price < 100:
        print("低于100不打折！你应该付款：", price)
    else:
        print("你输入的金额有问题！你的输入为：", price)
else:
    if price >= 200:
        print("你不是会员！你本次打9折！打完折后价格为：", price * 0.9)
    elif 100 <= price < 200:
        print("你不是会员！你本次打95折！打完折后价格为：", price * 0.95)
    elif 0 < price < 100:
        print("你不是会员！低于100不打折！你应该付款：", price)
    else:
        print("你不是会员！你输入的金额有误！你输入的价格为：", price)
