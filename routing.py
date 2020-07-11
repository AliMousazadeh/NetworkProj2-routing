import sys


class Router():

    def __init__(self, subnet, links):
        self.subnet = subnet
        self.links = links

    def printLinks(self):
        print(self.subnet)
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
