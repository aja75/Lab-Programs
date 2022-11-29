# import library
import os
import cv2
import PySimpleGUI as sg
import getpass

# global variables

def frame_output():

    global output_folder

    # print("hello, this program will aid you in splitting AVI videos into TIFF frames\n")
    # print("""Desktop output on windows is: 'C:\\Users\\PC_NAME\\Desktop'""")
    # pathway = input("Input output pathway for frame output: ")
    # folder = input("Input file name to hold video frames: ")
    # folder = folder.lower()

    output_folder = pathway + "/" + folder
    os.mkdir(output_folder)

def video_frame_ripper():
    global counts
    counts = 0

    # video = input("Input file pathway for video: ")
    video_rip = cv2.VideoCapture(video)
    # print("\n")
    # print("Processing...")

    if video_rip.isOpened():
        while True:
            success, image = video_rip.read()

            if success:
                window['-WORKING-'].update("Working...")
                cv2.imwrite(os.path.join(output_folder, "frame{:d}.tiff".format(counts)), image)
                counts += 1

            else:
                break
                window['-WORKING-'].update("")
                window['-DONE-'].update("Success! {} images are extracted to {}.".format(counts, output_folder))


    else:
        exit("Error, video could not be opened!")

    # exit("Success! {} images are extracted to {}.".format(counts,output_folder))



def GUI():
    global pathway
    global folder
    global video
    global window
    global clicked

    font = ("Arial",11)
    title_font = ("Arial",20)

    clicked = ""
    computer_name = getpass.getuser()
    desktop = "C:\\Users\\" + computer_name + "\\Desktop'"
    icon = ""
    sg.theme('Dark Blue 12')

    Title_Text = [
    [sg.Text('Frame Ripper',font=title_font)],
    [sg.Text('Version alpha 1.5.0',font=font)],
    [sg.Text('Developed by Anthony Aceto',font=font)]

    ]

    Introduction_Text = [
        [sg.Text("")],
        [sg.Text("This program will aid you in splitting videos into frames")],
        [sg.Text("Input File Output Pathway")],
        [sg.Text("Desktop output on windows is:" + desktop)],
        [sg.Input(key='-PATHWAY-'),sg.FolderBrowse()],
        [sg.Text("Input File Output Name")],
        [sg.Input(key='-NAME-')],
        [sg.Text("Input File Pathway of Video")],
        [sg.Input(key='-VIDEO-'),sg.FileBrowse(key='vid_select')],
        [sg.Text(key='-WORKING-')],
        [sg.Text(key='-DONE-')],
        [sg.Submit(),sg.Cancel()]
    ]

    window = sg.Window(title="Frame Ripper a1.5.0",layout = [Title_Text,Introduction_Text],size = (450,500),icon=r"C:\Users\Natio\PycharmProjects\FrameRipper\Ripper.ico")

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        if event == 'Submit':
            pathway = values['-PATHWAY-']
            folder = values['-NAME-']
            video = values['-VIDEO-']

            folder = folder.lower()
            frame_output()
            video_frame_ripper()

            # window['-WORKING-'].update("Done!")
            # clicked = True
            break

def main():

    GUI()
    # frame_output()
    # video_frame_ripper()

main()