import pytest

def fatorial(numero):
    resultado = 1
    if numero in (0,1):
        return resultado
    for n in range(1, numero + 1):
        resultado *= n 
    return resultado

def test_fatorial_zero():
    assert fatorial(0)==1

def test_fatorial_dois():
    assert fatorial(2) == 2 

def test_fatorial_tres():
    assert fatorial(3)==6

if __name__ == '__main__':
    pytest.main([__file__])
