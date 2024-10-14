import os
import random
import string
import sys
import time
import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageDraw, ImageFont
import io
from PIL import ImageTk
import requests

# Function to generate a random CAPTCHA string
def generate_captcha_text(length=6):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Function to create CAPTCHA image
def create_captcha_image(captcha_text):
    image = Image.new('RGB', (200, 80), (255, 255, 255))  # white background
    font = ImageFont.load_default()  # You can use custom fonts here
    draw = ImageDraw.Draw(image)
    draw.text((50, 25), captcha_text, font=font, fill=(0, 0, 0))  # black text
    return image

# Function to check CAPTCHA
def check_captcha():
    user_input = entry.get()
    if user_input.upper() == captcha_text:
        messagebox.showinfo("Success", "CAPTCHA Verified!")
        sys.exit()
    else:
        messagebox.showwarning("Stop", "you are bot")
    time.sleep(10)
    url = "https://www.youtube.com/watch?v=_Fd5HXM2WQM"
    webbrowser.open(url)
    time.sleep(1)
    sys.exit()

# Function to refresh CAPTCHA
def refresh_captcha():
    global captcha_text
    captcha_text = generate_captcha_text()
    image = create_captcha_image(captcha_text)
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    captcha_image = ImageTk.PhotoImage(Image.open(img_byte_arr))
    captcha_label.config(image=captcha_image)
    captcha_label.image = captcha_image  # Keep a reference to avoid garbage collection

# Set up the GUI window
window = tk.Tk()
window.title("CAPTCHA Verification")

# Generate initial CAPTCHA
captcha_text = generate_captcha_text()

# Create and display CAPTCHA image
captcha_image = create_captcha_image(captcha_text)
img_byte_arr = io.BytesIO()
captcha_image.save(img_byte_arr, format='PNG')
img_byte_arr.seek(0)
captcha_image = ImageTk.PhotoImage(Image.open(img_byte_arr))

# CAPTCHA label
captcha_label = tk.Label(window, image=captcha_image)
captcha_label.pack()

# Textbox for user input
entry = tk.Entry(window)
entry.pack()

# Button to check CAPTCHA
submit_button = tk.Button(window, text="Submit", command=check_captcha)
submit_button.pack()

# Button to refresh CAPTCHA
refresh_button = tk.Button(window, text="Refresh CAPTCHA", command=refresh_captcha)
refresh_button.pack()

window.mainloop()
