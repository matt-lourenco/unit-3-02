# Created by: Matthew Lourenco
# Created on: 3 Oct 2016
# This is a program that lets you guess what number it has chosen

import ui
from numpy import random

#choose random number
number_to_guess = random.randint(1, 10)
print(number_to_guess)

def guess_touch_up_inside(sender):
    guess = int(view['guess_textfield'].text)
    
    if guess == number_to_guess:
        view['reply_label'].text = 'Correct! The number was ' + str(number_to_guess)
    else:
        view['reply_label'].text = 'Incorrect. Guess again!'

view = ui.load_view()
view.present('full_screen')
