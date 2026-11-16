from fincalc import calcular_juros_simples


def test_juros_simples_valido():
    # Arrange & Act
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    # Assert
    assert round(montante, 2) == 1100.00


def test_juros_simples_tempo_zero():
    # Arrange & Act
    montante = calcular_juros_simples(1000.0, 5.0, 0)
    # Assert
    assert round(montante, 2) == 1000.00


def test_juros_simples_taxa_zero():
    # Arrange & Act
    montante = calcular_juros_simples(1000.0, 0.0, 3)
    # Assert
    assert round(montante, 2) == 1000.00
