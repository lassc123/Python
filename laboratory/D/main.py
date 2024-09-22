import cv2
import dlib
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os

# 全局变量和初始化
DATABASE_FILE = 'face_database.csv'
# 这个检测器专门用于检测图像中的正面人脸
face_detector = dlib.get_frontal_face_detector()
# 这个预测器被训练用来识别人脸上的 68 个关键点，这些点包括眼睛、鼻子、嘴巴、下巴和脸部轮廓的轮廓
shape_predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")
# 这个模型被训练用来将人脸图像转换成128维的特征向量（也称为人脸描述符或嵌入）
face_recognizer = dlib.face_recognition_model_v1(r"dlib_face_recognition_resnet_model_v1.dat")
# 'name' 列存储这个人的名字 'features' 列存储这个人的人脸特征向量（通常是一个128维的数组）
database = pd.DataFrame(columns=['name', 'features'])

def load_database():
    global database
    if os.path.exists(DATABASE_FILE):
        try:
            database = pd.read_csv(DATABASE_FILE)
            # 执行这行代码后，'features'列中的每个元素都会从字符串形式转换回原来的数值数组形式
            database['features'] = database['features'].apply(eval)
            print(f"Loaded {len(database)} records from the database.")
        except Exception as e:
            print(f"Error loading database: {e}")
            database = pd.DataFrame(columns=['name', 'features'])
    else:
        print("No existing database found. Starting with an empty database.")

def save_database():
    try:
        # 这行代码将更新后的数据库保存到一个 CSV 文件中。
        database.to_csv(DATABASE_FILE, index=False)
        print(f"Database saved to {DATABASE_FILE}")
    except Exception as e:
        print(f"Error saving database: {e}")

class ImprovedFaceRecognitionGUI:
    def __init__(self, window):
        # 这行代码将传入的窗口对象赋值给类的 window 属性，使得这个窗口对象可以在类的其他方法中被访问和使用
        self.window = window
        # 这行代码将窗口的标题设置为 "Improved Face Recognition System"
        self.window.title("Improved Face Recognition System")

        # tk.Label() 创建一个 Tkinter 标签对象
        # window 是传入的父窗口对象，表示这个标签将被放置在主窗口中
        self.video_label = tk.Label(window)
        # 调用 pack() 会使标签显示在窗口中，默认位置是居中
        # 这个标签将作为显示实时视频流的容器。在后续的代码中，捕获的视频帧会被转换为图像并显示在这个标签上
        self.video_label.pack()

        # 这两行代码创建并放置了一个用于容纳控制按钮的框架（Frame）
        # tk.Frame() 创建一个 Tkinter 框架对象。
        # 框架（Frame）是一个容器组件，用于组织和布局其他组件。
        self.control_frame = tk.Frame(window)
        self.control_frame.pack()

        # tk.Button() 创建一个 Tkinter 按钮对象
        # self.control_frame: 这是按钮的父容器，即之前创建的控制框架。这意味着按钮将被放置在这个框架内。
        # text="Add Face": 设置按钮上显示的文本。
        # command=self.add_face: 指定当按钮被点击时要执行的函数。
        self.add_face_button = tk.Button(self.control_frame, text="Add Face", command=self.add_face)
        # side=tk.LEFT 是pack()方法的一个参数，指定了按钮应该被放置在其父容器（在这里是control_frame）的左侧
        self.add_face_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT)

        # 这行代码创建了一个新的标签控件用于显示状态信息
        self.status_label = tk.Label(window, text="")
        self.status_label.pack()

        # cv2.VideoCapture(): 这是OpenCV库中用于创建视频捕获对象的函数。
        # 0: 作为参数传递给VideoCapture()，表示使用默认的摄像头。在多摄像头系统中，0通常代表第一个摄像头。
        self.cap = cv2.VideoCapture(0)
        self.is_paused = False

        self.update_frame()

    def update_frame(self):
        if not self.is_paused:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 这里直接调用face_detector对象，将灰度图像作为参数传入。
                # 检测器会在整个图像中搜索人脸。
                # 返回值 faces：
                #     这是一个包含所有检测到的人脸位置的列表。
                #     每个人脸通常表示为一个矩形区域（包含左上角和右下角的坐标）。
                faces = face_detector(gray)
                
                if len(faces) == 0:
                    self.show_status("No face detected", "red")
                else:
                    self.show_status("Face(s) detected", "green")

                for face in faces:
                    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
                    # cv2.rectangle()：
                    #     这是OpenCV库中用于在图像上绘制矩形的函数
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 这行代码将OpenCV格式的图像转换为PIL (Python Imaging Library) 格式的图像。
                # Image.fromarray(): 这是PIL库中的一个函数，用于从numpy数组创建一个PIL图像对象。
                # 这行代码的目的是将OpenCV格式的图像转换为PIL格式。
                # 这种转换通常是必要的，因为Tkinter的PhotoImage类更容易处理PIL格式的图像。
                # 这是在OpenCV和Tkinter之间创建图形用户界面时常见的一个步骤，允许在Tkinter窗口中显示从摄像头捕获的图像。
                img = Image.fromarray(img)
                # 这行代码将PIL格式的图像转换为Tkinter可以使用的PhotoImage对象。
                imgtk = ImageTk.PhotoImage(image=img)
                # self.video_label: 这是类中定义的一个Tkinter Label控件，用于显示视频帧。
                # .imgtk: 这不是Tkinter Label的标准属性，而是一个自定义属性。它的作用是保持对图像对象的引用。
                # 通过将图像对象赋值给标签的一个属性，可以确保图像对象不会被垃圾回收，从而能够正确显示在界面上。
                self.video_label.imgtk = imgtk
                # 这行代码的作用是将Label控件的图像更新为新的帧,通过不断执行这个操作，可以在GUI中显示实时的视频流。
                self.video_label.configure(image=imgtk)
            else:
                self.show_status("Failed to capture image", "red")

        # 这行代码设置了一个定时器，用于周期性地调用update_frame方法。
        # .after(): 这是Tkinter的一个方法，用于在指定的延迟后执行一个函数。
        self.window.after(10, self.update_frame)

    def extract_features(self, frame, face):
        try:
            shape = shape_predictor(frame, face)
            return np.array(face_recognizer.compute_face_descriptor(frame, shape))
        except Exception as e:
            self.show_status(f"Feature extraction failed: {str(e)}", "red")
            return None

    def add_face(self):
        # 用于检查视频是否处于暂停状态
        if self.is_paused:
            self.show_status("Please unpause the video to add a face", "red")
            return

        # 这行代码使用 Tkinter 的 simpledialog 模块来创建一个输入对话框，让用户输入人脸对应的名字
        # simpledialog.askstring()：
        #     这是 Tkinter 提供的一个函数，用于创建一个简单的对话框来获取用户输入的字符串
        name = simpledialog.askstring("Input", "Enter name for the face:")
        if name:
            # 这行代码使用OpenCV库来从摄像头捕获一帧图像
            # self.cap：
            #     这是一个VideoCapture对象，通常在类的初始化方法中创建（如 self.cap = cv2.VideoCapture(0)）。
            #     它代表了与摄像头的连接。
            # ret：一个布尔值，表示帧是否被正确读取。
            # frame：如果帧被成功读取，这将是一个包含图像数据的numpy数组；如果读取失败，则为None。
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector(gray)
                if len(faces) == 1:
                    # 这行代码调用了一个名为 extract_features 的方法来从检测到的人脸中提取特征
                    features = self.extract_features(frame, faces[0])
                    if features is not None:
                        global database
                        # 这行代码创建了一个新的 pandas DataFrame，用于存储新添加的人脸信息
                        # features.tolist():
                        #     将 NumPy 数组 features 转换为 Python 列表。
                        #     这是为了确保特征数据可以被正确地存储在 DataFrame 中。
                        new_data = pd.DataFrame({'name': [name], 'features': [features.tolist()]})
                        # 这行代码将新创建的人脸数据添加到现有的数据库中
                        # [database, new_data]: 这是一个列表，包含要合并的 DataFrame 对象。
                        # database 是现有的数据库，new_data 是新创建的包含新人脸信息的 DataFrame。
                        # ignore_index=True: 这个参数告诉 concat 函数忽略原有的索引，并创建一个新的连续索引。
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
        # 如果视频捕获原本在运行（is_paused 为 False），执行后会暂停（is_paused 变为 True）。
        # 如果视频捕获原本已暂停（is_paused 为 True），执行后会恢复运行（is_paused 变为 False）。
        self.is_paused = not self.is_paused
        if self.is_paused:
            # 这行代码的作用是将暂停按钮的文本从原来的文本（可能是"Pause"）更改为"Resume"。
            # .config(): 这是Tkinter控件的一个方法，用于修改控件的配置或属性。
            self.pause_button.config(text="Resume")
            self.show_status("Video paused", "blue")
        else:
            self.pause_button.config(text="Pause")
            self.show_status("Video resumed", "blue")

    def show_status(self, message, color):
        self.status_label.config(text=message, fg=color)

def main():
    load_database()
    # 这行代码是创建一个Tkinter应用程序的主窗口
    root = tk.Tk()
    # 这行代码是创建了一个 ImprovedFaceRecognitionGUI 类的实例
    app = ImprovedFaceRecognitionGUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (save_database(), root.destroy()))
    root.mainloop()

if __name__ == "__main__":
    main()