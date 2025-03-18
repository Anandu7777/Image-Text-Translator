
# Image Text Translator

A Python-based **Image Text Translator** using OCR and Google Translate. This application allows users to **extract text from an image**, translate it into multiple languages, and play the translated text as speech.

## Features 🚀
✅ **Extract text** from any image URL (JPEG, PNG, WEBP, HEIF, etc.)
✅ **Translate** extracted text into **Tamil, Hindi, Kannada, Telugu, Japanese, Malayalam**
✅ **Convert translated text into speech** (gTTS)
✅ **Modern UI with dark mode support** using `ttkbootstrap`
✅ **Progress alerts and error handling** for a smooth user experience
✅ **Auto-fixes image rotation** to improve OCR accuracy

---

## Installation 🔧
Ensure you have **Python 3.8+** installed. Then, install the required libraries:

```sh
pip install pillow pytesseract gtts deep-translator langcodes requests ttkbootstrap
```

---

## Usage 🛠
1. **Run the Application**
   ```sh
   python image_translator.py
   ```

2. **Enter an image URL** and click `Load`
3. **Select a language** for translation
4. Click `Translate` to extract & translate the text
5. Click `Play Speech` to listen to the translated text
6. Use `Clear` to reset the text box
7. Click `Quit` to exit

---

## Dependencies 📦
| Library          | Purpose |
|-----------------|------------------------------------------------|
| `pillow`        | Image handling (PIL)                          |
| `pytesseract`   | OCR (Optical Character Recognition)           |
| `gtts`          | Convert text to speech                        |
| `deep-translator` | Language translation using Google Translate |
| `langcodes`     | Handle language codes                         |
| `requests`      | Download images from URLs                     |
| `ttkbootstrap`  | Modern UI with dark mode support              |

---

## Notes 📌
- **Ensure Tesseract-OCR is installed** (for text extraction)
  - **Download**: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  - **Set path** in script:
    ```python
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

- **For Linux/Mac:** Replace `os.system("start translated_speech.mp3")` with:
  ```python
  os.system("mpg321 translated_speech.mp3")  # Linux
  os.system("afplay translated_speech.mp3")  # macOS
  ```

---

## Screenshots 🖼️
![image](https://github.com/user-attachments/assets/5bdda818-968f-497e-8daf-b58ea2c62089)
![image](https://github.com/user-attachments/assets/8f23210d-64a9-4eaf-8025-a012b6ab83bb)
![image](https://github.com/user-attachments/assets/7713329a-3500-4098-be80-c48daca87d28)





---

## License 📜
This project is open-source under the **MIT License**.

Feel free to contribute and enhance the project! 😊




