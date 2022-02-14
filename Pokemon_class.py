import numpy as np

class pokemon_funtions:

    def Number_to_Type(number):
        if number == 0:
            Type = 'Bug'
        elif number == 1:
            Type = 'Dark'
        elif number == 2:
            Type = 'Dragon'
        elif number == 3:
            Type = 'Electric'
        elif number == 4:
            Type = 'Fairy'
        elif number == 5:
            Type = 'Fighting'
        elif number == 6:
            Type = 'Fire'
        elif number == 7:
            Type = 'Flying'
        elif number == 8:
            Type = 'Ghost'
        elif number == 9:
            Type = 'Grass'
        elif number == 10:
            Type = 'Ground'
        elif number == 11:
            Type = 'Ice'
        elif number == 12:
            Type = 'Normal'
        elif number == 13:
            Type = 'Poison'
        elif number == 14:
            Type = 'Psychic'
        elif number == 15:
            Type = 'Rock'
        elif number == 16:
            Type = 'Steel'
        elif number == 17:
            Type = 'Water'
        return Type

    def AttackDefend(Attack, Defend):
        Type_Matrix = (
        [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1],
        [1, 0.5, 1, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1],
        [1, 1, 0.5, 0.5, 1, 1, 1, 2, 1, 0.5, 0, 1, 1, 1, 1, 1, 1, 2],
        [1, 2, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1],
        [0.5, 2, 1, 1, 0.5, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1],
        [2, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 2, 1, 2, 1, 1, 1, 0.5, 2, 0.5],
        [2, 1, 1, 0.5, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 1],
        [1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1],
        [0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 2],
        [0.5, 1, 1, 2, 1, 1, 2, 0, 1, 0.5, 1, 1, 1, 2, 1, 2, 2, 1],
        [1, 1, 2, 1, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2, 0.5, 1, 1, 0.5, 1, 0.5, 0, 1],
        [1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1],
        [2, 1, 1, 1, 1, 0.5, 2, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 0.5, 1],
        [1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5],
        [1, 1, 0.5, 1, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 0.5])

        Score = Type_Matrix[Attack][Defend]
        return Score

























