# Zadanie rekrutacyjne django rest api

Django Rest Api

## Instalacja Projektu

```
git clone https://github.com/cynarski/recruitment_task.git
cd rest_api
```

Uruchomienie projektu

```
docker-compose up -d
docker exec -it <CONTAINER ID> bash
cd rest_api/
python manage.py migreate
```

## Używanie api

Do projektu został dodany swagger aby łatwiej móc się posługiwać api. 
Wszelkie funkcje do testowania można znaleźć pod linkiem:
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)