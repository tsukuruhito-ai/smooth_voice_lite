import os

# 環境変数でデバッグモードを制御
DEBUG_MODE = os.getenv('DEBUG', '0') == '1'

def log_always(message, emoji="✅"):
    """常に表示（日常使用で見たいもの）"""
    print(f"{emoji} {message}")

def log_debug(message, emoji="🔧"):
    """デバッグ時のみ表示"""
    if DEBUG_MODE:
        print(f"{emoji} {message}")
