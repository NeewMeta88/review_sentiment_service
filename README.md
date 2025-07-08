# Сервис сбора отзывов пользователей 
### Установка и запуск

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

### Примеры curl-запросов и их ответов

### POST `/reviews`
#### Ввод
```bash
curl -X POST "http://127.0.0.1:8000/reviews" -H "Content-Type: application/json" -d "{\"text\": \"Очень люблю этот сервис!\"}"
```

#### Вывод
```bash
{"id":1,"text":"Очень люблю этот сервис!","sentiment":"positive","created_at":"2025-07-08T17:14:49.823796"}
```

### GET `/reviews?sentiment=negative`
#### Ввод
```bash
curl "http://127.0.0.1:8000/reviews?sentiment=negative"
```

#### Вывод
```bash
[{"id":2,"text":"ужас, ненавижу","sentiment":"negative","created_at":"2025-07-08T17:21:27.890133"}]
```