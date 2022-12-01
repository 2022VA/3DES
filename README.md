# 3DES
Vietne 3DES kriptogrāfijas algoritma izstrādei

# TODO
- [x] Uztaisīt web app skeletu
- [X] Izpētīt algoritmu un sarakstīt nepieciešamās funkcijas/darbus
- [X] Key aprēķināšana
- [X] Pirmā raunda sagatavošana
- [X] Viena raunda implementācija
- [X] SBox
- [X] Visu raundu implementācija
- [X] Dešifrēšana
- [ ] 2/3 atslēgas - 3DES - uztaisīt, lai ņem vērā papildus ierakstītās atslēgas, atkārtojot šibrēšanas ciklus. Ja ievadītas tikai 2 atslēgas, tad aprēķināt visas 3 atbilstoši dokumentēcijai.
- [ ] Labāks UI
- [ ] Programmas projektējuma apraksts
- [ ] Realizācijas apraksts
- [ ] Skaņošanas/testēšanas procesa apraksts
- [ ] Prezentācija
- [/] Projektējums - fails : google drive : Projektejums_3DES_E_G_A_2022.docx

## Iespējams nepieciešams sekojošs setup:
Web daļa caur Django, līdz ar to instalācija (ieteiktu darīt izmantojot virtual environment venv vai ko līdzīgu)
```
pip install psycopg2-binary
py -m pip install Django
```

## Palaišana:
ieiet folderī TripleDES
```
python manage.py runserver
atver web: http://127.0.0.1:8000/
```

## Koda atrašanās vieta
\kriptografija\views.py


## Izmantotie resursi
1. FIPS PUB 46-3 DATA ENCRYPTION STANDARD (DES)
2. Algoritms aprakstīts pa soļiem: https://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
3. Kalkulators, kur attēlo starprezultātus, izmantots atkļūdošanai un testēšanai: http://lpb.canb.auug.org.au/adfa/src/DEScalc/




