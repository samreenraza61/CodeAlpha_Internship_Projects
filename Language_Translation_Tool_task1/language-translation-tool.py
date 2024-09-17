import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from PIL import Image, ImageTk
import threading

# List of languages supported by the model (not exhaustive but includes many)
languages = {
    "English": "en",
    "Spanish": "es",
    "German": "de",
    "French": "fr",
    "Italian": "it",
    "Dutch": "nl",
    "Russian": "ru",
    "Chinese (Simplified)": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Korean": "ko",
    "Turkish": "tr",
    "Swedish": "sv",
    "Hindi": "hi",
    "Urdu": "ur",
    "Hebrew": "he",
    "Greek": "el",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Polish": "pl",
    "Romanian": "ro",
    "Czech": "cs",
    "Finnish": "fi",
    "Hungarian": "hu",
    "Bulgarian": "bg",
    "Danish": "da",
    "Norwegian": "no",
    "Thai": "th",
    "Ukrainian": "uk",
}

# Load the model and tokenizer once at the start
def preload_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name, from_pt=True)
    return tokenizer, model

# Function to handle translation using the pre-loaded model
def translate_text(text, tokenizer, model):
    encoded_text = tokenizer(text, return_tensors="tf", padding=True, truncation=True)
    generated_tokens = model.generate(encoded_text['input_ids'])
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translated_text

# Function to perform translation asynchronously
def perform_translation_async():
    source_lang_code = languages.get(source_lang_var.get(), "en")
    target_lang_code = languages.get(target_lang_var.get(), "es")
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    # Display loading message
    translated_text_output.config(state=tk.NORMAL)
    translated_text_output.delete("1.0", tk.END)
    translated_text_output.insert(tk.END, "Translating... Please wait.")
    translated_text_output.config(state=tk.DISABLED)

    # Run the translation in a separate thread
    def run_translation():
        try:
            translated_text = translate_text(text, tokenizer, model)
            translated_text_output.config(state=tk.NORMAL)
            translated_text_output.delete("1.0", tk.END)
            translated_text_output.insert(tk.END, translated_text)
            translated_text_output.config(state=tk.DISABLED)
            ask_to_translate_again()
        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

    translation_thread = threading.Thread(target=run_translation)
    translation_thread.start()

# Function to ask if the user wants to perform another translation
def ask_to_translate_again():
    response = messagebox.askyesno("Translate Again?", "Do you want to translate another text?")
    if response:
        text_input.delete("1.0", tk.END)
        translated_text_output.config(state=tk.NORMAL)
        translated_text_output.delete("1.0", tk.END)
        translated_text_output.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Goodbye", "Thank you for using the translation tool!")

# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("900x600")
root.configure(bg="#e0f7fa")  # Set background color to light blue

# Add a welcome label at the top
welcome_label = tk.Label(root, text="Welcome to Language Translation Tool!", font=("Arial", 24, "bold"), bg="#ffcc80", fg="#004d40")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Adding a sticker/image for better UI
img = Image.open("C:/Users/Lenovo/Downloads/language.png")
img = img.resize((100, 100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=img, bg="#e0f7fa")
image_label.grid(row=0, column=2, padx=10, pady=20)

# Create a right-side frame for additional images
right_frame = tk.Frame(root, bg="#e0f7fa")
right_frame.grid(row=1, column=2, rowspan=5, padx=10, pady=10)

# Function to load and resize images
def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)  # Resize the image
    return ImageTk.PhotoImage(img)

# Paths of additional images
image_paths = [
    "C:/Users/Lenovo/Downloads/elearning.png",
    "C:/Users/Lenovo/Downloads/communication.png",
    "C:/Users/Lenovo/Downloads/languages.png"
]

# Display the additional images on the right side
for img_path in image_paths:
    img_tk = load_image(img_path, (100, 100))
    image_label = tk.Label(right_frame, image=img_tk, bg="#e0f7fa")
    image_label.image = img_tk  # Keep a reference to prevent garbage collection
    image_label.pack(pady=10)

# Create and place widgets for language selection and text input
ttk.Label(root, text="Source Language:", background="#e0f7fa", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
source_lang_var = tk.StringVar()
source_lang_menu = ttk.Combobox(root, textvariable=source_lang_var, values=list(languages.keys()), state="readonly", font=("Arial", 12))
source_lang_menu.grid(row=1, column=1, padx=10, pady=10)
source_lang_menu.set("English")

ttk.Label(root, text="Target Language:", background="#e0f7fa", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10)
target_lang_var = tk.StringVar()
target_lang_menu = ttk.Combobox(root, textvariable=target_lang_var, values=list(languages.keys()), state="readonly", font=("Arial", 12))
target_lang_menu.grid(row=2, column=1, padx=10, pady=10)
target_lang_menu.set("Spanish")

# Text box to input the text to be translated
ttk.Label(root, text="Text to Translate:", background="#e0f7fa", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10)
text_input = tk.Text(root, height=5, width=50, font=("Arial", 12))
text_input.grid(row=3, column=1, padx=10, pady=10)

# Button to trigger the translation
translate_button = ttk.Button(root, text="Translate", command=perform_translation_async)
translate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Text box to display the translated text
ttk.Label(root, text="Translated Text:", background="#e0f7fa", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10)
translated_text_output = tk.Text(root, height=5, width=50, font=("Arial", 12), state=tk.DISABLED)
translated_text_output.grid(row=5, column=1, padx=10, pady=10)

# Preload the model once when the application starts
tokenizer, model = preload_model("en", "es")

# Run the application
root.mainloop()
