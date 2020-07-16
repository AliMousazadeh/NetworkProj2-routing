# NetworkProj2-routing

Enter router subnets first in the following format:
subnet1-subnet2-distance
Then enter "eoi" (end of input) when finished.
Then enter the source and destination nodes.
Output: planned path.

For example:

192.168.1.0-192.168.2.0-20

192.168.2.0-192.168.3.0-5

192.168.1.0-192.168.3.0-2

eoi

192.168.1.0-192.168.2.0

output:

['192.168.1.0', '192.168.3.0', '192.168.2.0']
