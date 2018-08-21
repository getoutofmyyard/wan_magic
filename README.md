# wan_magic
This is a fun WAN topology that I put together over a weekend. I hope that it serves as a useful
guideline for certain types of configurations in Cisco IOS.

My goal was to design a network with difficult and uncommon challenges to surmount. There is a dangling OSPF area hanging on
for dear life by a virtual link. Frame relay returns from the grave to haunt all of us. Routing loops occur by design and must be
prevented by tricky route map configurations. 

But, somehow, I got everything to work.

--------------------------------------------------------------
Here are some present and upcoming features of this topology:

Notable Features:
  OSPF and EIGRP operations, redistribution, and route manipulation;
  OSPF over frame relay (including frame relay switch configuration on a Cisco router);
  OSPF virtual link;
  IPsec hub-and-spoke configuration over NAT

Upcoming Features:
  Gateway redundancy with HSRP and dual-homed ISP connections;
  DMVPN
  
 ------------------------------------------------------------
 
 If you would like to toy around with this network, download the GNS3 project file in this repository, import the configuration
 files for each respective node, and have fun! I used Cisco IOS 15.2(4)S5 for all routers.
 
 
