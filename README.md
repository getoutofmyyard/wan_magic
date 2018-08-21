# wan_magic
This is a complex WAN topology that I put together over a weekend. I hope that it may serve as a useful
guideline for certain types of configurations in Cisco IOS.

The goal here was to develop a "difficult" network to deal with - one that involves as many moving parts as possible - as a
training exercise in my CCNP studies. Here are some present and upcoming features of this topology:

Notable Features:
  OSPF and EIGRP operations, redistribution, and route manipulation
  OSPF over frame relay (including frame relay switch configuration on a Cisco router)
  OSPF virtual link
  IPsec hub-and-spoke configuration (static)

Upcoming Features:
  Gateway redundancy with HSRP and dual-homed ISP connections
  DMVPN
  
 ------------------------------------------------------------
 
 If you would like to toy around with this network, download the GNS3 project file in this repository, import the configuration
 files for each respective node, and have fun! I used Cisco IOS 15.2(4)S5 for all routers.
 
 
