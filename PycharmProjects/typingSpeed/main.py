import tkinter as tk    #tkinter for Building GUI
import random
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root      # It stores the Tkinter main window(the root window)
        self.root.title("Typing Speed Test")     #setting window title --> Typing Speed Test
        self.sample_text = ""
        self.current_word = ""
        self.start_time = None
        self.word_count = 0

        self.text_label = tk.Label(root, text="Type the following:")
        self.text_label.pack()     # Creating a label widget that displays --> Type the following:

        self.sample_text_label = tk.Label(root, text=self.generate_sample_text())
        self.sample_text_label.pack()       # displays the random sample text generated by generate_sample_text

        self.entry = tk.Entry(root)      #Creating an empty widget user will type the sample text
        self.entry.pack()         # Packing the Entry Widget in to the root window

        self.result_label = tk.Label(root, text="")      #Creating empty label widget which displays the typing speed result
        self.result_label.pack()

        self.entry.bind('<Key>', self.check_input)
        # check_input method will be called when a key is pressed in the entry widget to check the input

    def generate_sample_text(self):
        # Add more sample texts here.
        sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question."
        ]
        self.sample_text = random.choice(sample_texts)
        return self.sample_text

    def check_input(self, event):
        if self.start_time is None:    #This None indicates that typing has just started
            self.start_time = time.time()    # setting the current time to self.start_time using time.time()

        user_input = self.entry.get()    # getting the content from entry widget
        if user_input == self.sample_text:
            self.word_count = len(user_input.split())   #counting the number of words by splitting the text
            self.calculate_typing_speed()

    def calculate_typing_speed(self):
        end_time = time.time()     #recording the end time of the typing
        time_elapsed = end_time - self.start_time
        words_per_minute = int(self.word_count / (time_elapsed / 60))
        self.result_label.config(text=f"Your typing speed: {words_per_minute} WPM")

def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()