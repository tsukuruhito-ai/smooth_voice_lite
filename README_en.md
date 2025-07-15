
=================================================================
# 🎤 Smooth Voice Lite
macOS Voice Input Tool - One-Key Recording & One-Key Sending for Seamless Voice Input Experience
=================================================================

[日本語版 / Japanese Version](README_ja.md)

## ✨ Features

- **Hybrid Operation Support**: 
  - External Keyboard: Right Command (record) + Right Shift (send) or F1 (record) + F2 (send) *Apple keyboards only
  - Notebook: Right Command (record) + Right Shift (send)
- **18 Services Supported**: Auto-detection for 16 web apps + 3 desktop apps
- **Universal Send System**: Auto-detection and sending via Enter/Cmd+Enter
- **High-Accuracy Speech Recognition**: OpenAI Whisper (faster-whisper)
- **Dictionary Function**: Improved conversion accuracy (e.g., クロード→Claude)
- **Audio Feedback**: Sound notifications for startup/recording/completion/error/timeout
- **Seamless Operation**: Complete workflow from recording to sending

## 🎯 Usage

### Basic Operation
1. Launch the tool
2. **Hold recording key** to start recording
3. **Release recording key** to stop recording and begin auto-processing
4. App detection → Text conversion → Send ready
5. **Press send key** to execute sending

### Operation Keys
- **💻 Notebook**: Right Command (record) + Right Shift (send)
- **🖥️ External Keyboard**: Right Command (record) + Right Shift (send) or F1 (record) + F2 (send)
- **📌 Use whichever you prefer!**

### Supported Apps & Send Commands

#### 🌐 Web Apps (16 types)
**AI Chat (Enter to send)**
- ChatGPT (chatgpt.com)
- Claude (claude.ai)
- Gemini (gemini.google.com)
- Copilot (copilot.microsoft.com)
- Perplexity (perplexity.ai)
- Grok (grok.com)
- GenSpark (genspark.ai)
- NotebookLM (notebooklm.google.com)

**Developer Tools (Cmd+Enter to send)**
- Tenbin AI (tenbin.ai)
- Cursor (cursor.so)
- GitHub (github.com)
- Notion (notion.so)

**Communication (Enter to send)**
- Discord (discord.com)
- Slack (slack.com)
- Chatwork (chatwork.com)
- LINE (line.me)

#### 🖥️ Desktop Apps (3 types)
**Cmd+Enter to send**
- Claude
- Visual Studio Code
- Cursor

#### 📝 Other Apps
- Text editors, Word, etc.: Text insertion only (no auto-send)

## 🛠️ Setup

### 1. Clone Repository
git clone https://github.com/tsukuruhito-ai/VOICE_INPUT_TOOL.git
cd VOICE_INPUT_TOOL

### 2. Create Virtual Environment & Install Packages
python3 -m venv voice_env
source voice_env/bin/activate
pip install -r requirements.txt

### 3. Permission Settings
Allow the following in macOS System Settings:
- **Microphone Access Permission**
- **Input Monitoring Permission**
- **Accessibility Permission**

### 4. Run
python src/voice_input_main.py

## 📁 Project Structure

VOICE_INPUT_TOOL/
├── src/
│   ├── dictionaries/          # Dictionary function
│   │   ├── basic_dictionary.py
│   │   └── dictionary_processor.py
│   ├── sounds/               # Sound effects
│   ├── temp/                # Temporary files
│   ├── logger.py            # Logging function
│   └── voice_input_main.py  # Main program
├── .gitignore
├── README.md
└── requirements.txt

## 🔧 Tech Stack

- **faster-whisper**: High-speed speech recognition (OpenAI Whisper optimized)
- **sounddevice**: Audio recording & playback
- **pynput**: Keyboard & mouse control
- **pyautogui**: Automation & screen control
- **pyobjc**: macOS app detection & system integration

## 🔧 Requirements

- **Python**: 3.8+ (Development: 3.13.5)
- **macOS**: 10.14+ (Development: Ventura 13.5)

## 📝 Developer

This is my first project and I'm still learning. Feedback, Issues, and PRs are welcome!

## 📄 License

MIT License

---

**🎤 Smooth Voice Lite - Seamless voice input experience in your hands.**