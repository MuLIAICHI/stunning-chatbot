import openai
import config
import tkinter as tk
import customtkinter

# Load your API key from an environment variable or secret management service
# openai.api_key = config.Open_AI_KEY

# Get the response :
# response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

# The UI :

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x340")
app.grid_columnconfigure(0, weight=1)

def process_input(input_text):
    # Your custom function that processes the input_text
    openai.api_key = config.Open_AI_KEY
    response = openai.Completion.create(model="text-davinci-003", prompt=input_text, temperature=0, max_tokens=7)
    return response['choices'][0]['text']

def get_input_and_process():
    # Get the input from the Text widget
    input_text = textboxU.get("1.0", tk.END).strip()
    textboxD.delete("1.0", tk.END)
    textboxD.insert(tk.END, process_input(input_text))


# Textbox U

textboxU = customtkinter.CTkTextbox(master=app, text_color="white", width=350, height=100)
textboxU.grid(row=0, column=0, padx=20, pady=20, sticky="ew")


# Use CTkButton

button = customtkinter.CTkButton(master=app, text="Submit", command=get_input_and_process)
button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

# Textbox D


textboxD = customtkinter.CTkTextbox(master=app, text_color="white", width=350, height=100)
textboxD.grid(row=2, column=0, padx=20, pady=20, sticky="ew")


app.mainloop()