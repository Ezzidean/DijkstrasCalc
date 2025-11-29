START = "A1"



class Vortex:
    def __init__(self,name, distanceFromStart=None, neighbors=None, start=START):
        #Change to take in values from list 
        self.name = name
        self._distance = distanceFromStart
        self.neighbors = neighbors
        self.start = start
    
    @property
    def distanceFromStart(self):
        return self._distance

    @distanceFromStart.setter
    def distanceFromStart(self, distance):
        self._distance = distance

"""
#Distance from start
def startDistanceCalc(node):
    #Starting nodes
    if (node == START):
        startDis = 0
        return startDis
    #Non-starting nodes
    elif(node.neighbors):
        #Find out if start is a neigbor
        node.neighbors
        distances = []
        startDis=0
        return startDis



print("Node Name:", N1.name,"\nAdj nodes:", N1.neighbors,"\nDistance from start:", startDistanceCalc(N1.name))
"""