# COVID-19 FAQ Chatbot

## Overview

This project is a **GUI-based chatbot** designed to answer frequently asked questions (FAQs) about COVID-19. It is built using Python's `tkinter` for the user interface and the `SentenceTransformer` model from Hugging Face for generating BERT embeddings, allowing the chatbot to provide contextually relevant responses. The chatbot can handle a range of questions, such as symptoms, prevention, vaccines, and more.

## Features

- **Question Input**: Users can enter questions in a text box.
- **BERT Embeddings**: The chatbot uses `SentenceTransformer` to encode the input question and find the most similar pre-defined FAQ.
- **FAQ Database**: A pre-defined list of COVID-19 FAQs is stored, allowing the chatbot to quickly retrieve the closest match based on the embeddings.
- **GUI Components**: Includes a text input area for the question, a submit button to trigger the chatbot response, and an output text area to display the answer.
- **Image Integration**: The chatbot integrates images related to COVID-19 as part of the user interface.

## Requirements

Before running the chatbot, ensure the following Python packages are installed:

- `sentence-transformers`: To load and use BERT-based models for sentence embeddings.
- `tensorflow`: Required for deep learning model operations.
- `pillow`: For handling images.

Install the packages using the following command:


pip install sentence-transformers tensorflow pillow

## Code Summary

### Libraries Used

- **tkinter**: For building the graphical user interface (GUI).
- **messagebox**: Provides message alerts in the GUI.
- **sentence-transformers**: For loading pre-trained models to generate embeddings.
- **tensorflow**: For managing TensorFlow operations.
- **Pillow (PIL)**: Used for handling and displaying images.

### Key Functions

1. get_embedding(question):
   - Uses `SentenceTransformer` to convert the user's input question into an embedding for similarity comparison.
   
2. find_closest_faq(embedding):
   - Computes the cosine similarity between the input question's embedding and a list of pre-defined FAQ embeddings to find the most relevant FAQ.

3. respond_to_question():
   - Retrieves the user’s question, generates the embedding, finds the closest matching FAQ, and displays the answer in the GUI.
   
4. load_image(path, size):
   - Loads and resizes an image to enhance the UI.

### GUI Layout

- **Welcome Label**: Displays a welcome message for the user.
- **Image Integration**: Displays COVID-19 related images to make the interface more informative.
- **Question Input**: A text box where users can type their COVID-19 related questions.
- **Submit Button**: A button that triggers the chatbot to process the question and retrieve an answer.
- **Answer Display**: A text box that shows the chatbot's answer based on the closest matching FAQ.

## Running the Application

1. Ensure that all required packages are installed.
2. Save the script in a Python file (e.g., `chatbot.py`).
3. Run the script using a Python interpreter:
   python chatbot.py
4. The GUI window will open, allowing users to input questions, submit them, and receive responses.

## References

This project utilizes the following third-party libraries and models:

- **sentence-transformers**: A library that provides pre-trained BERT models for generating sentence embeddings.
  - [GitHub Repository](https://github.com/UKPLab/sentence-transformers)
  - [License](https://github.com/UKPLab/sentence-transformers/blob/master/LICENSE)

- **tensorflow**: An open-source platform developed by Google for deep learning and machine learning tasks.
  - [GitHub Repository](https://github.com/tensorflow/tensorflow)
  - [License](https://github.com/tensorflow/tensorflow/blob/master/LICENSE)

- **pillow**: A library for opening, manipulating, and saving various image formats.
  - [GitHub Repository](https://github.com/python-pillow/Pillow)
  - [License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)
