# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:12:15 2023

@author: Dongli
"""

import networkx as nx
import matplotlib.pyplot as plt

relationships = {}

relationships['Dongli'] = ['Adam', 'Frank', 'George']
relationships['Adam'] = ['Ema', 'Dongli', 'Bob']
relationships['Ema'] = ['Adam', 'Bob', 'Dolly']
relationships['Bob'] = ['Adam', 'Ema', 'Dolly']
relationships['Dolly'] = ['Ema', 'Bob']
relationships['Frank'] = ['Dongli']
relationships['George'] = ['Dongli']

# Create a directed graph from the dictionary
G = nx.DiGraph(relationships)

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # Define a layout for the nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', arrowsize=20)

# Show the plot
plt.show()