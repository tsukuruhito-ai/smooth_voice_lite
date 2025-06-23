# 🎤 音声入力ツール

Whisperを使用したmacOS向け高精度音声入力ツール

## ✨ 機能

- **ワンクリック起動**: デスクトップの🎤VoiceInput.commandをダブルクリックで即座に起動
- **Escキー制御**: 録音開始・停止・終了をEscキーで直感的に操作
- **高精度音声認識**: OpenAI Whisper (faster-whisper) による高精度な音声テキスト変換
- **自動テキスト挿入**: 認識したテキストを自動的にアクティブなアプリに挿入
- **リアルタイム処理**: 録音終了と同時に即座にテキスト変換・挿入

## 🛠️ 技術スタック

- **音声処理**: faster-whisper 1.1.1 (OpenAI Whisper高速版)
- **システム操作**: PyAutoGUI, pynput, pyperclip
- **音声取得**: sounddevice
- **macOS連携**: pyobjc各種フレームワーク

## 🚀 使用方法

### 1. ワンクリック起動
🎤VoiceInput.command

### 2. 操作方法
1. **録音開始**: Escキーを押す
2. **録音停止**: もう一度Escキーを押す
3. **アプリ終了**: 録音停止状態でEscキーを押す

### 3. 自動テキスト挿入
- 録音停止と同時に音声認識を実行
- 認識したテキストを現在アクティブなアプリに自動挿入

## ⚙️ セットアップ

### 依存パッケージインストール
cd /Users/hasegawahajimeki/Desktop/voice_input_tool/
source voice_env/bin/activate
pip install -r requirements.txt

### macOS権限設定
- **マイクアクセス権限**: システム設定で許可
- **入力監視権限**: Escキー制御のため必要
- **アクセシビリティ権限**: 自動テキスト挿入のため必要

## 📁 プロジェクト構成

voice_input_tool/
├── voice_env/              # Python仮想環境
├── src/
│   └── voice_input_main.py # メインプログラム (17KB)
├── requirements.txt        # 依存パッケージ (46パッケージ)
├── .gitignore             # Git管理対象外設定
└── README.md              # このファイル

デスクトップ:
└── 🎤VoiceInput.command    # ワンクリック起動ランチャー

## 🎯 開発フェーズ

- ✅ **Phase 1**: 音声入力ツール開発・完成
- ✅ **Phase 2**: ワンクリック起動化・完成  
- ✅ **Phase 3**: Git管理導入・完成
- 🔄 **Phase 4**: 精度改善実験 (予定)

## 📝 開発メモ

このツールは完璧に動作する状態を保ちながら、Git管理下で継続的な改善実験を行う体制を整備済み。

次フェーズでは以下の実験を予定：
- Whisper base → medium/large 精度比較実験
- テキスト挿入方法改良実験
- UI改善実験