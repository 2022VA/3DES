# 3DES
Vietne 3DES kriptogrāfijas algoritma izstrādei

# TODO
- [x] Uztaisīt web app skeletu
- [X] Izpētīt algoritmu un sarakstīt nepieciešamās funkcijas/darbus
- [X] Key aprēķināšana
- [ ] Pirmā raunda sagatavošana
- [ ] Viena raunda implementācija
- [ ] SBox
- [ ] Visu raundu implementācija
- [ ] Ko var iznest no funkcijām, lai dekodējot mazāk koda
- [ ] 2/3 atslēgas - 3DES
- [ ] Labāks UI

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