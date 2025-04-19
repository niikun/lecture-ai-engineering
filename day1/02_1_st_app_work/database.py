# database.py
import sqlite3
import pandas as pd
from datetime import datetime
import streamlit as st
from config import DB_FILE
from metrics import calculate_metrics # metricsを計算するために必要

# --- スキーマ定義 ---
TABLE_NAME = "chat_history"
SCHEMA = f'''
CREATE TABLE IF NOT EXISTS {TABLE_NAME}
(id INTEGER PRIMARY KEY AUTOINCREMENT,
timestamp TEXT,
question TEXT,
answer TEXT,
feedback TEXT,
correct_answer TEXT,
is_correct REAL,
response_time REAL,
bleu_score REAL,
similarity_score REAL,
word_count INTEGER,
relevance_score REAL)
'''

# --- データベース初期化 ---
def init_db():
    """データベースとテーブルを初期化する"""
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.corsor()