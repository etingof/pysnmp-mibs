#
# PySNMP MIB module TCPIPX-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///home/tt/fixed_mibs/TCPIPX-MIB
# Produced by pysmi-0.0.2 at Mon Jun 22 23:53:36 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ModuleCompliance, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibTableRow, MibTableColumn, MibScalar, Unsigned32, TimeTicks, Counter64, MibTable, NotificationType, enterprises, ModuleIdentity, IpAddress, iso, Gauge32, MibIdentifier, Bits, ObjectIdentity, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibTableRow", "MibTableColumn", "MibScalar", "Unsigned32", "TimeTicks", "Counter64", "MibTable", "NotificationType", "enterprises", "ModuleIdentity", "IpAddress", "iso", "Gauge32", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class IpxAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(10,10)
    fixedLength = 10

novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
tcpx = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29))
tcpxTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 1))
tcpxUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 2))
tcpIpxConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1), )
tcpIpxConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1), ).setIndexNames((0, "TCPIPX-MIB", "tcpIpxConnLocalAddress"), (0, "TCPIPX-MIB", "tcpIpxConnLocalPort"), (0, "TCPIPX-MIB", "tcpIpxConnRemAddress"), (0, "TCPIPX-MIB", "tcpIpxConnRemPort"))
tcpIpxConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,)).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12),))).setMaxAccess("readwrite")
tcpIpxConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 2), IpxAddress()).setMaxAccess("readonly")
tcpIpxConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
tcpIpxConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 4), IpxAddress()).setMaxAccess("readonly")
tcpIpxConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
udpIpxTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1), )
udpIpxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1), ).setIndexNames((0, "TCPIPX-MIB", "udpIpxLocalAddress"), (0, "TCPIPX-MIB", "udpIpxLocalPort"))
udpIpxLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 1), IpxAddress()).setMaxAccess("readonly")
udpIpxLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
tcpUnspecConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2), )
tcpUnspecConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1), ).setIndexNames((0, "TCPIPX-MIB", "tcpUnspecConnLocalPort"))
tcpUnspecConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 12,)).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("deleteTCB", 12),))).setMaxAccess("readwrite")
tcpUnspecConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
udpUnspecTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2), )
udpUnspecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1), ).setIndexNames((0, "TCPIPX-MIB", "udpUnspecLocalPort"))
udpUnspecLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
mibBuilder.exportSymbols("TCPIPX-MIB", tcpIpxConnTable=tcpIpxConnTable, IpxAddress=IpxAddress, udpIpxEntry=udpIpxEntry, udpIpxLocalPort=udpIpxLocalPort, udpUnspecEntry=udpUnspecEntry, udpIpxTable=udpIpxTable, tcpIpxConnLocalAddress=tcpIpxConnLocalAddress, novell=novell, tcpUnspecConnTable=tcpUnspecConnTable, tcpUnspecConnLocalPort=tcpUnspecConnLocalPort, tcpx=tcpx, udpUnspecTable=udpUnspecTable, tcpIpxConnEntry=tcpIpxConnEntry, udpIpxLocalAddress=udpIpxLocalAddress, tcpIpxConnState=tcpIpxConnState, udpUnspecLocalPort=udpUnspecLocalPort, tcpIpxConnLocalPort=tcpIpxConnLocalPort, tcpxTcp=tcpxTcp, tcpIpxConnRemAddress=tcpIpxConnRemAddress, tcpUnspecConnEntry=tcpUnspecConnEntry, tcpUnspecConnState=tcpUnspecConnState, mibDoc=mibDoc, tcpIpxConnRemPort=tcpIpxConnRemPort, tcpxUdp=tcpxUdp)
