
# Language Translation Tool

## Overview

This project is a **GUI-based language translation tool** built using Python's `tkinter` library for the graphical user interface, and `transformers` from Hugging Face along with TensorFlow for translation capabilities. The tool allows users to input text in one language and receive the translated text in another. It supports multiple languages through pre-trained models from Helsinki-NLP's OPUS-MT.

## Features

- **Language Selection**: Users can select both the source and target languages from a dropdown menu.
- **Text Translation**: The tool uses pre-trained machine translation models to translate the input text.
- **GUI Components**: The application includes a text input area, a translate button, and a text area for displaying the translated output.
- **User Interaction**: After performing a translation, users can opt to translate another text.
- **Image Integration**: Additional images are displayed to enhance the UI experience.

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `transformers`: For loading and using pre-trained translation models.
- `tensorflow`: Required for handling TensorFlow-based models.
- `pillow`: For image loading and processing.

Install the packages using the following command:

```bash
pip install transformers tensorflow pillow
```

## Code Summary

### Libraries Used

- **tkinter**: For creating the graphical user interface (GUI).
- **ttk**: Provides additional GUI elements such as combo boxes and buttons.
- **messagebox**: Used for popup messages and alerts.
- **transformers**: Handles translation models and tokenizers.
- **tensorflow**: Manages model operations with TensorFlow.
- **Pillow (PIL)**: For image loading, resizing, and displaying.

### Key Functions

1. **`translate_text(text, source_lang, target_lang)`**:
   - Loads the pre-trained translation model and tokenizer for the selected language pair.
   - Encodes the input text and generates the translated text using the model.
   
2. **`perform_translation()`**:
   - Retrieves the selected source and target languages from the dropdown menus.
   - Fetches the input text from the text box, performs the translation, and displays the result in the GUI.
   - Handles errors and prompts the user to translate another text if desired.

3. **`ask_to_translate_again()`**:
   - Asks the user if they want to perform another translation and clears the text input if they agree.

4. **`load_image(path, size)`**:
   - Loads and resizes images for the GUI.

### GUI Layout

- **Welcome Label**: Displays a welcome message.
- **Image Integration**: Displays an initial image and additional images for UI enhancement.
- **Language Selection**: Dropdown menus for selecting the source and target languages.
- **Text Input**: Text box for entering text to be translated.
- **Translate Button**: Button to initiate the translation process.
- **Translated Text Output**: Text box to display the translated text.

## Running the Application

1. Ensure all required packages are installed.
2. Save the script in a Python file (e.g., `translation_tool.py`).
3. Run the script using a Python interpreter:

   ```bash
   python translation_tool.py
   ```

4. The GUI window will open, allowing you to input text, select languages, and view translations.

## References

This project utilizes the following third-party libraries and models:

- **transformers**: A library by Hugging Face providing state-of-the-art machine learning models for various NLP tasks.
  - [GitHub Repository](https://github.com/huggingface/transformers)
  - [License](https://github.com/huggingface/transformers/blob/main/LICENSE)

- **tensorflow**: An open-source platform developed by Google for machine learning and deep learning tasks.
  - [GitHub Repository](https://github.com/tensorflow/tensorflow)
  - [License](https://github.com/tensorflow/tensorflow/blob/master/LICENSE)

- **pillow**: A fork of the Python Imaging Library (PIL) that supports opening, manipulating, and saving many different image file formats.
  - [GitHub Repository](https://github.com/python-pillow/Pillow)
  - [License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)

- **Helsinki-NLP OPUS-MT Models**: Provides pre-trained models for machine translation tasks.
  - [Model Repository](https://github.com/Helsinki-NLP/opus-mt)
