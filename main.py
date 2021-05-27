#! /usr/bin/python3.8

import tkinter as tk
import os, platform

root = tk.Tk()
root.geometry("400x100")
root.title("Video Downloader")

entries_frame = tk.Frame(root)
entries_frame.grid(row=0,column=0)

options_frame = tk.Frame(root)
options_frame.grid(row=0,column=1)

link_label = tk.Label(entries_frame, text='Link')
link_label.grid(row=0,column=0)
link_entry = tk.Entry(entries_frame)
link_entry.grid(row=0,column=1)

location_label = tk.Label(entries_frame, text='Location')
location_label.grid(row=1,column=0)
location_entry = tk.Entry(entries_frame)
location_entry.grid(row=1,column=1)
location_default_label = tk.Label(entries_frame, text='(default = current \n\tdirectory)')
location_default_label.grid(row=1,column=2)


def download_video(option_1='', option_2='', option_3=''):
    print(os.getcwd())
    link = link_entry.get()
    location = location_entry.get()
    if location == '':
        location = '.'
    print(link)
    print(location)
    os.chdir(location)
    try:
        os.system(f'youtube-dl {link}')
        done_toplevel = tk.Toplevel(root)
        done_label = tk.Label(done_toplevel,text='Download completed!')
        done_label.pack()
        exit_done_toplevel = tk.Button(done_toplevel,text='Ok',command=done_toplevel.destroy)
        exit_done_toplevel.pack()
    except:
        os.system('pip install youtube-dl')
        os.system(f'youtube-dl {link}')

download_button = tk.Button(entries_frame, text='Download',command=download_video)
download_button.grid(row=2,column=0)
exit_button = tk.Button(entries_frame, text='Exit',command=root.destroy)
exit_button.grid(row=2,column=1)


root.mainloop()
