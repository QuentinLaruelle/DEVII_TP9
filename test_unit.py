# Python 3.9
# UTF-8
import unittest
import fraction_Quentin


class FractionInitTest(unittest.TestCase):
    def test_den_null(self):
        """Vérification de la création de la class Fraction dans le cas den==0"""
        self.assertRaises(ZeroDivisionError, fraction_Quentin.Fraction, *[1, 0])


my_fraction = fraction_Quentin.Fraction(1, 3)


class FractionAddTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de l'addition de la fraction et d'un entier positif"""
        self.assertEqual(my_fraction + 3, 3.33, "my_fraction+3")
        self.assertEqual(my_fraction + 20, 20.33, "my_fraction+20")

    def test_other_null(self):
        """Vérification de l'addition de la fraction et d'un entier null"""
        self.assertEqual(my_fraction+0, 0.33, "my_fraction+0")

    def test_other_negative(self):
        """Vérification de l'addition de la fraction et d'un entier negatif"""
        self.assertEqual(my_fraction+(-3), -2.67, "my_fraction-3")
        self.assertEqual(my_fraction+(-20), -19.67, "my_fraction-20")


class FactSubCase(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de la soustraction de la fraction et d'un entier positif"""
        self.assertEqual(my_fraction - 3, -2.67, "my_fraction-3")
        self.assertEqual(my_fraction - 20, -19.67, "my_fraction-20")

    def test_other_null(self):
        """Vérification de la soustraction de la fraction et d'un entier null"""
        self.assertEqual(my_fraction-0, 0.33, "my_fraction-0")

    def test_other_negative(self):
        """Vérification de la soustraction de la fraction et d'un entier negatif"""
        self.assertEqual(my_fraction - (- 3), 3.33, "my_fraction- (-3)")
        self.assertEqual(my_fraction - (-20), 20.33, "my_fraction- (-20)")


class FractionMulTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de la multiplication de la fraction et d'un entier positif"""
        self.assertEqual(my_fraction * 3, 1, "my_fraction * 3")
        self.assertEqual(my_fraction * 20, 6.67, "my_fraction * 20")

    def test_other_null(self):
        """Vérification de la multiplication de la fraction et d'un entier null"""
        self.assertEqual(my_fraction * 0, 0, "my_fraction * 0")

    def test_other_negative(self):
        """Vérification de la multiplication de la fraction et d'un entier negatif"""
        self.assertEqual(my_fraction * (-3), -1, "my_fraction * (-3)")
        self.assertEqual(my_fraction * (-20), -6.67, "my_fraction * (-20)")


class FractionTrueDivTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de la division de la fraction par un entier positif"""
        self.assertEqual(my_fraction / 3, 0.11, "my_fraction / 3")
        self.assertEqual(my_fraction / 20, 0.02, "my_fraction / 20")

    def test_other_null(self):
        """Vérification de la division de la fraction par un entier null"""
        self.assertRaises(ZeroDivisionError, my_fraction.__truediv__, 0)

    def test_other_negative(self):
        """Vérification de la division de la fraction par un entier negatif"""
        self.assertEqual(my_fraction / (-3), -0.11, "my_fraction / (-3)")
        self.assertEqual(my_fraction / (-20), -0.02, "my_fraction / (-20)")


class FractionPowTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de la puissance de la fraction par un entier positif"""
        self.assertEqual(my_fraction ** 2, 0.1111, "my_fraction ** 2")
        self.assertEqual(my_fraction ** 5, 0.0041, "my_fraction ** 5")

    def test_other_null(self):
        """Vérification de la puissance de la fraction par un entier null"""
        self.assertEqual(my_fraction ** 0, 1, "my_fraction ** 0")

    def test_other_negative(self):
        """Vérification de la puissance de la fraction par un entier negatif"""
        self.assertEqual(my_fraction ** (-2), 9, "my_fraction ** (-2)")
        self.assertEqual(my_fraction ** (-5), 243, "my_fraction ** (-5)")


class FractionEqualTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de l'égalité de la fraction avec un décimal positif"""
        self.assertEqual(my_fraction == 0.33, True, "my_fraction == 0.33")
        self.assertEqual(my_fraction == 5.2, False, "my_fraction == 5.2")

    def test_other_null(self):
        """Vérification de l'égalité de la fraction avec 0"""
        self.assertEqual(my_fraction == 0, False, "my_fraction == 0")

    def test_other_negative(self):
        """Vérification de l'égalité de la fraction avec un décimal positif"""
        self.assertEqual(my_fraction == (-0.33), False, "my_fraction == (-0.33)")
        self.assertEqual(my_fraction == (-5.2), False, "my_fraction == (-5.2)")


class FractionAdjacentTest(unittest.TestCase):
    def test_other_positive(self):
        """Vérification de si la fraction -  other = à une valeur de 1/x si other est positif"""
        self.assertEqual(my_fraction.is_adjacent_to(1/12), True, "my_fraction.is_adjacent_to(1/12)")
        self.assertEqual(my_fraction.is_adjacent_to(3/12), False, "my_fraction.is_adjacent_to(3/12)")

    def test_other_null(self):
        """Vérification de si la fraction -  other = à une valeur de 1/x si other est = 0"""
        self.assertRaises(ZeroDivisionError, my_fraction.is_adjacent_to, 0)

    def test_other_negative(self):
        """Vérification de si la fraction -  other = à une valeur de 1/x si other est négatif"""
        self.assertEqual(my_fraction.is_adjacent_to(-3/9), False, "my_fraction.is_adjacent_to(-3/9)")
        self.assertEqual(my_fraction.is_adjacent_to(-3/12), False, "my_fraction.is_adjacent_to(-3/12)")


class FractionIsZeroTest(unittest.TestCase):
    def test_fraction_positive(self):
        """Vérification de si une fraction positive est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(1, 8).is_zero(), False, "fraction.Fraction(1,8).is_zero()")
        self.assertEqual(fraction_Quentin.Fraction(14, 8).is_zero(), False, "fraction.Fraction(14,8).is_zero()")

    def test_fraction_null(self):
        """Vérification de si une fraction nulle est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(0, 8).is_zero(), True, "fraction.Fraction(0, 8).is_zero()")

    def test_fraction_negative(self):
        """Vérification de si une fraction negative est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(-3, 8).is_zero(), False, "fraction.Fraction(-3, 8).is_zero()")
        self.assertEqual(fraction_Quentin.Fraction(-20, 8).is_zero(), False, "fraction.Fraction(-20, 8).is_zero()")


class FractionIsIntegerTest(unittest.TestCase):
    def test_fraction_positive(self):
        """Vérification de si une fraction positive est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(1, 8).is_integer(), False, "fraction.Fraction(1, 8).is_integer()")
        self.assertEqual(fraction_Quentin.Fraction(14, 7).is_integer(), True, "fraction.Fraction(14, 7).is_integer()")

    def test_fraction_null(self):
        """Vérification de si une fraction nulle est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(0, 8).is_integer(), True, "fraction.Fraction(0, 8).is_integer()")

    def test_fraction_negative(self):
        """Vérification de si une fraction negative est = 0"""
        self.assertEqual(fraction_Quentin.Fraction(-3, 8).is_integer(), False, "fraction.Fraction(-3, 8).is_integer()")
        self.assertEqual(fraction_Quentin.Fraction(-24, 8).is_integer(), True, "fraction.Fraction(-24, 8).is_integer()")


class FractionIsProperTest(unittest.TestCase):
    def test_fraction_positive(self):
        """Vérification de si la valeur absolue d'une fraction positive est < 1"""
        self.assertEqual(fraction_Quentin.Fraction(1, 8).is_proper(), True, "fraction.Fraction(1, 8).is_proper()")
        self.assertEqual(fraction_Quentin.Fraction(14, 7).is_proper(), False, "fraction.Fraction(14, 7).is_proper()")

    def test_fraction_null(self):
        """Vérification de si la valeur absolue d'une fraction nulle est < 1"""
        self.assertEqual(fraction_Quentin.Fraction(0, 8).is_proper(), True, "fraction.Fraction(0, 8).is_proper()")

    def test_fraction_negative(self):
        """Vérification de si la valeur absolue d'une fraction negative est < 1"""
        self.assertEqual(fraction_Quentin.Fraction(-3, 8).is_proper(), True, "fraction.Fraction(-3, 8).is_proper()")
        self.assertEqual(fraction_Quentin.Fraction(-24, 8).is_proper(), False, "fraction.Fraction(-24, 8).is_proper()")


class FractionIsUnitTest(unittest.TestCase):
    def test_fraction_positive(self):
        """Vérification de si le numerateur = 1 quand la fraction positive est simplifiée"""
        self.assertEqual(fraction_Quentin.Fraction(4, 8).is_unit(), True, "fraction.Fraction(4, 8).is_unit()")
        self.assertEqual(fraction_Quentin.Fraction(14, 7).is_unit(), False, "fraction.Fraction(14, 7).is_unit()")

    def test_fraction_null(self):
        """Vérification de si le numerateur = 1 quand la fraction nulle est simplifiée"""
        self.assertEqual(fraction_Quentin.Fraction(0, 8).is_unit(), False, "fraction.Fraction(0, 8).is_unit()")

    def test_fraction_negative(self):
        """Vérification de si le numerateur = 1 quand la fraction négative est simplifiée"""
        self.assertEqual(fraction_Quentin.Fraction(-3, 8).is_unit(), False, "fraction.Fraction(-3, 8).is_unit()")
        self.assertEqual(fraction_Quentin.Fraction(-24, 8).is_unit(), False, "fraction.Fraction(-24, 8).is_unit()")


if __name__ == '__main__':
    unittest.main()
