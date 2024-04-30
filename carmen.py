import os
import tkinter as tk
from PIL import Image, ImageTk
import random
import time

class ProfessionalThiefGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professional Thief")

        self.images_path = "C:/Users/Nathaly/Desktop/Game based on Carmen Sandiego by Nathaly Fairlie Pearson Freitas/"
        self.countries = ["United States", "Canada", "Mexico", "Brazil", "Argentina", "France", "Germany", "Italy", "Russia", "China", "Japan", "Australia"]
        self.capitals = {
            "United States": "Washington, D.C.",
            "Canada": "Ottawa",
            "Mexico": "Mexico City",
            "Brazil": "Brasilia",
            "Argentina": "Buenos Aires",
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome",
            "Russia": "Moscow",
            "China": "Beijing",
            "Japan": "Tokyo",
            "Australia": "Canberra"
        }

        self.font_size = 15
        self.color = "black"

        self.start_x = 0
        self.start_y = 130
        self.start_xP = -200
        self.start_yP = 100

        self.target_country = random.choice(self.countries)
        self.target_capital = self.capitals[self.target_country]

        self.first_screen()
        self.animate()

    def first_screen(self):
        self.canvas = tk.Canvas(self, width=1000, height=1000)
        self.canvas.pack()

        self.canvas.create_text(500, 50, font=('Arial Black', 25), text="Welcome to Professional Thief!", fill=self.color)

        self.professional_thief_img = self.load_image('Professional thief.png')
        self.professional_thief = self.canvas.create_image(50, self.start_y, image=self.professional_thief_img)

        self.pol_run_img = self.load_image('pol_run.png')
        self.pol_run = self.canvas.create_image(50, self.start_yP, image=self.pol_run_img)

        self.canvas.create_text(500, 300, font=('Arial', self.font_size), text="A Professional Thief has stolen a valuable artifact and is on the run.", fill=self.color)
        self.canvas.create_text(500, 325, font=('Arial', self.font_size), text="Your mission is to track her down and recover the artifact.", fill=self.color)
        self.canvas.create_text(500, 350, font=('Arial', self.font_size), text="The Professional Thief was last seen in a country", fill=self.color)
        self.canvas.create_text(500, 375, font=('Arial', self.font_size), text="whose capital is: " + self.target_capital, fill=self.color)

    def animate(self):
        self.animate_pol()

    def animate_pol(self):
        self.start_xP += 5
        self.canvas.move(self.pol_run, 5, 0)
        if self.start_xP < 1000:
            self.after(50, self.animate_pol)
        else:
            self.show_wanted()

    def show_wanted(self):
        self.wanted_img = self.load_image('wanted.png')
        self.canvas.create_image(850, 100, image=self.wanted_img)

    def load_image(self, filename):
        image_path = os.path.join(self.images_path, filename)
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    app = ProfessionalThiefGame()
    app.mainloop()
