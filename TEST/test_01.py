
from Programa_01 import duplicados
import pytest

# test_duplicados.py
import pytest

def test_duplicados():
    assert duplicados(c=[1, 2, 3, 4, 5]) == False
    assert duplicados(c=[1, 2, 3, 4]) == True


