import random
import string
from alphabet import Alphabet
from rotor import Rotor
from permutation import Permutation
from reflector import Reflector

# Function to generate a random permutation
def random_permutation(alpha):
    alpha_list = list(alpha)
    random.shuffle(alpha_list)
    pairs = []
    while alpha_list:
        if len(alpha_list) >= 2:
            pair = (alpha_list.pop(0), alpha_list.pop(0))
            pairs.append(f"({pair[0]}{pair[1]})")
        elif alpha_list:
            pairs.append(f"({alpha_list.pop(0)})")  # Handle remaining odd character
    return " ".join(pairs)


# Function to generate a random unique ID
used_ids = set()


def generate_unique_id():
    while True:
        new_id = random.randint(1000, 9999)
        if new_id not in used_ids:
            used_ids.add(new_id)
            return new_id

alpha = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Function to randomize the settings
def randomize_settings(alpha):
    # Generate random permutations for the three rotors
    permutation1 = Permutation(random_permutation(alpha), alpha)
    permutation2 = Permutation(random_permutation(alpha), alpha)
    permutation3 = Permutation(random_permutation(alpha), alpha)

    # Create the rotors with random notches
    rotor1 = Rotor("I", permutation1, random.choice(alpha))
    rotor2 = Rotor("II", permutation2, random.choice(alpha))
    rotor3 = Rotor("III", permutation3, random.choice(alpha))

    # Create a random reflector
    reflector_permutation = Permutation(random_permutation(alpha), alpha)
    reflect = Reflector("ReflectorB", reflector_permutation)

    # Generate a unique ID
    config_id = generate_unique_id()

    # Save the settings with the ID as a key (for demonstration, using a dictionary)
    settings = {
        'rotor1': rotor1,
        'rotor2': rotor2,
        'rotor3': rotor3,
        'reflector': reflect,
        'id': config_id
    }

    return settings


# Example usage
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
settings = randomize_settings(alpha)
print(f"Settings ID: {settings}")
