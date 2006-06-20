# PySNMP SMI module. Autogenerated from smidump -f python IP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:09 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( PhysAddress, ) = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress")

# Objects

ip = MibIdentifier((1, 3, 6, 1, 2, 1, 4))
ipForwarding = MibScalar((1, 3, 6, 1, 2, 1, 4, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("forwarding", 1), ("notForwarding", 2), ))).setMaxAccess("readwrite")
ipDefaultTTL = MibScalar((1, 3, 6, 1, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
ipInReceives = MibScalar((1, 3, 6, 1, 2, 1, 4, 3), Counter32()).setMaxAccess("readonly")
ipInHdrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 4), Counter32()).setMaxAccess("readonly")
ipInAddrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 5), Counter32()).setMaxAccess("readonly")
ipForwDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 4, 6), Counter32()).setMaxAccess("readonly")
ipInUnknownProtos = MibScalar((1, 3, 6, 1, 2, 1, 4, 7), Counter32()).setMaxAccess("readonly")
ipInDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 8), Counter32()).setMaxAccess("readonly")
ipInDelivers = MibScalar((1, 3, 6, 1, 2, 1, 4, 9), Counter32()).setMaxAccess("readonly")
ipOutRequests = MibScalar((1, 3, 6, 1, 2, 1, 4, 10), Counter32()).setMaxAccess("readonly")
ipOutDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 11), Counter32()).setMaxAccess("readonly")
ipOutNoRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 12), Counter32()).setMaxAccess("readonly")
ipReasmTimeout = MibScalar((1, 3, 6, 1, 2, 1, 4, 13), Integer32()).setMaxAccess("readonly")
ipReasmReqds = MibScalar((1, 3, 6, 1, 2, 1, 4, 14), Counter32()).setMaxAccess("readonly")
ipReasmOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 15), Counter32()).setMaxAccess("readonly")
ipReasmFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 16), Counter32()).setMaxAccess("readonly")
ipFragOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 17), Counter32()).setMaxAccess("readonly")
ipFragFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 18), Counter32()).setMaxAccess("readonly")
ipFragCreates = MibScalar((1, 3, 6, 1, 2, 1, 4, 19), Counter32()).setMaxAccess("readonly")
ipAddrTable = MibTable((1, 3, 6, 1, 2, 1, 4, 20))
ipAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 20, 1)).setIndexNames((0, "IP-MIB", "ipAdEntAddr"))
ipAdEntAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 1), IpAddress()).setMaxAccess("readonly")
ipAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
ipAdEntNetMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 3), IpAddress()).setMaxAccess("readonly")
ipAdEntBcastAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
ipAdEntReasmMaxSize = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
ipNetToMediaTable = MibTable((1, 3, 6, 1, 2, 1, 4, 22))
ipNetToMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 22, 1)).setIndexNames((0, "IP-MIB", "ipNetToMediaIfIndex"), (0, "IP-MIB", "ipNetToMediaNetAddress"))
ipNetToMediaIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 22, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readcreate")
ipNetToMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 22, 1, 2), PhysAddress()).setMaxAccess("readcreate")
ipNetToMediaNetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 22, 1, 3), IpAddress()).setMaxAccess("readcreate")
ipNetToMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 22, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readcreate")
ipRoutingDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 23), Counter32()).setMaxAccess("readonly")
icmp = MibIdentifier((1, 3, 6, 1, 2, 1, 5))
icmpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 1), Counter32()).setMaxAccess("readonly")
icmpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 2), Counter32()).setMaxAccess("readonly")
icmpInDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 3), Counter32()).setMaxAccess("readonly")
icmpInTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 4), Counter32()).setMaxAccess("readonly")
icmpInParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 5), Counter32()).setMaxAccess("readonly")
icmpInSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 6), Counter32()).setMaxAccess("readonly")
icmpInRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 7), Counter32()).setMaxAccess("readonly")
icmpInEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 8), Counter32()).setMaxAccess("readonly")
icmpInEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 9), Counter32()).setMaxAccess("readonly")
icmpInTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 10), Counter32()).setMaxAccess("readonly")
icmpInTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 11), Counter32()).setMaxAccess("readonly")
icmpInAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 12), Counter32()).setMaxAccess("readonly")
icmpInAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 13), Counter32()).setMaxAccess("readonly")
icmpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 14), Counter32()).setMaxAccess("readonly")
icmpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 15), Counter32()).setMaxAccess("readonly")
icmpOutDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 16), Counter32()).setMaxAccess("readonly")
icmpOutTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 17), Counter32()).setMaxAccess("readonly")
icmpOutParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 18), Counter32()).setMaxAccess("readonly")
icmpOutSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 19), Counter32()).setMaxAccess("readonly")
icmpOutRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 20), Counter32()).setMaxAccess("readonly")
icmpOutEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 21), Counter32()).setMaxAccess("readonly")
icmpOutEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 22), Counter32()).setMaxAccess("readonly")
icmpOutTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 23), Counter32()).setMaxAccess("readonly")
icmpOutTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 24), Counter32()).setMaxAccess("readonly")
icmpOutAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 25), Counter32()).setMaxAccess("readonly")
icmpOutAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 26), Counter32()).setMaxAccess("readonly")
ipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 48)).setRevisions(("1994-11-01 00:00","1991-03-31 00:00",))
ipMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 48, 2))
ipMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 48, 2, 1))
ipMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 48, 2, 2))

# Augmentions

# Groups

icmpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 48, 2, 2, 2)).setObjects(("IP-MIB", "icmpOutRedirects"), ("IP-MIB", "icmpOutTimestamps"), ("IP-MIB", "icmpOutAddrMasks"), ("IP-MIB", "icmpInTimestamps"), ("IP-MIB", "icmpInEchos"), ("IP-MIB", "icmpInMsgs"), ("IP-MIB", "icmpInParmProbs"), ("IP-MIB", "icmpOutParmProbs"), ("IP-MIB", "icmpOutTimeExcds"), ("IP-MIB", "icmpInDestUnreachs"), ("IP-MIB", "icmpOutEchoReps"), ("IP-MIB", "icmpOutMsgs"), ("IP-MIB", "icmpOutTimestampReps"), ("IP-MIB", "icmpOutErrors"), ("IP-MIB", "icmpOutDestUnreachs"), ("IP-MIB", "icmpOutSrcQuenchs"), ("IP-MIB", "icmpOutAddrMaskReps"), ("IP-MIB", "icmpInAddrMaskReps"), ("IP-MIB", "icmpInTimeExcds"), ("IP-MIB", "icmpInErrors"), ("IP-MIB", "icmpOutEchos"), ("IP-MIB", "icmpInAddrMasks"), ("IP-MIB", "icmpInRedirects"), ("IP-MIB", "icmpInTimestampReps"), ("IP-MIB", "icmpInSrcQuenchs"), ("IP-MIB", "icmpInEchoReps"), )
ipGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 48, 2, 2, 1)).setObjects(("IP-MIB", "ipInDelivers"), ("IP-MIB", "ipOutDiscards"), ("IP-MIB", "ipForwDatagrams"), ("IP-MIB", "ipReasmFails"), ("IP-MIB", "ipForwarding"), ("IP-MIB", "ipRoutingDiscards"), ("IP-MIB", "ipNetToMediaNetAddress"), ("IP-MIB", "ipNetToMediaType"), ("IP-MIB", "ipInHdrErrors"), ("IP-MIB", "ipFragFails"), ("IP-MIB", "ipAdEntReasmMaxSize"), ("IP-MIB", "ipInReceives"), ("IP-MIB", "ipReasmTimeout"), ("IP-MIB", "ipFragCreates"), ("IP-MIB", "ipAdEntIfIndex"), ("IP-MIB", "ipDefaultTTL"), ("IP-MIB", "ipInUnknownProtos"), ("IP-MIB", "ipReasmOKs"), ("IP-MIB", "ipAdEntAddr"), ("IP-MIB", "ipOutNoRoutes"), ("IP-MIB", "ipNetToMediaIfIndex"), ("IP-MIB", "ipInAddrErrors"), ("IP-MIB", "ipFragOKs"), ("IP-MIB", "ipOutRequests"), ("IP-MIB", "ipNetToMediaPhysAddress"), ("IP-MIB", "ipReasmReqds"), ("IP-MIB", "ipAdEntNetMask"), ("IP-MIB", "ipAdEntBcastAddr"), ("IP-MIB", "ipInDiscards"), )

# Exports

# Module identity
mibBuilder.exportSymbols("IP-MIB", PYSNMP_MODULE_ID=ipMIB)

# Objects
mibBuilder.exportSymbols("IP-MIB", ip=ip, ipForwarding=ipForwarding, ipDefaultTTL=ipDefaultTTL, ipInReceives=ipInReceives, ipInHdrErrors=ipInHdrErrors, ipInAddrErrors=ipInAddrErrors, ipForwDatagrams=ipForwDatagrams, ipInUnknownProtos=ipInUnknownProtos, ipInDiscards=ipInDiscards, ipInDelivers=ipInDelivers, ipOutRequests=ipOutRequests, ipOutDiscards=ipOutDiscards, ipOutNoRoutes=ipOutNoRoutes, ipReasmTimeout=ipReasmTimeout, ipReasmReqds=ipReasmReqds, ipReasmOKs=ipReasmOKs, ipReasmFails=ipReasmFails, ipFragOKs=ipFragOKs, ipFragFails=ipFragFails, ipFragCreates=ipFragCreates, ipAddrTable=ipAddrTable, ipAddrEntry=ipAddrEntry, ipAdEntAddr=ipAdEntAddr, ipAdEntIfIndex=ipAdEntIfIndex, ipAdEntNetMask=ipAdEntNetMask, ipAdEntBcastAddr=ipAdEntBcastAddr, ipAdEntReasmMaxSize=ipAdEntReasmMaxSize, ipNetToMediaTable=ipNetToMediaTable, ipNetToMediaEntry=ipNetToMediaEntry, ipNetToMediaIfIndex=ipNetToMediaIfIndex, ipNetToMediaPhysAddress=ipNetToMediaPhysAddress, ipNetToMediaNetAddress=ipNetToMediaNetAddress, ipNetToMediaType=ipNetToMediaType, ipRoutingDiscards=ipRoutingDiscards, icmp=icmp, icmpInMsgs=icmpInMsgs, icmpInErrors=icmpInErrors, icmpInDestUnreachs=icmpInDestUnreachs, icmpInTimeExcds=icmpInTimeExcds, icmpInParmProbs=icmpInParmProbs, icmpInSrcQuenchs=icmpInSrcQuenchs, icmpInRedirects=icmpInRedirects, icmpInEchos=icmpInEchos, icmpInEchoReps=icmpInEchoReps, icmpInTimestamps=icmpInTimestamps, icmpInTimestampReps=icmpInTimestampReps, icmpInAddrMasks=icmpInAddrMasks, icmpInAddrMaskReps=icmpInAddrMaskReps, icmpOutMsgs=icmpOutMsgs, icmpOutErrors=icmpOutErrors, icmpOutDestUnreachs=icmpOutDestUnreachs, icmpOutTimeExcds=icmpOutTimeExcds, icmpOutParmProbs=icmpOutParmProbs, icmpOutSrcQuenchs=icmpOutSrcQuenchs, icmpOutRedirects=icmpOutRedirects, icmpOutEchos=icmpOutEchos, icmpOutEchoReps=icmpOutEchoReps, icmpOutTimestamps=icmpOutTimestamps, icmpOutTimestampReps=icmpOutTimestampReps, icmpOutAddrMasks=icmpOutAddrMasks, icmpOutAddrMaskReps=icmpOutAddrMaskReps, ipMIB=ipMIB, ipMIBConformance=ipMIBConformance, ipMIBCompliances=ipMIBCompliances, ipMIBGroups=ipMIBGroups)

# Groups
mibBuilder.exportSymbols("IP-MIB", icmpGroup=icmpGroup, ipGroup=ipGroup)
