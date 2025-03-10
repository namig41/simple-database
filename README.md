# Simple Memory Database

Это проект, включающий простую реализацию парсера команд и базы данных, которая работает в памяти. База данных поддерживает стандартные операции (SET, GET, UNSET, COUNTS, FIND), а также транзакции (BEGIN, ROLLBACK, COMMIT).

## Как запустить

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/simple-command-parser.git
   cd simple-command-parser
   ```

2. Установите необходимые зависимости:

   ```bash
   uv sync
   ```

3. Запустите проект:

   Запустите главный скрипт, чтобы начать взаимодействовать с базой данных и выполнять команды:

   ```bash
   uv run python -m app.main
   ```

## Примеры использования

### Пример 1: Основные операции

```
> SET A 10
> GET A
10
> COUNTS 10
1
> FIND 10
A
> UNSET A
> GET A
NULL
```

### Пример 2: Транзакции

```
> BEGIN
> SET A 10
> BEGIN
> SET A 20
> BEGIN
> SET A 30
> GET A
30
> ROLLBACK
> GET A
20
> COMMIT
> GET A
20
```

## Тестирование

Проект использует `pytest` для тестирования. Чтобы запустить тесты, выполните:

```bash
uv run pytest
```

Тесты охватывают следующие аспекты:

- Проверка базовых операций (`SET`, `GET`, `UNSET`, `COUNTS`, `FIND`).
- Проверка правильности работы транзакций (`BEGIN`, `ROLLBACK`, `COMMIT`).
- Проверка конвертации команд в строковый формат.
