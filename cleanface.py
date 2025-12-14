import os
import shutil
import face_recognition

source_dir = r"C:\face_database"
clean_dir = r"C:\clean_face_database"

if not os.path.exists(clean_dir):
    os.makedirs(clean_dir)

print("Scanning and copying clean face images...")

for student_name in os.listdir(source_dir):
    student_path = os.path.join(source_dir, student_name)
    if not os.path.isdir(student_path):
        continue

    clean_student_path = os.path.join(clean_dir, student_name)
    os.makedirs(clean_student_path, exist_ok=True)

    for image_name in os.listdir(student_path):
        image_path = os.path.join(student_path, image_name)

        try:
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)

            if len(face_locations) == 1:
              
                shutil.copy(image_path, clean_student_path)
                print(f"Copied clean image: {image_name} from {student_name}")
            else:
                print(f" Skipped {image_name} from {student_name} - Faces found: {len(face_locations)}")

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

print("Done! Clean images copied to C:\\clean_face_database")
