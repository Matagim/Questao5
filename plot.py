import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Core import CountCalls

def reporti(searchers, problems, verbose=True):
    """
    Mostra estatísticas resumidas para cada `searcher` em cada problema.
    Cria gráficos de barras para visualizar as métricas de desempenho.
    """
    for p in problems:    
        title = p.__str__()# Nome do problema
        plotation = []  # Dados para plotagem
        labels = []     # Labels dos searchers

        for searcher in searchers:
            prob = CountCalls(p)  # Conta chamadas para o problema
            soln = searcher(prob)  # Soluciona o problema
            counts = prob._counts  # Obtém métricas
            counts.update(actions=len(soln), cost=soln.path_cost)
            
            # Armazena os valores das métricas
            plotation.append([counts['result'], counts['is_goal'], counts['cost'], counts['actions']])
            labels.append(searcher.__name__)  # Nome do searcher
            print(plotation)
        plot_graph(plotation, labels, title)
           
        


        
        
def plot_graph(data, labels, title):
    """
    Cria um gráfico de barras para os dados fornecidos.

    Args:
        data (list of list): Lista contendo os valores das métricas para cada searcher.
        labels (list): Lista de nomes dos searchers.
        title (str): Título do gráfico.
    """
    num_searchers = len(data)
    num_metrics = len(data[0]) if data else 0
    metric_names = ["result", "is_goal", "cost", "actions"]
    bar_conteiner = []
    
    # Configuração do gráfico
    x = range(num_metrics)  # Posições das métricas
    largura = 0.8 / num_searchers  # Largura das barras
    plt.figure(figsize=(10, 6))
    
    for i, searcher_data in enumerate(data):
        # Define posições para as barras de cada searcher
        x_positions = [pos + i * largura for pos in x]
        bars = plt.bar(x_positions, searcher_data, width=largura, label=labels[i])
        

        for bar in bars:
            
            x_text = bar.get_x() + bar.get_width() / 2
            y_text  = bar.get_height()
            
            plt.text(
            x_text, y_text,  f'{y_text:.2f}',  # Texto formatado com duas casas decimais
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='black'
        )
    
    # Configurações do eixo X e título
    plt.title(title, fontsize=16)
    plt.xlabel("Métricas", fontsize=12)
    plt.ylabel("Valores", fontsize=12)
    plt.xticks([pos + largura * (num_searchers / 2 - 0.5) for pos in x], metric_names)
    plt.legend(title="Searchers")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()