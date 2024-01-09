from pydub import AudioSegment
import speech_recognition as sr
import nltk
from nltk.tokenize import sent_tokenize

# Ensure you have the nltk data
nltk.download('punkt')

# Convert m4a to wav
def convert_m4a_to_wav(m4a_file_path):
    audio = AudioSegment.from_file(m4a_file_path, format="m4a")
    wav_file_path = m4a_file_path.replace('.m4a', '.wav')
    audio.export(wav_file_path, format="wav")
    return wav_file_path

# Function to format time for SRT
def format_srt_time(h, m, s, ms):
    return '{:02}:{:02}:{:02},{:03}'.format(h, m, s, ms)

# Split text into sentences and create SRT formatted string
def text_to_srt(text):
    sentences = sent_tokenize(text)
    srt_string = ''
    start_time = 0
    segment_duration = 5  # assuming each sentence takes an average of 5 seconds

    for i, sentence in enumerate(sentences):
        # Calculate times
        end_time = start_time + segment_duration
        start_hours, start_minutes, start_seconds = start_time // 3600, (start_time % 3600) // 60, start_time % 60
        end_hours, end_minutes, end_seconds = end_time // 3600, (end_time % 3600) // 60, end_time % 60

        # Format SRT entry
        srt_string += '{}\n'.format(i+1)
        srt_string += '{} --> {}\n'.format(format_srt_time(start_hours, start_minutes, start_seconds, 0),
                                           format_srt_time(end_hours, end_minutes, end_seconds, 0))
        srt_string += sentence + '\n\n'

        # Update start time for next segment
        start_time = end_time

    return srt_string

# Function to save the SRT content to a file
def save_srt(srt_content, file_path):
    with open(file_path, 'w') as file:
        file.write(srt_content)

# Initialize the recognizer
r = sr.Recognizer()

# Convert the M4A file to WAV
wav_file_path = convert_m4a_to_wav("/Users/asif/desktop/baseline.m4a")

# Transcribe the audio file
with sr.AudioFile(wav_file_path) as source:
    audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data)
        # Generate SRT
        srt_content = text_to_srt(text)
        print(srt_content)
        # Save the SRT file
        srt_file_path = wav_file_path.replace('.wav', '.srt')
        save_srt(srt_content, srt_file_path)
        print(f"SRT content saved to {srt_file_path}")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
