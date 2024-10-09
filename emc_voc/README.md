# We describe here the EMC vocabulary

- We propose an RDF vocabulary that we call 'emc-voc', in order to semantically represent, store and query the entity matching contexts (i.e.,  epsilon, delta and omega) that we compute for pairs of individuals. 
This vocabulary is used to describe the link that is created when an entity matching context is detected for a pair of individuals. 
In RDF, this is equivalent to writing statements about statements, also known as reification in logic. 
Different representations have been proposed in the literature (Orlandi et al. 2021 for a comparative study). 
We modelled these statements in the form of singleton properties (Nguyen et al 2014). 
Other models to represent the contexts are possible, such as RDF-star https://w3c.github.io/rdf-star/cg-spec/ or by associating the contextual link to a named graph. 
We chose singleton properties due it is conciseness and the fact that it is supported by all triple stores, which is not the case for RDF-star. 

- For example the most specific EMC for Adam May and Jack Lankester is an EMC identified by the label emc\_id\_e\_3\_d\_3\_o\_3.
We express this fact with the triple:

```
Adam_May emc:emc_id_e_3_d_3_o_3 Jack_Lankester .
```

emc_id_e_3_d_3_o_3 is described with the vocabulary 'emc-voc':

```
emc_id_e_3_d_3_o_3 rdf:type emc:EMC ;
                            emc:epsilon e_3 ;
                            emc:delta d_3 ;
                            emc:omega o_3 .   
```

We can further describe each epsilon, delta and omega. 
For example e_3:

```
    emc:e_3 emc:includes dbo:position ;
            emc:includes dbo:wikiPageWikiLink ;
            emc:includes dbp:goals ;
	        emc:includes dbp:position ;
            emc:includes dbp:wikiPageUsesTemplate ;
            emc:includes dbp:years ;
	        emc:includes dct:subject .
```

- The file emc-voc.ttl describes the vocabulary. 
The file figure.pdf gives a graphical representation of emc-voc and a graphical representation of the
emc of a pair of football players: Adam May and Jack Lankester.

- Refs:
  - Nguyen, V., Bodenreider, O., Sheth, A.P.: Don’t like RDF reification?: making statements about statements using singleton property. 
In: Chung, C., Broder, A.Z., Shim, K., Suel, T. (eds.) 23rd International World
Wide Web Conference, WWW ’14, Seoul, Republic of Korea, April 7-
11, 2014. pp. 759–770. ACM (2014). https://doi.org/10.1145/2566486.2567973,
https://doi.org/10.1145/2566486.2567973
  - Orlandi, F., Graux, D., O’Sullivan, D.: Benchmarking rdf metadata repre-
sentations: Reification, singleton property and rdf. In: 2021 IEEE 15th In-
ternational Conference on Semantic Computing (ICSC). pp. 233–240 (2021).
https://doi.org/10.1109/ICSC50631.2021.00049
