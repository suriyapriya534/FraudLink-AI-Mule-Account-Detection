import networkx as nx
import pandas as pd

def build_graph(file_path):
    df = pd.read_csv(file_path)
    G = nx.DiGraph()

    for _, row in df.iterrows():
        G.add_edge(row['sender'], row['receiver'], 
                   amount=row['amount'], 
                   channel=row['channel'])
    return G