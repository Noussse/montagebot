import assemblyai as aai
from moviepy.editor import VideoFileClip,TextClip
import pysrt
def subtitle(video_file_path,output_path):
    #from mkv to mp3
    audio_file_path="audiofile.mp3"
    video = VideoFileClip(video_file_path)
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    #setting everything up
    aai.settings.api_key = "put your assemblyai api key here"
    transcriber = aai.Transcriber()

    # Request transcription with timestamps
    transcript = transcriber.transcribe(audio_file_path)

    if transcript.status == 'failed':
        raise Exception("Transcription failed")
    # Save the transcription result
    transcription_result = transcript.export_subtitles_srt()

    #generate srt
    with open(output_path, 'w') as f:
        f.write( transcription_result)


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
            txt_clip = TextClip(chunk, fontsize=105, color='#FBDD00', font='Arial-Bold',stroke_color='black', stroke_width=2)
            txt_clip = txt_clip.set_position(('center', 600)).set_start(start).set_duration(chunk_duration)
            subtitle_clips.append(txt_clip)
            start += chunk_duration  # Move the start time forward for the next chunk

    return subtitle_clips