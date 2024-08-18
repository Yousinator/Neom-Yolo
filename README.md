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
   - Navigate to the directory where `install_packages.bat` is saved.
   - Run the script by typing:

     ```batch
     install_packages.bat
     ```

3. **Verify Installation**: After running the script, ensure that the packages are installed correctly by executing:

   ```python
   python -c "import cv2; import yt_dlp as youtube_dl; from ultralytics import YOLO"
   ```

   If no errors occur, the packages have been successfully installed.

### Troubleshooting

- If you encounter issues with Python or `pip`, ensure that Python is properly installed and added to your system PATH.
- If the installation fails, check for error messages in the Command Prompt and resolve any issues accordingly.

For further assistance, please refer to the documentation of the individual packages or seek support from the project maintainers.
