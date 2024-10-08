# We describe here the EMC vocabulary

- We propose an RDF vocabulary that we call 'emc-voc', in order to semantically represent, store and query the entity matching contexts (i.e.,  epsilon, delta and omega) that we compute for pairs of individuals. 
This vocabulary is used to describe the link that is created when an entity matching context is detected for a pair of individuals. 
In RDF, this is equivalent to writing statements about statements, also known as reification in logic. 
Different representations have been proposed in the literature (Orlandi et al. 2021 for a comparative study). 
We modelled these statements in the form of singleton properties (Nguyen et al 2014}. 
Other models to represent the contexts are possible, such as RDF-star\footnote{\url{https://w3c.github.io/rdf-star/cg-spec/}} or by associating the contextual link to a named graph. 
We chose singleton properties due it is conciseness and the fact that it is supported by all triple stores, which is not the case for RDF-star. 

- For example the most specific EMC for Adam\_May and Jack\_Lankester is an EMC identified by the label emc\_id\_e\_3\_d\_3\_o\_3.
We express this fact with the triple:
'''
Adam\_May emc\_id\_e\_3\_d\_3\_o\_3 Jack\_Lankester .
'''
emc\_id\_e\_3\_d\_3\_o\_3 
