
FILTERED_PROPERTIES = []

def uri_2_prefix(uri):
    uri_split = uri.split('/')
    tmp = uri_split[-1]
    tmp = tmp.replace('.','_')
    tmp = tmp.replace('(','_')
    tmp = tmp.replace(')','_')
    tmp = tmp.replace(',','_')
    tmp = tmp.replace("'",'_')
    tmp = tmp.replace('&','_')
    return tmp

def load_csv(uri,file_path):
    triples = []
    with open(file_path,"r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            if not line.startswith("http"):
                continue
            line_split = line.strip().split(",")
            t = (uri,line_split[0],line_split[1])
            triples.append(t)
    return triples

def get_properties(instance):
    properties = set()
    for s,p,o in instance:
        if p not in properties:
            properties.add(p)
    return properties

def get_property_values(prop,instance):
    values = []
    for s,p,o in instance:
        if p == prop:
            values.append(o)
    return values

def compute_shared_unshared_properties(pair):
    i1_properties = get_properties(pair[0])
    i2_properties = get_properties(pair[1])
    
    shared_properties = i1_properties & i2_properties
    unshared_properties = i1_properties ^ i2_properties

    return shared_properties, unshared_properties

def compute_edo_for_a_pair(i1,i2):
        # epsilon: the set of properties with the same values
        # delta: the set of properties with different values
        # omega: the set of unshared properties
        epsilon, delta, omega = [],[],[]
        shared,unshared = compute_shared_unshared_properties((i1,i2))
        
        i1_properties = get_properties(i1)
        i2_properties = get_properties(i2)

        # shared and unsahred properties must cover all properties
        assert(set(list(i1_properties) + list(i2_properties)) == set(list(shared) + list(unshared))) 

        # for each property in shared
        for p in shared:
            # filter properties
            if p in FILTERED_PROPERTIES:
                continue
            # we not dot want the type here
            if "type" in p:
                continue
            # list of values for instances x and y     
            i1_list_of_values = get_property_values(p,i1)
            i2_list_of_values = get_property_values(p,i2)
            
            # we consider all properties as data properties
            i1_set_of_values = set(i1_list_of_values)
            i2_set_of_values = set(i2_list_of_values)

            i1_and_i2 = i1_set_of_values & i2_set_of_values
            i1_xor_i2 = i1_set_of_values ^ i2_set_of_values
 
            if len(i1_and_i2) != 0:
                epsilon.append(p)
            if len(i1_xor_i2) != 0:
                delta.append(p)
            # we can not have both sets empty 
            if len(i1_and_i2) == 0 and len(i1_xor_i2) ==0:
                raise exception("values/properties exception")

        for p in unshared:
            # filter properties
            if p in FILTERED_PROPERTIES:
                continue
            omega.append(p)

        # sort epsilon, delta omega in oder to use them as dict keys
        epsilon.sort()
        delta.sort()
        omega.sort()

        return epsilon,delta,omega


def cosine_line_correction(line):
    line_corrected = line.replace("(http",'("http')
    line_corrected = line_corrected.replace(",0.",'",0.')
    line_corrected = line_corrected.replace(",1.",'",1.')
    return line_corrected

def from_cosine_to_edo(file_cosine,query_triple,k):
    edos = []
    triples = []
    with open(file_cosine) as input_file:
        lines = input_file.readlines()
        for line in lines:
            # we reach nb edos required
            if len(edos) == k:
                break
            line_corrected = cosine_line_correction(line)
            tuple_ = eval(line_corrected)
            uri, cosine = tuple_[0],tuple_[1]
            rdf_file = uri_2_prefix(uri) + ".csv"
            try:
                rdf_triple = load_csv(uri,"./triples/" + rdf_file)
                edo = compute_edo_for_a_pair(query_triple,rdf_triple)
                t = (edo[0],edo[1],edo[2],uri)
                edos.append(t)
                triples.append(rdf_triple)

            except FileNotFoundError:
                print("File " + "./triples/"+ rdf_file + " not found")
    return edos, triples 


