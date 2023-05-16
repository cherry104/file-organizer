
# File Organizer

Welcome to the File Organizer project! This Python script helps you organize your files based on their extensions. It automatically moves files with specific extensions into designated folders, making it easier to keep your files well-organized.

## Introduction
The File Organizer project is a simple Python script that scans a specified directory for files and moves them into separate folders based on their file extensions. This can be particularly useful if you have a cluttered folder containing various files of different types, such as music files (.mp3), video files (.mp4), or PDF documents (.pdf).


## Installation

To use the File Organizer, follow these steps:

- Clone this repository to your local machine or download the ZIP file.

```bash
  git clone https://github.com/cherry104/file-organizer.git
  cd my-project
```
- Ensure that you have Python 3.x installed on your system.
- Specify the path to the folder to be organized and the path to the existing folders where files should be organized.
- You're all set! Now you can use the File Organizer to organize your files.


## Usage

- Open a terminal or command prompt.
- Navigate to the project directory.

```bash
cd file-organizer
```

- Run the script by executing the following command:
```bash
python organize.py
```

- The File Organizer will scan the specified directory and move the files into separate folders based on their extensions.
- Once the process is complete, you will see a summary of the files moved and their destinations.



## Configuration

By default, the File Organizer script is pre-configured to handle common file extensions such as .mp3 , .mp4, and .pdf. However, you can customize the script by modifying the organize.py file.

In the organize.py file, you will find a dictionary called extensions. You can add, remove, or modify file extensions and their corresponding folder names within this dictionary.

Simply add a new entry with the desired extension as the key and the corresponding folder path as the value. When you run the script, it will  move the files accordingly.


## Contributing

Contributions are always welcome! If you'd like to contribute to the File Organizer project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.

## License

The File Organizer project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute the code as per the terms of the license.