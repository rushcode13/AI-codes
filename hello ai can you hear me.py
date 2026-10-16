
import threading  #for multiple tasks related to voice and audio alongside
import sys  #for interaction with the system for using voice (sys is system) , updates the recording animation in terminal
import time  #controlls animation speeed
import pyaudio  #whatever you say using audio will be implemented in coding , captures sound from mic
import numpy as np
import matplotlib.pyplot as plt  #used in this case to draw the voice waveform graph
import wave  #saves audio in WAV file format
import speech_recognition as sr  #proveides tool for speech to text conversion
import speech_recognition as AudioData  #packages the recorded audio fo rspeech recognition

stop_event = threading.Event()  # Shared signal between threads

def wait_for_enter():
    input("\n Press Enter to stop recording..\n")
    stop_event.set()  # Signal to stop recording

def spinner():
    chars = '|/-\\'
    i = 0  #to set incimentation for looping of display of position of charecters with using i=i+1 later on
    while not stop_event.is_set:  #standout is for displaying the text
        sys.standout.write(f'\r Recording...{chars[i % 4]}')
        sys.stdout.flush()  #flush is to clear the storage there
        i = i + 1
        time.sleep(0.1)  #wait for 0.1secs
        print("Recording comlpete ..")

def record_audio():
    p = pyaudio.PyAudio()  #to capture
    stream = p.open(
        format=pyaudio.paInt16,  # 16-bit samples (65,536 precision levels)
        channels=1,  # Mono (one channel - simpler for speech)
        rate=16000,  # 16,000 samples/second (speech standard)
        input=True,  # This is an input stream (recording)
        frames_per_buffer=1024  # Process 1024 samples at a time
    )
    frames = []
    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()

    while not stop_event.is_set():
        frames.append(stream.read(1024))

    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def save_audio(data, rate, width, filename="recording.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"Saved: {filename}")

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"API Error: {e}")

def plot_waveform(data, rate):
    samples = np.frombuffer(data, dtype=np.int16) #buffer is temporary storage 
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples, color='blue')
    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)#grid pattern for effect
    plt.tight_layout()
    plt.show()

def main():
    print("=" * 40)
    print("HELLO AI CAN YOU HEAR ME?")
    print("=" * 40)
    print("\nSpeak into your microphone...")
    audio_data, rate, width = record_audio()
    save_audio(audio_data, rate, width)
    transcribe(audio_data, rate, width)
    plot_waveform(audio_data, rate)

if __name__ == "__main__":
    main()

