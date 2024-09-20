from rdflib import Graph, Literal, Namespace, URIRef, RDF, RDFS, XSD, ConjunctiveGraph
from urllib.parse import unquote

g = ConjunctiveGraph()
g.parse("out2.nq",format='nquads')


# Table 3
query="""
PREFIX emc: <http://example.org/emc/>
SELECT  ?emc ?size ?sized ?sizeo ?player2 ?cosine
WHERE{
    ?emc a emc:EMC ;
         emc:epsilon ?e ;
         emc:delta ?d ;
         emc:omega ?o .
    ?player1 ?emc ?player2 .
    ?player2 emc:hasCosine ?cosine .
    ?e emc:size ?size .
    ?d emc:size ?sized .
    ?o emc:size ?sizeo .
}
ORDER BY DESC (?size) (?player2)
"""
results = g.query(query)
print()
print("Table 3")
print("===========")
for row in results:
    print(str(row.emc) + " " + str(row.size) + " " + str(row.sized) + " " + str(row.sizeo) +" " + str(unquote(row.player2)) + " " +str(row.cosine))




# How many context ?
query1= """
PREFIX emc: <http://example.org/emc/>
SELECT (COUNT(?context) as ?TOTAL)
WHERE {
    ?context a emc:Context
}
"""

results = g.query(query1)
print()
print("Nb Contexts")
print("===========")
for row in results:
    print(row.TOTAL)

# How many EMC ?
query2="""
PREFIX emc: <http://example.org/emc/>
SELECT (COUNT(?emc) as ?TOTAL)
WHERE {
    ?emc a emc:EMC
}
"""
results = g.query(query2)
print()
print("Nb EMCs")
print("========")
for row in results:
    print(row.TOTAL)

# i1 EMC i2
query3="""
PREFIX emc: <http://example.org/emc/>
SELECT ?i1 ?i2
WHERE {
    ?i1  emc:emc_id_e_25_d_20_o_13 ?i2 
}
"""
results = g.query(query3)
print()
print("Individuals linked with: <emc:emc_id_e_25_d_20_o_13>")
print("===================================================")
for row in results:
    print(unquote(row.i1))
    print(unquote(row.i2))

# cosine of Adam_May and Marcus_Harness
query="""
PREFIX emc: <http://example.org/emc/>
PREFIX db:<http://dbpedia.org/resource/>
SELECT ?cosine
WHERE {
    db:Marcus_Harness emc:hasCosine ?cosine 
}
"""
results = g.query(query)
print()
print("Adam and Marcus cosine, table 3 col 7")
print("===================================================")
for row in results:
    print(unquote(row.cosine))

query="""
PREFIX emc: <http://example.org/emc/>
SELECT ?prop
WHERE {
    emc:emc_id_e_4_d_4_o_4 emc:epsilon ?epsilon .
    ?epsilon emc:includes ?prop .
}

"""
print()
print("properties in epsilon of Adam May and Leon Davies")
print("===================================================")
results = g.query(query)
for row in results:
    print(unquote(row.prop))

query="""
PREFIX emc: <http://example.org/emc/>
SELECT ?prop
WHERE {
    emc:emc_id_e_15_d_0_o_31 emc:delta ?delta .
    ?delta emc:includes ?prop .
}

"""
print()
print("properties in delta of Adam May and Sean Raggett")
print("===================================================")
results = g.query(query)
for row in results:
    print(unquote(row.prop))

print()
print("Propertie http://dbpedia.org/property/currentclub is in epsilon for (Adam_May,Leon_Davies) and in delta for (Adam_May,Sean Ragget)")



# named graph min/max cosine
query4="""
PREFIX emc: <http://example.org/emc/>
SELECT ?g 
WHERE {
    ?g emc:hasCosineMin "0.75"^^<http://www.w3.org/2001/XMLSchema#double> .
}
"""
print()
print("Named Graph with cosine min 0.75")
print("=================================")
results = g.query(query4)
for row in results:
    print(row.g)



# emc with team, goals, years, caps, clubs and diff in position
query5="""
PREFIX emc: <http://example.org/emc/>
SELECT ?emc
WHERE {
    ?emc a emc:EMC ;
        emc:epsilon ?e ;
        emc:delta ?d .
    ?e emc:includes <http://dbpedia.org/property/goals> ;
        emc:includes <http://dbpedia.org/ontology/team> ;
        emc:includes <http://dbpedia.org/property/years> ;
        emc:includes <http://dbpedia.org/property/caps> ;
        emc:includes <http://dbpedia.org/property/clubs> .
    ?d emc:includes <http://dbpedia.org/property/position> .
}
"""
print()
print("Query EMC by properties")
print("Epsilon: team, goals, years, caps, clubs")
print("Delta: position")
print("========================================")
results = g.query(query5)
for row in results:
    print(row.emc)

# players in the previous emcs
query6="""
PREFIX emc: <http://example.org/emc/>
SELECT ?player1 ?player2
WHERE {
    {?player1 emc:emc_id_e_18_d_14_o_22 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_10_d_4_o_14  ?player2 .}
    UNION
    {?player1 emc:emc_id_e_10_d_4_o_12 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_15_d_0_o_33 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_15_d_0_o_31 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_15_d_0_o_17 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_15_d_0_o_4 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_17_d_4_o_20 ?player2 .}
    UNION 
    {?player1 emc:emc_id_e_22_d_16_o_26 ?player2 .}

}
"""
results = g.query(query6)
print()
print("Players in the previous emcs")
print("============================")
for row in results:
    print(unquote(row.player2))


# emc with team, goals, years, caps, clubs and position
query7="""
PREFIX emc: <http://example.org/emc/>
SELECT ?emc
WHERE {
    ?emc a emc:EMC ;
        emc:epsilon ?e .
    ?e emc:includes <http://dbpedia.org/property/goals> ;
        emc:includes <http://dbpedia.org/ontology/team> ;
        emc:includes <http://dbpedia.org/property/years> ;
        emc:includes <http://dbpedia.org/property/caps> ;
        emc:includes <http://dbpedia.org/property/clubs> ;
        emc:includes <http://dbpedia.org/property/position> . 
}
"""
print()
print("Query EMC by properties")
print("Epsilon: team, goals, years, caps, clubs, position")
print("==================================================")
results = g.query(query7)
for row in results:
    print(row.emc)
"""
emc:emc_1_e_1_d_1_o_1
emc:emc_43_e_27_d_3_o_14
emc:emc_37_e_25_d_20_o_13
emc:emc_15_e_12_d_11_o_12
emc:emc_34_e_23_d_17_o_27
emc:emc_35_e_22_d_18_o_28
emc:emc_33_e_22_d_16_o_26
"""

query8="""
PREFIX emc: <http://example.org/emc/>
SELECT ?player1 ?player2
WHERE {
    {?player1 emc:emc_id_e_1_d_1_o_1 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_27_d_3_o_14 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_25_d_20_o_13 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_12_d_11_o_12 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_23_d_17_o_27 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_22_d_18_o_28 ?player2 .}
    UNION
    {?player1 emc:emc_id_e_22_d_16_o_26 ?player2 .}
}
"""
results = g.query(query8)
print()
print("Players in the previous emcs")
print("============================")
for row in results:
    print(unquote(row.player2))


