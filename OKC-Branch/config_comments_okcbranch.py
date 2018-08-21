OKC-Branch#show run
Building configuration...

Current configuration : 3289 bytes
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname OKC-Branch
!
boot-start-marker
boot-end-marker
!
!
!
!
ip dhcp pool sub1                       #Router configured to serve DHCP requests to the LAN
 network 172.20.0.0 255.255.255.0
 default-router 172.20.0.1
 domain-name oklahoma.local
!
!
!
!
!
!
crypto isakmp policy 10                 #Policy created for IKE phase 1 negotiations. Specifies default encryption (DES),
 hash md5                               #MD5 hash, and Diffie-Hellman group 2.
 authentication pre-share
 group 2
!
crypto isakmp key password address 70.164.65.65    255.255.255.252 no-xauth    #Sets PSK and peer IP address for IKE phase 1
!
!
crypto ipsec transform-set transformset esp-des esp-md5-hmac                   #Creates transform set "transformset" for phase 2 negotiations.
 mode tunnel                                                                   #DES and MD5 are used to reduce CPU overhead on my PC.
!
!
!
crypto map map 1 ipsec-isakmp                       #Creates a crypto map pointing to the above ISAKMP/IPSec configurations
 set peer 70.164.65.65                              #and uses ACL 101 to match traffic to be encrypted. This VPN will connect
 set transform-set transformset                     #Houston-HQ.
 match address 101
!
!
!
!
!
interface Loopback0                                #Configured this to force OSPF to use a router ID of 6.6.6.6
 ip address 6.6.6.6 255.255.255.255
!
interface Tunnel0
 no ip address
 shutdown
!
interface FastEthernet0/0                          #LAN interface. OSPF process 1 is enabled directly on the interface and assigned area 2.
 ip address 172.20.0.1 255.255.255.0               #Crypto map "map" is applied to the interface
 ip nat inside
 ip ospf 1 area 2
 speed auto
 duplex auto
 crypto map map
!
!
interface Serial2/1                                    #Link to Frame-Relay-Switch.
 ip address 99.100.25.2 255.255.255.240                #Point-to-multipoint OSPF is configured on top of "broadcast" frame relay
 ip nat outside                                        #IP maps to enable spoke-to-spoke OSPF neighborship. DLCIs are configured
 encapsulation frame-relay                             #to provide L2 connectivity to the hub and other spokes.
 ip ospf network point-to-multipoint
 ip ospf 1 area 2
 serial restart-delay 0
 frame-relay map ip 99.100.25.3 501 broadcast
 frame-relay map ip 99.100.25.4 601 broadcast
 frame-relay interface-dlci 102
 frame-relay interface-dlci 501
 frame-relay interface-dlci 601
 crypto map map
!
!
router ospf 1                                                           #OSPF configuration. FastEthernet0/0 is passive and will not advertise OSPF routes.
 passive-interface FastEthernet0/0                                      #Local interfaces are matched by network statements to enable OSPF advertising.
 network 10.0.0.0 0.0.0.15 area 2                                       #A distribution list has been configured to prevent this router from processing
 network 99.100.25.0 0.0.0.15 area 2                                    #internal ISP routes
 network 172.20.0.0 0.0.0.255 area 2
 distribute-list 111 in Serial2/1
!
ip nat inside source route-map nonat interface Serial2/1 overload       #NAT configuration. Calls route map "nonat" to match internal traffic to be NAT'd.
!                                                                       #The "overload" tag forces port address translation, as opposed to 1to1 or dynamic NAT.
!
!
ip route 0.0.0.0 0.0.0.0 Serial2/1 99.100.25.1                               #Default route pointing to ISP
!
ip access-list extended NAT                                                  #Defines ACL "NAT" to be used when matching traffic for translation.
 deny   ip 172.20.0.0 0.0.0.255 192.168.0.0 0.0.0.255                        #Does not translate IPSec traffic, but translates all other traffic.
 deny   ip 172.20.0.0 0.0.0.255 192.168.1.0 0.0.0.255
 permit ip 172.20.0.0 0.0.0.255 any
!
access-list 101 permit ip 172.20.0.0 0.0.0.255 192.168.0.0 0.0.0.255         #ACL that matches traffic to be encrypted by IPSec
access-list 101 permit ip 172.20.0.0 0.0.0.255 192.168.1.0 0.0.0.255
!
access-list 111 deny   ip 10.0.0.0 0.0.0.255 any                             #ACL used to define OSPF distribution list 111
!
route-map nonat permit 10                                                    #Route map "nonat" is called upon by NAT when matching traffic to be NAT'd
 match ip address NAT                                                        #"nonat" evaluates ACL "NAT"
!
!
!
!
!
end
