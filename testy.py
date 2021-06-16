import unittest
from datetime import timedelta
from parkomat import *
from parkomat import Parkomat
from wyjatki import *

class Tests(unittest.TestCase):

#Test1
#1.	Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.
    def test1(self):

        p = Parkomat()
        with self.assertRaises(ValueError) as e:
            p.change_current_time("2021", "11", "11", 24, 34, 00)
            print(str(e.value))

#Test2
#2.	Wrzucić 2zł, oczekiwany termin wyjazdu godzinę po aktualnym czasie. Dorzucić 4zł, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie. Dorzuć 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie. Dorzuć kolejne 5zł, oczekiwany termin wyjazdu wtedy godziny po aktualnym czasie.
    def test2(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "16", 12, 00, 00)
        #wrzucam 2zł
        p.add_coin(2, 1)
        self.assertEqual(p.get_current_time() + timedelta(hours=1), p.get_departure_time())
        #dorzucam 4zł
        p.add_coin(2, 2)
        self.assertEqual(p.get_current_time() + timedelta(hours=2), p.get_departure_time())
        #dorzucam 5zł
        p.add_coin(5, 1)
        self.assertEqual(p.get_current_time() + timedelta(hours=3), p.get_departure_time())
        #dorzucam kolejne 5zł
        p.add_coin(5, 1)
        self.assertEqual(p.get_current_time() + timedelta(hours=4), p.get_departure_time())

#Test3
#3.	Wrzuć tyle pieniędzy , aby termin wyjazdu przeszedł na kolejny dzień, zgodnie z zasadami:
# wrzuć tyle monet aby termin wyjazdu był po godzinie 19:00, dorzuć monetę 5zł.

    def test3(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "16", 17, 20, 00)
        p.add_coin(2, 1)
        p.add_coin(2, 2)
        p.add_coin(5, 1)
        print(p.get_current_time())
        print(p.get_current_time() + timedelta(hours=15))
        #self.assertEqual(p.get_current_time() + timedelta(hours=15), p.get_departure_time())

#Test4
#4.	Wrzuć tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień, zgodnie z zasadami:
# wrzuć  tyle monet aby termin wyjazdu był w piątek o godzinie 19:00, a potem dorzucić monetę 5zł.

    def test4(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "18", 17, 20, 00)
        p.add_coin(2, 1)
        p.add_coin(2, 2)
        p.add_coin(5, 1)
        print(p.get_current_time())
        print(p.get_current_time() + timedelta(hours=63))
        #self.assertEqual(p.get_current_time() + timedelta(hours=63), p.get_departure_time())

#Test5
#5.	Wrzucić 1zł, oczekiwany termin wyjazdu poł godziny po aktualnym czasie.
    def test5(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "16", 12, 00, 00)
        p.add_coin(1, 1)
        self.assertEqual(p.get_current_time() + timedelta(minutes=30), p.get_departure_time())

#Test6
#6.	Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie

    def test6(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "16", 12, 00, 00)
        p.add_coin(0.01, 200)
        self.assertEqual(p.get_current_time() + timedelta(hours=1), p.get_departure_time())

#Test7
#7.	Wrzucić 201 monet 1gr, oczekiwana informacja o przepełnieniu parkomatu.

    def test7(self):

        p = Parkomat()
        p.change_current_time("2021", "6", "16", 12, 00, 00)
        with self.assertRaises(PrzepelnienieParkomatuException) as e:
            p.add_coin(0.01, 201)
            print(str(e.value))

#Test8
#8. Wciśnięcie „Zatwierdź” bez wrzucania monet – oczekiwana informacja o błędzie.

    def test8(self):

        p = Parkomat()
        with self.assertRaises(NieWrzuconoPieniedzyException) as e:
            p.confirm("KTT347D")
            print(str(e.value))

#Test9
#Wciśnięcie „Zatwierdź” bez wpisania numeru rejestracyjnego – oczekiwana informacja o błędzie.
#Wciśniecie „Zatwierdź” po wpisaniu niepoprawnego numeru rejestracyjnego – oczekiwana informacja o błędzie

    def test9(self):

        p = Parkomat()
        p.add_coin(2, 1)
        with self.assertRaises(BlednaRejestracjaException) as e:
            p.get_license_plate('')
            print(str(e.value))

    if __name__ == '__main__':
        unittest.main()


