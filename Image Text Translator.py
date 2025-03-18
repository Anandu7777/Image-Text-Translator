import os
import tempfile
import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, Text, WORD, END
from PIL import Image, ImageOps
from pytesseract import pytesseract
from gtts import gTTS
from deep_translator import GoogleTranslator
from ttkbootstrap.dialogs import Messagebox


class ImageTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Text Translator")
        master.geometry("700x500")
        master.resizable(False, False)

        # Title Label
        ttk.Label(master, text="📷 Image Text Translator", font=("Arial", 16, "bold"), bootstyle="primary").pack(pady=10)

        # URL Input
        self.url_var = StringVar()
        ttk.Label(master, text="Enter Image URL:", font=("Arial", 12)).pack(anchor="w", padx=20)
        frame = ttk.Frame(master)
        frame.pack(pady=5, padx=20, fill=X)
        self.url_entry = ttk.Entry(frame, textvariable=self.url_var, width=50, bootstyle="info")
        self.url_entry.pack(side=LEFT, expand=True, fill=X, padx=(0, 5))
        ttk.Button(frame, text="Load", command=self.load_image, bootstyle="primary").pack(side=LEFT)

        # Language Selection
        self.languages = {"Tamil": "ta", "Hindi": "hi", "Kannada": "kn", "Telugu": "te", "Japanese": "ja",
                          "Malayalam": "ml"}
        self.language_var = StringVar(value="Tamil")

        ttk.Label(master, text="Select Language:", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(10, 0))
        self.lang_menu = ttk.Combobox(master, textvariable=self.language_var, values=list(self.languages.keys()),
                                      state="readonly", bootstyle="success")
        self.lang_menu.pack(padx=20, pady=5, fill=X)

        # Buttons
        btn_frame = ttk.Frame(master)
        btn_frame.pack(pady=10, padx=20, fill=X)
        ttk.Button(btn_frame, text="Translate", command=self.translate_text, bootstyle="success").pack(side=LEFT,
                                                                                                       expand=True,
                                                                                                       padx=5)
        ttk.Button(btn_frame, text="Play Speech", command=self.play_speech, bootstyle="warning").pack(side=LEFT,
                                                                                                      expand=True,
                                                                                                      padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_textbox, bootstyle="danger").pack(side=LEFT, expand=True,
                                                                                                 padx=5)

        # Text Box for Displaying Output
        self.textbox = Text(master, width=80, height=10, wrap=WORD, font=("Arial", 12))
        self.textbox.pack(padx=20, pady=5, fill=BOTH, expand=True)

        # Quit Button
        ttk.Button(master, text="Quit", command=root.destroy, bootstyle="dark").pack(pady=10)

    def load_image(self):
        """Download image from URL"""
        url = self.url_var.get().strip()
        if not url:
            Messagebox.show_error("Please enter a valid image URL.", "Error")
            return

        try:
            self.image_path = self.download_image(url)
            Messagebox.show_info("Image downloaded successfully!", "Success")
        except Exception as e:
            Messagebox.show_error(f"Failed to download image: {str(e)}", "Error")

    def download_image(self, url):
        """Save image to a temporary file"""
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.img')
        temp_file.close()

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(temp_file.name, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception("Failed to download image.")

        return temp_file.name

    def translate_text(self):
        try:
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = path_to_tesseract

            img = Image.open(self.image_path)
            img = ImageOps.exif_transpose(img)  # Fix rotation
            text = pytesseract.image_to_string(img)

            if not text.strip():
                Messagebox.show_error("No text detected in the image.", "Error")
                return

            self.textbox.delete('1.0', END)
            self.textbox.insert(END, f"📜 Extracted Text:\n{text}\n\n")

            translated_text = GoogleTranslator(source='auto', target=self.languages[self.language_var.get()]).translate(
                text)
            self.textbox.insert(END, f"🌍 Translated Text ({self.language_var.get()}):\n{translated_text}\n\n")

            self.translated_text = translated_text
            self.save_speech()

        except Exception as e:
            Messagebox.show_error(f"Error: {str(e)}", "Translation Failed")

    def save_speech(self):
        """Convert text to speech"""
        language = self.languages[self.language_var.get()]
        speech = gTTS(text=self.translated_text, lang=language, slow=False)
        speech.save("translated_speech.mp3")
        self.textbox.insert(END, "🔊 Speech file saved as 'translated_speech.mp3' 🎧\n\n")

    def play_speech(self):
        """Play translated speech"""
        if os.path.exists("translated_speech.mp3"):
            os.system("start translated_speech.mp3")
        else:
            Messagebox.show_error("No speech file found!", "Error")

    def clear_textbox(self):
        self.textbox.delete('1.0', END)


# Run the App with ttkbootstrap styling
root = ttk.Window(themename="superhero")  # You can try "darkly", "cyborg", "flatly", etc.
app = ImageTranslatorApp(root)
root.mainloop()
