import time
import random
def coffee_machine():
    coffe_requrments=[{'espresso':20},{'latte':40}]
    sugar=10
    latte_price=coffe_requrments[1]['latte']
    espresso_price=coffe_requrments[0]['espresso']

    lucky_spin=["in another time inchallah","oh my god sir you won a free coffee from digarto coffee"]
    name=input("what is your name ? ").lower()
    print("welcome " + name)
    print(f"latte is for {latte_price}$ \nespresso is for {espresso_price}$")
    wanted: str=input("winch coffe you want? espresso/latte\n").lower()
    if wanted == "i dont have enough money":
        lucky_coustmer=random.choice(lucky_spin)
        print(lucky_coustmer)
        return





    def preapering():
        print("wait 5 seconds...")
        time.sleep(5)
        print(f"{name} your coffe is ready 🍵")



    if wanted == "latte":
         print(f"latte is {latte_price}$")
         ask_for_sugar=input("sugar? +10$ ").lower()
         if ask_for_sugar == "yes":
             print("total price is $",latte_price+sugar)
         input("press enter to continue")
         preapering()



    elif wanted == 'espresso':
         print(f"espresso is {espresso_price}$")
         ask_sugar=input("you wanna sugar in ? +10$ ").lower()
         if ask_sugar=="yes":
             print("total price is $",sugar + espresso_price)
         input("press enter to continue")
         preapering()

    else:
        if wanted != "espresso" and wanted != "latte" and wanted != "i dont have enough money":
            print("please enter a word in menu!")

coffee_machine()







