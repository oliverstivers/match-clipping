import time
import clip_sound_from_video
import detect_match_start
import clip_out_videos


def main():
    clip_sound_from_video.extract_audio("feynman2024.mp4", "feynman.mp3")
    times = detect_match_start.find_offsets(
        "feynman.mp3", "match_start.wav", 3, 0
    )
    print(times)
    
    print(len(times))
    name_index = 1
    # for each start index, clip out a video starting at that time
    # TODO: change this name to use matches or something more useful
    for time in times:
        clip_out_videos.clip_out_videos(
            "feynman2024.mp4", "feynman/match" + str(name_index) + ".mp4", time, time + 165
        )
        name_index += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Total time: " + str(time.time()- start_time) + "s")
        


