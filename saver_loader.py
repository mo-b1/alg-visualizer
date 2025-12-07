import json
from node import *
from settings import*

class records:
    def __init__(self):
        self.filepath = "graphs.json"
        self.graphs = []
        self.load_graphs()

    def load_graphs(self):
        try:
            with open(self.filepath,"r") as f:
                self.graphs = json.load(f)
                self.counter = len(self.graphs)
            if self.counter > 0:
                PROGRAM_DATA["LOADER"]+=1
        except Exception as e:
            print("JSON file empty", e)
            self.counter=0

    def delete_matrix(self, matrix, a):
        if len(matrix) <1:
            return ("Matrix empty", False)
        found = False
        try:
            for graph in self.graphs:
                if graph["matrix"] == matrix:
                    self.graphs.remove(graph)
                    self.counter-=1
                    found = True
            with open(self.filepath,'w') as f:
                json.dump(self.graphs,f,indent=4)
                PROGRAM_DATA["LOADER"] = 0
            if len(self.graphs) == 0:
                PROGRAM_DATA["LOADER"] = -1
        except Exception as e:
            print("Delete error", e)
            return ("Error", False)
        if found:
            return ("Matrix deleted", True)
        else:
            return ("Matrix not found", False)


    def save_matrix(self, allNodes):
        if len(allNodes.matrix) <1:
            return ("Matrix empty", False)
        new = False
        try:
            graph_data = {"matrix": allNodes.matrix,"nodes": [(n.id,n.rect.center) for n in allNodes.nodes],"lines": [(line.node1.id, line.node2.id, line.colour, line.weight) for line in allNodes.lines]}
            all_matrices = [x["matrix"] for x in self.graphs]
            if graph_data["matrix"] not in all_matrices:
                self.graphs.append(graph_data)
                self.counter += 1
                new = True
                with open(self.filepath, 'w') as f:
                    json.dump(self.graphs, f,indent=4)
                if PROGRAM_DATA["LOADER"] == -1 :
                    PROGRAM_DATA["LOADER"] += 1
        except Exception as e:
            print("Save error", e)
            return ("Error", False)
        if new:
            return ("Save successful", True)
        else:
            return ("Matrix exists", False)


    def load_matrix(self,index):
        if not(0 <= index < len(self.graphs)):
            pass
            #return ("No graphs to load", False)
        try:
            with open(self.filepath,"r") as f:
                copy=json.load(f)
                PROGRAM_DATA["LOADER"] = (PROGRAM_DATA["LOADER"] + 1) % self.counter
                return copy[index]
        except Exception as e:
            print("Load error", e)
            #return ("Error", False)