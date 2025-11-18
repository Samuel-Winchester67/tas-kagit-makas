#make the starting page donee
#make the main game page soon




import random
import customtkinter as ctk
from customtkinter import CTkButton, CTkLabel


def game():

    app=ctk.CTk()
    app.title("Number Guess Game")
    app.geometry("400x400")


    def quit_the_game():
        app.destroy()


    def return_to_main():
        for widget in app.winfo_children():
            widget.destroy()
        main()



    def game_page():
        for widget in app.winfo_children():
            widget.destroy()

        the_secret=random.randint(1,100)
        chance=10


        test=CTkButton(app,text="⬅️ Return",fg_color="green",command=return_to_main)
        test.place(x=0,y=0)

        label1=ctk.CTkLabel(app,text="Guess The Number",font=("Arial",25,"bold"),text_color="#708090")
        label1.place(x=90,y=40)

        label2=ctk.CTkLabel(app,text="Between 1 to 100",font=("Arial",16,"bold"),text_color="#708090")
        label2.place(x=140,y=70)

        label3=ctk.CTkLabel(app,text=f"Chances Left: {chance}",font=("Arial",16,"bold"),text_color="red")
        label3.place(x=150,y=120)

        label_fedback=CTkLabel(app,text="",font=("Arial",20,"bold"),text_color="#708090")


        label4=ctk.CTkLabel(app,text="Enter a lower\nnumber",font=("Arial",30,"bold"),text_color="#00CCCC")
        label4.place(x=110,y=175)


        entry=ctk.CTkEntry(app,width=240)
        entry.place(x=90,y=260)
        guess=entry.get()





        button_check=CTkButton(app,text="Check",width=240,fg_color="green")
        button_check.place(x=90,y=300)

        button_reset=CTkButton(app,text="Reset",width=240,fg_color="red")
        button_reset.place(x=90,y=340)


    def main():

        welcome_label=ctk.CTkLabel(app,text="welcome",font=("Arial",35),text_color="white")
        welcome_label.place(x=130,y=10)

        box_label=ctk.CTkLabel(app,text="Enter a Level ",font=("Arial",12),text_color="white")
        box_label.place(x=130,y=90)

        start=ctk.CTkButton(app,text="Start",font=("Arial",12),text_color="white",fg_color="green",command=lambda :game_page())
        start.place(x=130,y=170)
        quit=ctk.CTkButton(app,text="Quit",font=("Arial",12),text_color="white",fg_color="red",command=lambda :quit_the_game())
        quit.place(x=130,y=210)

        levels=["easy","medium","hard","impossible"]
        box=ctk.CTkComboBox(app,values=levels,font=("Arial",20),text_color="white",button_color="cyan")
        box.place(x=130,y=120)
        if levels== "easy":
            chance=-5
        elif levels== "medium":
            chance=7
        elif levels== "hard":
            chance=5
        elif levels== "impossible":
            chance=3



    main()

    app.mainloop()
game()
