"""
音声入力ツール v1.5 - クリップボード対応版
Escキーを押している間録音し、離すと音声をテキストに変換してアクティブなフィールドに挿入
"""

import sounddevice as sd
import numpy as np
import pyautogui
from faster_whisper import WhisperModel
from pynput import keyboard
import scipy.io.wavfile as wav
import os
import time
import threading
import tkinter as tk
from tkinter import ttk
import subprocess

class VoiceInputTool:
    def __init__(self):
        print("🎤 音声入力ツール v1.5 初期化中...")
        
        # 基本設定
        self.sample_rate = 16000
        self.is_recording = False
        self.audio_data = []
        self.stream = None
        self.temp_dir = "temp"
        self.temp_file = os.path.join(self.temp_dir, "current_recording.wav")
        
        # UIフィードバック用
        self.feedback_root = None
        self.feedback_window = None
        self.recording_start_time = None
        
        # tempディレクトリ作成
        os.makedirs(self.temp_dir, exist_ok=True)
        
        # Whisperモデル初期化
        print("🧠 Whisperモデル読み込み中...")
        self.model = WhisperModel("base", device="cpu", compute_type="int8")
        print("✅ 初期化完了！")
        print("\n" + "="*50)
        print("🎯 使用方法:")
        print("  📌 Escキーを押している間録音")
        print("  📌 キーを離すと音声をテキストに変換")
        print("  📌 クリップボード経由で確実に挿入")
        print("  📌 Ctrl+C で終了")
        print("="*50 + "\n")

        # 🆕 追加部分：クリップボード初期化（問題の根本対策）
        print("🔧 クリップボード初期化中...")
        subprocess.run(['pbcopy'], input="", text=True)
        print("✅ クリップボード初期化完了")

    def setup_ui_root(self):
        """UIフィードバック用のルートウィンドウをセットアップ"""
        if self.feedback_root is None:
            self.feedback_root = tk.Tk()
            self.feedback_root.withdraw()  # メインウィンドウは非表示
            # バックグラウンドで動作させるための設定
            self.feedback_root.attributes('-topmost', True)

    def show_recording_feedback(self):
        """録音中のフィードバックを表示"""
        def create_recording_window():
            self.setup_ui_root()
            
            if self.feedback_window:
                self.feedback_window.destroy()
            
            # 録音中ウィンドウ作成
            self.feedback_window = tk.Toplevel(self.feedback_root)
            self.feedback_window.title("録音中")
            self.feedback_window.geometry("200x60")
            
            # macOSで画面右上に配置
            screen_width = self.feedback_window.winfo_screenwidth()
            self.feedback_window.geometry(f"200x60+{screen_width-220}+50")
            
            # ウィンドウ設定
            self.feedback_window.attributes('-topmost', True)
            self.feedback_window.resizable(False, False)
            
            # ラベル作成
            self.recording_label = tk.Label(
                self.feedback_window, 
                text="🎤 録音中... 0.0秒",
                font=("Arial", 12),
                fg="red"
            )
            self.recording_label.pack(expand=True)
            
            # 時間更新を開始
            self.update_recording_time()
        
        # UIスレッドで実行
        if threading.current_thread() is threading.main_thread():
            create_recording_window()
        else:
            self.feedback_root.after(0, create_recording_window)

    def update_recording_time(self):
        """録音時間を更新"""
        if self.is_recording and self.feedback_window and self.recording_start_time:
            elapsed = time.time() - self.recording_start_time
            self.recording_label.config(text=f"🎤 録音中... {elapsed:.1f}秒")
            # 100ms毎に更新
            self.feedback_window.after(100, self.update_recording_time)

    def show_processing_feedback(self):
        """処理中のフィードバックを表示"""
        def create_processing_window():
            self.setup_ui_root()
            
            if self.feedback_window:
                self.feedback_window.destroy()
            
            # 処理中ウィンドウ作成
            self.feedback_window = tk.Toplevel(self.feedback_root)
            self.feedback_window.title("変換中")
            self.feedback_window.geometry("180x60")
            
            # macOSで画面右上に配置
            screen_width = self.feedback_window.winfo_screenwidth()
            self.feedback_window.geometry(f"180x60+{screen_width-200}+50")
            
            # ウィンドウ設定
            self.feedback_window.attributes('-topmost', True)
            self.feedback_window.resizable(False, False)
            
            # ラベル作成
            processing_label = tk.Label(
                self.feedback_window, 
                text="⏳ 変換中...",
                font=("Arial", 12),
                fg="blue"
            )
            processing_label.pack(expand=True)
        
        # UIスレッドで実行
        if threading.current_thread() is threading.main_thread():
            create_processing_window()
        else:
            self.feedback_root.after(0, create_processing_window)

    def show_complete_feedback(self, message="✅ 完了"):
        """完了フィードバックを表示（1秒後自動消去）"""
        def create_complete_window():
            self.setup_ui_root()
            
            if self.feedback_window:
                self.feedback_window.destroy()
            
            # 完了ウィンドウ作成
            self.feedback_window = tk.Toplevel(self.feedback_root)
            self.feedback_window.title("完了")
            self.feedback_window.geometry("150x60")
            
            # macOSで画面右上に配置
            screen_width = self.feedback_window.winfo_screenwidth()
            self.feedback_window.geometry(f"150x60+{screen_width-170}+50")
            
            # ウィンドウ設定
            self.feedback_window.attributes('-topmost', True)
            self.feedback_window.resizable(False, False)
            
            # ラベル作成
            complete_label = tk.Label(
                self.feedback_window, 
                text=message,
                font=("Arial", 12),
                fg="green"
            )
            complete_label.pack(expand=True)
            
            # 1秒後に自動で閉じる
            self.feedback_window.after(1000, self.hide_feedback)
        
        # UIスレッドで実行
        if threading.current_thread() is threading.main_thread():
            create_complete_window()
        else:
            self.feedback_root.after(0, create_complete_window)

    def hide_feedback(self):
        """フィードバックウィンドウを非表示"""
        if self.feedback_window:
            self.feedback_window.destroy()
            self.feedback_window = None

    def audio_callback(self, indata, frames, time, status):
        """音声データを取得するコールバック"""
        if status:
            print(f"⚠️ 音声入力エラー: {status}")
        if self.is_recording:
            self.audio_data.extend(indata.copy().flatten())

    def start_recording(self):
        """録音開始"""
        if self.is_recording:
            return
            
        print("🎤 録音開始...")
        self.is_recording = True
        self.audio_data = []
        self.recording_start_time = time.time()
        
        # UIフィードバック表示
        threading.Thread(target=self.show_recording_feedback, daemon=True).start()
        
        try:
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=1,
                callback=self.audio_callback,
                dtype=np.float32
            )
            self.stream.start()
        except Exception as e:
            print(f"❌ 録音開始エラー: {e}")
            self.is_recording = False

    def stop_recording(self):
        """録音停止と音声処理"""
        if not self.is_recording:
            return
            
        print("⏹️ 録音停止")
        self.is_recording = False
        
        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None
        except Exception as e:
            print(f"⚠️ 録音停止エラー: {e}")
        
        # 音声処理を別スレッドで実行
        threading.Thread(target=self.process_audio, daemon=True).start()

    def insert_text_via_clipboard(self, text):
        """AppleScript + クリップボード経由でテキスト挿入（フォーカス修正版）"""
        try:
            
            # テキストをクリップボードにコピー
            subprocess.run(['pbcopy'], input=text, text=True)
            
            # フォーカスを前のアプリに戻してから貼り付け
            script = '''
            tell application "System Events"
                set frontApp to name of first application process whose frontmost is true
                if frontApp contains "Python" or frontApp contains "voice_input" then
                    key code 48 using command down
                    delay 0.2
                end if
            end tell
            tell application "System Events" to keystroke "v" using command down
            '''
            
            # 🆕 AppleScript実行直前にクリップボード再設定
            subprocess.run(['pbcopy'], input=text, text=True)
            
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            
            
            if result.returncode == 0:
                print("✅ テキスト挿入完了")
                return True
            else:
                return False
                
        except Exception as e:
            print(f"❌ テキスト挿入エラー: {e}")
            return False

    def _fallback_clipboard_insert(self, text):
        """フォールバック: 元のpyautogui方式"""
        print("🔍 フォールバック方式実行中...")
        try:
            # 新しいテキストをクリップボードにコピー
            process = subprocess.Popen(
                'pbcopy', 
                stdin=subprocess.PIPE, 
                text=True
            )
            process.communicate(text)
            
            # 少し待機してからペースト
            time.sleep(0.1)
            
            # Cmd+V でペースト
            pyautogui.hotkey('cmd', 'v')
            
            print("✅ テキスト挿入完了（フォールバック方式）")
            return True
            
        except Exception as e:
            print(f"⚠️ フォールバック挿入も失敗: {e}")
            return False

    def process_audio(self):
        """音声をテキストに変換してアクティブフィールドに挿入"""
        try:
            if len(self.audio_data) == 0:
                print("❌ 音声データがありません")
                self.show_complete_feedback("❌ 音声なし")
                return
            
            # 処理中フィードバック表示
            self.show_processing_feedback()
            
            # 音声データをnumpy配列に変換
            audio_array = np.array(self.audio_data, dtype=np.float32)
            duration = len(audio_array) / self.sample_rate
            
            print(f"📊 録音データ: {len(audio_array)}サンプル, {duration:.1f}秒")
            
            # 最低録音時間チェック
            if duration < 0.5:
                print("⚠️ 録音時間が短すぎます（最低0.5秒必要）")
                self.show_complete_feedback("⚠️ 録音短すぎ")
                return
            
            # 音声レベル確認（デバッグ用）
            max_level = np.max(np.abs(audio_array))
            rms_level = np.sqrt(np.mean(audio_array**2))
            print(f"🔊 音声レベル - Max: {max_level:.4f}, RMS: {rms_level:.4f}")
            
            if max_level < 0.01:
                print("⚠️ 音声レベルが低すぎます")
                self.show_complete_feedback("⚠️ 音声小さい")
                return
            
            # WAVファイルに保存
            wav_data = (audio_array * 32767).astype(np.int16)
            wav.write(self.temp_file, self.sample_rate, wav_data)
            print(f"💾 音声ファイル保存: {self.temp_file}")
            
            # Whisperで音声認識
            print("🧠 音声認識処理中...")
            segments, info = self.model.transcribe(
                self.temp_file,
                language="ja",
                beam_size=5,
                best_of=5
            )
            
            print(f"📋 認識言語: {info.language} (確率: {info.language_probability:.2f})")
            
            # 認識結果を結合
            transcribed_text = ""
            for segment in segments:
                print(f"📝 セグメント: '{segment.text}' (信頼度: {segment.avg_logprob:.2f})")
                transcribed_text += segment.text
            
            if transcribed_text.strip():
                print(f"📝 変換結果: '{transcribed_text}'")
                
                # テキスト挿入（クリップボード経由→フォールバック）
                success = self.insert_text_via_clipboard(transcribed_text)
                
                if not success:
                    print("📝 フォールバック：直接入力を試行")
                    try:
                        pyautogui.write(transcribed_text)
                        print("✅ テキスト挿入完了（直接入力）")
                    except Exception as e:
                        print(f"❌ 直接入力も失敗: {e}")
                        self.show_complete_feedback("❌ 挿入失敗")
                        return
                
                # 完了フィードバック表示
                self.show_complete_feedback("✅ 完了")
                
            else:
                print("❌ 音声を認識できませんでした")
                self.show_complete_feedback("❌ 認識失敗")
                
        except Exception as e:
            print(f"❌ 音声処理エラー: {e}")
            self.show_complete_feedback("❌ エラー")
        
        print("-" * 50)

    def on_press(self, key):
        """キー押下時の処理"""
        try:
            if key == keyboard.Key.esc:
                self.start_recording()
        except AttributeError:
            pass

    def on_release(self, key):
        """キー離し時の処理"""
        try:
            if key == keyboard.Key.esc:
                self.stop_recording()
        except AttributeError:
            pass

    def run(self):
        """メインループ実行"""
        print("🚀 音声入力ツール開始")
        print("💡 Escキーを押している間録音されます")
        
        # UIルート初期化
        self.setup_ui_root()
        
        # キーボードリスナー開始
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            try:
                # tkinterのメインループと組み合わせ
                def check_listener():
                    if listener.running:
                        self.feedback_root.after(100, check_listener)
                    else:
                        self.feedback_root.quit()
                
                check_listener()
                self.feedback_root.mainloop()
                
            except KeyboardInterrupt:
                print("\n🛑 プログラムを終了します")
            finally:
                if self.stream:
                    self.stream.stop()
                    self.stream.close()
                self.hide_feedback()

if __name__ == "__main__":
    tool = VoiceInputTool()
    tool.run()