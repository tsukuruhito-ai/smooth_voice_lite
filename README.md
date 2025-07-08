
=================================================================
# 🎤 Voice Input Tool
macOS向け音声入力ツール。ESCキー長押しで録音、アプリ自動判別、送信まで自動化。
=================================================================

## ✨ 特徴

- **ESCキー長押し操作**: 押している間だけ録音、離すと停止
- **アプリ自動判別**: Webアプリ16種 + デスクトップアプリ3種に対応
- **自動送信**: 録音→変換→送信まで完全自動
- **高精度音声認識**: OpenAI Whisper (faster-whisper)
- **辞書機能**: 変換精度向上（例：クロード→Claude）
- **音感フィードバック**: 起動/録音開始/完了/エラー/タイムアウトをSE音で通知
- **シームレス操作**: 録音から送信まで一連の流れで完結

## 🎯 使用方法

### 基本操作
1. ツールを起動
2. **ESCキー長押し**で録音開始
3. **ESCキー離す**で録音停止・自動処理開始
4. アプリ判別→テキスト変換→自動送信

### 対応アプリ・送信コマンド

#### 🌐 Webアプリ (16種)
**AIチャット (Enter送信)**
- ChatGPT (chatgpt.com)
- Claude (claude.ai)
- Gemini (gemini.google.com)
- Copilot (copilot.microsoft.com)
- Perplexity (perplexity.ai)
- Grok (grok.com)
- GenSpark (genspark.ai)
- NotebookLM (notebooklm.google.com)

**開発者ツール (Cmd+Enter送信)**
- Tenbin AI (tenbin.ai)
- Cursor (cursor.so)
- GitHub (github.com)
- Notion (notion.so)

**コミュニケーション (Enter送信)**
- Discord (discord.com)
- Slack (slack.com)
- Chatwork (chatwork.com)
- LINE (line.me)

#### 🖥️ デスクトップアプリ (3種)
**Cmd+Enter送信**
- Claude
- Visual Studio Code
- Cursor

#### 📝 その他のアプリ
- テキストエディタ、Word等：テキスト挿入のみ（送信なし）

## 🛠️ セットアップ

### 1. リポジトリクローン
git clone https://github.com/[username]/VOICE_INPUT_TOOL.git
cd VOICE_INPUT_TOOL

### 2. 仮想環境作成・パッケージインストール
python3 -m venv voice_env
source voice_env/bin/activate
pip install -r requirements.txt

### 3. 権限設定
macOSのシステム設定で以下を許可：
- **マイクアクセス権限**
- **入力監視権限**
- **アクセシビリティ権限**

### 4. 実行
python src/voice_input_main.py

## 📁 プロジェクト構成

VOICE_INPUT_TOOL/
├── src/
│   ├── dictionaries/          # 辞書機能
│   │   ├── basic_dictionary.py
│   │   └── dictionary_processor.py
│   ├── sounds/               # 効果音
│   ├── temps/               # 一時ファイル
│   ├── logger.py            # ログ機能
│   └── voice_input_main.py  # メインプログラム
├── .gitignore
├── README.md
└── requirements.txt

## 🔧 技術スタック

- **faster-whisper**: 高速音声認識（OpenAI Whisper最適化版）
- **sounddevice**: 音声録音・再生
- **pynput**: キーボード・マウス制御
- **pyautogui**: 自動操作・画面制御
- **pyobjc**: macOSアプリ判別・システム連携

## 📝 開発者

初回作成・学習中のプロジェクトです。フィードバックやIssue、PRを歓迎します！

## 📄 ライセンス

MIT License