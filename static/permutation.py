class Permutation:
    # The alphabet of this permutation.

    # List of cycles.


    # Set this permutation to that specified by CYCLES,
    # a string in the form "(cccc) (cc) ..." where the c's
    # are characters in ALPHABET, which is interpreted as a
    # permutation in cycle notation. Characters in the alphabet
    # that are not included in any cycle map to themselves.
    # Whitespace is ignored.
    def __init__(self, cycles, alphabet):
        self._alphabet = alphabet
        self._cycles = []
        self.addCycle(cycles)

    # Add the cycle c0->c1->...->cm->c0 to the permutation, where CYCLE is c0c1...cm.
    def addCycle(self, cycle):
        miniCycle = ""
        for c in cycle:
            if c == ')':
                self._cycles.append(miniCycle)
                miniCycle = ""
            elif c != ' ' and c != '(':
                miniCycle += c

    # Return the value of P modulo the size of this permutation.
    def wrap(self,p):
        r = p % self.size()
        if r < 0:
            r += self.size()
        return r

    # Returns the size of the alphabet I permute.
    def size(self):
        return self._alphabet.size()

    # Return the result of applying this permutation to P modulo the alphabet size.
    """
    def permute(self, p):
        return Permutation._alphabet.toInt(self.permuteHelper(self._alphabet.toChar(self.wrap(p))))
    """
    def permute(self, p):
        # Convert integer p to its corresponding character
        char = self._alphabet.toChar(self.wrap(p))
        # Apply the permutation
        permuted_char = self.permuteHelper(char)
        # Convert back to an integer index
        return self._alphabet.toInt(permuted_char)

    # Return the result of applying the inverse of this permutation to C modulo the alphabet size.
    """
    def invert(self, c):
        return Permutation._alphabet.toInt(self.invertHelper(self._alphabet.toChar(self.wrap(c))))
    """

    def invert(self, c):
        # Convert integer c to its corresponding character
        char = self._alphabet.toChar(self.wrap(c))
        # Apply the inverse permutation
        inverted_char = self.invertHelper(char)
        # Convert back to an integer index
        return self._alphabet.toInt(inverted_char)

    # Return the result of applying this permutation to the index of P in ALPHABET,
    # and converting the result to a character of ALPHABET.
    """
    def permuteHelper(self, p):
        if (not isinstance(p, str)):
            p = self._alphabet.toChar(p)
        if not (self._alphabet.contains(p)):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            j = 0
            while j < len(cycle):
                if p == cycle[j]:
                    if j == len(cycle) - 1:
                        p = cycle[0]
                        return p
                    else:
                        p = cycle[j + 1]
                    break
                j += 1
        return p
    """

    def permuteHelper(self, p):
        if not self._alphabet.contains(p):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            if p in cycle:
                j = cycle.index(p)
                # Return the next character in the cycle, or the first if it's the last
                return cycle[(j + 1) % len(cycle)]
        return p  # If p is not in any cycle, it maps to itself

    # Return the result of applying the inverse of this permutation to C.
    """
    def invertHelper(self, c):
        if (not isinstance(c, str)):
            c = self._alphabet.toChar(c)
        if not (self._alphabet.contains(c)):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            j = 0
            while j < len(cycle):
                if c == cycle[j]:
                    if j == 0:
                        c = cycle[len(cycle) - 1]
                    else:
                        c = cycle[j - 1]
                    break
                j += 1
        return c
        
    """

    def invertHelper(self, c):
        if not self._alphabet.contains(c):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            if c in cycle:
                j = cycle.index(c)
                # Return the previous character in the cycle, or the last if it's the first
                return cycle[j - 1]
        return c  # If c is not in any cycle, it maps to itself


    # Return the alphabet used to initialize this permutation.
    def alphabet(self):
        return self._alphabet