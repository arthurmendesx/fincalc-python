import pytest
from fincalc import calcular_rendimento_real


def test_rendimento_real_fisher():
    r_real = calcular_rendimento_real(10.0, 5.0)
    assert round(r_real, 2) == 4.76


def test_rendimento_real_inflacao_nula():
    r_real = calcular_rendimento_real(8.5, 0.0)
    assert round(r_real, 2) == 8.50


def test_rendimento_real_hiperdeflacao_invalida():
    with pytest.raises(ValueError):
        calcular_rendimento_real(10.0, -100.0)
