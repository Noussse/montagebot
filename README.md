# 🎬 MontageBot
## ⚡ Short Machine
A program that edits normal videos (camera and gameplay reaction, work, etc.) into shorts with subtitles.

Short Machine is designed to edit short videos. This bot was primarily used with CaseOh videos, giving you a rough idea of the camera placement and content format.

## 📌 Example:
![Example](https://github.com/user-attachments/assets/6206241c-33ad-41eb-9201-b6b7eaa51dbf)

## ✨ Features

- 🎥 **Camera Cropping:** The bot can crop the camera and place it at the top of a 9:16 format.

- ⚙️ **Main Video Settings:** Choose from three settings for the main video:
  1. 📏 **Normal Resolution with Blurry Background:** The original video barely zoomed in.
  2. 🔍 **Partial Resolution with Blurry Background:** Partially fills the space with a blurry background (more zoomed in than normal resolution).
  3. 📱 **Phone Resolution with Blurry Background:** The mode used in the "after photo."

- 🔤 **Subtitle Generation:** The program provides two versions of the edited short:
  1. 🎞️ A normal edited short.
  2. 📝 A short with subtitles.

  Subtitles are generated using AssemblyAI, with a limit of three words on screen at a time.

## 🚀 How to Use

### 🔧 Setup

1. 📦 Install dependencies: `moviepy`, `assemblyai`, `pysrt`, and `opencv`.
2. 📂 Fill in the video input and output paths in `short_building.py`.
3. 🔑 Insert your AssemblyAI key in `subtitle_generator.py`.
4. ▶️ Run `short_generator(main file).py` to start the program.

## 💻 Compatibility
This bot works with any streamer content that includes a camera setup.
