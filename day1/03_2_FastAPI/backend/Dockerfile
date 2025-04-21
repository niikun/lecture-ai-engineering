# Python 3.12.1ベースの公式イメージを使用
FROM python:3.12.1-slim

# 作業ディレクトリを作成
WORKDIR /app

# requirements.txt をコピーしてインストール
COPY requirements.txt .

# pipをアップグレードし、依存パッケージをインストール
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# アプリケーションコードを backend ディレクトリからコピー
COPY ./backend /app

# FastAPI のデフォルトポートを開放
EXPOSE 8000

# uvicorn を使ってアプリケーションを起動（main.py の app を使う）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]