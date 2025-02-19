# Название проекта

Тестовое SPBPARTS

## Требования

- [Docker](https://www.docker.com/get-started) (версия 20.10 или выше)
- [Docker Compose](https://docs.docker.com/compose/) (версия 1.27 или выше)

## Установка


2. **Соберите образы и запустите контейнеры**:

   ```bash
   docker-compose up --build
   ```

   Эта команда соберет образы и запустит все сервисы, определенные в `docker-compose.yml`.

## Доступ к приложению

После успешного запуска контейнеров вы сможете получить доступ к приложению по адресу:

http://localhost:5000


## Остановка контейнеров

Чтобы остановить запущенные контейнеры, выполните:

docker-compose down



Эта команда остановит и удалит все контейнеры, созданные с помощью `docker-compose up`.

## Настройка базы данных

Если ваш проект использует базу данных, убедитесь, что вы правильно настроили переменные окружения в файле `docker-compose.yml`.