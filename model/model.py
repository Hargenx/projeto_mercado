import pandas as pd

class ModeloSupermercado:
    def __init__(self, caminho_dados):
        self.df = pd.read_csv(caminho_dados, sep=";", decimal=",", thousands=".")
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df = self.df.sort_values("Date")

    def criar_coluna_mes(self):
        self.df["Mes"] = self.df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

    def obter_dados_por_mes(self, mes):
        return self.df[self.df["Mes"] == mes]

    def calcular_total_do_mes(self, mes, coluna_alvo="Total"):
        df_mes = self.obter_dados_por_mes(mes)
        total_mes = df_mes[coluna_alvo].sum()
        return total_mes
    
    def calcular_total_cogs(self, mes):
        df_filtrado = self.obter_dados_por_mes(mes)
        total_cogs = df_filtrado["cogs"].sum()
        return total_cogs

    def calcular_margem_de_lucro_bruta(self, mes):
        total_do_mes = self.calcular_total_do_mes(mes)
        total_custo = self.calcular_total_cogs(mes)
        #Margem de Lucro Bruta = (Total de Vendas - Total de Custos) / Total de Vendas
        margem_de_lucro_bruta = ((total_do_mes - total_custo) / total_do_mes)*100
        return margem_de_lucro_bruta
