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


# number of subnets
numRouters = int(input())
routers = []
for i in range(numRouters):
    # ith subnet
    subnet = input()
    # number of links for ith subnet
    numLinks = int(input())
    rows, cols = (numLinks, 2)
    links = [[0 for k in range(cols)] for t in range(rows)]
    for j in range(numLinks):
        # ith link and distance
        iLink = input()
        links[j][0], links[j][1] = iLink.split("-")
    routers.append(Router(subnet, links))
    print()
