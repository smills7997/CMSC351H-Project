import MaxFlowStructs as mfs
import MaxFlowAlgorithms as mfa

#Tests for my maximum flow algorithms
def main():
    testSingleInDegree()
    testSingleOutDegree()
    testSingleDegreeSubsets()
    print("All tests passed!")

#Test for a flow network with a single in-degree
def testSingleInDegree():
    test1 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test1.addEdge('S', 'T', 6)
    test1.addEdge('S', 'A', 8)
    test1.addEdge('A', 'B', 4)
    test1.addEdge('A', 'C', 5)
    test1.addEdge('B', 'T', 7)
    test1.addEdge('C', 'T', 9)

    test2 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test2.addEdge('S', 'A', 18)
    test2.addEdge('S', 'B', 21)
    test2.addEdge('S', 'C', 14)
    test2.addEdge('A', 'D', 6)
    test2.addEdge('A', 'E', 4)
    test2.addEdge('A', 'F', 5)
    test2.addEdge('B', 'G', 12)
    test2.addEdge('B', 'T', 6)
    test2.addEdge('C', 'H', 10)
    test2.addEdge('C', 'I', 8)
    test2.addEdge('D', 'T', 9)
    test2.addEdge('E', 'T', 3)
    test2.addEdge('F', 'T', 7)
    test2.addEdge('G', 'T', 8)
    test2.addEdge('H', 'T', 10)
    test2.addEdge('I', 'T', 7)

    test1_expected = mfa.fordFulkerson(test1)
    test1.clearFlows()
    test1_actual = mfa.singleInDegree(test1)
    assert(test1_expected == test1_actual)

    test2_expected = mfa.fordFulkerson(test2)
    test2.clearFlows()
    test2_actual = mfa.singleInDegree(test2)
    assert(test2_expected == test2_actual)

#Tests for a flow network with single outdegrees
def testSingleOutDegree():
    test1 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test1.addEdge('S', 'A', 10)
    test1.addEdge('S', 'B', 6)
    test1.addEdge('S', 'C', 13)
    test1.addEdge('S', 'D', 15)
    test1.addEdge('S', 'E', 6)
    test1.addEdge('A', 'F', 9)
    test1.addEdge('B', 'F', 11)
    test1.addEdge('C', 'F', 13)
    test1.addEdge('D', 'G', 4)
    test1.addEdge('E', 'G', 7)
    test1.addEdge('F', 'T', 28)
    test1.addEdge('G', 'T', 18)

    test1_expected = mfa.fordFulkerson(test1)
    test1.clearFlows()
    test1_actual = mfa.singleOutDegree(test1)
    assert(test1_expected == test1_actual)

    test2 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test2.addEdge('S', 'A', 10)
    test2.addEdge('S', 'B', 5)
    test2.addEdge('S', 'C', 8)
    test2.addEdge('S', 'D', 7)
    test2.addEdge('S', 'E', 10)
    test2.addEdge('S', 'H', 11)
    test2.addEdge('A', 'B', 9)
    test2.addEdge('B', 'G', 16)
    test2.addEdge('C', 'G', 8)
    test2.addEdge('D', 'F', 7)
    test2.addEdge('E', 'F', 10)
    test2.addEdge('F', 'H', 9)
    test2.addEdge('G', 'T', 18)
    test2.addEdge('H', 'T', 23)

    test2_expected = mfa.fordFulkerson(test2)
    test2.clearFlows()
    test2_actual = mfa.singleOutDegree(test2)
    assert(test2_actual == test2_expected)

#Tests custom algorithm for graphs with single in-degree or out-degree subsets
def testSingleDegreeSubsets():
    test1 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test1.addEdge('S', 'A', 20)
    test1.addEdge('S', 'B', 12)
    test1.addEdge('A', 'C', 5)
    test1.addEdge('A', 'D', 4)
    test1.addEdge('C', 'E', 5)
    test1.addEdge('D', 'E', 9)
    test1.addEdge('E', 'T', 8)
    test1.addEdge('B', 'F', 12)
    test1.addEdge('F', 'T', 13)

    test1_actual = mfa.singleInOrOutDegree(test1)
    test1_expected = mfa.fordFulkerson(test1)
    assert(test1_actual == test1_expected)

    test2 = mfs.FlowNetwork(mfs.Vertex('S', source=True), mfs.Vertex('T', sink=True))
    test2.addEdge('S', 'A', 20)
    test2.addEdge('S', 'B', 12)
    test2.addEdge('A', 'C', 12)
    test2.addEdge('A', 'G', 7)
    test2.addEdge('C', 'D', 5)
    test2.addEdge('D', 'F', 5)
    test2.addEdge('C', 'E', 4)
    test2.addEdge('E', 'F', 9)
    test2.addEdge('F', 'T', 8)
    test2.addEdge('G', 'T', 6)
    test2.addEdge('B', 'H', 12)
    test2.addEdge('H', 'T', 16)
    
    test2_actual = mfa.singleInOrOutDegree(test2)
    test2_expected = mfa.fordFulkerson(test2)

    assert(test2_actual == test2_expected)


def print_path(path):
    for vertex, res in path:
        print(str(vertex) + ", " + str(res))

def print_list(lst):
    for v in lst:
        print(str(v))

if __name__ == '__main__':
    main()