from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import resize,crop
from bluredvideo import blur_video
import pysrt
def shortproduction(originalvideo,resultplacment):
    clip = VideoFileClip(originalvideo)
    #bluring the video
    blur_video(originalvideo,r"blurredvid.mp4")
    blurredclip=VideoFileClip(r"blurredvid.mp4")
    #resizing and placing the blured video
    resizedblurredclip=blurredclip.resize(width=3000)
    blurposition=resizedblurredclip.set_position(("center","bottom"))
    #resizing the original video
    resized_video = clip.resize(height=1080)  
    #taking the streamer webcame and resizing it to fit the top center of the clip
    camera_feed = crop(clip,width=392,height=278,x1=0,y1=170).resize(width=1080)
    camera_feed_positioned = camera_feed.set_position(("center", -100))
    #placing the gameplay under the camera and zooming a little
    #enable either normal mode or phone mode
    #normal mode
    #gameplay_positioned = resized_video.set_position(("center", 900)).resize(width=1200)
    #phone mode
    #gameplay_positioned = resized_video.set_position(("center", "bottom")).resize(width=2500)
    #half half mode
    gameplay_positioned = resized_video.set_position(("center", 800)).resize(width=1600)
    #placing the clips by priority and the size of the video
    finalClip = CompositeVideoClip([blurposition,gameplay_positioned,camera_feed_positioned], size=(1080, 1920))
    finalClip.write_videofile(resultplacment)