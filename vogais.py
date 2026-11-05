#vogais são a, e, i, o, u
import numpy as np
import pandas as pd

# Fixar a semente para resultados reproduzíveis
np.random.seed(42)

# Criar dados aleatórios
dados = {
    "ID": np.arange(1, 11),  # IDs de 1 a 10
    "Idade": np.random.randint(18, 60, size=10),  # Idades entre 18 e 60
    "Salário": np.random.randint(2000, 10000, size=10),  # Salários entre 2000 e 10000
    "Departamento": np.random.choice(["RH", "TI", "Financeiro", "Marketing"], size=10)
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Mostrar o DataFrame
print("DataFrame inicial:")
print(df)

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Agrupar por departamento e calcular média de salário
print("\nMédia de salário por departamento:")
print(df.groupby("Departamento")["Salário"].mean())

# Filtrar funcionários com salário acima de 7000
print("\nFuncionários com salário acima de 7000:")
print(df[df["Salário"] > 7000])
