# wan_magic
This is a fun WAN topology that I put together over a weekend. I hope that it serves as a useful
guideline for certain types of configurations in Cisco IOS.

My goal was to design a funky network that would test my skills. Fortunately, everything works.

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
 
 
 Fun facts:
 
 Houston-Branch is an IPSec hub. All branches are spokes.
 ISP-Oklahoma is the hub of the frame relay topology and DR of area 2
 ISP-Internal1 and ISP-Internal2 are ASBRs; check out the route maps
 Houston-Branch LANs can ping all other LANs via IPSec
 NAT is running on all routers except ISP-Internal1 and ISP-Internal2
 
 
 
 
 
