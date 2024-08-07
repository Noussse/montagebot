# montagebot
## Short Machine
A program that edits normal videos (camera and gameplay reaction, work, etc.) into shorts with subtitles.

Short Machine is designed to edit short videos. This bot was primarily used with CaseOh videos, giving you a rough idea of the camera placement and content format.

## example:
**before**

![video before editing](https://github.com/user-attachments/assets/53a2adf2-72d1-4623-be62-9bc8d6abd3cb)

**after**

![video after editing](https://github.com/user-attachments/assets/5bef64b3-f501-4cf6-a87b-371dc92f9134)



## Features
**Camera Cropping:** The bot can crop the camera and place it at the top of a 9:16 format.

**Main Video Settings:** You can choose from three settings for the main video in the Short Machine file:

1.Full Resolution: Fully fills the space.

2.Partial Resolution with Blurry Background: Partially fills the space with a blurry background.

3.Normal Resolution with Blurry Background:Keeps normal resolution with a blurry background.

**Subtitle Generation:** The program provides two versions of the edited short:

1.A normal edited short.

2.A short with subtitles.

Subtitles are generated using AssemblyAI, with a limit of three words on screen at a time.

## How to Use
**Setup**

1.Make sure you download the moviepy, assemblyai, pysrt, and opencv libraries.

2.Fill in the video placement and output placement in the finalcut.py file.

3.Insert your AssemblyAI key in the subtitle_generator.py file.

4.Run the finalcut.py file to start the program.

## Compatibility
This bot will work with any streamer content that includes a camera setup.
