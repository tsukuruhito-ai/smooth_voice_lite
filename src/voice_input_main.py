"""
音声入力ツール 「Smooth Voice Lite」
1つのキーで録音から送信までスムースな体験を提供
19チャット系のコミュニケーションサービス
MacOSのみ対応
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
from dictionaries import apply_dictionary
from logger import log_always, log_debug

class VoiceInputTool:
    def __init__(self):
        log_debug("🎤 音声入力ツール 汎用送信システム版 初期化中...")
        
        # 🔧 パス設定（実行場所に依存しない絶対パス）
        # スクリプトファイルの場所を基準とする
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.temp_dir = os.path.join(self.script_dir, "temp")
        self.sounds_dir = os.path.join(self.script_dir, "sounds")
        
        # 基本設定
        self.sample_rate = 16000
        self.is_recording = False
        self.audio_data = []
        self.stream = None
        self.temp_file = os.path.join(self.temp_dir, "current_recording.wav")
        
        # 汎用送信システム
        self.send_command = None  # 'Enter' / 'Cmd+Enter' / None
        
        # 送信コマンド辞書
        self.SEND_COMMANDS = {
            # AIチャット (Enter系)
            'chatgpt.com': 'Enter',
            'claude.ai': 'Enter', 
            'gemini.google.com': 'Enter',
            'copilot.microsoft.com': 'Enter',
            'perplexity.ai': 'Enter',
            'grok.com': 'Enter',                # Grok
            'genspark.ai': 'Enter',
            'notebooklm.google.com': 'Enter',
            
            # 開発者ツール (Cmd+Enter系)
            'tenbin.ai': 'Cmd+Enter',
            'cursor.so': 'Cmd+Enter',
            'github.com': 'Cmd+Enter',
            'notion.so': 'Cmd+Enter',
            
            # コミュニケーション (Enter系)
            'discord.com': 'Enter',
            'slack.com': 'Enter',
            'chatwork.com': 'Enter',
            'line.me': 'Enter',
        }
        
        # デスクトップアプリ辞書
        self.DESKTOP_COMMANDS = {
            'Claude': 'Cmd+Enter',
            'Visual Studio Code': 'Cmd+Enter',
            'Cursor': 'Cmd+Enter',
        }

        # 送信待機状態管理
        self.waiting_for_send = False
        self.waiting_timer = None
            
        # 必要なディレクトリを作成
        os.makedirs(self.temp_dir, exist_ok=True)
        os.makedirs(self.sounds_dir, exist_ok=True)
        
        # Whisperモデル初期化
        log_debug("🧠 Whisperモデル読み込み中...")
        self.model = WhisperModel("small", device="cpu", compute_type="int8")
        log_debug("✅ 初期化完了！")
        self.play_sound_async('ready')
        print("\n" + "="*50)
        print("🎯 使用方法:")
        print("  📌 Macbookモード 　　: 右Command：録音 + 右Shift：送信")
        print("  📌 クラムシェルモード: 右Command：録音 + 右Shift：送信 or F1：録音 + F2：送信")
        print("  📌 Ctrl+C で終了")
        print("="*50 + "\n")

        # クリップボード初期化
        log_debug("🔧 クリップボード初期化中...")
        subprocess.run(['pbcopy'], input="", text=True)
        log_debug("✅ クリップボード初期化完了")

    def get_app_send_command(self):
        """Web + Desktop ハイブリッド判別システム"""
        try:
            script = '''
            tell application "System Events"
                set frontApp to name of first application process whose frontmost is true
                
                if frontApp is "Google Chrome" or frontApp contains "Chrome" then
                    tell application "Google Chrome"
                        set currentURL to URL of active tab of first window
                        return "WEB:" & currentURL
                    end tell
                else
                    return "DESKTOP:" & frontApp
                end if
            end tell
            '''
            
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            app_info = result.stdout.strip()
            
            print(f"🔍 アプリ判別結果: {app_info}")
            
            if app_info.startswith("WEB:"):
                # Web版判別
                url = app_info[4:]  # "WEB:" を除去
                return self._get_web_send_command(url)
            elif app_info.startswith("DESKTOP:"):
                # Desktop版判別
                app_name = app_info[8:]  # "DESKTOP:" を除去
                return self._get_desktop_send_command(app_name)
            else:
                return None
                
        except Exception as e:
            print(f"⚠️ アプリ判別エラー: {e}")
            return None

    def _get_web_send_command(self, url):
        """Web版URL判別"""
        for domain, command in self.SEND_COMMANDS.items():
            if domain in url:
                print(f"✅ Web版判別成功: {domain} → {command}")
                return command
        print(f"ℹ️ 未対応Web版: {url}")
        return None

    def _get_desktop_send_command(self, app_name):
        """Desktop版アプリ名判別"""
        for app, command in self.DESKTOP_COMMANDS.items():
            if app in app_name:
                print(f"✅ Desktop版判別成功: {app} → {command}")
                return command
        print(f"ℹ️ 未対応Desktop版: {app_name}")
        return None

    # 🆕 汎用送信システム実装
    def execute_send_command(self):
        """汎用送信コマンド実行"""
        if not self.send_command:
            print("❌ 送信コマンドが設定されていません")
            return False
            
        try:
            log_debug(f"📤 送信実行中 (コマンド: {self.send_command})...")
            
            if self.send_command == 'Enter':
                # Enter送信
                subprocess.run(['osascript', '-e', '''
                tell application "System Events"
                    key code 36
                end tell
                '''])
                print("✅ Enter送信完了")
                
            elif self.send_command == 'Cmd+Enter':
                # Cmd+Enter送信
                subprocess.run(['osascript', '-e', '''
                tell application "System Events"
                    key code 36 using command down
                end tell
                '''])
                print("✅ Cmd+Enter送信完了")
                
            else:
                print(f"❌ 未対応送信コマンド: {self.send_command}")
                return False
                
            return True
            
        except Exception as e:
            print(f"❌ 送信エラー: {e}")
            return False

    def play_sound_async(self, sound_type):
        """非同期音声フィードバック再生"""
        def play():
            sounds = {
                'start': os.path.join(self.sounds_dir, 'recording_start.mp3'),      # 録音開始
                'complete': os.path.join(self.sounds_dir, 'recording_complete.mp3'), # 録音完了
                'ready': os.path.join(self.sounds_dir, 'recording_ready.mp3'),       # 起動音
                'timeout': os.path.join(self.sounds_dir, 'recording_timeout.mp3'),   # タイムアウト音
                'error': 'Funk'        # エラー
            }
            try:
                sound_file = sounds.get(sound_type)
                if sound_file and sound_file != 'Funk' and os.path.exists(sound_file):
                    subprocess.run(['afplay', sound_file], check=False)
                elif sound_file == 'Funk':
                    # システム音の場合はそのまま
                    subprocess.run(['afplay', '/System/Library/Sounds/Funk.aiff'], check=False)
                else:
                    print(f"⚠️ 音声ファイルが見つかりません: {sound_file}")
            except Exception as e:
                print(f"⚠️ 音声再生エラー: {e}")
        
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
        
        # 汎用アプリ判別を最初に実行
        self.send_command = self.get_app_send_command()
        
        self.is_recording = True
        self.audio_data = []
        self.recording_start_time = time.time()
        
        # 音声フィードバック: 録音開始（非同期）
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
        self._cleanup_stream()
        
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
                log_debug("✅ テキスト挿入完了")
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
                self.play_sound_async('error')
                return
            
            # 測定ポイント1: 音声データ前処理開始
            audio_prep_start = time.time()
            
            # 音声データをnumpy配列に変換
            audio_array = np.array(self.audio_data, dtype=np.float32)
            duration = len(audio_array) / self.sample_rate
            
            log_debug(f"📊 録音データ: {len(audio_array)}サンプル, {duration:.1f}秒")
            
            # 最低録音時間チェック
            if duration < 0.5:
                print("⚠️ 録音時間が短すぎます（最低0.5秒必要）")
                self.play_sound_async('error')
                return
            
            # 音声レベル確認（デバッグ用）
            max_level = np.max(np.abs(audio_array))
            rms_level = np.sqrt(np.mean(audio_array**2))
            log_debug(f"🔊 音声レベル - Max: {max_level:.4f}, RMS: {rms_level:.4f}")
            
            if max_level < 0.01:
                print("⚠️ 音声レベルが低すぎます")
                self.play_sound_async('error')
                return
            
            # 測定ポイント2: WAVファイル保存開始
            wav_save_start = time.time()
            
            # WAVファイルに保存
            wav_data = (audio_array * 32767).astype(np.int16)
            wav.write(self.temp_file, self.sample_rate, wav_data)
            log_debug(f"💾 音声ファイル保存: {self.temp_file}")
            
            # 測定ポイント3: WAVファイル保存完了
            wav_save_end = time.time()
            
            # Whisper処理時間測定開始
            whisper_start = time.time()
            
            # Whisperで音声認識
            log_debug("🧠 音声認識処理中...")
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
            
            log_debug(f"📋 認識言語: {info.language} (確率: {info.language_probability:.2f})")
            
            # 測定ポイント4: テキスト結合開始
            text_combine_start = time.time()
            
            # セグメント処理
            log_debug("🧠 セグメント処理中...")
            
            # セグメント取得時間測定
            segments_fetch_start = time.time()
            segments_list = list(segments)
            segments_fetch_end = time.time()
            
            # セグメント処理時間測定
            segments_process_start = time.time()
            segment_texts = []
            
            for segment in segments_list:
                log_debug(f"📝 セグメント: '{segment.text}' (信頼度: {segment.avg_logprob:.2f})")
                segment_texts.append(segment.text)
            
            segments_process_end = time.time()
            
            # 文字列結合時間測定
            join_start = time.time()
            transcribed_text = "".join(segment_texts)

            # 辞書機能適用
            print("🔄 辞書処理適用中...")
            transcribed_text = apply_dictionary(transcribed_text)

            join_end = time.time()
            
            # テキスト結合完了
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
                        self.play_sound_async('error')
                        return
                
                insert_end = time.time()
                
                # 汎用送信判別結果に基づく送信待機モード
                if success and self.send_command:
                    log_debug(f"🎯 送信対応サービス検知 - 送信待機モード開始")
                    time.sleep(0.2)  # テキスト挿入完了待ち
                    self.enter_send_waiting_mode()
                elif success:
                    print("ℹ️ 送信なしサービス - 即座にアイドル復帰")
                
                # 詳細処理時間ログ出力
                audio_prep_time = wav_save_start - audio_prep_start
                wav_save_time = wav_save_end - wav_save_start
                whisper_prep_time = whisper_start - wav_save_end
                whisper_time = whisper_end - whisper_start
                text_combine_time = text_combine_end - text_combine_start
                insert_time = insert_end - insert_start
                total_time = insert_end - process_start
                
                log_debug("="*60)
                log_debug(f"📊 録音時間: {duration:.2f}秒")
                log_debug(f"🔧 音声データ前処理: {audio_prep_time:.2f}秒") 
                log_debug(f"💾 WAVファイル保存: {wav_save_time:.2f}秒") 
                log_debug(f"⚙️ Whisper前準備: {whisper_prep_time:.2f}秒")
                log_debug(f"🎤 Whisper処理: {whisper_time:.2f}秒")
                log_debug(f"📝 テキスト結合: {text_combine_time:.2f}秒")
                log_debug(f"  └ セグメント取得: {segments_fetch_end - segments_fetch_start:.2f}秒")
                log_debug(f"  └ セグメント処理: {segments_process_end - segments_process_start:.2f}秒")
                log_debug(f"  └ 文字列結合: {join_end - join_start:.2f}秒")
                log_debug(f"📋 テキスト挿入: {insert_time:.2f}秒")
                log_debug(f"⏱️ 総処理時間: {total_time:.2f}秒")
                if self.send_command:
                    log_debug(f"⏳ 送信待機中")
                log_debug("="*60)
                
            else:
                print("❌ 音声を認識できませんでした")
                self.play_sound_async('error')
                
        except Exception as e:
            print(f"❌ 音声処理エラー: {e}")
            self.play_sound_async('error')
        
        print("-" * 50)

    def on_press(self, key):
        """キー押下時の処理"""
        try:
            # F1キー録音（クラムシェル時）- キーコード145
            if hasattr(key, 'vk') and key.vk == 145:  # F1キー
                if self.waiting_for_send:
                    self.reset_waiting_state()
                self.start_recording()
                
            # F2キー送信（クラムシェル時）- キーコード144
            elif hasattr(key, 'vk') and key.vk == 144:  # F2キー
                if self.waiting_for_send and self.send_command:
                    log_debug(f"🚀 F2キー送信実行 (コマンド: {self.send_command})")
                    success = self.execute_send_command()
                    if success:
                        self.reset_waiting_state()
                    else:
                        self.play_sound_async('error')
                else:
                    print("⚠️ 送信待機状態ではありません")
                    
            # 右Command録音（ノート時）
            elif key == keyboard.Key.cmd_r:
                if self.waiting_for_send:
                    self.reset_waiting_state()
                self.start_recording()
                
            # 右Shift送信（ノート時）
            elif key == keyboard.Key.shift_r:
                if self.waiting_for_send and self.send_command:
                    log_debug(f"🚀 右Shiftキー送信実行 (コマンド: {self.send_command})")
                    success = self.execute_send_command()
                    if success:
                        self.reset_waiting_state()
                    else:
                        self.play_sound_async('error')
                else:
                    print("⚠️ 送信待機状態ではありません")
                    
        except AttributeError:
            pass

    def on_release(self, key):
        """キー離し時の処理"""
        try:
            # F1キー録音停止（クラムシェル時）
            if hasattr(key, 'vk') and key.vk == 145:  # F1キー
                self.stop_recording()
                
            # 右Command録音停止（ノート時）
            elif key == keyboard.Key.cmd_r:
                self.stop_recording()
        except AttributeError:
            pass

    def enter_send_waiting_mode(self):
        """送信待機状態に移行"""
        print(f"⏳ 送信待機状態開始")
        self.waiting_for_send = True
        
        # 15分タイムアウト設定
        if self.waiting_timer:
            self.waiting_timer.cancel()
        
        self.waiting_timer = threading.Timer(15 * 60, self.timeout_waiting_state)
        self.waiting_timer.start()

    def _cleanup_stream(self):
        """ストリームの安全なクリーンアップ"""
        try:
            if self.stream:
                if self.stream.active:
                    self.stream.stop()
                self.stream.close()
                self.stream = None
                time.sleep(0.1)  # リソース解放待ち
        except Exception as e:
            print(f"⚠️ ストリームクリーンアップエラー: {e}")
            self.stream = None

    def timeout_waiting_state(self):
        """送信待機状態タイムアウト"""
        print("⏰ 送信待機状態タイムアウト（15分経過）")
        self.play_sound_async('timeout') 
        self.is_recording = False
        self._cleanup_stream()
        self.reset_waiting_state()

    def reset_waiting_state(self):
        """送信待機状態をリセット"""
        if self.waiting_for_send:
            print("🔄 送信待機状態リセット")
            self.waiting_for_send = False
            self.send_command = None  # 🆕 送信コマンドもリセット
            if self.waiting_timer:
                self.waiting_timer.cancel()
                self.waiting_timer = None

    def run(self):
        """メインループ実行"""
        print("🚀 音声入力ツール 利用開始できます")
        print("💡 お使いの環境に応じた録音キーを押している間録音されます")
        log_debug("🎯 お使いの環境に応じた送信キーで送信可能です")
        
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
                if self.waiting_timer:
                    self.waiting_timer.cancel()

if __name__ == "__main__":
    tool = VoiceInputTool()
    tool.run()