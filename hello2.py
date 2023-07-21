from datetime import datetime 
from tkinter import *



def milyennapvan():
    """ Ez a fügyvény megállapítja, hogy hány óra van és milyen nap van. Mindezt magyarul. """
    global formatted_time, current_weekday
    
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    weekday_number = current_date.weekday()

    weekdays_hu = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

    current_weekday = weekdays_hu[weekday_number]
    formatted_time = int(current_time.strftime("%H"))


def koszontes():
    """ A fügvény napszaknak megfelelő köszöntés ír ki!"""
    global image_path, current_imag

    if formatted_time < 10: 
        greeting.set('Jó reggelt!')
        greetplus.set("Ez egy szép %s lesz." % current_weekday)
        image_path = "./img/1.gif"
        
    elif 10 <= formatted_time < 18:
        greeting.set("Jónapot kívánok!")
        greetplus.set("Ez egy lehetőségekkel teli %s ." % current_weekday)
        image_path = "./img/2.gif"
    else:
        greeting.set("Jó estét!")
        greetplus.set("Ez egy remek %s volt!" % current_weekday)
        image_path = "./img/3.gif"

    current_image = PhotoImage(file=image_path)  # PhotoImage objektum létrehozása
    img.configure(image=current_image)
    img.image = current_image


root = Tk()
root.title("Köszöntés")
root.configure(background="#14213d")
root.minsize(300, 300)
root.resizable(False, False)

#greeting
greeting = StringVar()
greeting_label = Label(root, textvariable=greeting, bg="#14213d", fg="#fca311", font=("Arial", 20))
greeting_label.pack(pady=(60,10))

#greetplus 
greetplus = StringVar()
greetplus_label = Label(root, textvariable=greetplus, bg="#14213d", fg="#fca311", font=("Arial", 12))
greetplus_label.pack(pady=(0,10))


#kép
current_image = PhotoImage(file="./img/1.gif")  # alapértelmezett kép
img = Label(root, image=current_image, borderwidth=0)
img.pack(pady=(0,10))


    
milyennapvan()

koszontes()

root.mainloop()
