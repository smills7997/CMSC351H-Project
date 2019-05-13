# Code Representing a maximum flow network

#Class to represent a Vertex in our graph
class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        if source and sink:
            raise Exception('A vertex can not be both a source and sink')
        self.isSource = source
        self.isSink = sink

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "Name: %s" % self.name
            
#Class to represent an Edge in our graph
class Edge:
    def __init__(self, start, end, cap, flow=0, reverse=False):
        self.start = start
        self.end = end
        self.capacity = cap
        self.flow = flow
        self.return_edge = None
        self.is_reverse = reverse
    
    def __hash__(self):
        return hash((self.start, self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return "Start: %s, End: %s, Current Flow: %s, Capacity: %s" \
            % (self.start, self.end, self.flow, self.capacity)

#Class to represent our Flow Network
class FlowNetwork:
    def __init__(self, source, sink):
        self.source = source
        self.sink = sink
        self.vertices = [source, sink]
        self.maxCapacity = 0
        self.graph = {source.name: [], sink.name: []}
    
    def getSource(self):
        return self.source
    
    def getSink(self):
        return self.sink

    def getVertices(self):
        return self.vertices

    def allEdges(self):
        edge_list = []
        for edge in self.graph.values():
            edge_list += edge
        return edge_list
    
    def getEdge(self, startV, endV):
        if startV in self.graph and endV in self.graph:
            for edge in self.graph[startV]:
                if edge.end == endV:
                    return edge
        return None

    #Returns all out going edges from a vertex
    def getEdges(self, startV, only_forward=False):
        if startV in self.graph:
            if not only_forward:
                return self.graph[startV]
            else:
                return filter(lambda edge: edge.is_reverse == False, self.graph[startV])

    def addVertex(self, name):
        new_vertex = Vertex(name)
        if new_vertex in self.vertices:
            return "A vertex with this name already exists"
        self.vertices.append(Vertex(name))
        self.graph[name] = []

    def addEdge(self, start, end, capacity):
        if not end in self.graph:
            self.addVertex(end)
        if not start in self.graph:
            self.addVertex(start)
        if capacity > self.maxCapacity:
            self.maxCapacity = capacity
        new_edge = Edge(start, end, capacity)
        reverse_edge = Edge(end, start, 0, reverse=True)
        new_edge.return_edge = reverse_edge
        reverse_edge.return_edge = new_edge
        self.graph[start].append(new_edge)
        self.graph[end].append(reverse_edge)

    def clearFlows(self):
        for vertex in self.vertices:
            for edge in self.graph[vertex.name]:
                edge.flow = 0

    #Return a path from the source to the sink, and the min residual flow along that path
    def getPath(self):
        def get_path_helper(start, path, current_flow):
            if start == self.sink.name:
                return path, current_flow
            else:
                for edge in self.graph[start]:
                    residual = edge.capacity - edge.flow
                    if residual > 0 and not (edge, residual) in path:
                        current_flow = min(current_flow, residual)
                        result, path_flow = get_path_helper(edge.end, path + [(edge, residual)], current_flow)
                        if result != None:
                            return result, path_flow
            return None, -1
        return get_path_helper(self.source.name, [], self.maxCapacity)

    def networkFlow(self):
        return sum(edge.flow for edge in self.graph[self.source.name])

                    