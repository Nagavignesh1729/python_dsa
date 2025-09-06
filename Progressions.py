class Progression:
    """
        An iterator producing generic progression
        By default produces the whole numbers (0, 1, 2, 3...)
    """
    def __init__(self, start = 0):
        """ Initialise current to the starting value of the progression. """
        self._current = start

    def _advance(self):
        """
            Update the self._current to a new value

            This should be overriden by a subclass to customize progression.

            By convention, if current is set to None, this designates the 
            end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """ Return the next element, or else Raise StopIterator error. """
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for next time
            return answer               # return answer
    
    def __iter__(self):
        """ By convention, an iterator must return itself as an iterator. """
        return self

    def print_progression(self, n):
        """ Print next n values of the progression """
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """ Iterator producing an arithmetic progression """
    def __init__(self, increment = 1, start = 0):
        """ Create an arithmetic progression 
        
        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """

        super().__init__(start)         # initialise base class 
        self._increment = increment
    
    def _advance(self):
        """ Update current value by adding the fixed increment. """
        self._current += self._increment


if __name__ == "__main__":
    whole_numbers = Progression()
    whole_numbers.print_progression(10)
    whole_numbers.print_progression(20)

    ap = ArithmeticProgression(5, 2)
    ap.print_progression(10)
    ap.print_progression(20)
