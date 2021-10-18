from termcolor import colored
class product:
    def __init__(self,name,code,price):
        self.name=name
        self.code=code
        self.price=price
class store:
    def __init__(self):
        self.product_list=[]
        self.cart=[]
    def add(self,Product):
        self.product_list.append(Product)
    def dislpay(self):
        for i in range(1):
            print("product name\tproduct code\tprice")
        for product in self.product_list:
            print(f"{product.name}\t\t\t\t{product.code}\t\t\tRs.{product.price}")
    def adding(self,product):
        for item in self.product_list:
            if item.code == product:
                self.cart.append(item)
    def remove(self,product):
        for item in self.cart:
            if item.code==product:
                self.cart.remove(item)
    def see_cart(self):
        for items in self.cart:
            print(colored(f"{items.name}",attrs=['bold']))
    def bill(self):
        amount=0
        for product in self.cart:
            amount+=product.price
        for i in range(1):
            print("product name\tproduct code\tprice")
        for product in self.cart:
            print(f"{product.name}\t\t\t\t{product.code}\t\t\tRs.{product.price}")
        print("Final billig amount is Rs.",amount)
s=store()
s.add(product("wheat",1,33))
s.add(product("meat",2,233))
s.add(product("milk",3,50))
s.add(product("biskut",4,10))

while (True):

    print("To display products type 1")

    print("To add product in cart  type 2")

    print("To remove product from cart type 3")


    print("To display products in cart type 4")
    print("To display final bill 5")
    user = int(input("enter your choice"))
    if user==1:
        s.dislpay()
    elif user==2:
        c=int(input("enter product code"))
        s.adding(c)
    elif user==3:
        c=int(input("enter product code"))

        s.remove(c)
    elif user==4:
        s.see_cart()
    elif user==5:
        s.bill()
        break
