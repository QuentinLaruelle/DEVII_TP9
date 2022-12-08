# Python 3.9
# UTF-8


class Fraction:
    """Class representing a fraction and operations on it

    Author : Q.Laruelle
    Date : December 2022
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.
        PRE : num est un entier par defaut 0, et den est un entier différent de 0 et par defaut 1
        POST : /
        RAISES : ZeroDivisionError si den == 0
        """
        if den == 0:
            raise ZeroDivisionError
        else:
            self.__num = num
            self.__den = den


    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction
        PRE : /
        POST : Retourne la Fraction simplifié au maximum
        """
        n = self.__num
        d = self.__den
        i = 2
        while i < min(n, d) + 1:
            if n % i == 0 and d % i == 0:
                n = n // i
                d = d // i
            else:
                i += 1
        return str(n)+"/"+str(d)

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : /
        POST : Retourne un entier + la Fraction
        """
        return (self.__num/self.__den)+2

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est un entier
         POST : Retourne num/den + other
         """
        return round(((self.__num/self.__den)+other), 2)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est un entier
         POST : Retourne num/den - other
        """
        return round(((self.__num/self.__den)-other), 2)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est un entier
         POST : Retourne num/den * other
        """
        return round(((self.__num/self.__den)*other), 2)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est un entier
         POST : Retourne (num/den)/other
        RAISES : ZeroDivisionError si other == 0
        """
        if other == 0:
            raise ZeroDivisionError
        else:
            return round(((self.__num/self.__den)/other), 2)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est un entier
         POST : Retourne (num/den) ** other
        """
        return round(((self.__num/self.__den)**other), 4)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est un entier
         POST : Retourne True si num/den == other sinon False

        """
        return round((self.__num/self.__den), 2) == other

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : Retourne la valeur decimal de la fraction
        """
        return self.__num/self.__den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : Retourne True si num == 0 sinon False
        """
        if self.__num == 0:
            return True
        else:
            return False

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : Retourne True si num/den == integer sinon False
        """
        if self.__num / self.__den % 1 == 0:
            return True
        else:
            return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : Retourne True si |num/den| < 1 sinon False
        """
        if abs(self.__num/self.__den) < 1:
            return True
        else:
            return False

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Retourne True si num == 1 lorsque la fraction est simplifié sinon False
        """
        n = self.__num
        d = self.__den
        i = 2
        while i < min(n, d) + 1:
            if n % i == 0 and d % i == 0:
                n = n // i
                d = d // i
            else:
                i += 1
        if n == 1:
            return True
        else:
            return False

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : /
        POST : Retourne True si |(num/den)-other|  = 1/x sinon False
        RAISES : ZeroDivisionError si other == 0
        """
        if other == 0:
            raise ZeroDivisionError
        else:
            max_range = int(min((self.__num/self.__den), other)**-1)
            response = False
            for i in range(1, max_range+1):
                if abs((self.__num/self.__den)-other) == 1/i:
                    response = True
            return response
