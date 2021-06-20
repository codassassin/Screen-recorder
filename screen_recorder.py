from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime
import shutil, os


# Folder_Name = ""
#
#
# def openLocation():
#     global Folder_Name
#     Folder_Name = filedialog.askdirectory()
#     if len(Folder_Name) > 1:
#         locationError.config(text=Folder_Name, fg="green")
#     else:
#         locationError.config(text="Please choose Folder!!", fg="red")


def record():
    choice = ytdChoices.get()
    # global Folder_Name
    # dest_folder = Folder_Name
    # print(dest_folder)

    if choice == 'Record screen only':
        while True:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            cv2.imshow('Screen Recorder', img_final)

            captured_video.write(img_final)
            if cv2.waitKey(20) == ord('q'):
                cv2.destroyAllWindows()
                break

    elif choice == 'Record screen and webcam':
        webcam = cv2.VideoCapture(0)

        while True:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            _, frame = webcam.read()

            frame = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), interpolation=cv2.INTER_AREA)
            fr_height, fr_width, _ = frame.shape

            img_final[0:fr_height, 0: fr_width, :] = frame[0:fr_height, 0:fr_width, :]
            cv2.imshow('Screen Recorder', img_final)

            captured_video.write(img_final)
            if cv2.waitKey(20) == ord('q'):
                cv2.destroyAllWindows()
                break

    else:
        print("Wrong choice!")

    # shutil.move(file_name, dest_folder)


###########################################################################
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
###########################################################################
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{timestamp}.mp4'
###########################################################################
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
###########################################################################

root = Tk()
root.title("Screen Recorder")
root.geometry("350x150")
root.columnconfigure(0, weight=1)


def Close():
    root.destroy()


# saveLabel = Label(root, text="Save the video file", font=("jost", 15, "bold"))
# saveLabel.grid()
#
# saveEntry = Button(root, width=10, bg="red", fg="white", text="Choose Path", command=openLocation)
# saveEntry.grid()
#
# locationError = Label(root, text="Error Msg of Path", fg="red", font=("jost", 10))
# locationError.grid()

ytdOption = Label(root, text="Choose an option", font=("jost", 15))
ytdOption.grid()

choices = ["Record screen only", "Record screen and webcam"]
ytdChoices = ttk.Combobox(root, values=choices, width=30)
ytdChoices.grid()

recordBtn = Button(root, text="RECORD", width=10, bg="lightblue", fg="white", command=record)
recordBtn.grid()

exit_button = Button(root, text="Exit", command=Close)
exit_button.grid()


developerLabel = Label(root, text="by @codassassin", font=("jost", 15))
developerLabel.grid()

root.mainloop()
