# CyberTool

CyberTool is a robust toolkit packed with essential features for cybersecurity professionals. From port scanning to threat intelligence integration, data processing, and graphical analysis, it offers everything you need to bolster your cyber defenses and stay ahead of threats.

## Prerequisites

Before using CyberTool, ensure you have the following dependencies installed:

- `pip install speech_recognition`
- `pip install mysql-connector-python`
- `pip install OTXv2`
- `pip install re`
- `pip install psutil`
- `pip install pandas`

## Installation and Usage

1. Download all the dependencies and extract the zip file to a folder.
2. Run the file named `CYBERTOOL.py`, which serves as the main program importing all the functions and tools.

### Notes

- CyberTool is designed for Linux machines only.
- To enable database functionality, update the following lines of code in the specified files:
  - `processlogs.py`: Update the MariaDB username and password (lines 50 and 51), and replace the file path to the `auth.log` file (line 31).
  - `processlogshttphttps.py`: Update the MariaDB username and password (lines 73 and 74).
  - `vtdatabase.py`: Update the MariaDB username and password (lines 21 and 22).
  - `exceltodb.py`: Update the MariaDB username and password (lines 31 and 32).
- Some functions prompt the user for the location of the file for data extraction. It's recommended to move the files you want to use to the same directory as the program.

## About the Author

CyberTool was created by Andre Llorente.
