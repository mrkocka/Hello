from datetime import datetime 
from tkinter import *

root = Tk()
root.title("Köszöntés")
root.configure(background="#14213d")
root.minsize(400, 400)

#cimke
text = Label(root, text="Nothing will work unless you do.", bg="#14213d", fg="#fca311", font=("Arial", 15))
text.pack(pady=(60,10))
text2 = Label(root, text="- Maya Angelou", bg="#14213d", fg="#fca311", font=("Arial", 15))
text2.pack(pady=(0,10))

#kép
image = PhotoImage(file="./img/1.gif")
img = Label(root, image=image, borderwidth=0)
img.pack()
root.mainloop()

root.mainloop()




def milyennapvan():
    global formatted_time, current_weekday

    """ Ez a fügyvény megállapítja, hogy hány óra van és milyen nap van. Mindezt magyarul. """
    current_time = datetime.now().time()
    
    current_date = datetime.now().date()
    weekday_number = current_date.weekday()

    weekdays_hu = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

    current_weekday = weekdays_hu[weekday_number]
    formatted_time = int(current_time.strftime("%H"))


def koszontes():
    """ A fügvény napszaknak megfelelő köszöntés ír ki!"""
   
    if formatted_time < 10: 
        print('Jó reggelt')
        print("Ez egy szép %s lesz." % current_weekday)
    elif 10 <= formatted_time < 18:
        print("Jónapot kívánok!")
        print("Ez egy szép lehetőségekkel teli %s ." % current_weekday)
    else: 
        print("Jó estét!")
        print("Ez egy remek °s volt!" % current_weekday)

    
milyennapvan()

koszontes()

