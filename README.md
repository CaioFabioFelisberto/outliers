# Cao de Guarda

Exemplo simples de deteccao de outliers em metricas de monitoramento de
servidores usando Python e o algoritmo `IsolationForest`, do scikit-learn.

O script simula 1.000 registros de uso de CPU e memoria RAM:

- 980 registros normais, com valores tipicos de CPU entre 10% e 40% e RAM
  entre 20% e 50%;
- 20 registros anomalos, representando cenarios como ataques DDoS, vazamentos
  de memoria ou travamentos;
- classificacao dos registros como `Normal` ou `Outlier (Anomalia)`.

## Tecnologias

- Python 3.12 ou superior
- NumPy
- pandas
- scikit-learn

## Estrutura do projeto

```text
.
├── src/
│   └── cao_de_guarda.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalacao

No Windows, abra o PowerShell na raiz do projeto e crie um ambiente virtual:

```powershell
py -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependencias:

```powershell
python -m pip install -r requirements.txt
```

Se o PowerShell bloquear a ativacao do ambiente virtual, execute o comando
abaixo uma vez na sua sessao:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Execucao

Com o ambiente virtual ativado:

```powershell
python .\src\cao_de_guarda.py
```

O programa exibe a contagem de registros normais e anomalos, seguida de uma
amostra das anomalias identificadas.

### Console do Windows

O script imprime emojis no resultado. Caso o console esteja usando uma
codificacao que nao suporte esses caracteres, execute-o assim:

```powershell
$env:PYTHONIOENCODING = "utf-8"
python .\src\cao_de_guarda.py
```

## Como funciona

1. Os dados de CPU e RAM sao gerados de forma deterministica com `seed=42`.
2. O `IsolationForest` e treinado com as duas metricas:

   ```python
   IsolationForest(contamination=0.02, random_state=42)
   ```

3. O parametro `contamination=0.02` informa ao modelo que aproximadamente 2%
   dos registros podem ser anomalias.
4. O modelo retorna:
   - `1` para registros normais;
   - `-1` para outliers.
5. Esses valores sao convertidos para os status exibidos no terminal.

## Limitacoes

Este projeto e um exemplo didatico. Os dados sao simulados e nao representam
logs reais de infraestrutura. Para uso em producao, seria necessario carregar
metricas reais, validar a qualidade dos dados, ajustar o modelo ao ambiente e
definir um fluxo de alertas e acompanhamento das anomalias.

## Licenca

Nenhuma licenca foi definida para este projeto.
