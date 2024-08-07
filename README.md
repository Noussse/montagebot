# montagebot
## Short Machine
A program that edits normal videos (camera and gameplay reaction, work, etc.) into shorts with subtitles.

Short Machine is designed to edit short videos. This bot was primarily used with CaseOh videos, giving you a rough idea of the camera placement and content format.

## example:
**before**

![video before editing](https://github.com/user-attachments/assets/53a2adf2-72d1-4623-be62-9bc8d6abd3cb)

**after**

![video after montage](https://github.com/user-attachments/assets/d4b6d7a9-0984-47fc-9845-3ed5ec1a865a)





## Features
**Camera Cropping:** The bot can crop the camera and place it at the top of a 9:16 format.

**Main Video Settings:** You can choose from three settings for the main video in the Short Machine file:

1.normal resolution with blurry background: the original video barly zoomed in 

2.Partial Resolution with Blurry Background: Partially fills the space with a blurry background (more zoomed in than normal resolotion).

3.phone Resolution with Blurry Background:the mode used in the "after photo"

**Subtitle Generation:** The program provides two versions of the edited short:

1.A normal edited short.

2.A short with subtitles.

Subtitles are generated using AssemblyAI, with a limit of three words on screen at a time.

## How to Use
**Setup**

1.Make sure you download the moviepy, assemblyai, pysrt, and opencv libraries.

2.Fill in the video placement and output placement in the short_building.py file.

3.Insert your AssemblyAI key in the subtitle_generator.py file.

4.Run the short_generator(main file).py file to start the program.

## Compatibility
This bot will work with any streamer content that includes a camera setup.
