import argparse

from moviepy.editor import VideoFileClip

def extract_audio_from_mp4(mp4_file_path, output_m4a_file_path):
    with VideoFileClip(mp4_file_path) as video:
        audio = video.audio
        audio.write_audiofile(output_m4a_file_path, codec='aac')

# # Example usage
# input_file = '/Users/asif/desktop/baseline.mp4'
# extract_audio_from_mp4(input_file, 'output.m4a')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract audio from the video")
    parser.add_argument("input_file", help="The input file with  ")
    parser.add_argument("output_file", help="the output file with path")
    
    args = parser.parse_args()

    extract_audio_from_mp4(args.input_file, args.output_file)
