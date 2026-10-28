# College Management - Ahmednagar College, Ahilyanagar

    python -m venv venv
    venv\Scripts\activate          (Windows)   |   source venv/bin/activate (Mac/Linux)
    pip install -r requirements.txt
    python manage.py makemigrations college
    python manage.py migrate
    python manage.py createsuperuser   (optional, for /admin/)
    python manage.py runserver

Open http://127.0.0.1:8000/
