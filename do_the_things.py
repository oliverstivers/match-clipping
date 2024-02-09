import time
import clip_sound_from_video
import detect_match_start
import clip_out_videos


def main():
    clip_sound_from_video.extract_audio("test-stream.mp4", "stream-audio-output.aac")
    times = detect_match_start.find_offsets(
        "stream-audio-output.aac", "match_start.wav", 2, 0
    )
    name_index = 0
    for time in times:
        clip_out_videos.clip_out_videos(
            "test-stream.mp4", "output" + str(name_index) + ".mp4", time, time + 165
        )
        name_index += 1


if __name__ == "__main__":
    start_time = time.time() * 1000.0
    main()
    print("Total time: " + str(time.time() * 1000.0 - start_time) + "ms")
