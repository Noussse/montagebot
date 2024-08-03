import moviepy.editor as mp
import pysrt
from SubtitleGenerator import subtitle
from shortmachine import shortproduction
def srt_to_subtitles(srt_file):
    subs = pysrt.open(srt_file)
    subtitle_clips = []

def srt_to_subtitles(srt_file):
    subs = pysrt.open(srt_file)
    subtitle_clips = []

    for sub in subs:
        start = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000
        end = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000
        duration = end - start

        # Split the text into chunks of up to 3 words each
        words = sub.text.split()
        num_chunks = (len(words) + 2) // 3  # Calculate the number of chunks (3 words per chunk)
        chunk_duration = duration / num_chunks  # Calculate the duration of each chunk

        for i in range(0, len(words), 3):
            chunk = ' '.join(words[i:i+3])
            # Create a subtitle clip for each chunk
            txt_clip = mp.TextClip(chunk, fontsize=105, color='#FBDD00', font='Arial-Bold',stroke_color='black', stroke_width=2)
            txt_clip = txt_clip.set_position(('center', 600)).set_start(start).set_duration(chunk_duration)
            subtitle_clips.append(txt_clip)
            start += chunk_duration  # Move the start time forward for the next chunk

    return subtitle_clips

def add_subtitles_to_video(video_file, srt_file, output_file):
    video = mp.VideoFileClip(video_file)
    subtitles = srt_to_subtitles(srt_file)
    final_video = mp.CompositeVideoClip([video] + subtitles)
    final_video.write_videofile(output_file, codec='libx264')

video_file = r""
resultplacement=r""
shortproduction(video_file,resultplacement)
subtitle(resultplacement,"text.srt")
srt_file = 'text.srt'
output_file = r""

add_subtitles_to_video(resultplacement, srt_file, output_file)
