class Alphabet:

    # Represents the String chars in alphabet.
    _chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # A new alphabet containing CHARS.
    def __init__(self, chars):
        self._chars = chars

    # Returns the size of the alphabet.
    def size(self):
        return len(self._chars)

    # Returns true if CH is in this alphabet.
    def contains(self, ch):
        for letter in self._chars:
            if letter == ch:
                return True
        return False


    # Returns character number INDEX in the alphabet. where 0 <= INDEX < size().
    def toChar(self, index):
        if index >= 0 and index < self.size():
            return self._chars[index]


    # Returns the index of character CH which must be in the alphabet. This is the inverse of toChar().
    def toInt(self, ch):
        for i in range(self.size()):
            if self._chars[i] == ch:
                return i
        raise Exception(f"Character '{ch}' not found in alphabet.")