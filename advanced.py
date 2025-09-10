# Code By Atul Kushwaha 
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip

# ------------ Input URL  ------------
raw_url = " Your Youtube Video Url"
if "?" in raw_url:
    raw_url = raw_url.split("?")[0]

yt = YouTube(raw_url, on_progress_callback=on_progress)

print("\n🎬 Title :", yt.title)
print("👤 Author:", yt.author)
print(f"⏱️ Length: {yt.length // 60} min {yt.length % 60} sec\n")


# ------------ Preferred Resolutions in Order ------------
preferred_res = ["1080p", "720p", "360p"]
# You can extend this:
# preferred_res = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]

video_stream = None
for res in preferred_res:
    video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4", res=res).first()
    if video_stream:
        print(f"✅ Selected VIDEO resolution: {res}")
        break

video_filename, audio_filename = None, None

# ------------ Download VIDEO ------------
if video_stream:
    try:
        video_filename = f"{yt.title}_VIDEO_ONLY_{video_stream.resolution}.mp4"
        video_stream.download(filename=video_filename)
        print(f"📥 Downloaded video as: {video_filename}")
    except Exception as e:
        print(f"❌ Video download error: {e}")
else:
    print("❌ No suitable video stream found!")

# ------------ Download AUDIO ------------
audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension="mp4").order_by("abr").desc().first()

if audio_stream:
    try:
        audio_filename = f"{yt.title}_AUDIO_ONLY_{audio_stream.abr}.mp4"
        audio_stream.download(filename=audio_filename)
        print(f"🎧 Downloaded audio as: {audio_filename}")
    except Exception as e:
        print(f"❌ Audio download error: {e}")
else:
    print("❌ No audio stream found!")

# ------------ Merge VIDEO + AUDIO ------------
if video_filename and audio_filename:
    print("\n🎬 Merging video + audio...")
    video = VideoFileClip(video_filename)
    audio = AudioFileClip(audio_filename)

    final_video = video.set_audio(audio)
    final_output = "merged_final.mp4"

    final_video.write_videofile(
        final_output,
        codec="libx264",
        audio_codec="aac",
        bitrate="5000k",
        audio_bitrate="192k",
        preset="ultrafast",
        threads=4
    )

    video.close()
    audio.close()
    final_video.close()

    # ------------ Cleanup Temp Files ------------
    try:
        os.remove(video_filename)
        os.remove(audio_filename)
        print("🧹 Removed temporary video/audio files.")
    except Exception as e:
        print(f"⚠️ Cleanup error: {e}")

    print(f"\n✅ Final merged file saved as: {final_output}")
else:
    print("\n❌ Could not merge. Missing video or audio file.")
  
