# Погода сегодня

## Цель проекта 
Проект служит для того что бы показывать пользователя погоду в любом городе

### Основные функции
Выводит погоду введенного города 

## Требования
Убедитесь, что на вашей системе установлены следующие компоненты:
- Docker
- Docker Compose

Следуйте официальной документации для установки Docker:
- [Установка Docker на Windows](https://docs.docker.com/docker-for-windows/install/)
- [Установка Docker на macOS](https://docs.docker.com/docker-for-mac/install/)
- [Установка Docker на Linux](https://docs.docker.com/engine/install/)

### Установка Docker Compose
Следуйте официальной документации для установки Docker Compose:
- [Инструкция по установке Docker Compose](https://docs.docker.com/compose/install/)

## запуск проекта
1) В терминале клонируем проект на свою машину:
- git clone git@github.com:denisdel123/weather_today.git

2) С терминала собираем и запускаем контейнер:
- docker-compose up -d --build   

3) С терминала входим в docker-compose и базу данных:
- docker-compose exec db psql -U postgres 

4) Создаем базу данных:
- create database <name_bd>;

6) Выходим из базы данных:
- \q

7) Переходим по ссылки

8) Введите город в котором вы хотите узнать погоду