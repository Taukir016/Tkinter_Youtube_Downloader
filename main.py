from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#Filelocation
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        LocationError.config(text=Folder_Name,fg="green")

    else:
        LocationError.config(text="Please Choose Folder!!",fg="red")

#Downlaod Video
def DownloadVideo():
    choice = ytdchoice.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste link again!!",fg="red")

#Download Function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")


root = Tk()
root.title("YTD DOWNLOADER")
root.geometry("500x500") #Set window
root.columnconfigure(0,weight=1) #Set all content in center

#YTD Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#EntryBox
ytdEntryvar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryvar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error Msg",fg="Red",font=("jost",10))
ytdError.grid()

#Asking to save file label
SaveLabel = Label(root,text="Save the video file",font=("jost",15,"bold"))
SaveLabel.grid()

#Btn of Save file
SaveEntry = Button(root,width=10,bg="red",fg="white",text="Choose file",command=openLocation)
SaveEntry.grid()

#ErrorMsg Location
LocationError = Label(root,text="Error Msg of path",fg="red",font=("jost",15))
LocationError.grid()

#Download Quality
ytdquality = Label(root,text="Selectquality",font=("jost",15))
ytdquality.grid()

#ColoumnBox
choices = ["720p","144p","Only Audio"]
ytdchoice = ttk.Combobox(root,values=choices)
ytdchoice.grid()

#Download Btn
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

# Devloperlabel
devloperlabel = Label(root,text="Its Nomi Code",font=("jost",30))
devloperlabel.grid()
root.mainloop()