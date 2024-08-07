from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import resize,crop
from blured_video import blur_video
def shortproduction(originalvideo,resultplacment):
    clip = VideoFileClip(originalvideo)

    #bluring the video

    blur_video(originalvideo,r"blurredvid.mp4")
    blurredclip=VideoFileClip(r"blurredvid.mp4")

    #resizing and placing the blured video

    resizedblurredclip=blurredclip.resize(width=3500)
    blurposition=resizedblurredclip.set_position(("center","bottom")) 

    #taking the streamer webcame and resizing it to fit the top center of the clip

    camera_feed = crop(clip,width=392,height=278,x1=0,y1=170).resize(width=1080)
    camera_feed_positioned = camera_feed.set_position(("center", -100))

    #enable either normal mode or phone mode or half mode
    
    #normal mode
    #gameplay_positioned = clip.set_position(("center", 900)).resize(width=1200)

    #phone mode
    testingsomthing=crop(clip,width=590,height=1050,x2=-660,y1=0).resize(width=800)
    gameplay_positioned = testingsomthing.set_position(("center", 500))

    #half half mode
    #gameplay_positioned = clip.set_position(("center", 800)).resize(width=1600)

    #placing the clips by priority and the size of the video
    finalClip = CompositeVideoClip([blurposition,gameplay_positioned,camera_feed_positioned], size=(1080, 1920))
    finalClip.write_videofile(resultplacment)