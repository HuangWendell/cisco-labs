﻿Copy complete, now saving to disk (please wait)...
Copy complete.
dcaspine1# 
dcaspine1# 
dcaspine1# 
dcaspine1# sh run | no

!Command: show running-config
!Running configuration last done at: Mon Jan 13 17:16:10 2020
!Time: Mon Jan 13 17:20:21 2020

version 9.3(2) Bios:version  
hostname dcaspine1
vdc dcaspine1 id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4096
  limit-resource port-channel minimum 0 maximum 511
  limit-resource u4route-mem minimum 248 maximum 248
  limit-resource u6route-mem minimum 96 maximum 96
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

feature telnet
feature nxapi
feature bash-shell
feature scp-server
nv overlay evpn
feature ospf
feature bgp
feature interface-vlan
feature vn-segment-vlan-based
feature lldp
feature nv overlay

username admin password 5 $5$nLRd2R1y$8ET5jDBofyp7NsF4iWqo.MNpLyR2nSmHr/yXMIoxjyB  role network-admin
ip domain-lookup
copp profile strict
evpn multisite border-gateway 65511
  delay-restore time 30
snmp-server user admin network-admin auth md5 0x5bda1c8ab64faacf812dc5becde952b5 priv 0x5bda1c8ab64faacf812dc5becde952b5 localizedkey
rmon event 1 description FATAL(1) owner PMON@FATAL
rmon event 2 description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 description ERROR(3) owner PMON@ERROR
rmon event 4 description WARNING(4) owner PMON@WARNING
rmon event 5 description INFORMATION(5) owner PMON@INFO

vlan 1,10,20,30,500,1234
vlan 20
  vn-segment 10020
vlan 1234
  name L3VNI-Routing-TENANT1
  vn-segment 101234

route-map ALL permit 10
route-map dci-tag permit 10
  match tag 54321 
vrf context TENANT1
  vni 101234
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto evpn
  address-family ipv6 unicast
    route-target both auto
    route-target both auto evpn
vrf context management


interface Vlan1

interface Vlan1234
  description L3VNI-Routing
  no shutdown
  vrf member TENANT1
  no ip redirects
  ip forward
  ipv6 address use-link-local-only
  no ipv6 redirects

interface nve1
  no shutdown
  host-reachability protocol bgp
  source-interface loopback1
  source-interface hold-down-time 1
  multisite border-gateway interface loopback100
  member vni 10020
    multisite ingress-replication
    ingress-replication protocol bgp
  member vni 101234 associate-vrf

interface Ethernet1/1
  no switchport
  medium p2p
  ip unnumbered loopback0
  ip ospf network point-to-point
  ip router ospf dca area 0.0.0.0
  evpn multisite fabric-tracking

interface Ethernet1/2
  no switchport
  ip address 169.254.12.2/24
  ip router ospf dca area 0.0.0.0
  evpn multisite fabric-tracking
  no shutdown

interface Ethernet1/3

interface Ethernet1/4

interface Ethernet1/5

interface Ethernet1/6
  description tors
  no switchport
  ip address 169.254.93.1/30 tag 54321
  ip router ospf dca area 0.0.0.0
  evpn multisite dci-tracking
  no shutdown

interface Ethernet1/7

interface Ethernet1/8

interface Ethernet1/9

interface Ethernet1/10

interface Ethernet1/11

interface Ethernet1/12

interface Ethernet1/13

interface Ethernet1/14

interface Ethernet1/15

interface Ethernet1/16

interface Ethernet1/17

interface Ethernet1/18

interface Ethernet1/19

interface Ethernet1/20

interface Ethernet1/21

interface Ethernet1/22

interface Ethernet1/23

interface Ethernet1/24

interface Ethernet1/25

interface Ethernet1/26

interface Ethernet1/27

interface Ethernet1/28

interface Ethernet1/29

interface Ethernet1/30

interface Ethernet1/31

interface Ethernet1/32

interface Ethernet1/33

interface Ethernet1/34

interface Ethernet1/35

interface Ethernet1/36

interface Ethernet1/37

interface Ethernet1/38

interface Ethernet1/39

interface Ethernet1/40

interface Ethernet1/41

interface Ethernet1/42

interface Ethernet1/43

interface Ethernet1/44

interface Ethernet1/45

interface Ethernet1/46

interface Ethernet1/47

interface Ethernet1/48

interface Ethernet1/49

interface Ethernet1/50

interface Ethernet1/51

interface Ethernet1/52

interface Ethernet1/53

interface Ethernet1/54

interface Ethernet1/55

interface Ethernet1/56

interface Ethernet1/57

interface Ethernet1/58

interface Ethernet1/59

interface Ethernet1/60

interface Ethernet1/61

interface Ethernet1/62

interface Ethernet1/63

interface Ethernet1/64

interface Ethernet1/65

interface Ethernet1/66

interface Ethernet1/67

interface Ethernet1/68

interface Ethernet1/69

interface Ethernet1/70

interface Ethernet1/71

interface Ethernet1/72

interface Ethernet1/73

interface Ethernet1/74

interface Ethernet1/75

interface Ethernet1/76

interface Ethernet1/77

interface Ethernet1/78

interface Ethernet1/79

interface Ethernet1/80

interface Ethernet1/81

interface Ethernet1/82

interface Ethernet1/83

interface Ethernet1/84

interface Ethernet1/85

interface Ethernet1/86

interface Ethernet1/87

interface Ethernet1/88

interface Ethernet1/89

interface Ethernet1/90

interface Ethernet1/91

interface Ethernet1/92

interface Ethernet1/93

interface Ethernet1/94

interface Ethernet1/95

interface Ethernet1/96

interface Ethernet1/97

interface Ethernet1/98

interface Ethernet1/99

interface Ethernet1/100

interface Ethernet1/101

interface Ethernet1/102

interface Ethernet1/103

interface Ethernet1/104

interface Ethernet1/105

interface Ethernet1/106

interface Ethernet1/107

interface Ethernet1/108

interface Ethernet1/109

interface Ethernet1/110

interface Ethernet1/111

interface Ethernet1/112

interface Ethernet1/113

interface Ethernet1/114

interface Ethernet1/115

interface Ethernet1/116

interface Ethernet1/117

interface Ethernet1/118

interface Ethernet1/119

interface Ethernet1/120

interface Ethernet1/121

interface Ethernet1/122

interface Ethernet1/123

interface Ethernet1/124

interface Ethernet1/125

interface Ethernet1/126

interface Ethernet1/127

interface Ethernet1/128

interface mgmt0
  vrf member management

interface loopback0
  ip address 100.64.1.2/32 tag 54321
  ip router ospf dca area 0.0.0.0

interface loopback1
  ip address 100.64.1.22/32 tag 54321
  ip router ospf dca area 0.0.0.0

interface loopback100
  description bgw-vtep
  ip address 100.64.100.100/32 tag 54321
  ip router ospf dca area 0.0.0.0
line console
line vty
boot nxos bootflash:/nxos.9.3.2.bin 
router ospf 1
  router-id 169.254.93.1
router ospf dca
  router-id 100.64.1.2
router bgp 65511
  router-id 100.64.1.2
  cluster-id 65511
  address-family ipv4 unicast
    redistribute direct route-map dci-tag
    maximum-paths 4
  address-family l2vpn evpn
    retain route-target all
  neighbor 100.64.93.93
    remote-as 65533
    update-source Ethernet1/6
    ebgp-multihop 5
    peer-type fabric-external
    address-family ipv4 unicast
    address-family l2vpn evpn
      send-community
      send-community extended
      rewrite-evpn-rt-asn
  neighbor 100.64.1.0/29
    remote-as 65511
    update-source loopback0
    address-family ipv4 unicast
      send-community
      send-community extended
      route-reflector-client
    address-family l2vpn evpn
      send-community
      send-community extended
      route-reflector-client



dcaspine1# 
dcaspine1# show nve interfa
Interface: nve1, State: Up, encapsulation: VXLAN
 VPC Capability: VPC-VIP-Only [not-notified]
 Local Router MAC: 5000.0002.0007
 Host Learning Mode: Control-Plane
 Source-Interface: loopback1 (primary: 100.64.1.22, secondary: 0.0.0.0)

dcaspine1# sh bgp l2vpn evpn
BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 213, Local Router ID is 100.64.1.2
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-i
njected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup, 2 - b
est2

   Network            Next Hop            Metric     LocPrf     Weight Path
Route Distinguisher: 100.64.1.1:3
*>i[5]:[0]:[0]:[24]:[172.16.1.0]/224
                      100.64.1.1               0        100          0 ?

Route Distinguisher: 100.64.1.1:32787
*>i[2]:[0]:[0]:[48]:[5000.0007.0000]:[32]:[172.16.1.2]/272
                      100.64.1.1                        100          0 i
*>i[3]:[0]:[32]:[100.64.1.1]/88
                      100.64.1.1                        100          0 i

Route Distinguisher: 100.64.1.1:32797
*>i[3]:[0]:[32]:[100.64.1.1]/88
                      100.64.1.1                        100          0 i

Route Distinguisher: 100.64.1.2:27001   (ES [0300.0000.00ff.e700.0309 0])
*>l[4]:[0300.0000.00ff.e700.0309]:[32]:[100.64.1.22]/136
                      100.64.1.22                       100      32768 i

Route Distinguisher: 100.64.1.2:32787    (L2VNI 10020)
*>l[2]:[0]:[0]:[48]:[5000.0002.0007]:[0]:[0.0.0.0]/216
                      100.64.1.22                       100      32768 i
*>e[2]:[0]:[0]:[48]:[5000.0004.0007]:[0]:[0.0.0.0]/216
                      100.64.2.11                                    0 65533 655
22 i
*>i[2]:[0]:[0]:[48]:[5000.0007.0000]:[32]:[172.16.1.2]/272
                      100.64.1.1                        100          0 i
*>i[3]:[0]:[32]:[100.64.1.1]/88
                      100.64.1.1                        100          0 i
*>l[3]:[0]:[32]:[100.64.1.22]/88
                      100.64.1.22                       100      32768 i
*>e[3]:[0]:[32]:[100.64.2.11]/88
                      100.64.2.11                                    0 65533 655
22 i

Route Distinguisher: 100.64.2.1:27001
*>e[4]:[0300.0000.00ff.f200.0309]:[32]:[100.64.2.11]/136
                      100.64.2.11                                    0 65533 655
22 i

Route Distinguisher: 100.64.2.1:32787
*>e[2]:[0]:[0]:[48]:[5000.0004.0007]:[0]:[0.0.0.0]/216
                      100.64.2.11                                    0 65533 655
22 i
*>e[3]:[0]:[32]:[100.64.2.11]/88
                      100.64.2.11                                    0 65533 655
22 i

Route Distinguisher: 100.64.1.2:3    (L3VNI 101234)
*>i[2]:[0]:[0]:[48]:[5000.0007.0000]:[32]:[172.16.1.2]/272
                      100.64.1.1                        100          0 i
*>i[5]:[0]:[0]:[24]:[172.16.1.0]/224
                      100.64.1.1               0        100          0 ?

dcaspine1# sh bgp l2vpn evpn summary 
BGP summary information for VRF default, address family L2VPN EVPN
BGP router identifier 100.64.1.2, local AS number 65511
BGP table version is 213, L2VPN EVPN config peers 3, capable peers 2
16 network entries and 16 paths using 3120 bytes of memory
BGP attribute entries [14/2296], BGP AS path entries [1/10]
BGP community entries [0/0], BGP clusterlist entries [0/0]

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
100.64.1.1      4 65511     177     136      213    0    0 01:53:10 4         
100.64.93.93    4 65533     210     129      213    0    0 01:53:59 3         

Neighbor        T    AS PfxRcd     Type-2     Type-3     Type-4     Type-5    
100.64.1.1      I 65511 4          1          2          0          1         
100.64.93.93    E 65533 3          1          1          1          0         
