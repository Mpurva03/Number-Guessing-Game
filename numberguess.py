import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x400")

        # Initialize game variables
        self.target_number = random.randint(1, 100)
        self.guesses = 0

        # Load and resize images
        self.background_image = Image.open("background.png").resize((400, 400))  # Resize to fit canvas
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.happy_image = ImageTk.PhotoImage(Image.open("happy.png"))
        self.sad_image = ImageTk.PhotoImage(Image.open("sad.png"))
        self.neutral_image = ImageTk.PhotoImage(Image.open("neutral.png"))

        # Create a canvas and set the background image
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_photo)

        # Create and place widgets on the canvas
        self.label = tk.Label(root, text="Guess a number between 1 and 100", bg="white", font=("Arial", 12, "bold"))
        self.canvas.create_window(200, 50, window=self.label)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.canvas.create_window(200, 100, window=self.entry)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess, font=("Arial", 12))
        self.canvas.create_window(200, 150, window=self.guess_button)

        self.result_label = tk.Label(root, text="", bg="white", font=("Arial", 12, "bold"))
        self.canvas.create_window(200, 200, window=self.result_label)

        self.image_label = tk.Label(root, bg="white")
        self.canvas.create_window(200, 300, window=self.image_label)
        self.update_image(self.neutral_image)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        self.guesses += 1

        # Determine proximity and give feedback
        if guess < self.target_number:
            if self.target_number - guess <= 10:
                self.result_label.config(text="Low! Try again.")
            else:
                self.result_label.config(text="Too low! Try again.")
            self.update_image(self.sad_image)
        elif guess > self.target_number:
            if guess - self.target_number <= 10:
                self.result_label.config(text="High! Try again.")
            else:
                self.result_label.config(text="Too high! Try again.")
            self.update_image(self.sad_image)
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.guesses} tries!")
            self.update_image(self.happy_image)  # Show happy image when guessed correctly
            self.reset_game()

    def update_image(self, image):
        self.image_label.config(image=image)
        self.image_label.image = image

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.guesses = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.update_image(self.neutral_image)  # Reset to neutral image for the next game

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
