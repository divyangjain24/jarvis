import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import webbrowser
import time

class JarvisGUI:
    def __init__(self, root, assistant):
        self.root = root
        self.assistant = assistant
        self.root.title("Jarvis - Virtual Desktop Assistant")
        self.root.configure(bg="#1f1f1f")

        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="I am Kittu", font=("Roboto", 16), bg="#1f1f1f", fg="white")
        header_label.pack(pady=10)

        # Text Entry
        self.command_entry = tk.Entry(self.root, width=40, font=("Roboto", 12))
        self.command_entry.pack(pady=10)

        # Button Frame
        button_frame = tk.Frame(self.root, bg="#1f1f1f")
        button_frame.pack(pady=10)

        # Button
        submit_button = ttk.Button(button_frame, text="Submit", command=self.process_command, style="TButton")
        submit_button.pack(side=tk.LEFT, padx=10)

        # Microphone Button
        microphone_button = ttk.Button(button_frame, text="🎤", command=self.listen, style="TButton")
        microphone_button.pack(side=tk.RIGHT, padx=10)

    def process_command(self):
        command = self.command_entry.get()
        self.assistant.process_command(command)

    def listen(self):
        command = self.assistant.listen()
        self.command_entry.delete(0, tk.END)
        self.command_entry.insert(0, command)
        self.process_command()

class JarvisAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        """Function to convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Function to listen for user speech input"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

    def process_command(self, command):
        """Function to process user command and perform appropriate actions"""
        if "hello" in command:
            self.speak("Hello! I'm Kittu. How can I help you today?")
        elif "kanna" in command:
            self.speak("mein hu kaaliya")
        elif "what is the time" in command:
            current_time = time.strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}.")
        elif "open youtube" in command:
            self.speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
        elif "open whatsapp" in command:
            self.speak("Opening WhatsApp.")
            webbrowser.open("https://web.whatsapp.com/")
        elif "exit" in command:
            self.speak("Goodbye!")
            self.engine.stop()
            self.root.quit()
        else:
            self.speak("Sorry, I didn't understand that command.")

def main():
    root = tk.Tk()
    assistant = JarvisAssistant()
    style = ttk.Style(root)
    style.configure("TButton", foreground="black", background="#2d2d2d", font=("Roboto", 12))
    gui = JarvisGUI(root, assistant)
    root.mainloop()

if __name__ == "__main__":
    main()
