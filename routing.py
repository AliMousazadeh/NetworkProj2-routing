import sys
import numpy as np


class Router():

    def __init__(self, subnet, links):
        self.subnet = subnet
        self.links = links

    def printLinks(self):
        numLinks = len(self.links)
        for i in range(numLinks):
            print(self.links[i][0] + "-" + self.links[i][1])


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
            distanceGraph[i][j] = routers[i].links[index][1]
        else:
            distanceGraph[i][j] = 0
