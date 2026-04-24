import sys
import io
from glosario import definicion_django


def test_definicion_django_prints_term(capsys):
    # Capturamos la salida y comprobamos que contiene 'Django' y 'MVT'
    definicion_django()
    captured = capsys.readouterr()
    assert "Django" in captured.out
    assert "MVT" in captured.out
