import machine
import neopixel
import time
import random

# Configuration de la matrice LED
led_pin = 7  # Pin connectée à la matrice LED
num_pixels = 64  # Nombre de LEDs dans la matrice

# Initialisation de la broche et de la matrice LED
pin = machine.Pin(led_pin, machine.Pin.OUT)
pixels = neopixel.NeoPixel(pin, num_pixels)

# Configuration du bouton
button_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)  # Pin du bouton

# Couleur de la LED allumée
led_color = (5, 0, 0)  # Rouge

def light_random_led():
    # Éteindre toutes les LEDs
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0) 

    # Choisir un index aléatoire
    random_index = random.randint(0, num_pixels - 1)
    
    # Allumer la LED à la position aléatoire
    pixels[random_index] = led_color
    pixels.write()  # Met à jour la matrice LED

# Variable pour stocker l'état précédent du bouton
previous_button_state = button_pin.value()

while True:
    # Lire l'état actuel du bouton
    current_button_state = button_pin.value()

    # Détecter un appui sur le bouton (front descendant)
    if previous_button_state == 1 and current_button_state == 0:
        light_random_led()  # Déplacer la "pomme" à une position aléatoire
        time.sleep(0.1)  # Petite pause pour éviter la détection multiple

    # Mettre à jour l'état précédent du bouton
    previous_button_state = current_button_state
