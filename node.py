from settings import*
import pygame
from line import Line
import time
import algorithms

class Node():
    def __init__(self, id,pos):
        self.pos = pos
        self.id = id

        self.image = PROGRAM_DATA["NODE_IMAGE"].convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.rect= self.image.get_frect(center=pos)

        self.node_lines = []

        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False

        self.textS = dafont.render(str(id), True, "black")
        self.textR = self.textS.get_frect(center = pos)

    def draw(self, screen):
        self.textR.center = self.rect.center
        screen.blit(self.image, self.rect)
        screen.blit(self.textS, self.textR)


    def move(self):
        mpos = pygame.mouse.get_pos()
        mbut = pygame.mouse.get_pressed()
        self.prev_x = self.rect.x-10
        self.prev_y = self.rect.y-10
        if self.rect.collidepoint(mpos) and mbut[0]:
            if not self.dragging:
                self.offset_x = mpos[0]-self.rect.x
                self.offset_y = mpos[1]-self.rect.y
            self.rect.x = mpos[0] - self.offset_x
            self.rect.y = mpos[1] -self.offset_y
            self.dragging = True
        else:
            self.dragging = False


class Nodes():
    def __init__(self):

        self.nodes = []
        self.lines = []
        self.matrix = []
        self.shortest_distances = None
        self.route_table = None

        self.reg_pos = (1/3*WINDOW_WIDTH, 1/4*WINDOW_HEIGHT)

        self.node1 = None
        self.node2 = None
        self.alternator = 1

        self.animating = False
        self.animateLines = []
        self.time = 0
        self.nowIndex = 0

    def update(self, screen):
        #stores last two clicked nodes
        mpos = pygame.mouse.get_pos()
        mbut = pygame.mouse.get_just_pressed()

        mouse_rect = pygame.Rect(mpos, (10, 10))
        index = mouse_rect.collidelist(self.nodes)

        if index != -1 and mbut[0]:
            if self.nodes[index] not in [self.node1, self.node2]:
                if self.alternator > 0:
                    self.node1 = self.nodes[index]
                    self.alternator *= -1
                else:
                    self.node2 = self.nodes[index]
                    self.alternator *= -1

        #regular stuff
        for line in self.lines:
            line.node1 = self.nodes[self.nodes.index(line.node1)]
            line.node2 = self.nodes[self.nodes.index(line.node2)]
            line.update()
            line.draw(screen)
        for node in self.nodes:
            node.move()
            node.draw(screen)
        if self.animating:
            self.animate()

    def add_new_node(self):
        new_node = Node(len(self.nodes),self.reg_pos)
        #moves the nodes on spawn not colliding with any other node
        while self.nodes and new_node.rect.collidelist([x.rect for x in self.nodes]) !=-1:
            new_node.rect.x+=40
        self.nodes.append(new_node)
        self.update_matrix()

        #resets the previous shortest distances/route table as they need to be re-calculated now
        self.shortest_distances = None
        self.route_table = None

    def create_lines(self):
        #waits till user input is finished
        if not PROGRAM_DATA["INPUT_ACTIVE"]:
            li =  any(line.node1 == self.node1 and line.node2 == self.node2 for line in self.lines)
            if self.node1 != None and self.node2 != None and self.node1 != self.node2 and (not li):
                node1_index = self.nodes.index(self.node1)
                node2_index = self.nodes.index(self.node2)
                if node1_index<node2_index:
                    a = Line(self.node1, self.node2,LINE_COLOUR, int(PROGRAM_DATA["USER_TEXT"] or 0))
                else:
                    a = Line(self.node2, self.node1,LINE_COLOUR,int(PROGRAM_DATA["USER_TEXT"] or 0))
                self.lines.append(a)
                self.nodes[min([node1_index,node2_index])].node_lines.append(a)
                self.node1,self.node2 = None,None
                self.shortest_distances = None
                self.route_table = None
            self.update_matrix()

    def update_matrix(self):
        self.matrix = [[0] * len(self.nodes) for node in self.nodes]
        for line in self.lines:
            start = self.nodes.index(line.node1)
            end = self.nodes.index(line.node2)
            self.matrix[start][end] = line.weight
            self.matrix[end][start] = line.weight

    def load_matrix(self, data):

        matrix = data["matrix"]
        nodes= data["nodes"]
        lines = data["lines"]

        self.RESET()
        self.matrix=matrix
        for n in nodes:
            new_node = Node(n[0], n[1])
            self.nodes.append(new_node)
        for lin in lines:
            self.lines.append(Line(self.nodes[lin[0]],self.nodes[lin[1]] , lin[2], lin[3]))

    def input_matrix(self, matrix):
        self.RESET()
        self.matrix = matrix

        for i in range(len(matrix)):
            self.add_new_node()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if matrix[i][j]>0:
                    self.lines.append(Line(self.nodes[min(i,j)], self.nodes[max(i,j)], LINE_COLOUR, matrix[i][j]))


    def show_list_format(self):
        li = [[] for node in self.nodes]
        for n in li:
            nIndex = li.index(n)
            for nodeLine in self.nodes[nIndex].node_lines:
                n.append(nodeLine.node2.id)
        print(li)

    def RESET(self):
        self.matrix = []
        self.nodes = []
        self.lines = []
        self.node1 = None
        self.node2 = None
        self.alternator = 1
        self.animating = False
        self.animateLines = []
        self.nowIndex = 0
        self.time = 0
        self.shortest_distances = None
        self.route_table = None


    def prims(self):
        if not self.matrix:
            return("Matrix empty", False)
        if self.animating:
            return ("Wait", False)
        m = self.matrix.copy()
        selected = algorithms.prims(m)
        if len(selected)>1:
            if selected[1] == False:
                return selected
        for node in selected:
            for line in self.lines:
                line.colour = LINE_COLOUR
                if line.node1.id == node[0] and line.node2.id == node[1] or line.node1.id == node[1] and line.node2.id == node[0]:
                    if len(node) >2:
                        self.animateLines.append([line, True])
                    else:
                        self.animateLines.append([line])
        self.animating=True
        return ("nice",True)

    def floyd(self):
        result = algorithms.floyds(self.matrix.copy())
        if result[1] == False:
            return result
        self.shortest_distances = result[0]
        self.route_table = result[1]
        print("-----------------------------------")
        for row in self.shortest_distances:
            print(row)
        print("-----------------------------------")
        for row in self.route_table:
            print(row)
        print("-----------------------------------")
        return("nice", True)

    def show_shortest(self):
        if self.animating:
            return ("Wait", False)
        if self.shortest_distances == None:
            return ("Run floyds", False)
        if None in [self.node1,self.node2]:
            return ("Pick two nodes", False)
        start = self.node1.id
        end = self.node2.id
        if self.shortest_distances[start][end] == float('inf'):
            return ("No path exists", False)

        a = self.route_table[start][end]
        if a == start:
            for line in self.lines:
                if line.node1.id == start and line.node2.id ==end or line.node1.id == end and line.node2.id ==start:
                    line.colour = "red"
                    self.node1 = None
                    self.node2 = None
                    return ("", True, False)
        nodes_in_between = [a]
        while a != start:
            a = self.route_table[start][a]
            nodes_in_between.append(a)
        nodes_in_between.reverse()
        nodes_in_between.append(end)
        for line in self.lines:
            line.colour = LINE_COLOUR
            for i in range(len(nodes_in_between)-1):
                if line.node1.id == nodes_in_between[i] and line.node2.id ==nodes_in_between[i+1] or line.node1.id == nodes_in_between[i+1] and line.node2.id ==nodes_in_between[i]:
                    line.colour = "red"
        self.node1 =None
        self.node2 = None
        return (f"Path distance {self.shortest_distances[start][end]}", True, False)


    def reset_animation(self):
        self.animating = False
        self.animateLines = []
        self.nowIndex = 0
        self.time = 0
        for line in self.lines:
            line.colour = LINE_COLOUR

    def animate(self):
        if self.nowIndex == len(self.animateLines):
            self.animating = False
            self.animateLines = []
            self.nowIndex =0
            self.time = 0
            return

        if time.time() - self.time > PROGRAM_DATA["ANIMATION_SPEED"]:
            a=self.animateLines[self.nowIndex]
            if len(a)>1:
                self.animateLines[self.nowIndex][0].colour = "red"
            else:
                self.animateLines[self.nowIndex][0].colour = "green"
            self.animateLines[self.nowIndex][0].time = time.time()
            self.nowIndex+=1
            self.time = time.time()


