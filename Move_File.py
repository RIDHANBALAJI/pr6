

import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/HP/Downloads/"
to_dir = "C:/Users/HP/OneDrive/Desktop/Documents"

list_dir = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
#print(list_dir)


class Move_File(FileSystemEventHandler):

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        print("Hey,{event.src_path} has been created!")


    def on_deleted(self, event):
        name,extension=os.path.splitext(event.src_path)
        print("Oops! Someone deleted {event.src_path}")


    def on_modified(self, event):
        name,extension=os.path.splitext(event.src_path)
        print("Someone has modified {event.src_path}")

        

        for key,value in list_dir.items():
            time.sleep(1)
        if extension in value:
           file_name=os.path.basename(event.src_path)
           print("downloaded")
           path1=from_dir+'/'+file_name
           path2=to_dir+'/'+key
           path3=to_dir+'/'+key+'/'+file_name

           if os.path.exists(path2):
                print("Directory Exists...")
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)

                        
           else:
                print("Making Directory...")
                os.makedirs(path2)
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)

event_handler = Move_File()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()         

           
                    




    