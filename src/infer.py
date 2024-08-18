import cv2
import yt_dlp as youtube_dl
import os
from ultralytics import YOLO

# Define a fixed path for testing
# This path is where the downloaded video will be temporarily stored
temp_video_path = "/tmp/test_video.mp4"


# Function to download a YouTube video using yt_dlp
# Parameters:
#   url: The URL of the YouTube video to download
#   output_path: The path where the downloaded video will be saved
# This function uses yt_dlp to download the video with the best video and audio quality.
def download_youtube_video(url, output_path):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Download the best video and audio, merge if necessary
        "outtmpl": output_path,  # Specify the output path for the downloaded file
        "noplaylist": True,  # Do not download playlists, just the single video
        "merge_output_format": "mp4",  # Ensure the final output format is MP4
        "progress_hooks": [
            print_download_progress
        ],  # Optional: Hook to print download progress
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Download the video from the provided URL


# Function to print the download progress
# Parameters:
#   d: A dictionary containing download status information provided by yt_dlp
# This function is called by yt_dlp during the download process to indicate when a download has finished.
def print_download_progress(d):
    if d["status"] == "finished":
        print(
            f"Finished downloading: {d['filename']}"
        )  # Print the name of the downloaded file


# Load the YOLOv8 model
# The 'yolov8l' model is loaded for object detection tasks
# This model will be used to perform real-time inference on video frames
model = YOLO("yolov8l")


# Function to process the video in real-time
# Parameters:
#   video_path: The path to the video file to be processed
# This function reads the video frame by frame, performs object detection using the YOLO model,
# and prints a message whenever a "bottle" is detected in the video frames.
def process_video(video_path):
    print(f"Attempting to open video file: {video_path}")
    cap = cv2.VideoCapture(video_path)  # Open the video file

    if not cap.isOpened():
        # If the video file cannot be opened, print an error message and check if the file exists
        print("Error: Video file could not be opened.")
        if os.path.exists(video_path):
            print(f"File exists: {os.path.getsize(video_path)} bytes")
        else:
            print("File does not exist.")
        return

    frame_count = 0  # Initialize a counter for the frames processed

    while cap.isOpened():
        ret, frame = cap.read()  # Read a frame from the video
        if not ret:
            # If there are no more frames to read (end of video or error), exit the loop
            print("End of video or read error.")
            break

        frame_count += 1  # Increment the frame counter

        # Perform object detection on the current frame using the YOLO model
        results = model(frame)

        # Process each detection result in the current frame
        for result in results:
            if "bottle" in result.verbose():  # Check if a "bottle" was detected
                print(
                    f"Bottle detected at frame {frame_count}!"
                )  # Print a message with the frame number

    cap.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows


# Main function
# Parameters:
#   youtube_url: The URL of the YouTube video to download and process
# This is the main entry point of the script. It downloads the video, processes it, and then cleans up.
def main(youtube_url):
    print("Downloading YouTube video...")
    download_youtube_video(
        youtube_url, temp_video_path
    )  # Download the video from the provided URL

    print("Processing video...")
    process_video(temp_video_path)  # Process the downloaded video with the YOLO model

    # Clean up by removing the downloaded video file
    os.remove(temp_video_path)


# Entry point for the script execution
# Replace 'youtube_url' with the URL of the video you want to process
if __name__ == "__main__":
    youtube_url = (
        "https://www.youtube.com/watch?v=jYjjc1DWpQQ"  # Replace with your video URL
    )
    main(youtube_url)  # Call the main function with the provided YouTube URL
