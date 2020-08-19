import networkx as nx
import json
import matplotlib.pyplot as plt

class AccumAE:

    def CalcPropStats(self, file_path, isPlot, plotFileName):
        '''
        This function calculates propagated statistics of a graph
        given as a json file input.
        (This means the sum of all leafs nodes errors(AE) when
        AE of each node = sum(AEi) + currentError * (minDistance + 1))
        (i - all input nodes of current node,
         current error - error of current node
         minDistance - current node minimum distance from root)

        this is done using the following steps:
        - Json is converted to python dictionary
        - Build DAG (Directed Acyclic Graph) from this dictionary
        - topologically sort nodes in graph
        - Calculate AE of each node and summing up all leafs AEs
        :param file_path: json file
        :return: integer that shows the propagated statistics in
                 DAG (directed acyclic graph)
        '''
        data = self.__ConvertJsonToPython(file_path)
        graph = self.__BuildGraph(data)
        topSort = list(self.__ToplogicSort(graph))
        if isPlot:
            self.__PlotGraph(graph, plotFileName)

        return self.__CalculateAE(graph, topSort)

    def __BuildGraph(self, data):
        graph = nx.DiGraph()
        for key in data:
            graph.add_node(key, error=data[key]['error'])
            targetNodes = data[key]['nodes']
            for var in targetNodes:
                graph.add_edge(key, var)

        return graph

    # json to python
    def __ConvertJsonToPython(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)

        return data

    # sorting graph using topological sort
    def __ToplogicSort(self, data):
        return nx.topological_sort(data)

    # Calc sum of predecessors' AE
    def __SumPredecessorsAE(self, graph, node, AEPerNode):
        predList = graph.predecessors(node)
        sum = 0
        for var in predList:
            sum += AEPerNode[var]

        return sum

    # traverse list and calculate AE
    def __CalculateAE(self, graph, TopolSorted):
        AEPerNode = {}
        for var in TopolSorted:
            AEPerNode[var] = self.__SumPredecessorsAE(graph, var, AEPerNode) + \
                             graph._node[var]['error'] * (1 + nx.shortest_path_length(graph, 'root', var))

        return self.__CalulateLeafsSum(graph, AEPerNode)

    # calculate the leafs sum
    def __CalulateLeafsSum(self,graph, AEPerNode):
        sum = 0
        for var in AEPerNode:
            if 0 == graph.out_degree(var):
                sum += AEPerNode[var]

        return round(sum, 2)

    #Plot graph
    def __PlotGraph(self, graph, plotFileName):
        nx.draw_networkx(graph, pos=nx.spring_layout(graph), arrows=True, with_labels=True)
        plt.savefig(plotFileName)
        plt.savefig(str(plotFileName))
        #plt.show()