import machine
import neopixel
import time
import random

# Configuration de la matrice LED
led_pin = 23  # Pin connectée à la matrice LED
num_pixels = 64  # Nombre de LEDs dans la matrice

# Initialisation de la broche et de la matrice LED
pin = machine.Pin(led_pin, machine.Pin.OUT)
pixels = neopixel.NeoPixel(pin, num_pixels)

# Couleur de la pomme
apple_color = (255, 0, 0)  # Rouge

# Fonction pour allumer la LED à une position aléatoire
def place_apple():
    # Éteindre toutes les LEDs avant de placer la pomme
    for j in range(num_pixels):
        pixels[j] = (0, 0, 0)  # Éteindre les LEDs

    # Choisir un index aléatoire pour la pomme
    apple_index = random.randint(0, num_pixels - 1)

    # Allumer la LED à la position choisie
    pixels[apple_index] = apple_color
    pixels.write()  # Met à jour les LEDs
    return apple_index  # Retourne la position de la pomme

# Boucle principale
while True:
    apple_index = place_apple()  # Place la pomme à une position aléatoire
    time.sleep(1)  # Attendre 1 seconde avant de déplacer la pomme
