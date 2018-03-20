Example of Django REST & Datatables & CRUD




Load fixtures:

python manage.py loaddata risk/fixtures/risk.json
python manage.py loaddata risk/fixtures/responses.json
python manage.py loaddata risk/fixtures/country.json




Dump fixtures:

python manage.py dumpdata risk.risk --indent 4 > risk/fixtures/risk.json
python manage.py dumpdata risk.responses --indent 4 > risk/fixtures/responses.json
python manage.py dumpdata risk.responses --indent 4 > risk/fixtures/country.json