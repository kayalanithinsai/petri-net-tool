"""
Have to input Petrinet(create).
push tokens list to the queue.
for each queue element explore all possible states generated and push them to queue should I store a rank,parents dictionary for each possible tokens vector.

More concise algo:-
step-1
genrate n places, m transitions, get all arcs for the petrinet,initial state for tokens.
Step-2
"""
from Place import Place
from Arc import Arc
from Transition import Transition
class Petrinet:
    def __init__(self):
        self.places = []
        self.transitions = []
        self.arcs = []

    # function for adding places
    def add_place(self,place):
        assert (type(place)==Place), "object is not of type Place."
        self.places.append(place)

    # function for adding arcs
    def add_arc(self, arc):
        assert (type(arc)==Arc), "object is not of type Arc."
        self.arcs.append(arc)

    # function for adding transition
    def add_transition(self, transition):
        assert (type(transition)==Transition), "object is not of type Transition."
        self.transitions.append(transition)

    # function for geting a dictionary mapping for palce and its corresponding index
    def get_palce_index_mapping(self):
        m = {}
        cur=0
        for place in self.places:
            if m.get(place) == None:
                m[place] = cur
                cur+=1
        return m

    # function to find the initial state of the graph
    def find_initial_state(self):
        n = len(self.places)
        s = [1 for x in range(n)]
        self.placeindex = self.get_palce_index_mapping()
        for arc in self.arcs:
            if arc.status == "output":
                if s[self.placeindex[arc.to]]==1:
                     s[self.placeindex[arc.to]]=0
        return s

    # function to find the reachability graph
    def reachability_graph(self):
        queue = []
        vis = []
        graph_edges = []
        queue.append(self.find_initial_state())
        while len(queue) != 0:
            u = queue.pop(0)
            if u in vis:
                continue
            else:
                vis.append(u)
            for transition in self.transitions:
                if transition.can_fire(u,self.placeindex):
                    v = transition.fire(u,self.placeindex)
                    graph_edges.append([u,v,transition])
                    if v not in vis:
                        queue.append(v)
        self.print_graph(graph_edges)

    # function to print graph
    def print_graph(self,graph_edges):
        for edge in graph_edges:
            edge[0] = [str(x) for x in edge[0]]
            edge[1] = [str(x) for x in edge[1]]
            print("".join(edge[0])+" ---"+str(edge[2])+"---> "+"".join(edge[1]))
