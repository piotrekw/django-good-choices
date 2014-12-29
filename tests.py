from good_choices import Choices


def test_ordering():
    class Ch(Choices):
        A = 3, 'A'
        B = 2, 'B'
        C = 4, 'C'
        D = 1, 'D'
    assert Ch.choices == [(1, 'D'), (2, 'B'), (3, 'A'), (4, 'C')]

def test_values():
    class Ch(Choices):
        A = 3, 'A'
        B = 2, 'B'
        C = 4, 'C'
        D = 1, 'D'
    assert Ch.A == 3
    assert Ch.B == 2
    assert Ch.C == 4
    assert Ch.D == 1

def test_define_only_values():
    class Ch(Choices):
        A = 'X'
        B = 'Y'
        C = 'Z'
    assert Ch.choices == [('X', 'X'), ('Y', 'Y'), ('Z', 'Z')]
