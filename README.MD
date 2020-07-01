# Esquenta dev full cycle
Uma integração com python, django e docker

## Criando com o framework django no python
Utilizando o django e containers docker contruimos uma aplicação com a área administrativa

## Comandos
* Criando um volume:
```sh
$ docker volume create iniciando-django-pgdata
```

* Levantando a aplicação:
```sh
$ docker-compose up
```

* Acessando o container:
```sh
$ docker-compose exec app bash
```

* Criando o super usuário:
```sh
$ python manage.py createsuperuser
```

* Criando a migração (banco de dados):
```sh
$ python manage.py makemigrations
```

* Aplicando a migração (banco de dados):
```sh
$ python manage.py migrate
```

> Para não esquecer:

* Criando um novo projeto django:
```sh
$ docker-compose run app django-admin startproject iniciando_com_django
```

* Criando um app no django. Isso estende as funções da aplicação
```sh
$ django-admin startapp app
```

## Acesse
[localhost:8080](https://localhost:8080/)