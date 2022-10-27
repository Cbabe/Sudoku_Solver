
class Node:

    def __init__(self, idx, data=0):  # Constructor
        """
        id : Integer (1, 2, 3, ...)
        """
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self, neighbour, weight=0):
        """
        neighbour : Node Object
        weight : Default Value = 0

        adds the neightbour_id : wt pair into the dictionary
        """
        if neighbour.id not in self.connectedTo.keys():
            self.connectedTo[neighbour.id] = weight

    # setter
    def setData(self, data):
        self.data = data

    # getter
    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getData(self):
        return self.data

    def getWeight(self, neighbour):
        return self.connectedTo[neighbour.id]

    def __str__(self):
        return str(self.data) + " Connected to : " + \
            str([x.data for x in self.connectedTo])


class Graph:

    totalV = 0  # total vertices in the graph

    def __init__(self):
        """
        allNodes = Dictionary (key:value)
                   idx : Node Object
        """
        self.allNodes = dict()

    def addNode(self, idx):
        """ adds the node """
        if idx in self.allNodes:
            return None

        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data):
        """ set node data acc to idx """
        if idx in self.allNodes:
            node = self.allNodes[idx]
            node.setData(data)
        else:
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt=0):
        """
        Adds edge between 2 nodes
        Undirected graph

        src = node_id = edge starts from
        dst = node_id = edge ends at

        To make it a directed graph comment the second line
        """
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)

    def isNeighbour(self, u, v, total):
        """
        check neighbour exists or not
        """
        if u >= 1 and u <= total and v >= 1 and v <= total and u != v:
            if v in self.allNodes[u].getConnections():
                return True
        return False

    def printEdges(self):
        """ print all edges """
        for idx in self.allNodes:
            node = self.allNodes[idx]
            for con in node.getConnections():
                print(node.getID(), " --> ",
                      self.allNodes[con].getID())

    # getter
    def getNode(self, idx):
        if idx in self.allNodes:
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self):
        return self.allNodes.keys()
