from alphabet import Alphabet
from rotor import Rotor
from permutation import Permutation
from reflector import Reflector

class Machine:
    # Common alphabet of my rotors.
    _alphabet = None

    # Number of rotors.
    _numRotors = None

    # Number of pawls.
    _pawls = None

    # Collection of all rotors given by machine.
    _allRotors = None

    # List of rotors.
    _rotors = None

    # A new Enigma machine with alphabet ALPHA, 1 < NUMROTORS rotor slots, and 0 <= PAWLS < NUMROTORS pawls.
    # ALLROTORS contains all the available rotors.
    def __init__(self, alpha, numRotors, pawls, allRotors):
        # DEFINE ALL INSTANCE VARIABLES HERE, PLUS THE LINE BELOW
        self._allRotors = allRotors
        self._pawls = pawls
        self._numRotors = numRotors
        self._alphabet = alpha
        self._rotors = []
#pawls are levers (specific name for lever)
    # Return the number of rotor slots I have.
    def numRotors(self):
        return self._numRotors

    # Set my rotors to the rotors named ROTORS from my set of available rotors (ROTORS[0] names the reflector).
    # Initially, all rotors are set at their 0 setting.
    """
    def insertRotors(self, rotors):
        _rotors = []
        i = 0
        while i < len(rotors):
            for rotor in self._allRotors:
                if rotors[i] == rotor.name():
                    self._rotors.append(rotor)
                    i += 1
                    if len(_rotors) == len(rotors):
                        raise Exception("Misnamed rotors.")
    """

    def insertRotors(self, rotors):
        # Clear any previously inserted rotors
        self._rotors = []

        for rotor_name in rotors:
            found = False
            for rotor in self._allRotors:
                if rotor_name == rotor.name():
                    self._rotors.append(rotor)
                    found = True
                    break

            if not found:
                raise Exception(f"Rotor '{rotor_name}' is not in the list of available rotors.")

        if len(self._rotors) != len(rotors):
            raise Exception("Misnamed rotors.")

    # Set my rotors according to SETTING, which must be a string of numRotors()-1 characters in my alphabet.
    # The first letter refers to the leftmost rotor setting (not counting the reflector).
    def setRotors(self, setting):
        if not (len(setting) == self._numRotors - 1):
            raise Exception("Setting is wrong length")
        elif not self._rotors[0].reflecting():
            raise Exception("Missing Reflector")
        elif len(setting) == self._numRotors - 1:
            i = 0
            while i < len(setting):
                if not (self._alphabet.contains(setting[i - 1])):
                    raise Exception("String setting not in alphabet.")
                else:
                    self._rotors[i].setChar(setting[i - 1])
                i += 1
                # i - 1 because want to check setting and have to discount the setting by doing i - 1

    # Returns the result of converting the input character C (as an index in the range 0..alphabet size - 1),
    # after first advancing the machine.
    def convert(self, c):
        numAdv = [False] * len(self._rotors)  # Initialize numAdv with False for each rotor
        numAdv[len(self._rotors) - 1] = True  # Last rotor always advances

        # Advance the necessary rotors
        for i in range(len(self._rotors) - 1):
            if self._rotors[i + 1].atNotch() and self._rotors[i].rotates():
                self._rotors[i].advance()
                numAdv[i] = True

        # Further advance based on double stepping mechanism
        """
        for i in range(len(self._rotors) - 1):
            if numAdv[i]:
                if not numAdv[i + 1]:
                    self._rotors[i + 1].advance()
        """
        for i in range(len(self._rotors) - 1):
            if numAdv[i] and not numAdv[i + 1]:
                self._rotors[i + 1].advance()

        # Last rotor always advances
        self._rotors[len(self._rotors) - 1].advance()

        # Forward conversion through the rotors
        for i in range(len(self._rotors) - 1, -1, -1):
            c = self._rotors[i].convertForward(c)

        # Backward conversion through the rotors
        for i in range(1, len(self._rotors)):
            c = self._rotors[i].convertBackward(c)

        return c

#----------------------------------------------------------------------------------------

alpha = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#create permutations for rotors
permutation1 = Permutation("(AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP) (RX) (SZ) (TV)", alpha)
permutation2 = Permutation("(AB) (CD) (EF) (GH) (IJ) (KL) (MN) (OP) (QR) (ST) (UV) (WX) (YZ)", alpha)
permutation3 = Permutation("(AZ) (BY) (CX) (DW) (EV) (FU) (GT) (HS) (IR) (JQ) (KP) (LO) (MN)", alpha)

# create rotors
rotor1 = Rotor("I", permutation1, "Q")
rotor2 = Rotor("II", permutation2, "E")
rotor3 = Rotor("III", permutation3, "V")

# Create a reflector
reflect = Reflector("ReflectorB", Permutation("(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)", alpha))

# All rotors available
allRotors = [rotor1, rotor2, rotor3, reflect]

# Set up the machine with 4 slots, 1 pawl
machine = Machine(alpha, 4, 1, allRotors)

# Insert the rotors into the machine
machine.insertRotors(["ReflectorB", "III", "II", "I"])


# Set the initial settings of the rotors
machine.setRotors("AAA")  # Set to the starting position

# Input character 'A' should be converted to another character
def encryption():
    user_input = input("Input a word you would like to encrypt: ")
    encrypt = ''
    for letter in user_input:
        input_char = f"{letter.upper()}"
        input_index = alpha.toInt(input_char)

        # Convert the character
        converted_index = machine.convert(input_index)
        converted_char = alpha.toChar(converted_index)

        encrypt += converted_char

    # Print the output character
    print(f"Input word: {user_input}")
    print(f"Encrypted word: {encrypt}")


    machine.setRotors("AAA")

def decryption(encrypt):
    decrypt = ''
    for letter in encrypt:
        input_char = f"{letter.upper()}"
        input_index = alpha.toInt(input_char)

        # Convert the character in reverse to the orginal word
        converted_index = machine.convert(input_index)
        converted_char = alpha.toChar(converted_index)

        decrypt += converted_char

    # Print the decrypted message
    return f"{decrypt}"


