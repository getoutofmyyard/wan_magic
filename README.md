# wan_magic
This is a wide area network that I put together over a weekend. It is a work in progress.

Upcoming Features:

  Gateway redundancy with HSRP and dual-homed ISP connections;
  
  DMVPN
  
-------------------------------------------------------------------------------------------
 Network diagram is saved as topology.jpg in the master directory.
 
 All non-private IP addresses were made up by me. Any association with a real world IP address is purely coincidental.
 
 -------------------------------------------------------------------------------------------
 
 Fun facts:
 
 Houston-HQ is an IPSec hub. All branches are spokes. i.e. Houston-HQ LANs can ping all other LANs via IPSec, and vice versa.
 
 OSPF area 2 is running over frame relay. ISP-Oklahoma is the DR of area 2 and the frame relay hub.
 
 Area 2 is tethered to area 0 with a virtual link.
 
 ISP-Internal-1 and ISP-Internal-2 are redistributing OSPF and EIGRP. Plenty of route maps.
 
 You'll need to run "ip dhcp" on the virtual workstations and let them acquire an IP address before they can ping.
 
 
 
 
 
