# Lunch_service

## Instalation

### Python and PostgreSQL must be already installed !

```shell
git clone https://github.com/YuriiKindrat/Lunch_service
python3 -m venv venv
venv/Scripts/activate
pip install -r requirments.txt
```
Create file called ".env" in the main directory with parameters :
* DB_HOST="host_name"
* DB_NAME="db_name"
* DB_USER="user name"
* DB_PASSWORD="db password"
```shell
python manage.py migrate
python manage.py runserver
```

### To use Docker:
```shell
docker-compose build
docker-compose up
```

### To read documentation:
Enter the endpoint swagger/ or redoc/