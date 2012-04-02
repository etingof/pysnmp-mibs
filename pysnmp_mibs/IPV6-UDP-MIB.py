# PySNMP SMI module. Autogenerated from smidump -f python IPV6-UDP-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:14 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Ipv6Address, Ipv6IfIndexOrZero, ) = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6IfIndexOrZero")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, experimental, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "experimental", "mib-2")

# Objects

udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
ipv6UdpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 6))
if mibBuilder.loadTexts: ipv6UdpTable.setDescription("A table containing UDP listener information for\nUDP/IPv6 endpoints.")
ipv6UdpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 6, 1)).setIndexNames((0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"), (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"), (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if mibBuilder.loadTexts: ipv6UdpEntry.setDescription("Information about a particular current UDP listener.\n\nNote that conceptual rows in this table require an\nadditional index object compared to udpTable, since\nIPv6 addresses are not guaranteed to be unique on the\nmanaged node.")
ipv6UdpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 1), Ipv6Address()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setDescription("The local IPv6 address for this UDP listener.\nIn the case of a UDP listener which is willing\nto accept datagrams for any IPv6 address\nassociated with the managed node, the value ::0\nis used.")
ipv6UdpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipv6UdpLocalPort.setDescription("The local port number for this UDP listener.")
ipv6UdpIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 3), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6UdpIfIndex.setDescription("An index object used to disambiguate conceptual rows in\nthe table, since the ipv6UdpLocalAddress/ipv6UdpLocalPort\npair may not be unique.\n\nThis object identifies the local interface that is\nassociated with ipv6UdpLocalAddress for this UDP listener.\nIf such a local interface cannot be determined, this object\nshould take on the value 0.  (A possible example of this\nwould be if the value of ipv6UdpLocalAddress is ::0.)\n\nThe interface identified by a particular non-0 value of\nthis index is the same interface as identified by the same\nvalue of ipv6IfIndex.\n\nThe value of this object must remain constant during\nthe life of this UDP endpoint.")
ipv6UdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 87)).setRevisions(("1998-01-29 00:00",))
if mibBuilder.loadTexts: ipv6UdpMIB.setOrganization("IETF IPv6 MIB Working Group")
if mibBuilder.loadTexts: ipv6UdpMIB.setContactInfo("               Mike Daniele\n\nPostal: Compaq Computer Corporation\n        110 Spitbrook Rd\n        Nashua, NH 03062.\n        US\n\nPhone:  +1 603 884 1423\nEmail:  daniele@zk3.dec.com")
if mibBuilder.loadTexts: ipv6UdpMIB.setDescription("The MIB module for entities implementing UDP over IPv6.")
ipv6UdpConformance = MibIdentifier((1, 3, 6, 1, 3, 87, 2))
ipv6UdpCompliances = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 1))
ipv6UdpGroups = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 2))

# Augmentions

# Groups

ipv6UdpGroup = ObjectGroup((1, 3, 6, 1, 3, 87, 2, 2, 1)).setObjects(*(("IPV6-UDP-MIB", "ipv6UdpIfIndex"), ) )
if mibBuilder.loadTexts: ipv6UdpGroup.setDescription("The group of objects providing management of\nUDP over IPv6.")

# Compliances

ipv6UdpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 87, 2, 1, 1)).setObjects(*(("IPV6-UDP-MIB", "ipv6UdpGroup"), ) )
if mibBuilder.loadTexts: ipv6UdpCompliance.setDescription("The compliance statement for SNMPv2 entities which\nimplement UDP over IPv6.")

# Exports

# Module identity
mibBuilder.exportSymbols("IPV6-UDP-MIB", PYSNMP_MODULE_ID=ipv6UdpMIB)

# Objects
mibBuilder.exportSymbols("IPV6-UDP-MIB", udp=udp, ipv6UdpTable=ipv6UdpTable, ipv6UdpEntry=ipv6UdpEntry, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpIfIndex=ipv6UdpIfIndex, ipv6UdpMIB=ipv6UdpMIB, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpCompliances=ipv6UdpCompliances, ipv6UdpGroups=ipv6UdpGroups)

# Groups
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpGroup=ipv6UdpGroup)

# Compliances
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpCompliance=ipv6UdpCompliance)
