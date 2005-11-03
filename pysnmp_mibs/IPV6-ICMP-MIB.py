# PySNMP SMI module. Autogenerated from smidump -f python IPV6-ICMP-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:06 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ipv6IfEntry, ) = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")

# Objects

ipv6IcmpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 56)).setRevisions(("1998-01-08 21:55",))
ipv6IcmpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 1))
ipv6IfIcmpTable = MibTable((1, 3, 6, 1, 2, 1, 56, 1, 1))
ipv6IfIcmpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 56, 1, 1, 1))
ipv6IfIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpInGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
ipv6IfIcmpOutGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
ipv6IcmpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2))
ipv6IcmpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 1))
ipv6IcmpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 2))

# Augmentions
ipv6IfEntry, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
ipv6IfEntry.registerAugmentions(("IPV6-ICMP-MIB", "ipv6IfIcmpEntry"))
apply(ipv6IfIcmpEntry.setIndexNames, ipv6IfEntry.getIndexNames())

# Groups

ipv6IcmpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 56, 2, 2, 1)).setObjects(("IPV6-ICMP-MIB", "ipv6IfIcmpOutAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembReductions"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembReductions"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterAdvertisements"), )

# Exports

# Module identity
mibBuilder.exportSymbols("IPV6-ICMP-MIB", PYSNMP_MODULE_ID=ipv6IcmpMIB)

# Objects
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IcmpMIB=ipv6IcmpMIB, ipv6IcmpMIBObjects=ipv6IcmpMIBObjects, ipv6IfIcmpTable=ipv6IfIcmpTable, ipv6IfIcmpEntry=ipv6IfIcmpEntry, ipv6IfIcmpInMsgs=ipv6IfIcmpInMsgs, ipv6IfIcmpInErrors=ipv6IfIcmpInErrors, ipv6IfIcmpInDestUnreachs=ipv6IfIcmpInDestUnreachs, ipv6IfIcmpInAdminProhibs=ipv6IfIcmpInAdminProhibs, ipv6IfIcmpInTimeExcds=ipv6IfIcmpInTimeExcds, ipv6IfIcmpInParmProblems=ipv6IfIcmpInParmProblems, ipv6IfIcmpInPktTooBigs=ipv6IfIcmpInPktTooBigs, ipv6IfIcmpInEchos=ipv6IfIcmpInEchos, ipv6IfIcmpInEchoReplies=ipv6IfIcmpInEchoReplies, ipv6IfIcmpInRouterSolicits=ipv6IfIcmpInRouterSolicits, ipv6IfIcmpInRouterAdvertisements=ipv6IfIcmpInRouterAdvertisements, ipv6IfIcmpInNeighborSolicits=ipv6IfIcmpInNeighborSolicits, ipv6IfIcmpInNeighborAdvertisements=ipv6IfIcmpInNeighborAdvertisements, ipv6IfIcmpInRedirects=ipv6IfIcmpInRedirects, ipv6IfIcmpInGroupMembQueries=ipv6IfIcmpInGroupMembQueries, ipv6IfIcmpInGroupMembResponses=ipv6IfIcmpInGroupMembResponses, ipv6IfIcmpInGroupMembReductions=ipv6IfIcmpInGroupMembReductions, ipv6IfIcmpOutMsgs=ipv6IfIcmpOutMsgs, ipv6IfIcmpOutErrors=ipv6IfIcmpOutErrors, ipv6IfIcmpOutDestUnreachs=ipv6IfIcmpOutDestUnreachs, ipv6IfIcmpOutAdminProhibs=ipv6IfIcmpOutAdminProhibs, ipv6IfIcmpOutTimeExcds=ipv6IfIcmpOutTimeExcds, ipv6IfIcmpOutParmProblems=ipv6IfIcmpOutParmProblems, ipv6IfIcmpOutPktTooBigs=ipv6IfIcmpOutPktTooBigs, ipv6IfIcmpOutEchos=ipv6IfIcmpOutEchos, ipv6IfIcmpOutEchoReplies=ipv6IfIcmpOutEchoReplies, ipv6IfIcmpOutRouterSolicits=ipv6IfIcmpOutRouterSolicits, ipv6IfIcmpOutRouterAdvertisements=ipv6IfIcmpOutRouterAdvertisements, ipv6IfIcmpOutNeighborSolicits=ipv6IfIcmpOutNeighborSolicits, ipv6IfIcmpOutNeighborAdvertisements=ipv6IfIcmpOutNeighborAdvertisements, ipv6IfIcmpOutRedirects=ipv6IfIcmpOutRedirects, ipv6IfIcmpOutGroupMembQueries=ipv6IfIcmpOutGroupMembQueries, ipv6IfIcmpOutGroupMembResponses=ipv6IfIcmpOutGroupMembResponses, ipv6IfIcmpOutGroupMembReductions=ipv6IfIcmpOutGroupMembReductions, ipv6IcmpConformance=ipv6IcmpConformance, ipv6IcmpCompliances=ipv6IcmpCompliances, ipv6IcmpGroups=ipv6IcmpGroups)

# Groups
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IcmpGroup=ipv6IcmpGroup)
