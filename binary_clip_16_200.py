s tk
from tkinter import filedialog
import os

def extract_data():
    file_path = file_entry.get()
    start_point = start_entry.get()
    end_point = end_entry.get()

    if