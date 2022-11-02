#!/usr/bin/python3
from re import A
import xml.sax

from Clases import Atribute, Node, Edge, Graph
class CustomContentHandler( xml.sax.ContentHandler ):
    def __init__(self, nodes, edges):
        self.CurrentData = ""
        self.id = ""
        self.id_osm = ""
        self.lon = ""
        self.lat = ""
        self.length = ""
        self.data = ""
        self.key = ""
        self.source = ""
        self.target = ""
        self.nodes = nodes
        self.edges = edges
        self.listAttr = ['osmid_original', 'lon', 'lat', 'length']
        self.listKeys = []

# Call when an element start
    
    def startElement(self, tag, attributes):
        self.CurrentData = tag

        if tag == 'node': #Se prepara para añadir un nodo
            self.id = attributes['id'] 

        elif tag == 'data': #Se prepara para añadir uno de los datos pedidos, evitando otras claves
            for key in self.listKeys:
                if key.id==attributes['key']:
                    self.key= attributes['key']
                    break
                else: 
                    self.key=""
            
        

        elif tag == 'edge': #Se prepara para añadir una arista
            self.source = attributes['source']
            self.target = attributes['target']
            self.id = attributes['id']

        elif tag == 'key': #Sirve para comprobar a qué id corresponden los datos que estamos buscando
            for x in self.listAttr:
                if x == attributes['attr.name']:
                    atr = Atribute(attributes['id'], attributes['attr.name'])
                    self.listKeys.append(atr)

                #He creado una clase Atribute para guardar tanto el id como el nombre del atributo, y este se añade a una lista, en la que solo se 
                #encuentran el nombre de los atributos que queremos usar

# Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "data":
            
            #Se compara la lista creada anteriormente, para que si el id y el nombre del atributo coinciden se guarde ese dato para la posterior
            #creación del nodo/arista

            for key in self.listKeys:
                
                if(self.key) == key.id and key.name == "osmid_original":
                    self.id_osm = self.data

                elif(self.key) == key.id and key.name == "lon":
                    self.lon = self.data

                elif(self.key) == key.id and key.name == "lat":
                    self.lat = self.data

                elif(self.key) == key.id and key.name == "length":
                    self.length = self.data

        if tag == "node":
            # CrearNodo como un metodo que tenga tanto el constructor, así como añadirlo a la lista
            node = Node(self.id, self.id_osm, self.lon, self.lat)
            self.nodes.append(node)
        
        if tag == "edge":
            edge = Edge(self.id, self.source, self.target, self.length)
            self.edges.append(edge)

        self.CurrentData = ''
    
   # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "data" and self.key!="":
            self.data = content

   

def main():

    nodes = []
    edges = []

    handler = CustomContentHandler(nodes, edges)

    xml.sax.parse('CR_Capital.xml', handler)
    
    graph = Graph(len(nodes))

    for node in nodes:
        print(node.__dict__)
    
    
    for x in edges:
        graph.add_edge(int(x.source), int(x.target))

    
    print("En ello")
    graph.print_adjList()


if __name__ == '__main__':
    main()