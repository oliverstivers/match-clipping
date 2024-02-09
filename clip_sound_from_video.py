import subprocess

def extract_audio(input_file, output_file):
    command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "copy", output_file]
    subprocess.run(command, check=True)

