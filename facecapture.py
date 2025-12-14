import cv2
import os


dataset_path = r"C:\face_database"
os.makedirs(dataset_path, exist_ok=True)


total_students = 25
max_images = 10  


cap = cv2.VideoCapture(0)

for i in range(total_students):
    student_name = input(f"\n[{i+1}/{total_students}] Enter full name of the student: ").strip()
    student_folder = os.path.join(dataset_path, student_name)
    os.makedirs(student_folder, exist_ok=True)

    print(f"[INFO] Capturing images for {student_name}")
    print("[INFO] Press 'c' to capture image, 'q' to quit.")

    image_count = 0
    while image_count < max_images:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to access webcam.")
            break

        cv2.imshow(f"Capturing for {student_name}", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            image_path = os.path.join(student_folder, f"{image_count + 1}.jpg")
            cv2.imwrite(image_path, frame)
            image_count += 1
            print(f"[✓] Saved {image_path}")

        elif key == ord('q'):
            print("[INFO] Quitting the program.")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    print(f"[INFO] Done capturing images for {student_name}.")

cap.release()
cv2.destroyAllWindows()