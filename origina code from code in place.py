from graphics import Canvas
import random
import time
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
VELOCITY = 30
DELAY = 0.08 
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # List of possible countries
    countries = ["United States", "Canada", "Mexico", "Brazil", "Argentina", "France", "Germany", "Italy", "Russia", "China", "Japan", "Australia"]
    
    # Dictionary of country capitals
    capitals = {
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
    # Dictionary of country flags
    flags = {
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
    # First screen
    font_size = 15
    color= "black"
    start_x = 0
    start_y = 130
    start_xP = -200
    start_yP= 100
    
    #choose a aleatory country
    target_country = random.choice(countries)
    
    
    #set up for the first question
    target_capital = capitals[target_country]
    canvas.create_text(35, 50, font='Arial Black', font_size = 25, text= "Welcome to Professional Thief!", color=color)
    
    #animation
    pol_run = canvas.create_image(start_xP,start_yP, 'pol_run.png')
    professional_thief= canvas.create_image(start_x,start_y, 'Professional thief.png')
    
    while (start_xP <= CANVAS_WIDTH ):
        start_x += VELOCITY
        canvas.moveto(professional_thief, start_x, start_y)
        start_xP += VELOCITY
        canvas.moveto(pol_run, start_xP, start_yP)
        time.sleep(DELAY)
    
    #First question   
    canvas.create_text(20, 300, font='Arial', font_size = font_size  , text="A Professional Thief  has stolen a valuable artifact and is on the run.", color=color)
    canvas.create_text(20, 325, font='Arial', font_size = font_size  , text="Your mission is to track her down and recover the artifact.", color=color)
    canvas.create_text(20, 350, font='Arial', font_size = font_size ,color=color, text = "The Professional Thief was last seen in a country")
    canvas.create_text(20, 375, font='Arial', font_size = font_size ,color=color, text = "whose capital is : " )
    canvas.create_text(150, 375, font='Arial Black', font_size = font_size ,color=color, text = str(target_capital))
    canvas.create_image(CANVAS_WIDTH/3,100,'wanted.png') 
    
    #indicate where user must white the answer
    canvas.create_text(20, 425, font='Arial Black', font_size = font_size , text = "Please use the terminalto write your answer!", color="blue")
        
        
    #Set up for second screen and second question
    while True:
        
        guess = input("Enter the name of a country: ")
        guess = guess.title()
        previusly_country = guess
        if guess == target_country:
            target_country = random.choice(countries)
            target_capital = capitals[target_country]
            target_flag = flags[target_country]
            while previusly_country == target_country:
                target_country = random.choice(countries)
                target_capital = capitals[target_country]
                target_flag = flags[target_country]
            
            canvas.clear()
            
            
            flag = canvas.create_image(10,10,target_flag)
            canvas.create_image(300,250, 'police.png' )
            canvas.create_text(15, 250, font='Arial Black', font_size = font_size , text="The Professional Thief fled", color=color)
            canvas.create_text(15, 275, font='Arial Black', font_size = font_size , text="to another country,", color=color)
            canvas.create_text(15, 300, font='Arial Black', font_size = font_size , text="tour inteligence says", color=color)
            canvas.create_text(15, 325, font='Arial Black', font_size = font_size , text="that she was last saw", color=color)
            canvas.create_text(15, 350, font='Arial Black', font_size = font_size , text="in a country with the", color=color)
            canvas.create_text(15, 375, font='Arial Black', font_size = font_size , text="displayed flag !", color=color)
            
            #Set up for verify if second answer is right
            while True:
                congrats = ""
                guess = input("Enter the name of a country: ")
                guess = guess.title()
                if guess == target_country:
                    print("Congratulations! You found the Professional Thief!")
                    #set up for the 3rd screen
                    canvas.clear()
                    
                    
                    canvas.create_image(100, 100, 'jail.png')
                    canvas.create_text(15, 20, font='Arial Black', font_size = font_size+10 , text="The Professional Thief got cought!", color="blue")
                    congrats = "stop"
                    break
               
                else:
                    print("Wrong guess! The Professional Thief is not in", guess)
                    print("The Professional Thief was last seen in a country with displayed flag")
                    
        else:
            print("Wrong guess! The Professional Thief is not in", guess)
            print("The Professional Thief was last seen in a country whose capital is", target_capital)
        
        if congrats == "stop":
            break        

if __name__=='__main__':
    main()