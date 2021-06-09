from parkomat import Parkomat
from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import Spinbox

# tworzenia okna

okno = Tk()
okno.geometry('500x600')
okno.title("Parkomat")
tytul = Label(okno, text="PARKOMAT", font=("Times New Roman", "21"), foreground="grey").grid(column=1, row=1)
p = Parkomat()

def liczba_monet(przycisk_monety):
    return liczba_monet_spinbox.get()

# przyciski dodawania monet
przycisk1gr= Button(okno, text="1gr", height=3, width=12, foreground="black",
                    command=lambda: [p.add_coin(0.01, liczba_monet(liczba_monet_spinbox)),
                                     datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=300)

przycisk2gr = Button(okno, text="2gr", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(0.02, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=300)

przycisk5gr = Button(okno, text="5gr", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(0.05, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=300)

przycisk10gr = Button(okno, text="10gr", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(0.1, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=350)

przycisk20gr = Button(okno, text="20gr", height=3, width=12,  foreground="black",
                      command=lambda: [p.add_coin(0.2, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=350)

przycisk50gr = Button(okno, text="50gr", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(0.5, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=350)

przycisk1zl = Button(okno, text="1zł", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(1, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=400)

przycisk2zl= Button(okno, text="2zł", height=3, width=12, foreground="black",
                    command=lambda: [p.add_coin(2, liczba_monet(liczba_monet_spinbox)),
                                     datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=400)

przycisk5zl = Button(okno, text="5zł", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(5, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=400)


przycisk10zl = Button(okno, text="10zł", height=3, width=12,  foreground="black",
                      command=lambda: [p.add_coin(10, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=450)

przycisk20zl = Button(okno, text="20zł", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(20, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=450)

przycisk50zl = Button(okno, text="50zł", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(50, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=450)


# oprogramowanie przycisku zatwierdz
def zatwierdz_rejestracje():
    okno.rejestracja = ''
    setattr(okno, 'rejestracja', wpisywanie_rejestracji.get(1.0, END))
    numer_rej =p.get_license_plate(okno.rejestracja)
    Label(okno, text=p.get_license_plate(okno.rejestracja)).place(x=300, y=205)
    return numer_rej


# Przycisk zatwierdz
zatwierdz_przycisk = Button(okno, text="Zatwierdź", height=3, width=43, foreground="black",
                            command=lambda: [zatwierdz_rejestracje()]).place(x=20, y=500)

# miejsce na wpisanie rejestracji
Label(okno, text="Nr rejestracyjny(wpisz od 4 do 10 znaków):", foreground="grey", font=("Times New Roman", "16")).place(x=80, y=185)
wpisywanie_rejestracji = Text(okno, height=1, width=25)
wpisywanie_rejestracji.place(x=100, y=205)

# miejsce na wpisanie nowej daty
Label(okno, text="Zmiana daty(wpisz date w formacie YYYY MM DD HH MM SS:)", foreground="grey", font=("Times New Roman", "16")).place(x=30, y=130)
wpisywanie_nowej_daty = Text(okno, height=1, width=25)
wpisywanie_nowej_daty.place(x=100, y=155)


# funkcja zmieniająca datę
def aktdata():
    okno.date = ''
    setattr(okno, 'date', wpisywanie_nowej_daty.get(1.0, END))
    okno.date = okno.date.split(" ", 5)
    p.change_current_time(okno.date[0], okno.date[1], okno.date[2], int(okno.date[3]), int(okno.date[4]),
                            int(okno.date[5]))


# funkcja wypisująca zmienioną datę

def zapis_Zmiany_daty_przycisk(data):
    data.configure(text=str(p.get_current_time()))

# przycisk do zmiany daty

zmiana_daty_przycisk = Button(okno, text="Zmień date", width=10,
                                  command=lambda: [aktdata(), zapis_Zmiany_daty_przycisk(data_aktualna)]).place(x=320,
                                                                                                                y=150)

Label(okno, text="Aktualna data:", foreground="grey", font=("Times New Roman", "16")).place(x=80, y=40)
data_aktualna = Label(okno, width=30, text=p.get_current_time())
data_aktualna.place(x=100, y=60)
Label(okno, text="Data wyjazdu:", foreground="grey", font=("Times New Roman", "16")).place(x=80, y=80)
datawyjazdu = Label(okno, width=30, text=p.get_departure_time())
datawyjazdu.place(x=100, y=100)
Label(okno, text="Wpisz ilość monet:", foreground="grey", font=("Times New Roman", "16")).place(x=80, y=235)
liczba_monet_spinbox = Spinbox(okno, from_=1, to=200, width=20)
liczba_monet_spinbox.place(x=100, y=260)



