import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
VELOCITY = 30
DELAY = 0.08 
MAX_WRONG_GUESSES = 3

class ProfessionalThiefGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professional Thief")

        self.images_path = r"C:\Users\shift\Desktop\Professional-thief-Base-on-Carmem"
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

        self.flags = {
            "United States": "United_States-Flag.png",
            "Canada":"Canada-Flag.png",
            "Mexico": "Mexico-Flag.png",
            "Brazil": "Brazil-Flag.png",
            "Argentina": "Argentina-Flag.png",
            "France": "France-Flag.png",
            "Germany": "Germany-Flag.png",
            "Italy": "Italy-Flag.png",
            "Russia": "Russia-Flag.png",
            "China": "China-Flag.png",
            "Japan": "Japan-Flag.png",
            "Australia": "Australia-Flag.png"
        }

        self.font_size = 15
        self.color = "black"

        self.start_x = 0
        self.start_y = 130
        self.start_xP = -200
        self.start_yP = 100

        self.wrong_guesses = 0  # Inicializa o contador de respostas erradas
        self.target_country = random.choice(self.countries)
        self.target_capital = self.capitals[self.target_country]

        self.create_canvas()
        self.first_screen()
        self.animate()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

    def first_screen(self):
        self.canvas.create_text(500, 50, font=('Arial Black', 25), text="Welcome to Professional Thief!", fill=self.color)

        self.professional_thief_img = self.load_image('Professional thief.png')
        self.professional_thief = self.canvas.create_image(50, 180, image=self.professional_thief_img)

        self.pol_run_img = self.load_image('pol_run.png')
        self.pol_run = self.canvas.create_image(-110,180, image=self.pol_run_img)

        welcome_text = "Welcome to Professional Thief!\n\n"
        welcome_text += "A Professional Thief has stolen a valuable artifact and is on the run.\n\n"
        welcome_text += "Your mission is to track her down and recover the artifact.\n\n"
        welcome_text += f"The Professional Thief was last seen in a country whose capital is: {self.target_capital}"

        self.canvas.create_text(500, 375, font=('Arial', self.font_size), text=welcome_text, fill=self.color, anchor=tk.CENTER)     
    def animate(self):
        self.animate_pol()
        self.animate_thief()

    def animate_pol(self):
        self.start_xP += VELOCITY
        self.canvas.move(self.pol_run, VELOCITY, 0)
        if self.start_xP < CANVAS_WIDTH:
            self.after(int(DELAY * 1000), self.animate_pol)
        else:
            self.show_wanted()

    def animate_thief(self):
        self.start_x += VELOCITY
        self.canvas.move(self.professional_thief, VELOCITY, 0)
        if self.start_x < CANVAS_WIDTH:
            self.after(int(DELAY * 1000), self.animate_thief)
 
   
    def show_wanted(self):
        self.wanted_img = self.load_image('wanted.png')
        self.canvas.create_image(500, 170, image=self.wanted_img)
        # Chama a função para mostrar a caixa de texto após a imagem "wanted"
        self.after(int(DELAY * 1000), self.show_input_box(confirm_command=self.check_input))
        
    
    
    def show_input_box(self, confirm_command=None):
        self.input_entry = tk.Entry(self, font=('Arial', self.font_size))
        self.input_entry.place(x=350, y=500)
        
        self.confirm_button = tk.Button(self, text="Confirmar", command=confirm_command)
        self.confirm_button.place(x=600, y=500)

    
    def check_input(self):
        guess = self.input_entry.get().strip().title()
        self.previusly_country = guess  # Salvando a tentativa anterior

        if guess == self.target_country:
            messagebox.showinfo("contatulations","Correct Answer")
            self.target_country = random.choice(self.countries)
            self.target_capital = self.capitals[self.target_country]
            self.target_flag = self.flags[self.target_country]
            while self.previusly_country == self.target_country:
                self.target_country = random.choice(self.countries)
                self.target_capital = self.capitals[self.target_country]
                self.target_flag = self.flags[self.target_country]

            # Configuração da segunda tela
            self.canvas.delete(tk.ALL)  # Limpa a tela
            self.input_entry.destroy()
            self.confirm_button.destroy()
            self.segunda_pagina()
        else:
            self.wrong_guesses += 1
            remaining_guesses = MAX_WRONG_GUESSES - self.wrong_guesses
            if self.wrong_guesses >= MAX_WRONG_GUESSES:
                messagebox.showinfo("Game Over", f"GAME OVER. No more attempts remaining.")
                self.destroy()
            else:
                messagebox.showinfo("Incorrect Answer", f"Wrong guess! {remaining_guesses} attempts remaining.")

    def segunda_pagina(self):
            self.show_input_box(confirm_command=self.check_second_input)
             # Carrega a imagem da bandeira
            flag_image = self.load_image(self.flags[self.target_country])
            if flag_image:
                
                flag_label = tk.Label(self.canvas, image=flag_image)
                flag_label.image = flag_image  # Mantém uma referência para evitar a coleta de lixo
                # Posiciona a imagem no centro do canvas
                flag_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
               # Carrega e adiciona a imagem da polícia
                police_image = self.load_image('police.png')
                if police_image:
                    police_label = tk.Label(self.canvas, image=police_image)
                    police_label.image = police_image  # Mantém uma referência para evitar a coleta de lixo
                    police_label.place(relx=0.2, rely=0.45, anchor=tk.CENTER)  # Coloca a imagem no canvas
                
                info_text = "The Professional Thief fled\nto another country,\nour intelligence says\nthat she was last seen\nin a country with the\ndisplayed flag!"

                self.canvas.create_text(500, 350, font=('Arial Black', self.font_size), text=info_text, fill=self.color, anchor=tk.CENTER)

                # Verificação da segunda resposta
                self.after(100, self.check_second_input)
        
            
    def check_second_input(self):
        guess2 = self.input_entry.get().strip().title()
        self.previusly_country = guess2  # Salvando a tentativa anterior

        if guess2 == self.target_country:                
            
            self.canvas.delete(tk.ALL)  # Limpa a tela
            self.input_entry.destroy()
            self.confirm_button.destroy()
            
            self.canvas.create_image(500, 500, image=self.load_image('jail.png'))
            self.canvas.create_text(15, 20, font=('Arial Black', self.font_size + 10), text="The Professional Thief got caught!", fill="blue")
       

    def load_image(self, filename):
        image_path = os.path.join(self.images_path, filename)
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    app = ProfessionalThiefGame()
    app.mainloop()
