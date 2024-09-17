class Rotor:

    # The name of the rotor.
    _name = ""

    # The permutation implemented by this rotor in its 0 position.
    _permutation = None


    # The setting of the rotor.
    _setting = 0

    # String of notches.
    _notches = ""

    # A rotor named NAME whose permuation in its default setting is PERM, and whose notches are at the positions indicated in NOTCHES. The Rotor is initially in its 0 setting (first character of its alphabet).
    def __init__(self, name, perm, notches):
        pass  # delete this line when you are finished coding this method
        self._name = name
        self._permutation = perm
        self._notches = notches
        self._setting = 0


    # Return my name.
    def name(self):
        return self._name

    # Return my alphabet.
    def alphabet(self):
        return self._permutation.alphabet()

    # Return my permutation.
    def permutation(self):
        return self._permutation

    # Return the size of my alphabet.
    def size(self):
        return self._permutation.size()

    # Return true iff I have a ratchet and can move.
    def rotates(self):
        return True

    # Return true iff I reflect.
    def reflecting(self):
        return False

    # Return my current setting.
    def setting(self):
        return self._setting

    # Set setting() to POSN.
    def set(self, posn):
        self._setting = posn

    # Set setting() to character CPOSN.
    def setChar(self, cposn):
        _setting = self._permutation.alphabet().toInt(cposn)

    # Return the conversion of P (an integer in the range 0..size()-1) according to my permutation.
    def convertForward(self, p):
        if isinstance(p, str):
            p = self.alphabet().toInt(p)
        p = self._permutation.permute(p + self._setting)
        return self._permutation.wrap(p - self._setting)

    # Return the conversion of E (an integer in the range 0..size()-1) accoding to the inverse of my permutation.
    def convertBackward(self, e):
        if isinstance(e, str):
            e = self.alphabet().toInt(e)
        e = self._permutation.invert(e + self._setting)
        return self._permutation.wrap(e - self._setting)

    # Return true iff I am positioned to allow the rotor to my left to advance.
    def atNotch(self):
        for notch in self._notches:
            if self.alphabet().toInt(notch) == self._setting:
                return True
        return False

    # Advance me one position, if possible.
    def advance(self):
        self.set(self._permutation.wrap(self._setting + 1))
        # put wrap just in case position is at the end of