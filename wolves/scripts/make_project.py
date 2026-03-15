import os
import csv
import shutil

project_name = "/mnt/c/Users/stein/Documents/Aulas/HealthDS/wolves"

folders = [
    "data",
    "cytoscape",
    "images",
    "docs"
]

# Create project structure
os.makedirs(project_name, exist_ok=True)

for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# -----------------------
# Create nodes.csv
# -----------------------
nodes = [
    ["id","label","type","area"],
    ["wolf","Gray Wolf","predator","forest"],
    ["elk","Elk","herbivore","valley"],
    ["willow","Willow Tree","plant","riverbank"],
    ["beaver","Beaver","ecosystem_engineer","riverbank"],
    ["rabbit","Rabbit","herbivore","grassland"],
    ["grass","Grass","plant","grassland"]
]

with open(f"{project_name}/data/nodes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(nodes)

# -----------------------
# Create edges.csv
# -----------------------
edges = [
    ["source","target","relationship","effect"],
    ["wolf","elk","predation","negative"],
    ["wolf","rabbit","predation","negative"],
    ["elk","willow","grazing","negative"],
    ["rabbit","grass","grazing","negative"],
    ["willow","beaver","habitat","positive"],
]

with open(f"{project_name}/data/edges.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(edges)

# -----------------------
# Create expression.csv
# -----------------------
expression = [
    ["node","year","population_index"],
    ["wolf","1990","0.1"],
    ["wolf","2005","0.8"],
    ["elk","1990","0.9"],
    ["elk","2005","0.4"],
    ["willow","1990","0.3"],
    ["willow","2005","0.7"],
]

with open(f"{project_name}/data/expression.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(expression)

# -----------------------
# Create README
# -----------------------
readme_text = """# Yellowstone Ecosystem Graph

This project models ecological relationships inspired by the Yellowstone wolf reintroduction.

## Data

Three CSV tables are used:

- nodes.csv — ecosystem entities
- edges.csv — relationships between entities
- expression.csv — population/expression levels

## Visualization

The graph will be visualized using Cytoscape.

## Structure

data/ – CSV tables  
cytoscape/ – Cytoscape project  
images/ – Graph screenshots  
docs/ – Final report
"""

with open(f"{project_name}/README.md", "w") as f:
    f.write(readme_text)

print("Project structure created successfully.")