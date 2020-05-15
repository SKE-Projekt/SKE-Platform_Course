Pętle i zapętlenia

Edlang posiada możliwość zapętlenia instrukcji - wykonania ich wiele razy bez konieczności powtórnego pisania.

Konktrukcja pętli wygląda w ten sposób

    Loop(warunek)
        # Ciało pętli
    EndLoop

gdzie warunek jest jakąś wartością logiczną. Wszystkie instrukcje znajdujące się pomiędzy instrukcją Loop a EndLoop będą powtarzane tak długo jak warunek będzie prawdziwy.

przykład pętli wypisującej Cześć! 10 razy

    Int k = 0;
    Loop(k < 10)
        Print("Cześć");
        k = k - 1; # Ważna cześć, bez tego nasza pętla będzie się wykonywać w nieskończoność
    EndLoop

### Scope - co to?
Pętla jest specjalną, blokową konstrukcją języka. W Edlangu wszystkie blokowe konstrukcję tworzą własny scope co oznacza, że zmienne stworzone w środku ich ciała po wyjściu z niego przestają istnieć.

    Int k = 0;
    Loop(k < 10)
        Int a = 4; # z każdym obrotem pętli zmienna jest tworzona od nowa
        Print("Cześć ", a);
        k = k - 1; # Ważna cześć, bez tego nasza pętla będzie się wykonywać w nieskończoność
    EndLoop
    Print("Cześć", a); # Błąd, a nie istnieje poza ciałem pętli