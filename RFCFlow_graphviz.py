from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='SAP RFC Read Connection Flow', format='png')

# Nodes
dot.node('A', 'Start: Configure RFC Parameters\n(ASHOST, SYSNR, CLIENT, USER, PASSWD, LANG)')
dot.node('B', 'Initialize RFC Connection\n(C++ Application using SAP RFC Library)')
dot.node('C', 'Establish Connection to SAP System')
dot.node('D', 'Execute RFC Function Module\n(e.g., RFC_READ_TABLE)')
dot.node('E', 'Retrieve Data in Chunks')
dot.node('F', 'Store / Process Data')
dot.node('G', 'Connection Close & Cleanup')
dot.node('H', 'End')

# Edges
dot.edges([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H')])

# Render and display
file_path = '/mnt/data/sap_rfc_flow'
dot.render(file_path, cleanup=True)
file_path + '.png'
