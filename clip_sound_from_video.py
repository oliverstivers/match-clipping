import subprocess


def extract_audio(input_file, output_file, start_seconds=0):
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-ss",
        str(start_seconds),
        "-vn",
        "-acodec",
        "copy",
        output_file,
    ]
    subprocess.run(command, check=True)
