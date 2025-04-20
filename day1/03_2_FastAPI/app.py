import os
import torch
from transformers import pipeline
import time
import traceback
from fastapi import FastAPI, HTTPException,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional,List,Dict,Any
import uvicorn
import nest_asyncio
from pyngrok import ngrok

# --- 設定 ---  
# モデル名を設定
MODEL_NAME = "google/gemma-2-2b-jpn-it"  # お好みのモデルに変更可能です
print(f"モデル名を設定: {MODEL_NAME}")

# --- モデル設定クラス ---
class Config:
    def __init__(self,model_name=MODEL_NAME):
        self.MODEL_NAME = model_name

config = Config(MODEL_NAME)

# --- FastAPIアプリケーション定義 ---
app = FastAPI(
    title="ローカルLLM APIサービス",
    description="transformersモデルを使用したテキスト生成のためのAPI",
    version="1.0.0"
)

# CORSミドルウェアを追加