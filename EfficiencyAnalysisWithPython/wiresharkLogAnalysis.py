from scapy.all import *
import struct

packets = rdpcap("BACnetPerformaceTestResult_duration_25ms.pcapng")


print(packets[0])





