print("welcome to Ngaew grocery")
vaseline=65
lipoil=229
keyboard=550


Username= input("enter your username :")
Password = input("enter your password :")


if Username=="c":
     if Password != "j":
        print("try again")



     else:
        print("enjoy your shopping")
        print("welcome to Ngaew grocery")
        print("vaseline : 65 THB,","lip oil : 229 THB,","keyboard : 550 THB,","perfume : 480 THB")
        yourbasket1 = (input("my basket lists :"))
        piece=int(input("piece="))
        if yourbasket1=="vaseline":
            print("vaseline",vaseline*piece,"THB")
        elif yourbasket1=="lipoil":
            print("lip oil", lipoil, "THB")
            print("lip oil", lipoil * piece, "THB")
        elif yourbasket1=="keyboard":
            print("keyboard",keyboard,"THB")
            print("keyboard", keyboard * piece, "THB")

else:
    print("try again")
