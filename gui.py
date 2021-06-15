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

# przyciski do wrzucania monet i banknotów
przycisk1gr= Button(okno, text="1gr", height=3, width=12, foreground="black",
                    command=lambda: [p.add_coin(0.01, liczba_monet(liczba_monet_spinbox)),
                                     data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=300)

przycisk2gr = Button(okno, text="2gr", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(0.02, liczba_monet(liczba_monet_spinbox)),
                                      data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=300)

przycisk5gr = Button(okno, text="5gr", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(0.05, liczba_monet(liczba_monet_spinbox)),
                                      data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=300)

przycisk10gr = Button(okno, text="10gr", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(0.1, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=350)

przycisk20gr = Button(okno, text="20gr", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(0.2, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=350)

przycisk50gr = Button(okno, text="50gr", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(0.5, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=350)

przycisk1zl = Button(okno, text="1zł", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(1, liczba_monet(liczba_monet_spinbox)),
                                      data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=400)

przycisk2zl= Button(okno, text="2zł", height=3, width=12, foreground="black",
                    command=lambda: [p.add_coin(2, liczba_monet(liczba_monet_spinbox)),
                                     data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=400)

przycisk5zl = Button(okno, text="5zł", height=3, width=12, foreground="black",
                     command=lambda: [p.add_coin(5, liczba_monet(liczba_monet_spinbox)),
                                      data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=400)


przycisk10zl = Button(okno, text="10zł", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(10, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=20, y=450)

przycisk20zl = Button(okno, text="20zł", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(20, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=160, y=450)

przycisk50zl = Button(okno, text="50zł", height=3, width=12, foreground="black",
                      command=lambda: [p.add_coin(50, liczba_monet(liczba_monet_spinbox)),
                                       data_wyjazdu.configure(text=str(p.get_departure_time()))]).place(x=300, y=450)

def otworz_nowe_okno():
    nowe_okno = Toplevel(okno)
    nowe_okno.geometry('400x300')
    nazwa_okna = Label(nowe_okno, text='Bilet:', font=("Times New Roman", "16"))
    nazwa_okna.pack()

    Label(nowe_okno, text='Rejestracja: ').pack()
    rej = Label(nowe_okno, text=p.get_license_plate(okno.rejestracja)).pack()

    Label(nowe_okno, text='Data zakupu: ').pack()
    aktualna_data = Label(nowe_okno, text=p.get_current_time()).pack()

    Label(nowe_okno, text='Data wyjazdu: ').pack()
    data_wyjazdu = Label(nowe_okno, text=p.get_departure_time()).pack()

def zatwierdz_rejestracje():
    okno.rejestracja = ''
    setattr(okno, 'rejestracja:', wypisz_rejestracje.get(1.0, END))
    numerRej =p.get_license_plate(okno.rejestracja)
    Label(okno, text=p.get_license_plate(okno.rejestracja)).place(x=300, y=205)
    return numerRej

przycisk_zatwierdz = Button(okno, text="Zatwierdź", height=3, width=43, foreground="black",
                            command=lambda: [zatwierdz_rejestracje(),otworz_nowe_okno()]).place(x=20, y=500)
# miejsce na wpisanie rejestracji

Label(okno, text="Nr rejestracyjny(wpisz od 4 do 10 znaków):", foreground="grey", font=("Times New Roman", "16")).place(x=20, y=180)
wypisz_rejestracje = Text(okno, height=1.3, width=26)
wypisz_rejestracje.place(x=100, y=213)

# miejsce na wpisanie nowej daty
Label(okno, text="Zmiana daty (Format daty: YYYY MM DD HH MM SS):", foreground="grey", font=("Times New Roman", "16")).place(x=20, y=120)
wpisz_nowa_date = Text(okno, height=1.3, width=26)
wpisz_nowa_date.place(x=100, y=155)


# funkcja zmieniająca datę
def aktdata():
    okno.date = ''
    setattr(okno, 'date', wpisz_nowa_date.get(1.0, END))
    okno.date = okno.date.split(" ", 5)
    p.change_current_time(okno.date[0], okno.date[1], okno.date[2], int(okno.date[3]), int(okno.date[4]),
                            int(okno.date[5]))


# wypisywanie zmienionej daty:

def zmiana_daty(data):
    data.configure(text=str(p.get_current_time()))

#przycisk do zmiany daty

przycisk_do_zmiany_daty = Button(okno, text="Zmień date", width=10, foreground="black",
                                 command=lambda: [aktdata(), zmiana_daty(aktualna_data)]).place(x=300, y=150)

Label(okno, text="Aktualna data:", foreground="grey", font=("Times New Roman", "16")).place(x=20, y=40)
aktualna_data = Label(okno, text=p.get_current_time(),font=("Times New Roman", "16"), width=25)
aktualna_data.place(x=120, y=40)
Label(okno, text="Data wyjazdu:", foreground="grey", font=("Times New Roman", "16")).place(x=20, y=80)
data_wyjazdu = Label(okno, text=p.get_departure_time(), font=("Times New Roman", "16"), width=25)
data_wyjazdu.place(x=120, y=80)
Label(okno, text="Podaj ilość monet:", foreground="grey", font=("Times New Roman", "16")).place(x=20, y=250)
liczba_monet_spinbox = Spinbox(okno, from_=1, to=200, width=20)
liczba_monet_spinbox.place(x=140, y=250)

# funkjca tworząca nowe okno i wyświetlająća rejestrcję, date zakupu, date wyjazdu





