Upon completion of the Networking Basics course, students will be able to perform the following tasks:

- Explain important concepts in network communication.
- Explain network types, components, and connections.
- Configure mobile devices for wireless access.
- Configure an integrated wireless router and wireless client to connect securely to the internet.
- Explain the importance of standards and protocols in network communications.
- Describe common network media.
- Explain how communication occurs on Ethernet networks.
- Explain the features of an IP address.
- Explain how IPv4 addresses are used in network communication and segmentation.
- Explain features of IPv6 addressing.
- Configure a DHCP server.
- Explain how routers connect networks together.
- Explain how ARP enables communication on a network.
- Create a fully connected LAN.
- Explain how clients access internet services.
- Explain the function of common application layer services.
- Use various tools to test and troubleshoot network connectivity.

I am saving this to test in the end whether I am stupid or not.
It said that I need to download Cisco packet tracer and take a course on that too?
Well, Lets do it I guess.

17.5.26 15:09
I am not doing a course on how to use this old ass app.

# 1.1 Network Types
so far basic stuff.

# 1.2 Data Transmission

Volunteered data, Inferred data, Observed data.

Everything is basically binary. Data can be transferred via electricity, optic fiber or wireless.

# Bandwidth and Throughput
Bandwidth is how much data can be transferred, throughput is the actual amount. 

I continued on. its 18.5.26 at 16:23. This is mad boring. I came around a question. 

[ELI5: The difference between a router, switch, hub, a bridge and a modem : r/explainlikeimfive](https://www.reddit.com/r/explainlikeimfive/comments/crarrw/eli5_the_difference_between_a_router_switch_hub_a/)

# Module 3: Wireless and Mobile Networks
This is very basic. Its about different networks and how to pair Bluetooth devices or connect to a Wi-Fi network. Very basic stuff.

4.2.1 LAN Wireless Frequencies

The wireless technologies most frequently used in home networks are in the unlicensed 2.4 GHz and 5 GHz frequency ranges.

Bluetooth is a technology that makes use of the 2.4 GHz band. It is limited to low-speed, short-range communications, but has the advantage of communicating with many devices at the same time. This one-to-many communication has made Bluetooth technology the preferred method for connecting computer peripherals such as wireless mice, keyboards and printers. Bluetooth is a good method for transmitting audio to speakers or headphones.

Other technologies that use the 2.4 GHz and 5 GHz bands are the modern wireless LAN technologies that conform to the various IEEE 802.11 standards. Unlike Bluetooth technology, 802.11 devices transmit at a much higher power level giving them a great range and improved throughput. Certain areas of the electromagnetic spectrum can be used without a permit.

The figure shows where wireless technologies exist on the electromagnetic spectrum.

The figure shows where wireless technologies exist on the electromagnetic spectrum. From left to right, audio is found at the extremely low, very low, and low end of the spectrum. AM broadcast is found between the medium and high portion of the spectrum. Short-wave radio is found only at the high portion of the spectrum. FM broadcast is found at the very high portion of the spectrum. Television is found at the very high and Ultra High portions of the spectrum. Cellular B40megahertz and NPCS 930 megahertz are both found at the Ultra High portion of the spectrum. Between Ultra High and super high are cordless phones at 902 to 928 megahertz, IEEE 802.11 b, g, n, and ad are at 2.400 to 2.4835 gigahertz, and IEEE 802.11 a, n, ac, and ad are at 5.725 to 5.850 gigahertz. Infrared wireless LAN is found in the Infrared portion of the spectrum. To the right of Infrared is visible light, Ultra Violet light, and then X-rays are at the right most end of the spectrum.

![[Pasted image 20260519202411.png]]

24.5.26 16:23
I am taking the exam between Module 4 and 5. I should probably study more often.
I got an 85%.

# 5.3 Network Communication Models

TCP/IP Model

Application
Transport
Internet
Network Access

Ethernet - IP - TCP - HTTP

  
# 9.1.1 Video - IPv4 Unicast, Broadcast, Multicast

Unicast - a way to send packet to one singular device.
**Note:** In this course, all communication between devices is unicast unless otherwise noted.

IPv4 unicast host addresses are in the address range of 1.1.1.1 to 223.255.255.255. However, within this range are many addresses that are reserved for special purposes. These special purpose addresses will be discussed later in this module.

**Note**: In the animation, notice that the subnet mask for 255.255.255.0 is represented using slash notion or /24. This indicates that the subnet mask is 24 bits long. The subnet mask 255.255.255.0 in binary is 11111111.11111111.11111111.00000000.

Broadcast - Every device on the network will receive the packet.

Multicast - Only a selected few devices on the network will receive the packet, if selected.
A multicast packet is a packet with a destination IP address that is a multicast address. ==IPv4 has reserved the 224.0.0.0 to 239.255.255.255 addresses as a multicast range.==
**Private IPv4 Ranges:**

- **Class A:** `10.0.0.0` to `10.255.255.255`
- **Class B:** `172.16.0.0` to `172.31.255.255`
- **Class C:** `192.168.0.0` to `192.168.255.255`

_Note: Addresses starting with `100.64.x.x` through `100.127.x.x` are also private, typically used by Internet Service Providers (ISPs) for Carrier-Grade NAT (CGNAT)._

# Module 10: IPv6 Addressing Formats and Rules
(31.5.26 16:23)

# Module 11: Dynamic Addressing with DHCP
(1.6.26 13:26)
11.1.1 Static IPv4 Address Assignment

IPv4 addresses can be assigned either statically or dynamically.

With a static assignment, the network administrator must manually configure the network information for a host. At a minimum, this includes the following:

- **IP address** - This identifies the host on the network.
- **Subnet mask** - This is used to identify the network on which the host is connected.
- **Default gateway** - This identifies the networking device that the host uses to access the internet or another remote network.

Static addresses have some advantages. For instance, they are useful for printers, servers, and other networking devices that need to be accessible to clients on the network. If hosts normally access a server at a particular IPv4 address, it would not be good if that address changed.

Static assignment of addressing information can provide increased control of network resources, but it can be time consuming to enter the information on each host. When IPv4 addresses are entered statically, the host only performs basic error checks on the IPv4 address. Therefore, errors are more likely to occur.

When using static IPv4 addressing, it is important to maintain an accurate list of which IPv4 addresses are assigned to which devices. Additionally, these are permanent addresses and are not normally reused.

# Module 12: Gateways to Other Networks
(3.6.26 13:00)
12.3.3 Gateways to Other Networks Quiz
I got a 100%. two tries with 91% beforehand. I searched up on Google a bit to know more about NAT and what it does and how it works. It's kinda interesting, though I am interested in CyberSec and it's just one aspect.