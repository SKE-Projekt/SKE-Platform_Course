Operacje na wartościach

W poprzednim dziale poznaliśmy typy wartości w Edlangu. Teraz przyjrzyjmy się co możemy z nimi robić:

### Operacje matematyczne
W Edlangu mamy 5 operacji matematycznych, które możemy wykonywać na wartościach:

1. Dodawanie, +
2. Odejmowanie, -
3. Mnożenie, *
4. Dzielenie, /
5. Reszta z dzielenia, %

Operacje te wykonywane są od lewej do prawej. W celu zmiany kolejności wykonywania działań należy użyć nawiasów

    Print(12 + 3 / 2); # Wypisuje 13
    Print((12 + 3) / 2); # Wypisuje 7

Zachęcamy do eksperymentowania, które operacje jak działają na danych typach wartości(niektóre można nawet mieszać z innymi typami).

Wartość operacji zawsze jest tego samego typu co wartość lewej wartości w operacji.

##### Wtrącenie na temat list i stringów
Wartości typu String mogą być jedynie ze sobą dodawane(wartość z prawej strony jest doklejana do wartości z lewej strony).

Wartości typu List mogą być dodawane(co skutkuje dodaniem elementów prawej strony do listy elementów lewej strony) oraz od listy można odejmować wartość liczbą - skutkuje to usunięciem ostatniego elementu.

    Print("Hello, " + "World"); # Hello, World
    Print({1, 2} - 1); # {1}

### Operacje logiczne

W programowaniu mamy również coś takiego jak operacje logiczne. Polegają one na stwierdzeniu czy coś jest prawdą czy nie. W Edlangu wyróżniamy:

1. Czy dana wartość jest równa innej, eq
2. Czy dana wartość nie jest równa innej, neq
3. Czy dana wartość jest większa od innej, >
4. Czy dana wartość jest mniejsza od innej, <
5. Czy dana wartość jest mniejsza od lub równa innej, leq
6. Czy dana wartość jest większa od lub równa innej, geq
7. Czy obie dane wartości logiczne są prawdzie, and
8. Czy dowolna z danych wartości logicznych jest prawdziwa, or

W przypadku Stringów i List pod uwagę brana jest ich długość(liczba elementów, z których się składają).

Wynikiem danej operacji jest wartość typu Int równa 0 w przypadku gdy operacja jest nieprawdziwa lub 1 w przypadku gdy operacja jest prawdziwa.

    Print(5 > 4); # 1
    Print(5 < 4); # 0

Operator neq można wykorzystać do odwrócenia wartości logicznej - 0 zamienia się w jeden a 1 w 0

    Print(neq (5 > 4)); # 0
    Print(neq (5 < 4)); # 1

### Operacja indeksowa

W przypadku List i Stringów mamy operator indeksowy - pobiera on wartość elementu na waskazanym miejscu(miejsce liczone jest 0)

    Print("Hello"[0]); # H
    Print({{1, 2, 3}, {3, 2, 1}}[1][0]); # 3

### Funkcje specjalne
#### Print
Funkcja print wypisuje podane wartości a następnie przechodzi do następnej linijki.

#### Len
Funkcja Len zwraca długość podanej Listy lub Stringu jako wartość typu Int
