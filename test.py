# box=[]
# x=input("enter your name")
#
# box.append(x)
# print(box)
#
# #append= single
# #extend=multi
import random


tas_kagit_makas=["tas","kagit","makas"]
print("Enter tas kagit or makas for play ")
the_start=input("")
comp= random.choice(tas_kagit_makas)
print(f"computer choiced : {comp}")



if the_start==comp:

    print("berabere")

elif the_start=="tas" and comp=="makas" or the_start=="makas" and comp=="kagit" or the_start=="kagit" and comp=="tas":
     print("good 👌 ")

elif the_start=="makas" and comp=="tas" or the_start=="kagit" and comp=="makas" or the_start=="tas" and comp=="kagit":
    print(" easy for computer  🙆‍♂️")
else:
     print("error")


