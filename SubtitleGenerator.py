import assemblyai as aai
from moviepy.editor import VideoFileClip
def subtitle(video_file_path,output_path):
    #from mkv to mp3
    audio_file_path="audiofile.mp3"
    video = VideoFileClip(video_file_path)
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    #setting everything up
    aai.settings.api_key = "ea50099c36374406ad9f8ae76851f3e0"
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
