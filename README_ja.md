
=================================================================
# 🎤 Smooth Voice Lite
macOS向け音声入力ツール。ワンキー録音・ワンキー送信のなめらかな音声入力体験。
=================================================================

[英語版 / English Version](README_en.md)

## ✨ 特徴

- **ハイブリッド操作対応**: 
  - 外部キーボード: 右Command録音 + 右Shift送信 or F1録音 + F2送信　※apple純正キーボードのみ
  - ノート時: 右Command録音 + 右Shift送信
- **18サービス対応**: Web版16種 + Desktop版3種のアプリ自動判別
- **汎用送信システム**: Enter/Cmd+Enter自動判別・送信
- **高精度音声認識**: OpenAI Whisper (faster-whisper)
- **辞書機能**: 変換精度向上（例：クロード→Claude）
- **音声フィードバック**: 起動/録音開始/完了/エラー/タイムアウトをSE音で通知
- **シームレス操作**: 録音から送信まで一連の流れで完結

## 🎯 使用方法

### 基本操作
1. ツールを起動
2. **録音キー長押し**で録音開始
3. **録音キー離す**で録音停止・自動処理開始
4. アプリ判別→テキスト変換→送信待機
5. **送信キー**で送信実行

### 操作キー
- **💻 ノート時**: 右Command録音 + 右Shift送信
- **🖥️ 外部キーボード**: 右Command録音 + 右Shift送信 or F1録音 + F2送信
- **📌 お好みでどちらでも使えます！**

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
git clone https://github.com/tsukuruhito-ai/smooth_voice_lite.git
cd smooth_voice_lite

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
│   ├── temp/                # 一時ファイル
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

## 🔧 動作環境

- **Python**: 3.8以上（開発環境: 3.13.5）
- **macOS**: 10.14以上（開発環境: Ventura 13.5）

## 📝 開発者

初回作成・学習中のプロジェクトです。フィードバックやIssue、PRを歓迎します！

## 📄 ライセンス

MIT License

---

**🎤 Smooth Voice Lite - なめらかな音声入力体験を、あなたの手に。**