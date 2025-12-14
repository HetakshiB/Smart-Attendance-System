import os
import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime

dataset_path = r"C:\clean_face_database"

known_face_encodings = []
known_face_names = []

print("Loading known faces...")


for student_name in os.listdir(dataset_path):
    student_folder = os.path.join(dataset_path, student_name)
    if not os.path.isdir(student_folder):
        continue

    for filename in os.listdir(student_folder):
        filepath = os.path.join(student_folder, filename)
        image = face_recognition.load_image_file(filepath)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0:
            continue 

        encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(student_name)

unique_students = set(known_face_names)
attendance_dict = {name: "Absent" for name in unique_students}

print(f"Loaded encodings for {len(unique_students)} students.")


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Webcam started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

 
    small_face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
    small_face_encodings = face_recognition.face_encodings(rgb_small_frame, small_face_locations)

    face_names = []

    for face_encoding in small_face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        face_names.append(name)

        
        if name != "Unknown":
            attendance_dict[name] = "Present"

    
    for (top, right, bottom, left), name in zip(small_face_locations, face_names):
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)

        display_text = f"{name} - Present" if name != "Unknown" else "Unknown"
        cv2.putText(frame, display_text, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Real-time Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


attendance_file = f"Attendance_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
with open(attendance_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Attendance"])
    for name in sorted(attendance_dict.keys()):
        writer.writerow([name, attendance_dict[name]])
print(f"\nAttendance saved to {attendance_file}")


print("\nPresent Students:")
for name in sorted(attendance_dict.keys()):
    if attendance_dict[name] == "Present":
        print(f"- {name}")
