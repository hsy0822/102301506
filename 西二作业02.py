#6.设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。
# 具有的 公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，
# 计算已售出 商品价值income，修改商品信息的函数setdata

class Product:
    #初始化商品信息
    def __init__(self, id, name, price, total_amount, remaining_amount):
        self.id = id
        self.name =name
        self.price = price
        self.total_amount = total_amount
        self.remaining_amount = remaining_amount

    #显示商品信息
    def display(self):
        print("商品序号:", self.id)
        print("商品名:", self.name)
        print("单价:", self.price)
        print("总数量:", self.total_amount)
        print("剩余数量:", self.remaining_amount)

    #计算已售出商品价值
    def income(self):
        return self.price * (self.total_amount - self.remaining_amount)

    #修改商品信息
    def setdata(self, id, name, price, total_amount, remaining_amount):
        self.id = id
        self.name = name
        self.price = price
        self.total_amount = total_amount
        self.remaining_amount = remaining_amount

# 创建一个商品对象
product = Product(1, "《摆烂的艺术》", 20, 100, 50)

# 显示商品信息
product.display()

# 计算已售出商品价值
solded= product.income()
print(f"{product.name}已经售出的价值:", solded)

# 修改商品信息
product.setdata(1, "《摆烂的艺术2》", 30, 100, 30)