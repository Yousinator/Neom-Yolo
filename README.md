## Setup

To get started with this project, follow these steps to install the required Python packages:

### Prerequisites

1. **Python Installation**: Ensure that Python is installed on your system. You can download Python from the [official website](https://www.python.org/downloads/). Make sure to add Python to your system PATH during installation.

2. **Git Installation**: Ensure that Git is installed on your system. You can download Git from the [official website](https://git-scm.com/downloads).

### Clone the Repository

1. **Clone the Repository**: Open Command Prompt or PowerShell and run the following command to clone the repository:

   ```bash
   git clone https://github.com/Yousinator/Neom-Yolo.git
   ```

2. **Navigate to the Project Directory**: Change to the project directory:

   ```bash
   cd Neom-Yolo
   ```

### Running the Setup Script

1. **Download or Clone the Project**: Ensure you have the project files on your local machine. If you haven’t already, you can clone the repository or download the project files.

2. **Run the Batch Script**:

   - Open Command Prompt (you may need to run it as Administrator).
   - Navigate to the directory where `setup.bat` is saved.
   - Run the script by typing:

     ```batch
     setup.bat
     ```

3. **Verify Installation**: After running the script, ensure that the packages are installed correctly by executing:

   ```python
   python -c "import cv2; import yt_dlp as youtube_dl; from ultralytics import YOLO"
   ```

   If no errors occur, the packages have been successfully installed.

### `infer.py` File

The main Python script is located in the `src` directory and is responsible for downloading a YouTube video and processing it using a pre-trained YOLOv8 model to detect objects within the video frames.

#### Script Functionality

- **Video Download**: The script uses `yt_dlp` to download a YouTube video specified by a URL. The video is saved to a temporary location on your local machine.

- **Object Detection**: After downloading, the script processes the video frame-by-frame. It uses the YOLOv8 model from the `ultralytics` package to detect objects within each frame. For example, the script is set up to print a message whenever it detects a "bottle" in the video.

- **Clean Up**: Once the video processing is complete, the script deletes the downloaded video file from your system.

#### How to Run the Script

1. **Navigate to the `src` Directory**: Before running the script, navigate to the `src` directory where the script is located:

   ```bash
   cd src
   ```

2. **Run the Python Script**: Execute the script with the following command:

   ```bash
   python infer.py
   ```

3. **Post-Processing**: After the script finishes processing the video, it will automatically clean up by removing the temporary video file.

**Script Example Use Case:**

This script is useful for tasks such as automated content moderation, where specific objects need to be detected in video content. By customizing the object detection logic within the script, it can be adapted for various purposes like surveillance, video analysis, or media content filtering.

### Troubleshooting

- If you encounter issues with Python or `pip`, ensure that Python is properly installed and added to your system PATH.
- If the installation fails, check for error messages in the Command Prompt and resolve any issues accordingly.

For further assistance, please refer to the documentation of the individual packages or seek support from the project maintainers.
