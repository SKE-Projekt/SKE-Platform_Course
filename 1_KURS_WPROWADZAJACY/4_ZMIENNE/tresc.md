Zmienne i czym je się je

Nasze poprzednie programy były niczym innym jak pisaniem instrukcji komputerowi, żeby wypisał jakiś trwały i od razu ustalony tekst na wyjście. Edlang potrafi jednak o wiele więcej.

Edlang daje nam możliwość zapisania wartości w pamięci komputera i nadania jej nazwy(symbolu) pozwalającego odwołać się do niej w następnej części programu.

    Int zmienna1;

Właśnie zadklerowaliśmy(czyli stworzyliśmy ją pamięci komputera) pierwszą zmienną przechowującą wartość typu Int.

    Int zmienna_int;
    Float zmienna_float;
    String zmienna_string;
    List zmienna_list;

Zmienna może być dowolnego typu.

Jednak sama deklaracja zmiennej to za mało. Trzeba jeszcze nadać jej wartość(korzystanie ze zmiennych, które nie posiadają wartości prowadzi do błędów). Do tego Edlang wykorzystuje operator przypisania.

    Int zmienna_int = 1; # zmienna_int ma teraz wartość 1
    Float zmienna_float = 3.2;
    
    String zmienna_string; # możemy również zadeklarować zmienną
    zmienna_string = "Hello"; # i później nadać jej wartość

    List zmienna_list = {zmienna_int, 3, zmienna_float};

Jak widać we wcześniejszym przykładzie, aby uzyskać wartość zapisaną w zmiennej wystarczy napisać jej nazwę.

### Wczytywanie z wejścia

Co więcej, przy zmiennych nie musimy podawać im wartości w samym kodzie. Możemy wczytać czemu mają się równać za pomocą funkcji Read.

    Int zmienna_var = 1;
    Print(zmienna_var); # 1

    Read(zmienna_var); # Wczytujemy wartość z wejścia
    Print(zmienna_var); # Wczytana wartość

