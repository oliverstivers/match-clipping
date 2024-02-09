import detect_match_start
from moviepy.video.io.VideoFileClip import VideoFileClip

def clip_out_videos(input_file, output_file, start, end_time):
    clip = VideoFileClip(input_file).subclip(start, end_time)

    clip.write_videofile(output_file, codec="libx264", fps=clip.fps)

    clip.close




