
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
├── docs/                    # ドキュメント
│   └── security/           # セキュリティ関連
│       ├── self_audit_report.md
│       ├── bandit_result.txt
│       └── safety_result.txt
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

## 🔒 セキュリティ検証

### ⚠️ このツールについて
このツールは以下のmacOS権限を使用します：
- **マイクアクセス** (音声認識)
- **入力監視** (キーボード操作の検出)
- **アクセシビリティ** (自動操作・アプリ判別)

透明性を保つため、全コードを公開し、継続的なセキュリティ検証を実施しています。

### 📊 検証済み項目 (2025-07-16更新)

#### ✅ 静的解析結果
- **bandit**: 21件Low severity警告 → 全て正常な機能実装
- **safety**: 95パッケージ中脆弱性0件 → 完全に安全

#### ✅ 安全性確認済み
- 🌐 **外部通信**: 一切なし（完全ローカル処理）
- 🔑 **認証情報**: ハードコーディングなし
- 📁 **ファイル操作**: 適切な一時ファイル管理のみ
- ⚡ **権限使用**: 機能に必要な最小限のみ

### 🙏 技術者の皆さまへ
**第三者による検証を募集中です！**

OSレベルの権限を使用するツールのため、より多くの目でのチェックを希望しています。

**特に検証して欲しいポイント**
- 不正なネットワーク通信の有無
- キーロガー機能の悪用可能性
- 実行時の動作監視
- セキュリティ上の改善提案

**フィードバック方法**
- GitHub Issues での報告

### 📋 詳細な検証レポート
- [自己監査完了レポート](docs/security/self_audit_report.md)
- [bandit静的解析結果](docs/security/bandit_result.txt)
- [safety脆弱性チェック結果](docs/security/safety_result.txt)

## 📄 ライセンス

MIT License

---

**🎤 Smooth Voice Lite - なめらかな音声入力体験を、あなたの手に。**