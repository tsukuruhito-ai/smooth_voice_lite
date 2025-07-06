"""
辞書処理エンジン
Phase P-1-1: シンプルな置換処理 + 拡張性確保
"""

from .basic_dictionary import BASIC_DICTIONARY

def apply_dictionary(text):
    """
    辞書を適用してテキストを変換
    
    Args:
        text (str): 変換前のテキスト
        
    Returns:
        str: 変換後のテキスト
    """
    if not text or not text.strip():
        return text
    
    # 🎯 Phase P-1-1: シンプルな文字列置換
    result = text
    
    for japanese_word, english_word in BASIC_DICTIONARY.items():
        if japanese_word in result:
            result = result.replace(japanese_word, english_word)
            print(f"🔄 辞書変換: '{japanese_word}' → '{english_word}'")
    
    return result

# 🔮 Phase P-1-3以降の拡張予定
# - 部分マッチング対応
# - 複数辞書対応
# - カテゴリ別処理
