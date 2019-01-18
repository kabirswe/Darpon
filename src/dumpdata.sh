python manage.py dumpdata auth.user --indent 2 > fixtures/user.json
python manage.py dumpdata account --indent 2 > fixtures/account.json
python manage.py dumpdata socialaccount --indent 2 > fixtures/socialaccount.json
python manage.py dumpdata preferences --indent 2 > fixtures/preferences.json
