from moviepy.editor import VideoFileClip,CompositeVideoClip
from Subtitle_Generator import subtitle,srt_to_subtitles
from short_building import shortproduction
def add_subtitles_to_video(video_file, srt_file, output_file):
    video = VideoFileClip(video_file)
    subtitles = srt_to_subtitles(srt_file)
    video_withSubtitles = CompositeVideoClip([video] + subtitles)
    video_withSubtitles.write_videofile(output_file, codec='libx264')

video_file = r""
short_without_subtitles_placement=r""
shortproduction(video_file,short_without_subtitles_placement)
srt_file = 'text.srt'
subtitle(short_without_subtitles_placement,srt_file)
short_with_subtitles_placement = r""

add_subtitles_to_video(short_without_subtitles_placement, srt_file, short_with_subtitles_placement)
