# FRC Stream Match Auto Clipper
Idk I dont have a name for it yet. 

This project was made to automatically clip match videos from FRC event streams in real time and upload them to a GCS bucket. FRC teams could view their matches replayed from the stream shorly after they happened, essentially allowing teams to rewind on twitch, something disabled due to DMCA worries. 

This project organization is a mess. I dont know why I did it like this. I would not do it this way again. 

clip_sound_from_video extracts the audio from the video source and saves to a file locally. detect_match_start analyzes the audio and finds correlations between the audio track and the match start sounds, then returns a list of all the timestamps that it detected a match start. Tested on real event live stream recordings, it has near 100% accuracy. After that, in clip_out_videos, we take the list of timestamps and clip a match-length video from the live stream recording and export it. There's also some code for uploading, but it's disabled right now and might need some work to get set up again. 

If I were to develop this further, I might make some sort of dashboard for accessing videos and make it actually run on a live event stream. Maybe if I have time to spare and wanna work on a software project......

