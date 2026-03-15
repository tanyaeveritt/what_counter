import warnings
warnings.filterwarnings('ignore')

import speech_recognition as sr
import threading
from datetime import datetime
import re

class AudioWhatCounter:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.what_count = 0
        self.running = False
        self.lock = threading.Lock()
        self.session_start = datetime.now()
        self.matches_found = []
        
        # Adjust recognizer settings for better performance
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        print("✅ Text-based 'what' detector initialized")
    
    def detect_what_variations(self, text):
        """
        Detect variations of 'what' in transcribed text
        Matches: what, whaat, whaaaat, whaaat, whattt, what's, etc.
        """
        # Pattern to match: wh + a(s with length >= 1) + t(s)
        pattern = r'\bwha+t+s?\b'
        
        matches = re.findall(pattern, text.lower())
        
        return matches
    
    def transcribe_audio(self, audio_data):
        """Transcribe audio to text"""
        try:
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
            return None
    
    def listen_and_process(self):
        """Continuously listen to microphone and process audio"""
        with sr.Microphone() as source:
            print("🎤 Audio listener started...")
            print("   (Calibrating microphone...)")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("   ✅ Calibration complete!\n")
            
            while self.running:
                try:
                    print("⏳ Listening...", end="", flush=True)
                    audio = self.recognizer.listen(
                        source, 
                        timeout=10,
                        phrase_time_limit=15
                    )
                    print(" ✓ Got audio!", flush=True)
                    
                    # Transcribe audio
                    transcribed_text = self.transcribe_audio(audio)
                    
                    if transcribed_text:
                        print(f"   📝 Transcribed: {transcribed_text}")
                        
                        # Detect 'what' variations in text
                        what_matches = self.detect_what_variations(transcribed_text)
                        
                        if what_matches:
                            with self.lock:
                                self.what_count += len(what_matches)
                                for match in what_matches:
                                    self.matches_found.append({
                                        'word': match,
                                        'timestamp': datetime.now(),
                                        'full_text': transcribed_text
                                    })
                            
                            # Format matches without backslash in f-string
                            matches_str = ', '.join([f'"{w}"' for w in what_matches])
                            print(f"   ✅ MATCH! Found: {matches_str}")
                            print(f"   📊 Total 'what' count: {self.what_count}\n")
                        else:
                            print(f"   ⚠️  No 'what' detected\n")
                    else:
                        print("   ⚠️  Could not transcribe audio\n")
                        
                except sr.WaitTimeoutError:
                    print(" ⏱️ (timeout)", flush=True)
                    pass
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"\n❌ Error: {e}")
    
    def start(self):
        """Start the listener in a background thread"""
        self.running = True
        listener_thread = threading.Thread(target=self.listen_and_process, daemon=True)
        listener_thread.start()
        
        # Main thread for user interaction
        try:
            while self.running:
                user_input = input("(Commands: 'status', 'matches', 'reset', 'quit'): ").lower().strip()
                
                if user_input == 'status':
                    elapsed = datetime.now() - self.session_start
                    print(f"\n📊 Status:")
                    print(f"   Total 'what' count: {self.what_count}")
                    print(f"   Session time: {elapsed}\n")
                    
                elif user_input == 'matches':
                    with self.lock:
                        if self.matches_found:
                            print(f"\n📋 All Detected 'What' Variations:")
                            for i, match in enumerate(self.matches_found, 1):
                                print(f"   {i}. \"{match['word']}\" - at {match['timestamp'].strftime('%H:%M:%S')}")
                                print(f"      Full sentence: {match['full_text']}")
                        else:
                            print("\n📋 No 'what' matches found yet")
                    print()
                    
                elif user_input == 'reset':
                    with self.lock:
                        self.what_count = 0
                        self.matches_found.clear()
                        self.session_start = datetime.now()
                    print("🔄 Counter reset!\n")
                    
                elif user_input == 'quit':
                    self.running = False
                    print("\n👋 Stopping listener...")
                    break
                    
        except KeyboardInterrupt:
            self.running = False
            print("\n👋 Stopping listener...")
    
    def get_stats(self):
        """Get current statistics"""
        with self.lock:
            elapsed = datetime.now() - self.session_start
            return {
                'total_count': self.what_count,
                'session_duration': elapsed,
                'matches': self.matches_found
            }


def main():
    print("🎙️  What Counter - Text-Based Audio Listener")
    print("=" * 50)
    print("Detects 'what' variations from speech-to-text")
    print("=" * 50 + "\n")
    
    counter = AudioWhatCounter()
    
    try:
        counter.start()
    finally:
        stats = counter.get_stats()
        print("\n" + "=" * 50)
        print(f"📈 Final Report:")
        print(f"   Total 'what' count: {stats['total_count']}")
        print(f"   Session duration: {stats['session_duration']}")
        
        if stats['matches']:
            print(f"\n   'What' variations found:")
            variation_counts = {}
            for match in stats['matches']:
                word = match['word']
                variation_counts[word] = variation_counts.get(word, 0) + 1
            
            for variation, count in sorted(variation_counts.items(), key=lambda x: x[1], reverse=True):
                print(f"      '{variation}': {count}x")
        
        print("=" * 50)


if __name__ == "__main__":
    main()
