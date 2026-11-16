from fincalc import calcular_aposentadoria


def test_aposentadoria_valida():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    # Assert
    assert round(patrimonio, 2) == 265277.59


def test_aposentadoria_zero_anos():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 0, 6.0)
    # Assert
    assert round(patrimonio, 2) == 10000.00


def test_aposentadoria_taxa_zero():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(0.0, 100.0, 1, 0.0)
    # Assert
    assert round(patrimonio, 2) == 1200.00
