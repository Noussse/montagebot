import cv2
def blur_video(input_video_path,output_video_path) :
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video

    # Create VideoWriter object
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Define a larger kernel size for stronger blur
    kernel_size = (51, 51)  # Increase kernel size for stronger blur

    # Process each frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply Gaussian blur to the frame
        blurred_frame = cv2.GaussianBlur(frame, kernel_size, 0)  # Adjust kernel size as needed

        # Write the blurred frame to the output video
        out.write(blurred_frame)

    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("Blurring complete. Output saved to:", output_video_path)
