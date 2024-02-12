import detect_match_start
from moviepy.video.io.VideoFileClip import VideoFileClip


# clips a video out from input_file to output_file, from start_time in seconds to end_time in seconds
def clip_out_videos(input_file, output_file, start, end_time):
    clip = VideoFileClip(input_file).subclip(start, end_time)

    clip.write_videofile(output_file, codec="libx264", fps=clip.fps)

    clip.close()




