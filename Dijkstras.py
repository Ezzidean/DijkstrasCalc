from Node import Vortex
nPrime = []
    
A1 = Vortex("A1", None, [["A2", 5], ["A3", 2]])
A2 = Vortex("A2", None, [["A1", 3], ["A3", 4]])
A4 = Vortex("A4", None, [["A2", 4]])

def distanceCalc(node):
    # Starting nodes
    if node.name == node.start:
        node.distanceFromStart = 0
        return node.distanceFromStart
    # Non-starting nodes
    for name, distance in node.neighbors:
        print("Neighbor:", name, "Distance:", distance)
        if (name == node.start):
            node.distanceFromStart = distance
            return distance

#Checks node
#print("Node Name:", N1.name,"\nAdj nodes:", N1.neighbors,"\nDistance from start:", distanceCalc(N1))

def dijkstras(node):
    if  (node.distanceFromStart == 0):
        nPrime = node.name
        return nPrime
    else:
        return
        
    #TODO Complete calculation code 
        
    #Add smallest distance from start to Nprime
    #Move to smallest node
    #add smallest node Nprim
    
    #Probably need distance and name from object
    def calucation(prevN, currN, Nprime):
        if(Nprime == 0):
        #Checks if currently at Nprime
            return prevN
        elif(prevN + currN < Nprime):
        #Compares curr + prev distance compared to N prime
            Nprime = currN
            return Nprime
        else:
            return Nprime
    return nPrime

def nPrimeAdder(listItem):
    print(nPrime)
    if (listItem != None):
        nPrime.append(listItem)
        return nPrime
    else:
        return

#TODO Fix Nprime: currently it is being redefined locally within functions (Possibly make it an Object)
def testing(nodes):
    for node in nodes:
        print("Node Name:", node.name,"\nAdj nodes:", node.neighbors,"\nDistance from of", node.name, "from start:", distanceCalc(node))
        nPrime = nPrimeAdder((dijkstras(node)))
        print("CurrNode", node.name, "NPrime:", nPrime)
    
def main():
    vortexs = [A1,A2,A4]
    #outputs information
    testing(vortexs)

    #calcuation 



main()

