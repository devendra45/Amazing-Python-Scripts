#Imports libraries
import moviepy.editor
from tkinter.filedialog import *

#Opens file
video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

#Converts to audio
audio.write_audiofile("audio.mp3")
print("Completed!")
