import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Simulando logs de monitoramento de servidor (CPU % e Memória RAM %)
np.random.seed(42)
n = 1000

# 98% dos logs são requisições normais (CPU entre 10% e 40%, RAM entre 20% e 50%)
cpu_normal = np.random.normal(25, 5, 980)
ram_normal = np.random.normal(35, 5, 980)

# 2% dos logs são ANOMALIAS (Ataques DDoS, leaks de memória ou travamentos)
cpu_anomalia = np.random.uniform(80, 100, 20)
ram_anomalia = np.random.uniform(85, 99, 20)

df = pd.DataFrame({
    'cpu_usage': np.hstack((cpu_normal, cpu_anomalia)),
    'ram_usage': np.hstack((ram_normal, ram_anomalia))
})

# 2. Treinando o Isolation Forest
# contamination=0.02 indica que esperamos cerca de 2% de anomalias na base
iso_forest = IsolationForest(contamination=0.02, random_state=42)
df['anomalia'] = iso_forest.fit_predict(df[['cpu_usage', 'ram_usage']])

# O Isolation Forest retorna -1 para Outliers (Anomalias) e 1 para Dados Normais
df['status'] = df['anomalia'].map({1: '🟢 Normal', -1: '🚨 Outlier (Anomalia)'})

print("📊 --- RESULTADO DA DETECÇÃO DE OUTLIERS ---")
print(df['status'].value_counts())

print("\n🚨 --- EXEMPLOS DE ANOMALIAS DETECTADAS PELO MODELO ---")
anomalias_detectadas = df[df['anomalia'] == -1]
print(anomalias_detectadas.head(10))