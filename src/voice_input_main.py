"""
音声入力ツール Phase S-1 - 音声フィードバック実装版
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
import subprocess

class VoiceInputTool:
    def __init__(self):
        print("🎤 音声入力ツール Phase S-1 初期化中...")
        
        # 基本設定
        self.sample_rate = 16000
        self.is_recording = False
        self.audio_data = []
        self.stream = None
        self.temp_dir = "temp"
        self.temp_file = os.path.join(self.temp_dir, "current_recording.wav")
        
        # tempディレクトリ作成
        os.makedirs(self.temp_dir, exist_ok=True)
        
        # Whisperモデル初期化
        print("🧠 Whisperモデル読み込み中...")
        self.model = WhisperModel("small", device="cpu", compute_type="int8")
        print("✅ 初期化完了！")
        print("\n" + "="*50)
        print("🎯 使用方法:")
        print("  📌 Escキーを押している間録音")
        print("  📌 キーを離すと音声をテキストに変換")
        print("  📌 音声フィードバック: 🎵ピッ(開始) → 🎵ピピッ(完了)")
        print("  📌 Ctrl+C で終了")
        print("="*50 + "\n")

        # クリップボード初期化
        print("🔧 クリップボード初期化中...")
        subprocess.run(['pbcopy'], input="", text=True)
        print("✅ クリップボード初期化完了")

    def play_sound_async(self, sound_type):
        """🎵 非同期音声フィードバック再生（最終版）"""
        def play():
            sounds = {
                'start': 'Glass',      # 録音開始: クリスタル音
                'complete': 'Submarine', # 録音完了: 深めの完了音
                'error': 'Funk'        # エラー: 目立つが不快でない
            }
            try:
                subprocess.run(['afplay', f'/System/Library/Sounds/{sounds[sound_type]}.aiff'], 
                            check=False)
            except:
                pass
        
        threading.Thread(target=play, daemon=True).start()

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
        
        # 🎵 音声フィードバック: 録音開始（非同期）
        self.play_sound_async('start')
        
        # 録音開始処理（最優先）
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
            self.play_sound_async('error')
            self.is_recording = False

    def stop_recording(self):
        """録音停止と音声処理"""
        if not self.is_recording:
            return
            
        print("⏹️ 録音停止")
        # 🎵 音声フィードバック: 録音停止
        self.play_sound_async('complete')
        
        self.is_recording = False
        
        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None
        except Exception as e:
            print(f"⚠️ 録音停止エラー: {e}")
            self.play_sound_async('error')
        
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
            
            # AppleScript実行直前にクリップボード再設定
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
            # Phase 7-C: 詳細時間測定開始
            process_start = time.time()
            
            if len(self.audio_data) == 0:
                print("❌ 音声データがありません")
                # 🎵 音声フィードバック: エラー
                self.play_sound_async('error')
                return
            
            # 測定ポイント1: 音声データ前処理開始
            audio_prep_start = time.time()
            
            # 音声データをnumpy配列に変換
            audio_array = np.array(self.audio_data, dtype=np.float32)
            duration = len(audio_array) / self.sample_rate
            
            print(f"📊 録音データ: {len(audio_array)}サンプル, {duration:.1f}秒")
            
            # 最低録音時間チェック
            if duration < 0.5:
                print("⚠️ 録音時間が短すぎます（最低0.5秒必要）")
                # 🎵 音声フィードバック: エラー
                self.play_sound_async('error')
                return
            
            # 音声レベル確認（デバッグ用）
            max_level = np.max(np.abs(audio_array))
            rms_level = np.sqrt(np.mean(audio_array**2))
            print(f"🔊 音声レベル - Max: {max_level:.4f}, RMS: {rms_level:.4f}")
            
            if max_level < 0.01:
                print("⚠️ 音声レベルが低すぎます")
                # 🎵 音声フィードバック: エラー
                self.play_sound_async('error')
                return
            
            # 測定ポイント2: WAVファイル保存開始
            wav_save_start = time.time()
            
            # WAVファイルに保存
            wav_data = (audio_array * 32767).astype(np.int16)
            wav.write(self.temp_file, self.sample_rate, wav_data)
            print(f"💾 音声ファイル保存: {self.temp_file}")
            
            # 測定ポイント3: WAVファイル保存完了
            wav_save_end = time.time()
            
            # Whisper処理時間測定開始
            whisper_start = time.time()
            
            # Whisperで音声認識
            print("🧠 音声認識処理中...")
            segments, info = self.model.transcribe(
                self.temp_file,
                language="ja",
                beam_size=1,
                best_of=1,
                temperature=0.0,
                no_speech_threshold=0.6,
                log_prob_threshold=-1.0,
                compression_ratio_threshold=2.4
            )
            
            whisper_end = time.time()
            
            print(f"📋 認識言語: {info.language} (確率: {info.language_probability:.2f})")
            
            # 測定ポイント4: テキスト結合開始
            text_combine_start = time.time()
            
            # セグメント処理
            print("🧠 セグメント処理中...")
            
            # セグメント取得時間測定
            segments_fetch_start = time.time()
            segments_list = list(segments)
            segments_fetch_end = time.time()
            
            # セグメント処理時間測定
            segments_process_start = time.time()
            segment_texts = []
            
            for segment in segments_list:
                print(f"📝 セグメント: '{segment.text}' (信頼度: {segment.avg_logprob:.2f})")
                segment_texts.append(segment.text)
            
            segments_process_end = time.time()
            
            # 文字列結合時間測定
            join_start = time.time()
            transcribed_text = "".join(segment_texts)
            join_end = time.time()
            
            # 測定ポイント5: テキスト結合完了
            text_combine_end = time.time()
            
            if transcribed_text.strip():
                print(f"📝 変換結果: '{transcribed_text}'")
                
                # テキスト挿入時間測定開始
                insert_start = time.time()
                
                # テキスト挿入（クリップボード経由→フォールバック）
                success = self.insert_text_via_clipboard(transcribed_text)
                
                if not success:
                    print("📝 フォールバック：直接入力を試行")
                    try:
                        pyautogui.write(transcribed_text)
                        print("✅ テキスト挿入完了（直接入力）")
                        success = True
                    except Exception as e:
                        print(f"❌ 直接入力も失敗: {e}")
                        # 🎵 音声フィードバック: エラー
                        self.play_sound_async('error')
                        return
                
                insert_end = time.time()
                
                # Phase 7-C: 詳細処理時間ログ出力
                audio_prep_time = wav_save_start - audio_prep_start
                wav_save_time = wav_save_end - wav_save_start
                whisper_prep_time = whisper_start - wav_save_end
                whisper_time = whisper_end - whisper_start
                text_combine_time = text_combine_end - text_combine_start
                insert_time = insert_end - insert_start
                total_time = insert_end - process_start
                
                print("="*60)
                print("🔬 Phase 7-C 詳細時間分析:")
                print(f"📊 録音時間: {duration:.2f}秒")
                print(f"🔧 音声データ前処理: {audio_prep_time:.2f}秒")
                print(f"💾 WAVファイル保存: {wav_save_time:.2f}秒") 
                print(f"⚙️ Whisper前準備: {whisper_prep_time:.2f}秒")
                print(f"🎤 Whisper処理: {whisper_time:.2f}秒")
                print(f"📝 テキスト結合: {text_combine_time:.2f}秒")
                print(f"  └ セグメント取得: {segments_fetch_end - segments_fetch_start:.2f}秒")
                print(f"  └ セグメント処理: {segments_process_end - segments_process_start:.2f}秒")
                print(f"  └ 文字列結合: {join_end - join_start:.2f}秒")
                print(f"📋 テキスト挿入: {insert_time:.2f}秒")
                print(f"⏱️ 総処理時間: {total_time:.2f}秒")
                print("="*60)
                
            else:
                print("❌ 音声を認識できませんでした")
                # 🎵 音声フィードバック: エラー
                self.play_sound_async('error')
                
        except Exception as e:
            print(f"❌ 音声処理エラー: {e}")
            # 🎵 音声フィードバック: エラー
            self.play_sound_async('error')
        
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
        print("🚀 音声入力ツール Phase S-1 開始")
        print("💡 Escキーを押している間録音されます")
        print("🎵 音声フィードバック: ピッ(開始) → ピピッ(完了)")
        
        # キーボードリスナー開始
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            try:
                listener.join()
                    
            except KeyboardInterrupt:
                print("\n🛑 プログラムを終了します")
            finally:
                if self.stream:
                    self.stream.stop()
                    self.stream.close()

if __name__ == "__main__":
    tool = VoiceInputTool()
    tool.run()