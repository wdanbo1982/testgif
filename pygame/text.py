# ~ while True:  #while为真进入死循环
    # ~ pizza = input("请输入比萨配料：")
    # ~ if pizza != "quit" :
      # ~ print(pizza)  
      
    # ~ elif pizza == "quit":
        # ~ break  #跳出死循环

boolean = True    
while boolean:
    pizza = input("请输入比萨配料：")
    if pizza != "quit" :
      print(pizza)  
      
    elif pizza == "quit":
        boolean = False
