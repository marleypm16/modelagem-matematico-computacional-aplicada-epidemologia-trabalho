import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 100000  # População total da simulação
I0, E0, R0 = 10, 0, 0  # Condições iniciais: 10 infetados, 0 expostos, 0 recuperados
S0 = N - I0 - E0 - R0  # O resto da população começa como suscetível

sigma = 1 / 5  # Taxa de progressão
gamma = 1 / 7  # Taxa de recuperação


beta_cenario1 = 0.8  # Cenário 1: Sem intervenção (alta transmissão)
beta_cenario2 = (
    0.4  # Cenário 2: Com intervenção (uso de repelentes, eliminação de focos)
)

# Vetor de tempo: simulação a decorrer ao longo de 100 dias
t = np.linspace(0, 100, 100)


def modelo_seir(y, t, N, beta, sigma, gamma):
    """
    Função que define as equações diferenciais do modelo SEIR.
    """
    S, E, I, R = y

    dSdt = -beta * S * I / N

    dEdt = (beta * S * I / N) - (sigma * E)

    dIdt = (sigma * E) - (gamma * I)

    dRdt = gamma * I

    return dSdt, dEdt, dIdt, dRdt


y0 = S0, E0, I0, R0

# =====================================================================
# 3. Execução das Simulações (Integração Numérica)
# =====================================================================
# Resolvendo o cenário 1 (Sem intervenção)
ret1 = odeint(modelo_seir, y0, t, args=(N, beta_cenario1, sigma, gamma))
S1, E1, I1, R1 = ret1.T

# Resolvendo o cenário 2 (Com intervenção)
ret2 = odeint(modelo_seir, y0, t, args=(N, beta_cenario2, sigma, gamma))
S2, E2, I2, R2 = ret2.T

# =====================================================================
# 4. Geração dos Gráficos (Comparativo)
# =====================================================================
# Criando uma figura com dois gráficos lado a lado (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Plot Cenário 1 ---
ax1.plot(t, S1 / 1000, "b", alpha=0.7, linewidth=2, label="Suscetíveis (S)")
ax1.plot(t, E1 / 1000, "y", alpha=0.7, linewidth=2, label="Expostos (E)")
ax1.plot(t, I1 / 1000, "r", alpha=0.7, linewidth=2, label="Infetados (I)")
ax1.plot(t, R1 / 1000, "g", alpha=0.7, linewidth=2, label="Recuperados (R)")
ax1.set_title(f"Cenário 1: Sem Intervenção ($\\beta$ = {beta_cenario1})", fontsize=13)
ax1.set_xlabel("Tempo (Dias)", fontsize=11)
ax1.set_ylabel("População (em milhares)", fontsize=11)
ax1.legend(loc="best")
ax1.grid(True, linestyle="--", alpha=0.6)

# --- Plot Cenário 2 ---
ax2.plot(t, S2 / 1000, "b", alpha=0.7, linewidth=2, label="Suscetíveis (S)")
ax2.plot(t, E2 / 1000, "y", alpha=0.7, linewidth=2, label="Expostos (E)")
ax2.plot(t, I2 / 1000, "r", alpha=0.7, linewidth=2, label="Infetados (I)")
ax2.plot(t, R2 / 1000, "g", alpha=0.7, linewidth=2, label="Recuperados (R)")
ax2.set_title(f"Cenário 2: Com Intervenção ($\\beta$ = {beta_cenario2})", fontsize=13)
ax2.set_xlabel("Tempo (Dias)", fontsize=11)
ax2.set_ylabel("População (em milhares)", fontsize=11)
ax2.legend(loc="best")
ax2.grid(True, linestyle="--", alpha=0.6)

# Título geral da figura
fig.suptitle(
    "Comparativo da Dinâmica SEIR na Propagação da Dengue", fontsize=16, y=1.02
)
plt.tight_layout()

# Mostrar o gráfico final na tela
plt.show()
