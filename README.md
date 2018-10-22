# wan_magic
This is a WAN that I created to practice for the CCNP ROUTE exam. Maybe it will help someone else.

10/21/2018
----------
BGP peering was included in the design. IGPs still run between the ISP and branches, though I've cut down the routing table across all devices fairly significantly since implementing BGP.

DMVPN is working in a different project file. I just need to figure out how to add it to the current project without causing performance issues.
  
-------------------------------------------------------------------------------------------
Network diagram is saved as topology.jpg in the master directory.
 
All non-private IP addresses were made up by me. Any association with a real world IP address is purely coincidental.
 
-------------------------------------------------------------------------------------------
 
Fun facts:
 
Houston-HQ is an IPSec hub. All branches are spokes. i.e. Houston-HQ LANs can ping all other LANs via IPSec, and vice versa.
 
OSPF area 2 is running over frame relay. ISP-Oklahoma is the DR of area 2 and the frame relay hub.
 
Area 2 is tethered to area 0 with a virtual link.
 
ISP-Internal-1 and ISP-Internal-2 are redistributing OSPF and EIGRP. Plenty of route maps.
 
You'll need to run "ip dhcp" on the workstations and let them acquire an IP address before they can ping.
 
 
 
 
 
