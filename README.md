# News API

Bu loyiha Django Rest Framework yordamida yaratildi va yangiliklar sayti uchun API yaratadi.

## Talablar

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- django-filter

## O'rnatish

1. Loyihani klonlash:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Virtual muhit yaratish va faollashtirish:

    ```bash
    python -m venv env
    source env/bin/activate  # macOS/Linux
    .\env\Scripts\activate  # Windows
    ```

3. Talablarni o'rnatish:

    ```bash
    pip install -r requirements.txt
    ```

4. Migratsiyalarni bajarish:

    ```bash
    python manage.py migrate
    ```

5. Superuser yaratish:

    ```bash
    python manage.py createsuperuser
    ```

6. Serverni ishga tushirish:

    ```bash
    python manage.py runserver
    ```

## Foydalanish

Admin panelga kirish uchun `http://localhost:8000/admin/` manziliga o'ting va superuser login ma'lumotlarini kiriting.

## API Endpoints

- `/api/categories/` - Kategoriyalar ro'yxati
- `/api/authors/` - Mualliflar ro'yxati
- `/api/news/` - Yangiliklar ro'yxati

## Postman Kollektsiyasi

Har bir endpoint uchun Postman kollektsiyasi quyidagi sahifadan yuklab olinishi mumkin: [Postman Collection](<Postman-Collection-URL>)
