# wan_magic
This is a WAN that I created to practice for the CCNP ROUTE exam. Maybe it will help someone else along the way. After opening the project, be sure to import the most recent configurations into their respective devices.

You'll need to run "ip dhcp" on the workstations and let them acquire an IP address before they can ping.

11/10/2018
----------
DMVPN has been introduced into the lab. HQ is the DMVPN hub. Spokes are found at the edge of ASNs 3 and 4. The DMVPN address space is 10.222.222.0/29. Spokes will build VPN tunnels to each other dynamically. Unfortunately, I haven't figured out how to get remote access to each LAN on the other side of the spoke routers.

There are redundant IPSec connections between the 10.15 subnets in ASN 4. I'm looking for a better approach to this.

My next move is to get DMVPN remote access working. Later, I'll introduce IPv6.  

10/21/2018
----------
BGP peering was included in the design. IGPs still run between the ISP and branches, though I've cut down the routing table across all devices fairly significantly since implementing BGP.

DMVPN is working in a different project file. I just need to figure out how to add it to the current project without causing performance issues.
  
-------------------------------------------------------------------------------------------
Network diagram is saved as topology.jpg in the master directory.
 
All non-private IP addresses were made up by me. Any association with a real world IP address is purely coincidental.
 
-----------------------------------------------------------------------------------------
 

 
 
 
 
 
