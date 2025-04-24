# app.py
import streamlit as st
import ui                   # UIモジュール
import llm                  # LLMモジュール
import database             # データベースモジュール
import metrics              # 評価指標モジュール
import data                 # データモジュール
import torch
from transformers import pipeline
from config import MODEL_NAME
from huggingface_hub import HfFolder

# --- アプリケーション設定 ---
st.set_page_config(page_title="AI Chatbot", layout="wide")

# --- 初期化処理 ---
metrics.initialize_nltk()

# データベースの初期化（テーブルが存在しない場合、作成）
database.init_db()

# データベースが空ならサンプルデータを投入
data.ensure_initial_data()

# LLMモデルのロード（キャッシュを利用）
# モデルをキャッシュして再利用

st.title("🤖 GEMMA2 Chatbot with Feedback")
st.write("Gemma2 モデルを使用したチャットボットです。回答に対してフィードバックを行えます。")

st.markdown("---")
# --- サイドバー ---
st.sidebar.title("ナビゲーション")
# セッション状態を使用して選択ページを保持
if 'page' not in st.session_state:
    st.session_state.page = "チャット" # デフォルトページ
page = st.sidebar.radio(
    "ページ選択",
    ["チャット", "フィードバック", "データベース", "評価指標"],
    key="page_selector",
    index=["チャット","履歴閲覧","サンプルデータ管理"].index(st.session_state.page),
    on_change=lambda: setattr(st.session_state,'page',st.session_state.page_selector)
)

pipe = llm.load_model()
llm.generate_response(pipe,user_question)