import cv2
import dlib
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import os

# 全局变量和初始化
DATABASE_FILE = 'face_database.csv'
face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(r"D:\Code\Python\laboratory\D\shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1(r"D:\Code\Python\laboratory\D\dlib_face_recognition_resnet_model_v1.dat")
database = pd.DataFrame(columns=['name', 'features'])

def load_database():
    global database
    if os.path.exists(DATABASE_FILE):
        try:
            database = pd.read_csv(DATABASE_FILE)
            database['features'] = database['features'].apply(eval)
            print(f"Loaded {len(database)} records from the database.")
        except Exception as e:
            print(f"Error loading database: {e}")
            database = pd.DataFrame(columns=['name', 'features'])
    else:
        print("No existing database found. Starting with an empty database.")

def save_database():
    try:
        database.to_csv(DATABASE_FILE, index=False)
        print(f"Database saved to {DATABASE_FILE}")
    except Exception as e:
        print(f"Error saving database: {e}")

class ImprovedFaceRecognitionGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Improved Face Recognition System")

        self.video_label = tk.Label(window)
        self.video_label.pack()

        self.control_frame = tk.Frame(window)
        self.control_frame.pack()

        self.add_face_button = tk.Button(self.control_frame, text="Add Face", command=self.add_face)
        self.add_face_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(window, text="")
        self.status_label.pack()

        self.cap = cv2.VideoCapture(0)
        self.is_paused = False

        self.update_frame()

    def update_frame(self):
        if not self.is_paused:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector(gray)
                
                if len(faces) == 0:
                    self.show_status("No face detected", "red")
                else:
                    self.show_status("Face(s) detected", "green")

                for face in faces:
                    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            else:
                self.show_status("Failed to capture image", "red")

        self.window.after(10, self.update_frame)

    def extract_features(self, frame, face):
        try:
            shape = shape_predictor(frame, face)
            return np.array(face_recognizer.compute_face_descriptor(frame, shape))
        except Exception as e:
            self.show_status(f"Feature extraction failed: {str(e)}", "red")
            return None

    def add_face(self):
        if self.is_paused:
            self.show_status("Please unpause the video to add a face", "red")
            return

        name = simpledialog.askstring("Input", "Enter name for the face:")
        if name:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector(gray)
                if len(faces) == 1:
                    features = self.extract_features(frame, faces[0])
                    if features is not None:
                        global database
                        new_data = pd.DataFrame({'name': [name], 'features': [features.tolist()]})
                        database = pd.concat([database, new_data], ignore_index=True)
                        save_database()
                        self.show_status(f"Added {name} to the database", "green")
                    else:
                        self.show_status("Failed to extract features", "red")
                elif len(faces) == 0:
                    self.show_status("No face detected", "red")
                else:
                    self.show_status("Multiple faces detected. Please ensure only one face is visible.", "red")
            else:
                self.show_status("Failed to capture image", "red")

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
            self.show_status("Video paused", "blue")
        else:
            self.pause_button.config(text="Pause")
            self.show_status("Video resumed", "blue")

    def show_status(self, message, color):
        self.status_label.config(text=message, fg=color)

def main():
    load_database()
    root = tk.Tk()
    app = ImprovedFaceRecognitionGUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (save_database(), root.destroy()))
    root.mainloop()

if __name__ == "__main__":
    main()