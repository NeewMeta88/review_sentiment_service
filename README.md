# Review Sentimental Service

Сервис сбора отзывов пользователей 

---
## 🚀 Установка и запуск

### 1. Клонируйте проект

```bash
git clone https://github.com/NeewMeta88/review_sentiment_service.git
```

### 2. Установите зависимости

```bash
pip install fastapi uvicorn
```

### 3. Запуск сервера

```bash
python -m uvicorn main:app --reload
```

---

## 📄 Документация API
### POST `/reviews`
#### Ввод
```bash
curl -X POST "http://127.0.0.1:8000/reviews" -H "Content-Type: application/json" -d "{\"text\": \"Очень люблю этот сервис!\"}"
```

#### Вывод
```bash
{"id":1,
"text":"Очень люблю этот сервис!",
"sentiment":"positive",
"created_at":"2025-07-08T17:14:49.823796"}
```

---

### GET `/reviews?sentiment=negative`
#### Ввод
```bash
curl "http://127.0.0.1:8000/reviews?sentiment=negative"
```

#### Вывод
```bash
[{"id":2,
"text":"ужас, ненавижу",
"sentiment":"negative",
"created_at":"2025-07-08T17:21:27.890133"}]
```