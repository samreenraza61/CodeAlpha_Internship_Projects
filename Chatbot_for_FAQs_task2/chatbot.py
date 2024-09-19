import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sentence_transformers import SentenceTransformer, util
from PIL import Image, ImageTk
import os

# Load BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define the FAQ data
faq_data = {
    "Question": [
        "What is COVID-19?", "How does COVID-19 spread?", "What are the symptoms of COVID-19?",
        "What should I do if I have symptoms?", "How can I protect myself from COVID-19?",
        "What is the difference between COVID-19 and the flu?", "What are the long-term effects of COVID-19?",
        "Can COVID-19 be spread by asymptomatic individuals?", "What is social distancing?", 
        "Can pets spread COVID-19?", "What should I do if I test positive for COVID-19?", 
        "What is the incubation period for COVID-19?", "Can COVID-19 be transmitted through food?", 
        "Can COVID-19 be transmitted through surfaces?", "What are the variants of COVID-19?",
        "What is contact tracing?", "What is a PCR test?", "What is a rapid antigen test?",
        "Do masks protect against COVID-19?", "Can vaccinated people still get COVID-19?",
        "What is herd immunity?", "How effective are COVID-19 vaccines?", 
        "Are there side effects to COVID-19 vaccines?", "What is long COVID?", 
        "How do COVID-19 vaccines work?", "Do I need a booster shot?", 
        "Can I take over-the-counter medications for COVID-19 symptoms?", 
        "What should I do if I’m exposed to COVID-19?", "How is COVID-19 treated?",
        "What is quarantine?", "What is isolation?", 
        "What is the role of ventilators in treating COVID-19?", 
        "Are there new treatments for COVID-19?", "How can I get tested for COVID-19?",
        "What is the difference between quarantine and isolation?", "What is COVID-19 reinfection?",
        "Can I get COVID-19 from a vaccine?", "What is the mortality rate of COVID-19?", 
        "What is a super-spreader event?", "How can I monitor my symptoms at home?", 
        "Can children get COVID-19?", "Should I wear gloves to protect against COVID-19?",
        "What is a COVID-19 immunity passport?", "Can pregnant women get vaccinated?", 
        "How long does immunity from the vaccine last?", "What is an mRNA vaccine?",
        "How do I protect high-risk individuals?", "Can I travel if I am vaccinated?",
        "What are the symptoms of COVID-19 in children?", "Can COVID-19 affect mental health?"
    ],
    "Answer": [
        "COVID-19 is an infectious disease caused by the SARS-CoV-2 virus.", 
        "COVID-19 spreads mainly through droplets generated when an infected person coughs, sneezes, or exhales.", 
        "Common symptoms include fever, dry cough, and tiredness. Other symptoms may include aches and pains, nasal congestion, headache, sore throat, or diarrhea.",
        "If you have symptoms, you should self-isolate, contact your healthcare provider, and follow local health guidelines.", 
        "To protect yourself, practice good hand hygiene, wear masks, maintain social distancing, and get vaccinated.",
        "COVID-19 and the flu have similar symptoms, but COVID-19 can cause more severe illness and has a higher risk of complications.",
        "Long-term effects of COVID-19 can include fatigue, difficulty breathing, and neurological symptoms like brain fog.",
        "Yes, COVID-19 can be spread by individuals who do not show symptoms of the disease.",
        "Social distancing involves keeping a physical distance from others to prevent the spread of the virus.",
        "Pets are not known to be a major source of COVID-19 transmission, but they can be infected in rare cases.",
        "If you test positive, you should self-isolate, inform close contacts, and follow local health guidelines.",
        "The incubation period for COVID-19 is typically 2 to 14 days after exposure to the virus.",
        "COVID-19 is not considered to be transmitted through food. However, it can be spread through contaminated surfaces.",
        "COVID-19 can be transmitted through surfaces, though this is not considered the primary mode of transmission.",
        "Variants of COVID-19 include Alpha, Beta, Gamma, Delta, and others, each with different mutations.",
        "Contact tracing involves identifying and informing people who may have been exposed to COVID-19.",
        "A PCR test detects the genetic material of the virus using a laboratory method called polymerase chain reaction.",
        "A rapid antigen test detects proteins from the virus and provides results more quickly than a PCR test.",
        "Masks can help protect against COVID-19 by reducing the spread of respiratory droplets.",
        "Yes, vaccinated people can still get COVID-19, but vaccines are highly effective in preventing severe illness.",
        "Herd immunity occurs when a large portion of the population becomes immune to a disease, reducing its spread.",
        "COVID-19 vaccines have been shown to be highly effective in preventing severe illness and hospitalization.",
        "Yes, COVID-19 vaccines can have side effects, such as sore arm, fatigue, or mild fever.",
        "Long COVID refers to symptoms that persist for weeks or months after the initial infection has resolved.",
        "COVID-19 vaccines work by stimulating the immune system to recognize and fight the virus.",
        "Booster shots may be recommended to maintain immunity over time, depending on current guidelines.",
        "Over-the-counter medications may help alleviate symptoms, but they do not cure COVID-19.",
        "If exposed to COVID-19, follow local quarantine guidelines and monitor for symptoms.",
        "Treatment for COVID-19 varies based on severity and may include antiviral medications, oxygen therapy, and supportive care.",
        "Quarantine is the practice of separating individuals who may have been exposed to the virus from those who are healthy.",
        "Isolation involves separating individuals who are infected with the virus from those who are not.",
        "Ventilators support breathing in patients with severe COVID-19 by providing mechanical assistance.",
        "New treatments for COVID-19 are continually being researched and developed.",
        "You can get tested for COVID-19 through local health services, clinics, and testing centers.",
        "Quarantine separates those exposed to the virus, while isolation separates those who are infected.",
        "COVID-19 reinfection occurs when a person contracts the virus again after recovering from an initial infection.",
        "You cannot get COVID-19 from a vaccine; vaccines are designed to prevent infection.",
        "The mortality rate of COVID-19 varies by region and population but is generally higher than the seasonal flu.",
        "A super-spreader event is a gathering where one or more individuals spread the virus to many others.",
        "Monitor symptoms at home by keeping track of fever, cough, and difficulty breathing, and seek medical advice if needed.",
        "Yes, children can get COVID-19, although they often experience milder symptoms than adults.",
        "Wearing gloves is not necessary for protection against COVID-19; hand hygiene and masks are more effective.",
        "A COVID-19 immunity passport is a document that may indicate a person’s vaccination status or immunity.",
        "Pregnant women can get vaccinated, but they should consult with their healthcare provider for personalized advice.",
        "Immunity from the vaccine can last several months, but booster shots may be required for ongoing protection.",
        "An mRNA vaccine uses messenger RNA to instruct cells to produce a protein that triggers an immune response.",
        "Protect high-risk individuals by ensuring they follow health guidelines and are vaccinated if eligible.",
        "Vaccinated individuals can travel, but they should follow travel guidelines and restrictions.",
        "Symptoms of COVID-19 in children can include fever, cough, and fatigue, similar to adults but often milder.",
        "COVID-19 can affect mental health, leading to anxiety, depression, and other psychological effects."
    ]
}

# Encode FAQ questions
faq_questions = faq_data['Question']
faq_answers = faq_data['Answer']
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

# Function to find the closest answer
def faq_chatbot(user_question):
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(user_embedding, faq_embeddings)
    best_match_idx = similarities.argmax().item()
    return faq_answers[best_match_idx]

# Function to handle user query
def handle_query():
    user_question = text_input.get("1.0", tk.END).strip()
    if not user_question:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return

    # Display loading message
    translated_text_output.config(state=tk.NORMAL)
    translated_text_output.delete("1.0", tk.END)
    translated_text_output.insert(tk.END, "Processing... Please wait.")
    translated_text_output.config(state=tk.DISABLED)

    # Run chatbot function
    response = faq_chatbot(user_question)
    translated_text_output.config(state=tk.NORMAL)
    translated_text_output.delete("1.0", tk.END)
    translated_text_output.insert(tk.END, f"Bot: {response}")
    translated_text_output.config(state=tk.DISABLED)
    ask_to_translate_again()

# Function to ask if the user wants to perform another query
def ask_to_translate_again():
    response = messagebox.askyesno("Ask Another Question?", "Do you want to ask another question?")
    if response:
        text_input.delete("1.0", tk.END)
        translated_text_output.config(state=tk.NORMAL)
        translated_text_output.delete("1.0", tk.END)
        translated_text_output.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Goodbye", "Thank you for using the chatbot!")

# Create the main window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("900x600")
root.configure(bg="#e0f7fa")  # Set background color to light blue

# Add a welcome label at the top
welcome_label = tk.Label(root, text="Welcome to the FAQ Chatbot!", font=("Arial", 24, "bold"), bg="#ffcc80", fg="#004d40")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Add an introductory message in a smaller font
intro_message = """Hello and thank you for reaching out.
I'm here to provide you with the latest and most accurate information about COVID-19.
Whether you have questions about symptoms, prevention, treatment, or anything else related to the pandemic, I'm here to help."""

# Display the intro message across multiple lines with a smaller font
intro_label = tk.Label(root, text=intro_message, font=("Arial", 14), bg="#e0f7fa", justify="left", wraplength=600)
intro_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

# Adding a sticker/image for better UI
img = Image.open("C:/Users/Lenovo/Downloads/chatbot.png")
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
    "C:/Users/Lenovo/Downloads/covid2.png",
    "C:/Users/Lenovo/Downloads/covid1.png",
    "C:/Users/Lenovo/Downloads/chatbot1.png"

]

# Display the additional images on the right side
for img_path in image_paths:
    img_tk = load_image(img_path, (100, 100))
    image_label = tk.Label(right_frame, image=img_tk, bg="#e0f7fa")
    image_label.image = img_tk  # Keep a reference to prevent garbage collection
    image_label.pack(pady=10)

# Text box to input the question
ttk.Label(root, text="Enter your question:", background="#e0f7fa", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10)
text_input = tk.Text(root, height=5, width=50, font=("Arial", 12))
text_input.grid(row=3, column=1, padx=10, pady=10)

# Button to trigger the chatbot response
translate_button = ttk.Button(root, text="Ask", command=handle_query)
translate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Text box to display the chatbot response
ttk.Label(root, text="Response:", background="#e0f7fa", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10)
translated_text_output = tk.Text(root, height=5, width=50, font=("Arial", 12), state=tk.DISABLED)
translated_text_output.grid(row=5, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
