# Python 3.12.1 のスリム版
FROM python:3.12.1-slim

# 作業ディレクトリを作成
WORKDIR /app

# requirements.txt をコピー（共通の requirements.txt を使用している想定）
COPY requirements.txt .

# Flask のみ必要な場合はピンポイントで入れてもOK
RUN pip install --upgrade pip \
    && pip install --no-cache-dir flask

# アプリケーションコードをコピー
COPY ./frontend /app

# ポート開放（Flaskデフォルト: 5000）
EXPOSE 5000

# Flaskアプリ起動（app.pyの内容に合わせて変更）
CMD ["python", "app.py"]