
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
git clone https://github.com/tsukuruhito-ai/smooth_voice_lite.git
cd smooth_voice_lite

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
├── docs/                    # Documentation
│   └── security/           # Security-related
│       ├── self_audit_report.md
│       ├── bandit_result.txt
│       └── safety_result.txt
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

## 🔒 Security Verification

### ⚠️ About This Tool
This tool uses the following macOS permissions:
- **Microphone Access** (Speech recognition)
- **Input Monitoring** (Keyboard operation detection)
- **Accessibility** (Automation & app detection)

To ensure transparency, all code is open-source and we conduct continuous security verification.

### 📊 Verified Items (Updated: 2025-07-16)

#### ✅ Static Analysis Results
- **bandit**: 21 Low severity warnings → All normal functional implementations
- **safety**: 0 vulnerabilities in 95 packages → Completely safe

#### ✅ Safety Confirmed
- 🌐 **External Communication**: None (Complete local processing)
- 🔑 **Authentication Info**: No hardcoded credentials
- 📁 **File Operations**: Only appropriate temporary file management
- ⚡ **Permission Usage**: Only minimum necessary for functionality

### 🙏 To Technical Community
**We are seeking third-party verification!**

Since this tool requires OS-level permissions, we welcome review from more technical experts.

**Points We'd Like Verified**
- Absence of malicious network communications
- Potential misuse of keylogger functionality
- Runtime behavior monitoring
- Security improvement suggestions

**Feedback Method**
- GitHub Issues for reports and suggestions

### 📋 Detailed Verification Reports
- [Self-Audit Completion Report](docs/security/self_audit_report.md)
- [bandit Static Analysis Results](docs/security/bandit_result.txt)
- [safety Vulnerability Check Results](docs/security/safety_result.txt)

## 📄 License

MIT License

---

**🎤 Smooth Voice Lite - Seamless voice input experience in your hands.**