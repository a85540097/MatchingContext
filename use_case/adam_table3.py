from Lib import *
from rdflib import Graph, Literal, Namespace, URIRef, RDF, RDFS, XSD, ConjunctiveGraph
from urllib.parse import quote


COSINE_FILE = './Adam_May__footballer__xaa'
VEC1_CSV = './triples/Adam_May__footballer_.csv'
VEC1_URI = "http://dbpedia.org/resource/Adam_May_(footballer)"
SLICE_PARAM = 100

PREFIX = "http://example.org/emc/"
NAMED_GAPH_PREFIX = "http://emc.org/"

if __name__ == "__main__":
    k = 51
    # compute edos for adam and its 50
    shaun_triples = load_csv(VEC1_URI,VEC1_CSV)
    edos,triples = from_cosine_to_edo(COSINE_FILE,shaun_triples,k)
    edos.sort(key=lambda x: (len(x[0]),x[3]))
    edos.reverse()
    # print table 3 column 1 -> 6. To find cosine similarity values see ./Adam_May__footballer__xaa
    i = 0 
    for edo in edos:
        print(str(i) + " " + str(len(edo[0])) + " " +str(len(edo[1])) + " " + str(len(edo[2])) + " " + str(edo[3]))
        i += 1



