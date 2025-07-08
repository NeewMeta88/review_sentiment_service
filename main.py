import sqlite3
from datetime import datetime
from enum import Enum
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DB_NAME = "reviews.db"
POSITIVE_WORDS = ["хорош", "люблю"]
NEGATIVE_WORDS = ["плохо", "ненавиж"]


class ReviewIn(BaseModel):
    text: str


class ReviewOut(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str


class Sentiment(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """)


def analyze_sentiment(text: str) -> str:
    lower_text = text.lower()
    if any(word in lower_text for word in POSITIVE_WORDS):
        return "positive"
    if any(word in lower_text for word in NEGATIVE_WORDS):
        return "negative"
    return "neutral"


@app.on_event("startup")
def startup():
    init_db()


@app.post("/reviews", response_model=ReviewOut)
def create_review(review: ReviewIn):
    sentiment = analyze_sentiment(review.text)
    created_at = datetime.utcnow().isoformat()
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
            (review.text, sentiment, created_at)
        )
        review_id = cursor.lastrowid
    return ReviewOut(id=review_id, text=review.text, sentiment=sentiment, created_at=created_at)


@app.get("/reviews", response_model=List[ReviewOut])
def get_reviews(sentiment: Optional[Sentiment] = None):
    query = "SELECT id, text, sentiment, created_at FROM reviews"
    params = ()
    if sentiment:
        query += " WHERE sentiment = ?"
        params = (sentiment,)
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return [ReviewOut(id=row[0], text=row[1], sentiment=row[2], created_at=row[3]) for row in rows]
