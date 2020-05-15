Warunki i instrukcje

W Edlangu mamy prostą budowę instrukcji warunkowej

    If (warunek)
        # Ciało warunku
    EndIf

Jeżeli warunek jest prawdziwy logicznie to instrukcje w ciele funkcji zostaną wykonane. W przeciwnym wypadku nie.

Warunek można rozszerzyć o instrukcję Else

    If (warunek)
        # Ciało warunku
    Else
        # Ciało else
    Endif

Jeżeli waruenk jest prawdziwy logiczny ciało warunku zostanie wykonane, w przeciwnym wypadku ciało else zostanie wykonane.

Do tego całego możma dołożyć również ElseIf

    If (warunek1)
        # Ciało warunku 1
    ElseIf (warunek2)
        # Ciało warunku 2
    ElseIf (warunek3)
        # Ciało warunku 3
    Else
        # Ciało else
    EndIf

Jeżeli warunek1 jest prawdziwy to jego ciało zostanie wykonane, w przeciwnym wypadku jeżeli warunek2 jest prawdziwy to jego ciało zostanie wykonane, w przeciwnym wypadku jeżeli warunek3 jest prawdziwy to jego ciało zostanie wykonane, w przeciwnym wypadku ciało else zostanie wykonane.

### Scope
Każdy blok If/ElseIf/Else posiada oddzielny scope. Oznacza to, że zmienne stworzone w środku ich ciała po wyjściu z niego przestają istnieć.

### Zwracanie wartości
Blok If/ElseIf/Else zwraca wartość ostatniej, wykonanej w sobie instrukcji.

    Int k = If(2 eq 2) 4; Else 6; EndIf # Przyjmie wartość 4 - ostatnia instrukcja wykonana w ciele spełnionego warunku