from moviepy.editor import VideoFileClip

def extract_audio_from_mp4(mp4_file_path, output_m4a_file_path):
    with VideoFileClip(mp4_file_path) as video:
        audio = video.audio
        audio.write_audiofile(output_m4a_file_path, codec='aac')

# Example usage
input_file = '/Users/asif/desktop/baseline.mp4'
extract_audio_from_mp4(input_file, 'output.m4a')
