# Modelagem Matemático-Computacional Aplicada à Epidemiologia: Simulação da Dengue via Modelo SEIR

Este repositório contém a implementação de um modelo epidemiológico **SEIR** (Suscetíveis, Expostos, Infetados, Recuperados) para a simulação da propagação da dengue sob dois cenários distintos (com e sem intervenção humana).

---

## 📌 Visão Geral do Modelo SEIR

O modelo SEIR divide a população de tamanho total $N$ em quatro compartimentos (ou estados de saúde) que evoluem ao longo do tempo:

1. **Suscetíveis (S):** Indivíduos saudáveis que podem contrair o vírus ao serem picados por mosquitos transmissores infetados.
2. **Expostos (E):** Indivíduos que já contraíram o vírus (foram picados), mas ainda estão no período de incubação e não transmitem a doença.
3. **Infetados (I):** Indivíduos infetados e capazes de transmitir a doença (ou manter o ciclo de transmissão vetor-hospedeiro ativo).
4. **Recuperados (R):** Indivíduos que se recuperaram da infecção e adquiriram imunidade.


### ⚙️ Parâmetros da Simulação
- **População Total (N):** $100.000$ indivíduos.
- **Condições Iniciais:** 10 infetados (I_0 = 10), 0 expostos (E_0 = 0), 0 recuperados (R_0 = 0) e 99.990 suscetíveis (S_0).
- **Período de Incubação Médio (sigma):** 5 dias (sigma = 0.2).
- **Período Médio de Recuperação (gamma):** 7 dias (gamma ≈ 0.143).
- **Cenários Analisados:**
  - **Cenário 1 (Sem Intervenção):** Alta taxa de transmissão (beta = 0.9), representando uma situação em que não há controle de vetores ou uso de repelentes.
  - **Cenário 2 (Com Intervenção):** Redução da taxa de transmissão pela metade (beta = 0.4), simulando o impacto de campanhas de eliminação de focos de mosquitos e uso generalizado de repelentes.

---

## 📁 Estrutura do Repositório

- [main.py]: Código principal contendo a definição das equações do modelo, a integração numérica das EDOs utilizando a biblioteca `scipy.integrate.odeint`, e a plotagem dos resultados com o `matplotlib`.
- [pyproject.toml]: Arquivo de configuração do projeto definindo dependências (`numpy`, `scipy`, `matplotlib`) e requisitos de versão do Python.
- [uv.lock]: Arquivo de bloqueio de dependências gerado pelo gerenciador de pacotes `uv`.

---

## 🚀 Como Executar o Projeto

Você pode executar o projeto de duas formas principais: usando o moderno gerenciador **uv** (altamente recomendado e já configurado neste repositório) ou utilizando o **pip** padrão do Python.

### Requisitos Prévios
- Python instalado (versão recomendada: `>=3.14` conforme o `pyproject.toml`).

### Opção 1: Utilizando o `uv` (Recomendado)
O `uv` é um gerenciador extremamente rápido para projetos Python. Se você já o tem instalado, basta executar o comando abaixo na raiz do projeto:

```bash
uv run main.py
```
*Nota: O `uv` criará o ambiente virtual automaticamente e instalará as dependências (`numpy`, `scipy` e `matplotlib`) necessárias antes de executar o script.*

### Opção 2: Utilizando Ambiente Virtual Padrão (`venv` + `pip`)
Se preferir usar o ecossistema padrão do Python:

1. **Criar um ambiente virtual:**
   ```bash
   python -m venv .venv
   ```

2. **Ativar o ambiente virtual:**
   - **No Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **No Windows (Prompt de Comando - cmd):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **No Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. **Instalar as dependências:**
   Você pode instalar as dependências declaradas no arquivo `pyproject.toml` executando:
   ```bash
   pip install .
   ```
   Ou instalá-las individualmente:
   ```bash
   pip install numpy scipy matplotlib
   ```

4. **Executar a simulação:**
   ```bash
   python main.py
   ```

---

## 📊 Resultados Esperados

Ao executar o script, será aberta uma janela gráfica gerada pelo `matplotlib` mostrando dois gráficos comparativos lado a lado:
1. **Cenário 1 (Sem Intervenção):** Apresenta um pico de infecção precoce e muito acentuado, indicando uma rápida propagação e uma alta taxa de contágio simultâneo.
2. **Cenário 2 (Com Intervenção):** O pico de infecção é reduzido de forma drástica ("achatamento da curva") e deslocado mais para a direita (dando mais tempo de resposta às entidades de saúde pública).

---
