from suma_dos_numeros import suma

def test_suma_de_positivos():
    res = suma(1,2)
    expected = 3
    assert res == expected

def test_suma_con_cero():
    res = suma(0,2)
    expected = 2
    assert res == expected

def test_suma_negativo_y_positivo():
    res = suma(-1,2)
    expected = 1
    assert res == expected

def test_suma_de_negativos():
    res = suma(-1,-2)
    expected = -3
    assert res == expected

