import subprocess

# extracts the sound from a video, from inpu_file, outputting to output_file, starting at start_seconds
# copies, audio codec, with mp4 video you must specify output file as .aac, need to test what it is with .ts
# Note to self.... maybe use ffprobe to see audio codec, then automatically use for output?
def extract_audio(input_file, output_file, start_seconds=0):
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-ss",
        str(start_seconds),
        "-vn",
        "-acodec",
        "pcm_s16le",
        output_file,
    ]
    subprocess.run(command, check=True)


