Liczby, napisy, listy

W poprzednim dziale mieliśmy pierwsze spotkanie z językiem Edlang - prosty program, który wypisuje napis na wyjście. Ale jak on to właściwie robi?

Za samo wypisanie napisu odpowiedzialna jest funkcja ```Print```. Funkcja ta wypisuje to co jej powiemy więc :

```
Print("Cześć");
```

wypisze napis *Cześć*. Aby wypisać wiele rzeczy w jednej linijce możemy podać je po przecinku - przekazać argumenty:

```
Print("Cześć ", "SKE", "!");
```

wypisze napis *Cześć SKE!*.

Jednak czym są te rzeczy, które jej podajemy? W języku Edlang nazywamy je wartościami i rozróżniamy 4 typy wartości:

- ```Int - liczby całkowite```
- ```Float - liczby z przecinkiem```
- ```String - napisy```
- ```List - listy innych wartości```

Po krótce przejdziemy teraz przez każde z nich:

#### Int
Int oznacza liczbę całkowitą. 

```
Print(5);
```

Powyższy kod wypisuje na wyjście liczbę 5.

#### Float
Float oznacza liczbę przedstawiającą ułamek dziesiętny - innymi słowy liczbę z przecinkiem.

```
Print(3.2);
```

Edlang pozwala na pominięcie 0 na początku lub końcu liczby więc Float jest zarówno

```
Print(.2);
```

i

```
Print(3.);
```
#### String
String oznacza napis. Zbiór liter tworzący jakiś fragment tekstu. W Edlangu string oznacza się parą apostrofów albo cudzysłowiem.

```
Print("Cześć");
```

```
Print('Cześć');
```

Napisy muszą być odpowiednio oznaczone inaczej Edlang uzna, że je za instrukcję. Muszą również być otwarte i zamknięte TYM SAMYM ZNAKIEM. Poniższy kod jest niepoprawny:

```
Print("Cześć'); # Da błąd
```

#### List
List oznacza liste innych wartości. Edlang listy oznacza poprzez {}. Przykłady list

    Print({1}); # jedno-elementowa lista zawierająca liczbę całkowitą 1


    Print({1, 2.3, "Jest Dobrze"}); # trzy-elementowa lista zawierająca liczbę całkowtią 1, liczbę zmienno przecinkową 2.3 i napis "Jest Dobrze".

Listy mogą również zawierać inne listy:

    Print({{1, 2, 3}, {1, 2, 3}, {1, 2, 3}}); # lista zawierająca 3 elementy będące listami 3 elementowymi

---
To są typy wartości w Edlangu. W następnym dziale dowiemy się jakie operacje możemy na nich wykonywać czyli jak możemy coś liczyć.