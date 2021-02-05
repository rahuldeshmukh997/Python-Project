class Meal:
    bill=0
    def veg(s):
        print("----------Veg-Menu------------ ")
        print("Code \t Menu \t \t Price")
        print("a. \t Vada Pav \t 10Rs.")
        print("b. \t Medu Wada \t 20Rs.")
        print("c. \t Idli \t \t 30Rs.")
        print("------------------------------")

    def nonveg(s):
        print("-------------NonVeg-Menu--------------")
        print("Code \t Menu \t \t \t Price")
        print("d. \t Chicken Tandoori \t 40Rs.")
        print("e. \t Fish Curry \t \t 50Rs.")
        print("f. \t Chicken Biryani \t 60Rs.")
        print("--------------------------------------")

    def menu(s):
        i = int (input ("Enter ' 1 ' for Veg and ' 2 ' for Non-Veg and zero(' 0 ') for exit: "))
        while i!= 0:
            if i == 1:
                s.veg()
                sel = input ("You ask for Veg Menu please enter ' Y ' to proceed: ")
                while(sel == 'y' or sel=='Y'):
                    order = input ("Enter code of the food you wish to order: ")
                    if order == 'a':
                        print("You have selected ' Vada Pav '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*10)
                        i=0
                        
                    elif order == 'b':
                        print("You have selected ' Medu Wada '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*20)
                        i=0
                    elif order == 'c':
                        print("You have selected ' Idli '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*30)
                        i=0
                    else:
                        print("You may be selected Non-Veg menu code or may be it's invalid.")
                    sel =(input("If you want Re-Order then press ' 1 ' if no then press ' 0 ' : "))
                    if sel == '1':    
                        i=0
                        s.menu()
                        
                    else:
                        i=0
            elif i == 2:
                s.nonveg()
                sel = input ("You ask for Non-Veg Menu please enter ' Y ' to proceed: ")
                while(sel == 'y'):
                    order = input ("Enter code of the food you wish to order: ")
                    if order == 'd':
                        print("You have selected ' Chicken Tandoori '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*40)
                        i=0
                        
                    elif order == 'e':
                        print("You have selected ' Fish Curry '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*50)
                        i=0
                    elif order == 'f':
                        print("You have selected ' Chicken Biryani '")
                        qty=int(input("Enter Quantity: "))
                        s.bill = s.bill + (qty*60)
                        i=0
                    else:
                        print("You may be selected Veg menu code or may be it's invalid.")
                    sel =  (input("If you want Re-Order then press ' 1 ' if no then press ' 0 ' : "))
                    if sel == 1:
                        i=0
                        s.menu()
                    else:
                        i=0
            else:
                print("You may be selected wrong menu code. Please Select Correct Options")
                s.menu()
        i=0       
    def totalBill(s):
        print("Your Total Bill Is : ",s.bill)
        print("Thank You ! Enjoy Your Meal !")
                                   
m=Meal()
m.menu()
m.totalBill()
