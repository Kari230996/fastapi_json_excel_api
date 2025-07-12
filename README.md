
---

## 📦 FastAPI JSON/Excel API

🔗 **Документация Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Это небольшое API-приложение на FastAPI, которое обрабатывает GET и POST запросы, и возвращает ответы в формате JSON или Excel-файла (`.xlsx`).

> 🔧 Задание: реализовать приложение на FastAPI, которое возвращает данные в формате JSON или Excel, и работает на `localhost`.

---

### 🚀 Функциональность

* ✅ `POST /items/` — добавить запись (в формате JSON или Excel)
* ✅ `GET /items/` — получить все записи (в формате JSON или Excel)
* 📦 Данные временно хранятся в памяти (без базы данных)

---

### 🛠 Установка и запуск

#### 1. Клонируй репозиторий (если необходимо)

```bash
git clone https://github.com/Kari230996/fastapi_json_excel_api.git
cd fastapi_json_excel_api
```

#### 2. Создай виртуальное окружение

```bash
python -m venv venv
```

#### 3. Активируй виртуальное окружение

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

#### 4. Установи зависимости

```bash
pip install -r requirements.txt
```

#### 5. Запусти сервер

```bash
uvicorn main:app --reload
```

---

### 📄 Примеры запросов

#### 🔹 POST /items/

* JSON-данные:

```json
{
  "name": "Karina",
  "age": 28,
  "email": "karina@example.com"
}
```

* Параметры:

  * `format=json` (по умолчанию)
  * `format=excel` (для скачивания Excel-файла)

#### 🔹 GET /items/

* Получить все записи:

  * `http://127.0.0.1:8000/items/?format=json`
  * `http://127.0.0.1:8000/items/?format=excel`

---

### 🔗 Swagger-документация

Документация доступна по адресу:
📄 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 📦 Зависимости (`requirements.txt`)

```txt
fastapi
uvicorn
pandas
openpyxl
```

---


