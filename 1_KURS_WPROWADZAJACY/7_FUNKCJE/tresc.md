Funkcje - programy w programie

Ostatnią rzeczą, którą chcemy wam przedstawić w Edlangu są funkcje. Jest to sposób na stworzenie małego podprogramu w naszym programie. Ułatwia to wykonywanie tego samego kodu w różnych miejscach programu.

Funkcja posiada określoną nazwę oraz typ wartości jaką zwraca - tak samo jak zmienna. Posiada również listę argumentów, które należy do niej przekazać - takich parametrów początkowych.

    Function funkcja_dodaj(Int a, Int b) : Int
        a + b;
    EndFunction

powyższa funkcje przyjmuje dwa argumenty typu int a następnie zwraca wartość typu int będącą wynikiem ich sumowania(tak jak w przypadku ifów zwracana jest ostatnia instrukcja).

Aby skorzystać z tej funkcji w kodzie należy ją wywołać(uruchomić)

    Function funkcja_dodaj(Int a, Int b) : Int
        a + b;
    EndFunction

    Print(funkcja_dodaj(1, 2));

wywołanie funkcji polega na napisaniu jej nazwy oraz podaniu w nawiasach wartości dla jej argumentów(argumenty są zmiennymi istniejącymi w scopie funkcji).

Funkcje mogą również oczywiście nie przyjmować żadnych argumentów

    Function funkcja_bez_args() : String
        "NIE BIORE ARGUMENTOW";
    EndFunction

    Print(funckja_bez_args());