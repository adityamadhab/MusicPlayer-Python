import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x400")
        self.playlist = []
        self.current_index = 0

        # Initialize Pygame
        pygame.mixer.init()

        # Create GUI
        self.create_gui()

    def create_gui(self):
        # Create playlist frame
        playlist_frame = tk.Frame(self.root)
        playlist_frame.pack(pady=20)

        # Create playlist label
        playlist_label = tk.Label(playlist_frame, text="Playlist")
        playlist_label.pack()

        # Create listbox to display playlist
        self.playlist_box = tk.Listbox(playlist_frame, selectmode=tk.SINGLE, height=10, width=40)
        self.playlist_box.pack()

        # Create buttons frame for the first line of buttons
        button_frame1 = tk.Frame(self.root)
        button_frame1.pack(pady=(0, 10))

        prev_button = tk.Button(button_frame1, text="<< Prev", command=self.prev_song)
        play_button = tk.Button(button_frame1, text="Play", command=self.play)
        pause_button = tk.Button(button_frame1, text="Pause", command=self.pause)
        next_button = tk.Button(button_frame1, text="Next >>", command=self.next_song)

        prev_button.pack(side=tk.LEFT)
        play_button.pack(side=tk.LEFT, padx=10)
        pause_button.pack(side=tk.LEFT)
        next_button.pack(side=tk.LEFT)

        # Create buttons frame for the second line of buttons
        button_frame2 = tk.Frame(self.root)
        button_frame2.pack(pady=(0, 20))

        add_button = tk.Button(button_frame2, text="Add to Playlist", command=self.add_to_playlist)
        remove_button = tk.Button(button_frame2, text="Remove from Playlist", command=self.remove_from_playlist)

        add_button.pack(side=tk.LEFT)
        remove_button.pack(side=tk.LEFT)

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def remove_from_playlist(self):
        if len(self.playlist_box.curselection()) > 0:
            selected_index = self.playlist_box.curselection()[0]
            del self.playlist[selected_index]
            self.playlist_box.delete(selected_index)

    def play(self):
        if pygame.mixer.music.get_busy() and not pygame.mixer.music.get_pos():
            pygame.mixer.music.unpause()
        elif self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def prev_song(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play()

    def next_song(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

