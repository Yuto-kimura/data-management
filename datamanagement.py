class MenuItem2:
    def hello(self):
        print("Hello,"+self.name+"!")


menu_item2 = MenuItem2()
print("What is your name?")
menu_item2.name = input(">")
menu_item2.hello()
