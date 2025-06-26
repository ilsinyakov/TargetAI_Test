# TargetAI Test Automation

## Структура проекта

```
TargetAI_Test/
├── pages/                # Page Object Model (POM) классы для страниц
│   ├── base_page.py
│   ├── login_page.py
│   └── agents_page.py
├── locators/             # Селекторы для каждой страницы
│   ├── login_locators.py
│   └── agents_locators.py
├── tests/                # Тесты
│   └── test_add_agent.py
├── conftest.py           # Фикстуры pytest и настройка окружения
├── config.py             # Конфигурация (URL и др.)
├── .env                  # Логин и пароль (НЕ коммитить!)
├── pyproject.toml        # Зависимости и конфигурация проекта (uv)
├── .gitignore            # Исключения для git
└── README.md             # Описание и инструкции
```

## Быстрый старт

### 1. Установка uv
[Документация uv](https://github.com/astral-sh/uv)

```sh
pip install uv
```

### 2. Создание и активация виртуального окружения

```sh
uv venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 3. Установка зависимостей

```sh
uv sync
```

### 4. Установка браузеров Playwright

```sh
playwright install
```

### 5. Настройка переменных окружения

Создайте файл `.env` в корне проекта:
```
LOGIN=your_email@example.com
PASSWORD=your_password
```

### 6. Запуск тестов

```sh
pytest
```

### 7. Просмотр отчёта Allure

Allure должен быть установлен в системе.  
[Документация Allure](https://allurereport.org/docs/)
```sh
allure serve allure-results
```

---

**Примечание:**
- Все селекторы и шаги тестов вынесены в отдельные модули для удобства поддержки.
- Для корректной работы тестов необходимы валидные логин и пароль.
- Файл `.env` не должен попадать в git (уже добавлен в `.gitignore`). 
