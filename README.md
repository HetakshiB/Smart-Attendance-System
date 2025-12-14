The Smart Attendance System is an automated attendance management solution that uses face recognition technology to identify students and mark their attendance accurately.
This system eliminates manual attendance, reduces proxy attendance, and improves efficiency by using real-time face detection and recognition.

Technologies Used
Python
OpenCV
face_recognition library
OS & Shutil modules
CSV file handling
Webcam (real-time video capture)

System Workflow
Firstly, the system asks for the user’s name.
Then, it captures the image using the camera.
After that, the system processes the image using face recognition.
If the face matches the stored data, attendance is marked automatically.
Finally, the attendance record is saved in the database (CSV file).

Project Structure
Smart-Attendance-System/
│
├── face_capture.py          # Captures face images using webcam
├── face_cleaning.py         # Filters and stores only clear face images
├── attendance_monitor.py    # Recognizes faces & marks attendance
├── face_database/           # Raw captured face images
├── clean_face_database/     # Clean & verified face images
├── attendance.csv           # Auto-generated attendance record
└── README.md

Face Capture Module
This module captures student face images using a webcam.

Features
Prompts for student name
Captures multiple images per student
Stores images in a structured folder format
Manual capture using keyboard controls

Controls
Press c → Capture image
Press q → Quit program

Images are stored in:
C:\face_database\Student_Name\

Face Cleaning Module
This module filters the captured images and keeps only clear and recognizable faces.

What it does
Scans each captured image
Detects faces using face_recognition
Accepts images with exactly one face

Discards:
Blurred images
Multiple faces
No face detected

Clean images are saved to:
C:\clean_face_database\Student_Name\

Attendance Monitoring Module
This module performs real-time face recognition and attendance marking.

Functionality
Opens webcam for live monitoring
Detects faces in real time

Displays:
Bounding box
Student name
Matches faces with clean database
Automatically marks detected students as Present

Attendance Output
Attendance is saved automatically in a CSV file
Only students detected during the session are marked present
File is created when the camera session ends

Example:
attendance.csv
Key Advantages
Fully automated attendance system
High accuracy using face recognition
Eliminates fake/proxy attendance
Easy to use and scalable
Real-time detection and storage

Future Enhancements
GUI integration
Cloud database support
Mobile camera integration
Timestamp-based attendance
Admin dashboard

How to Run the Project

Install dependencies:
pip install opencv-python face_recognition

Run face capture script:
python face_capture.py

Clean the captured images:
python face_cleaning.py

Start attendance monitoring:
python attendance_monitor.py
