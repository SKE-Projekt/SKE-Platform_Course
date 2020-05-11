#!/usr/bin/bash

echo "Generowanie pliku strukturalnego"
python3 gen_structure.py $1

if [ $? -ne 0 ]; then
    echo "Podczas generowania pliku strukturalnego wystąpił błąd"
    exit 1
fi

tar -cvf $1.tar.gz $1 $1.json
