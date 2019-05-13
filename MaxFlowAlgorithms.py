# This file contains the algorithms discussed in my paper, as well as
# an implementation of the Ford-Fulkerson algorithm for baseline testing
import MaxFlowStructs as mfs

# Implementation of the Ford-Fulkerson algorithm to serve as a test
def fordFulkerson(graph):
    path, path_flow = graph.getPath()
    while not path is None:
        for edge, _ in path:
            edge.flow += path_flow
            edge.return_edge.flow -= path_flow

        path, path_flow = graph.getPath()

    return graph.networkFlow()

#Implementation of my max flow algorithm for graph's with single in-degree
def singleInDegree(graph):
    def singleInDegreeHelper(vertex, capacity):
        if vertex == graph.sink.name:
            return capacity
        else:
            maxFlows = [singleInDegreeHelper(edge.end, edge.capacity) \
                for edge in graph.getEdges(vertex, True)]
            idealFlow = sum(maxFlows)
            if idealFlow < capacity:
                return idealFlow
            else:
                return capacity
  
    return sum([singleInDegreeHelper(edge.end, edge.capacity) \
        for edge in graph.getEdges(graph.source.name, True)])

#Implementation of my max flow algorithm for graph's with single out-degree
def singleOutDegree(graph):
    def singleOutDegreeHelper(current_edge, capacity):
        current_vertex = current_edge.end
        if current_vertex == graph.source.name:
            return capacity
        else:
            maxFlows = []
            edges = []
            for edge in filter(lambda e: e.is_reverse, graph.getEdges(current_vertex)):
                max_into = singleOutDegreeHelper(edge, min(capacity, edge.return_edge.capacity))
                maxFlows.append(max_into)
                edges.append(edge.return_edge)
            idealFlow = sum(maxFlows)
            if idealFlow < capacity:
                return idealFlow
            else:
                return capacity
    count = 0
    for edge in graph.getEdges(graph.sink.name):
        count += singleOutDegreeHelper(edge, edge.return_edge.capacity)

    return count     

#Implementation of the algorithm for graphs with one in-degree/out-degree subsets
def singleInOrOutDegree(network):
    #Given a source finds the matching sink
    def findSink(source):
        current_vertex = list(network.getEdges(source, True))[0].end
        count = 0
        num_reverse = len(list(filter(lambda e: e.is_reverse, network.graph[source])))
        while num_reverse == 1 or count > 0 and current_vertex != network.sink.name:
            f_edges = list(network.getEdges(current_vertex, True))
            if len(f_edges) > 1:
                count += 1
            elif num_reverse > 1:
                count -= 1
            current_vertex = f_edges[0].end
            num_reverse = len(list(filter(lambda e: e.is_reverse, network.graph[current_vertex])))
        return current_vertex

    #Calculates the maximum amount of flow through a subset
    def flowThroughSubset(source, sink, max_input=None):
        flows = []
        for edge in network.getEdges(source, True):
            current_vertex = edge.end
            current_flow = edge.capacity
            while current_vertex != sink:
                f_edges = list(network.getEdges(current_vertex, True))
                if len(f_edges) > 1:
                    local_sink = findSink(current_vertex)
                    current_flow = min(flowThroughSubset(current_vertex, local_sink, \
                        current_flow), current_flow)
                    current_vertex = local_sink
                else:
                    current_flow = min(f_edges[0].capacity, current_flow)
                    current_vertex = f_edges[0].end
            flows.append(current_flow)
        if max_input == None:
            return sum(flows)
        return min(sum(flows), max_input)

    return flowThroughSubset(network.source.name, network.sink.name)

