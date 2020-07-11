import sys
import numpy as np


class Router():

    def __init__(self, subnet, links):
        self.subnet = subnet
        self.links = links
        self.routingTable = []

    def printLinks(self):
        numLinks = len(self.links)
        for i in range(numLinks):
            print(self.links[i][0] + "-" + self.links[i][1])


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        shortestPath = [[] for rows in range(self.V)]

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    shortestPath[v].append(u)
        return shortestPath


routerSubnets = []
routers = []
links = []
userInput = []
while True:
    userInput = input()
    if (userInput == 'eoi'):
        break
    router1Subnet, router2Subnet, dist = userInput.split("-")

    if router1Subnet not in routerSubnets:
        routerSubnets.append(router1Subnet)
        routers.append(Router(router1Subnet, []))
    if router2Subnet not in routerSubnets:
        routerSubnets.append(router2Subnet)
        routers.append(Router(router2Subnet, []))

    router1Index = routerSubnets.index(router1Subnet)
    router2Index = routerSubnets.index(router2Subnet)

    routers[router1Index].links.append([router2Subnet, dist])
    routers[router2Index].links.append([router1Subnet, dist])

rows, cols = (len(routers), len(routers))
distanceGraph = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        if routers[j].subnet in [link[0] for link in routers[i].links]:
            index = [link[0]
                     for link in routers[i].links].index(routers[j].subnet)
            distanceGraph[i][j] = int(routers[i].links[index][1])
        else:
            distanceGraph[i][j] = 0


g = Graph(len(routers))
g.graph = distanceGraph

for i in range(len(routers)):
    routers[i].routingTable = g.dijkstra(i)

startEndInput = input()
packetLocation, packetDestination = startEndInput.split("-")

plannedPath = routers[routerSubnets.index(
    packetLocation)].routingTable[routerSubnets.index(
        packetDestination)]
plannedPath.append(routerSubnets.index(
    packetDestination))

plannedPathAddresses = []
for i in range(len(plannedPath)):
    plannedPathAddresses.append(routerSubnets[plannedPath[i]])

print(plannedPathAddresses)
