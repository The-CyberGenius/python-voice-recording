import sounddevice
from scipy.io.wavfile import write

# Sample rate
fs = 44100

# Ask to enter the recording time
second = int(input("Enter the Recording Time in seconds: "))
print("Recording...\n")
frames_to_record = int(second * fs)
record_voice = sounddevice.rec(frames_to_record, samplerate=fs, channels=2)
sounddevice.wait()
write("Myrecording.wav", fs, record_voice)
print("Recording is done. Please check your folder to listen to the recording.")