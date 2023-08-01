#library
import pandas as pd
from scipy import stats

#pathway
arq_path = input (r"path:")
col_name = "SW QRN" 

#reading
df = pd.read_excel(arq_path)
colunm = df[col_name].dropna()

#main
def shapiro_wilk_test(data):
    _, p_value = stats.shapiro(data)
    return p_value

# run
p_value = shapiro_wilk_test(colunm)

if p_value > 0.05:
    print(f'O p-value é {p_value:.4f}. Distribuição normal.')
else:
    print(f'O p-value é {p_value:.4f}. Distribuição não normal.')
