1. Clone the repository.

2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Apply migrations:

python manage.py makemigrations
python manage.py migrate

4. Add data to the database:

python add_data.py

Represh database if needed:
del db.sqlite3

5. Run the server:

python manage.py runserver