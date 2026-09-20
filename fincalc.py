# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros compostos."""
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_aposentadoria(
    patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_parcela_price(
    valor_emprestimo: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela
    Tabela Price."""
    i = taxa_mensal / 100
    numerador = (1 + i) ** meses
    denominador = ((1 + i) ** meses) - 1
    parcela = valor_emprestimo * (numerador / denominador)
    return parcela


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_depreciacao_linear(
    valor_inicial:float, valor_residual:float, vida_util_anos:int
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    return (valor_inicial - valor_residual) / vida_util_anos


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")

    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")

    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(
        f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}"
    )

    imposto = calcular_irrf(3000.0)
    print(f"Imposto de Renda (Salário R$ 3.000): R$ {imposto:.2f}")

    # TESTE DO ALUNO 3
    valor_parcela = calcular_parcela_price(10000.0, 1.5, 12)
    print(f"Amortização Price (Parcela): R$ {valor_parcela:.2f}")


    # TESTE DO ALUNO 4
    valor_futuro = calcular_valor_futuro(500.0, 0.5, 24)
    print(f"Valor Futuro com Aportes: R$ {valor_futuro:.2f}")


    # TESTE DO ALUNO 5
    depreciacao_anual = calcular_depreciacao_linear(100000.0, 45000.0, 8)
    print(f"Depreciação anual: R$ {depreciacao_anual:.2f} ")