# SKE-Platform_Course
Specyfikacja i narzędzia do tworzenia kursów na platformie SKE


### Specyfikacja
Kurs składać się będzię z rekurencyjnych obiektów klasy kurs.
Obiekty te mają być powiązanie poprzez łączenie się ze swoim "ojcem" czy też wyższym kursem.

Kursy bez ojca będą uważane jako kursy, wszystkie pozostałe będą lekcjami czy też częściami.

Potrzebne są również klasy pomocne mające na celu śledzenie odpowiedzi oraz postępów ucznia.

#### Klasa kurs
Klasa kurs powinna posiadać:
* Tytuł kursu
* Treść kursu - wersja markdown
* Treść kursu - wersja html
* Odwołanie do kursu-ojca(Możliwa wartość NULL)

#### Klasa ćwiczenie
Klasa ćwiczenia powinna posiadać
* odwołanie do poprawnego rozwiązania zapisanego w formie pliku
* odwołanie do skryptu sprawdzającego(z wartością defaultową jako prosty diff)
* treść
* rozwiązanie przykładowe(możliwe do przejrzenia - zapisanie tego faktu w danych)

#### Klasa rozwiązanie
Klasa rozwiązanie powinna posiadać:
* odwołanie do ćwiczenia
* odwołanie do ucznia
* status([NIESPRAWDZONE / POPRAWNE / BŁĘDNE])

### Klasa przejrzenie_rozwiązania
* odwołanie do ćwiczenia
* odwołanie do ucznia
* data przejrzenia
* flaga czy wcześniej przesłał poprawne rozwiązanie

#### Klasa progres_ucznia
Klasa progres_ucznia powinna posiadać:
* odwołanie do kursu
* odwołanie do ucznia
* liczba przejrzanych bezpośrednich pod-kursów
* liczba wykonanych poprawnie ćwiczeń
* liczba wykonanych poprawnie ćwiczeń bezpośrednich pod-kursów

### Tworzenie kursów
Kursy mają przestrzegać odpowiędnią strukturę folderową:
```
- KURS
    - tresc.md [pierwsza linijka zawiera w sobie tytuł kursu]
    - exer
        - [cwiczenia]
    - NO_POD_KURS1
        - tresc.md
        - exer
            - [cwiczenia]
    - NO_POD_KURS2
        - tresc.md
        - exer
            - NO_CWICZENIE1
                - tresc.md
                - przyklad.ed [rozwiazanie przykladowe]
                - wynik.out [oczekiwany wynik]
                - start.ed [kod dawany jako szkielet]
                - {sprawdz.sh} [specjalna sprawdzarka]
```

### Dodawanie kursów
Dodawanie kursów odbywa się bezpośrednio na stronie konkursowej przyciskiem "Dodaj kurs". Należy wgrać wygenerowaną uprzednio paczkę.

### Aktualizacja kursów
Aktualizowanie kursów odbywa się na stronie głównej kursu-ojca. Należy wgrać na nowo wygenerowaną paczkę - wszystkie ćwiczenie i ich rozwiązania powinny zostać policzone na nowo.


# TODO
* Aktualizacja kursów powinna brać pod uwagę zmiany w rozwiązaniu przykładowym podczas obliczania podglądania przed wysłaniem poprawnego rozwiązania.
* Możliwość zaliczania na platformie rozwiązań przez nauczyciela
