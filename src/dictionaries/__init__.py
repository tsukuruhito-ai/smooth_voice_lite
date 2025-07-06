"""
音声入力ツール 辞書機能
Phase P-1-1: 基本辞書システム
"""

from .dictionary_processor import apply_dictionary
from .basic_dictionary import BASIC_DICTIONARY

__all__ = ['apply_dictionary', 'BASIC_DICTIONARY']
