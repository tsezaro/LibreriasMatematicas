import networkx as nx
import matplotlib.pyplot as plt
 

#1 
class Grafo:


    
    #grafo = nx.Graph()   
    def __init__(self, enlaces):        
        #self.aristasYPesos= aristasYPesos
        self.grafo = nx.Graph()       
        self.grafo.add_weighted_edges_from(enlaces) 
 
    def emitoGrafo(self,direcciones = None):
        #if direcciones == None:
        pos = nx.shell_layout(self.grafo)
        #else:
            #pos = nx.shell_layout(direcciones)
        nx.draw_networkx_nodes(self.grafo, pos, node_color='red', node_size=700)
        nx.draw_networkx_labels(self.grafo, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edges(self.grafo, pos, edge_color='blue', width=3, arrowstyle= '<|-|>', arrowsize = 10)
        labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
 
    def nodos(self):
        print("Número de nodos: ", self.grafo.number_of_nodes())


    #2.1
    def vecinos(self, nodo):
        print("Vecinos: ", list(self.grafo.neighbors(nodo)))

    #2.2
    def emitircantidadAr(self):
        print("Cantidad de aristas de cada nodo: ",self.grafo.degree()) 
    
    #2.3
    def matriz(self):
        print(dict(self.grafo.degree()))

    #2.4
    def matrizAdyacencia(self):
        M = nx.adjacency_matrix(self.grafo)
        print(M.todense()) 
    

    #2.5
    def matrizIncidencia(self):
        M = nx.incidence_matrix(self.grafo)
        print(M.todense())       
        

    #2.6
    def valores(self, nodo):
        print("Valores de los enlaces del nodo: ",self.grafo,'c')
    
   #2.7
    def longitud(self,nodo):
        print("Longitud de Ruta mas corta desde: ",nx.single_source_shortest_path_length(self.grafo,nodo))

    #2.8
    def promCorfloydWarshall(self):
        print("Promedio de la ruta mas corta ", nx.algorithms.average_shortest_path_length(self.grafo, method="floyd-warshall"))

    #2.9
    def RutacortaDijkstra(self,nodo1,nodo2):
        print("Ruta mas corta usando el algoritmo de Dijkstra entre:",nx.algorithms.dijkstra_path(self.grafo,nodo1,nodo2))

    #2.10
    def longCorta(self,nodo1,nodo2):
        print("Longitud de Ruta ponderada más corta entre:",nx.dijkstra_path_length(self.grafo,nodo1,nodo2))

    #2.11
    def logiN(self,nodo):
        print("Longitud de Ruta ponderada más corta desde el nodo:", nx.single_source_dijkstra_path_length(self.grafo,nodo))

    #2.12
    def radioG(self):
        print("Radio:",nx.radius(self.grafo))


    #2.13 2.14 2.15 2.16 2.17
    def UVWXYZ(self):
        print("Diámetro:", nx.diameter(self.grafo))
        print("Excentricidad:", nx.eccentricity(self.grafo))
        print("Centro:", nx.center(self.grafo))
        print("Periferia:", nx.periphery(self.grafo))
        print("Densidad:", nx.density(self.grafo))

    #2.18 2.19 2.20
    def emitoGrafodirigido(self):
        pos = nx.shell_layout(self.grafo)
        H = self.grafo.to_directed()
        pos = nx.shell_layout(H)
        pos = nx.shell_layout(H)
        nx.draw_networkx_nodes(H, pos, node_color='red', node_size=700)
        nx.draw_networkx_labels(H, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edges(H, pos, edge_color='blue', width=3, arrowstyle= '<|-|>', arrowsize = 10)
        labels = nx.get_edge_attributes(H, 'weight')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()



grafo = Grafo([('a', 'b', 6),
               ('a', 'd', 2),
               ('a', 'h', 5),
               ('b', 'c', 7),
               ('b', 'e', 8),
               ('b', 'g', 11),
               ('c', 'g', 4),
               ('d', 'a', 9),
               ('d', 'c', 3),
               ('d', 'f', 5),
               ('e', 'd', 6),
               ('e', 'h', 12),
               ('f', 'b', 2),
               ('f', 'g', 9)])
 

grafo.vecinos('h')
grafo.emitircantidadAr()
grafo.matriz()
grafo.matrizAdyacencia()
grafo.matrizIncidencia()
grafo.valores('c')
grafo.longitud('c')
grafo.promCorfloydWarshall()
grafo.RutacortaDijkstra('a','h')
grafo.logiN('g')
grafo.radioG()
grafo.UVWXYZ()
grafo.emitoGrafo()
grafo.emitoGrafodirigido()



#3

import re 

texto ="""
1. AEP;CNQ;95.45;680.00
2. EZE;IRJ;39.50;4780.00
3. JNI;COC;51.44;1160.00
4. LPG;AEP;66.26;7580.00
5. MDQ;GPO;18.85;720.00
6. FDO;RYO;26.49;340.00
"""

busqueda = r'(?<=;)[A-Z]{3}\;[0-9]{2}\.[0-9]{2}'


x = re.findall(busqueda, texto) 

print(x)

