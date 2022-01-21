from app import magic_square
import pytest


testdata = [
    ([[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7),
    ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1),
    ([[4, 9, 7], [3, 5, 2], [8, 1, 6]], 10)
]

@pytest.mark.parametrize('sample, output', testdata)
def test_magic_square(sample, output):

    got = magic_square(sample)
    want = output

    assert got == want


