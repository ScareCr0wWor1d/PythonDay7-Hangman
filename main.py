# Le Pendu
import random
from hangman_art import logo, stages
from hangman_mots import liste_mot

mot_cache = []
vie = 6
trouver = 0
let_try = []
game_over = False

mot = random.choice(liste_mot)

longmot = len(mot)

print(logo)

for letter in mot:
    mot_cache += '_'

print(mot)

print(mot_cache)

while not game_over:
    print(stages[vie])
    guess = input("Choisir une lettre: ").lower()

    if guess in let_try:
        print("Vous avez déjà entré cette lettre!")
    else:
        let_try += guess
        let_try.sort()
        print(f"Lettres utilisées : {' '.join(let_try)}")
        if guess in mot:
            for position in range(longmot):
                lettre = mot[position]
                if guess == mot[position]:
                    mot_cache[position] = lettre
            print(f"{' '.join(mot_cache)}")

            if "_" not in mot_cache:
                print(f"Vous avez choisi la lettre {guess} et elle est dans le mot")
                print(f"Vous gagnez! Vous avez trouver le mot : {mot}")
                game_over = True

        else:
            print(f"Vous avez choisi la lettre {guess} et elle n'est pas dans le mot")
            vie -= 1
            if vie == 0:
                print(stages[vie])
                print("Die! Die! Die!")
                game_over = True
