# PySNMP SMI module. Autogenerated from smidump -f python CLNS-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:25:52 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( PhysAddress, ) = mibBuilder.importSymbols("RFC1213-MIB", "PhysAddress")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "experimental")

# Types

class ClnpAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,21)
    pass


# Objects

clns = MibIdentifier((1, 3, 6, 1, 3, 1))
clnp = MibIdentifier((1, 3, 6, 1, 3, 1, 1))
clnpForwarding = MibScalar((1, 3, 6, 1, 3, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("is", 1), ("es", 2), ))).setMaxAccess("readwrite")
clnpDefaultLifeTime = MibScalar((1, 3, 6, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
clnpInReceives = MibScalar((1, 3, 6, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
clnpInHdrErrors = MibScalar((1, 3, 6, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
clnpInAddrErrors = MibScalar((1, 3, 6, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
clnpForwPDUs = MibScalar((1, 3, 6, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
clnpInUnknownNLPs = MibScalar((1, 3, 6, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
clnpInUnknownULPs = MibScalar((1, 3, 6, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
clnpInDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
clnpInDelivers = MibScalar((1, 3, 6, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
clnpOutRequests = MibScalar((1, 3, 6, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
clnpOutDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
clnpOutNoRoutes = MibScalar((1, 3, 6, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
clnpReasmTimeout = MibScalar((1, 3, 6, 1, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
clnpReasmReqds = MibScalar((1, 3, 6, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
clnpReasmOKs = MibScalar((1, 3, 6, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
clnpReasmFails = MibScalar((1, 3, 6, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
clnpSegOKs = MibScalar((1, 3, 6, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
clnpSegFails = MibScalar((1, 3, 6, 1, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
clnpSegCreates = MibScalar((1, 3, 6, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
clnpAddrTable = MibTable((1, 3, 6, 1, 3, 1, 1, 21))
clnpAddrEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 21, 1)).setIndexNames((0, "CLNS-MIB", "clnpAdEntAddr"))
clnpAdEntAddr = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 1), ClnpAddress()).setMaxAccess("readonly")
clnpAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 2), Integer32()).setMaxAccess("readonly")
clnpAdEntReasmMaxSize = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
clnpRoutingTable = MibTable((1, 3, 6, 1, 3, 1, 1, 22))
clnpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 22, 1)).setIndexNames((0, "CLNS-MIB", "clnpRouteDest"))
clnpRouteDest = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 1), ClnpAddress()).setMaxAccess("readwrite")
clnpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 2), Integer32()).setMaxAccess("readwrite")
clnpRouteMetric1 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 3), Integer32()).setMaxAccess("readwrite")
clnpRouteMetric2 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 4), Integer32()).setMaxAccess("readwrite")
clnpRouteMetric3 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 5), Integer32()).setMaxAccess("readwrite")
clnpRouteMetric4 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 6), Integer32()).setMaxAccess("readwrite")
clnpRouteNextHop = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 7), ClnpAddress()).setMaxAccess("readwrite")
clnpRouteType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("direct", 3), ("remote", 4), ))).setMaxAccess("readwrite")
clnpRouteProto = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(12,3,13,14,11,1,9,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("local", 2), ("netmgmt", 3), ("is-is", 9), ))).setMaxAccess("readonly")
clnpRouteAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 10), Integer32()).setMaxAccess("readwrite")
clnpRouteMetric5 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 11), Integer32()).setMaxAccess("readwrite")
clnpRouteInfo = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 12), ObjectIdentifier()).setMaxAccess("readonly")
clnpNetToMediaTable = MibTable((1, 3, 6, 1, 3, 1, 1, 23))
clnpNetToMediaEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 23, 1)).setIndexNames((0, "CLNS-MIB", "clnpNetToMediaIfIndex"), (0, "CLNS-MIB", "clnpNetToMediaNetAddress"))
clnpNetToMediaIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 1), Integer32()).setMaxAccess("readwrite")
clnpNetToMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 2), PhysAddress()).setMaxAccess("readwrite")
clnpNetToMediaNetAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 3), ClnpAddress()).setMaxAccess("readwrite")
clnpNetToMediaType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readwrite")
clnpNetToMediaAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 5), Integer32()).setMaxAccess("readwrite")
clnpNetToMediaHoldTime = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 6), Integer32()).setMaxAccess("readwrite")
clnpMediaToNetTable = MibTable((1, 3, 6, 1, 3, 1, 1, 24))
clnpMediaToNetEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 24, 1)).setIndexNames((0, "CLNS-MIB", "clnpMediaToNetIfIndex"), (0, "CLNS-MIB", "clnpMediaToNetPhysAddress"))
clnpMediaToNetIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 1), Integer32()).setMaxAccess("readwrite")
clnpMediaToNetAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 2), ClnpAddress()).setMaxAccess("readwrite")
clnpMediaToNetPhysAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 3), PhysAddress()).setMaxAccess("readwrite")
clnpMediaToNetType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readwrite")
clnpMediaToNetAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 5), Integer32()).setMaxAccess("readwrite")
clnpMediaToNetHoldTime = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 6), Integer32()).setMaxAccess("readwrite")
clnpInOpts = MibScalar((1, 3, 6, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
clnpOutOpts = MibScalar((1, 3, 6, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
clnpRoutingDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
error = MibIdentifier((1, 3, 6, 1, 3, 1, 2))
clnpInErrors = MibScalar((1, 3, 6, 1, 3, 1, 2, 1), Counter32()).setMaxAccess("readonly")
clnpOutErrors = MibScalar((1, 3, 6, 1, 3, 1, 2, 2), Counter32()).setMaxAccess("readonly")
clnpInErrUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 3), Counter32()).setMaxAccess("readonly")
clnpInErrProcs = MibScalar((1, 3, 6, 1, 3, 1, 2, 4), Counter32()).setMaxAccess("readonly")
clnpInErrCksums = MibScalar((1, 3, 6, 1, 3, 1, 2, 5), Counter32()).setMaxAccess("readonly")
clnpInErrCongests = MibScalar((1, 3, 6, 1, 3, 1, 2, 6), Counter32()).setMaxAccess("readonly")
clnpInErrHdrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 7), Counter32()).setMaxAccess("readonly")
clnpInErrSegs = MibScalar((1, 3, 6, 1, 3, 1, 2, 8), Counter32()).setMaxAccess("readonly")
clnpInErrIncomps = MibScalar((1, 3, 6, 1, 3, 1, 2, 9), Counter32()).setMaxAccess("readonly")
clnpInErrDups = MibScalar((1, 3, 6, 1, 3, 1, 2, 10), Counter32()).setMaxAccess("readonly")
clnpInErrUnreachDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 11), Counter32()).setMaxAccess("readonly")
clnpInErrUnknownDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 12), Counter32()).setMaxAccess("readonly")
clnpInErrSRUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 13), Counter32()).setMaxAccess("readonly")
clnpInErrSRSyntaxes = MibScalar((1, 3, 6, 1, 3, 1, 2, 14), Counter32()).setMaxAccess("readonly")
clnpInErrSRUnkAddrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 15), Counter32()).setMaxAccess("readonly")
clnpInErrSRBadPaths = MibScalar((1, 3, 6, 1, 3, 1, 2, 16), Counter32()).setMaxAccess("readonly")
clnpInErrHops = MibScalar((1, 3, 6, 1, 3, 1, 2, 17), Counter32()).setMaxAccess("readonly")
clnpInErrHopReassms = MibScalar((1, 3, 6, 1, 3, 1, 2, 18), Counter32()).setMaxAccess("readonly")
clnpInErrUnsOptions = MibScalar((1, 3, 6, 1, 3, 1, 2, 19), Counter32()).setMaxAccess("readonly")
clnpInErrUnsVersions = MibScalar((1, 3, 6, 1, 3, 1, 2, 20), Counter32()).setMaxAccess("readonly")
clnpInErrUnsSecurities = MibScalar((1, 3, 6, 1, 3, 1, 2, 21), Counter32()).setMaxAccess("readonly")
clnpInErrUnsSRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 22), Counter32()).setMaxAccess("readonly")
clnpInErrUnsRRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 23), Counter32()).setMaxAccess("readonly")
clnpInErrInterferences = MibScalar((1, 3, 6, 1, 3, 1, 2, 24), Counter32()).setMaxAccess("readonly")
clnpOutErrUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 25), Counter32()).setMaxAccess("readonly")
clnpOutErrProcs = MibScalar((1, 3, 6, 1, 3, 1, 2, 26), Counter32()).setMaxAccess("readonly")
clnpOutErrCksums = MibScalar((1, 3, 6, 1, 3, 1, 2, 27), Counter32()).setMaxAccess("readonly")
clnpOutErrCongests = MibScalar((1, 3, 6, 1, 3, 1, 2, 28), Counter32()).setMaxAccess("readonly")
clnpOutErrHdrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 29), Counter32()).setMaxAccess("readonly")
clnpOutErrSegs = MibScalar((1, 3, 6, 1, 3, 1, 2, 30), Counter32()).setMaxAccess("readonly")
clnpOutErrIncomps = MibScalar((1, 3, 6, 1, 3, 1, 2, 31), Counter32()).setMaxAccess("readonly")
clnpOutErrDups = MibScalar((1, 3, 6, 1, 3, 1, 2, 32), Counter32()).setMaxAccess("readonly")
clnpOutErrUnreachDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 33), Counter32()).setMaxAccess("readonly")
clnpOutErrUnknownDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 34), Counter32()).setMaxAccess("readonly")
clnpOutErrSRUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 35), Counter32()).setMaxAccess("readonly")
clnpOutErrSRSyntaxes = MibScalar((1, 3, 6, 1, 3, 1, 2, 36), Counter32()).setMaxAccess("readonly")
clnpOutErrSRUnkAddrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 37), Counter32()).setMaxAccess("readonly")
clnpOutErrSRBadPaths = MibScalar((1, 3, 6, 1, 3, 1, 2, 38), Counter32()).setMaxAccess("readonly")
clnpOutErrHops = MibScalar((1, 3, 6, 1, 3, 1, 2, 39), Counter32()).setMaxAccess("readonly")
clnpOutErrHopReassms = MibScalar((1, 3, 6, 1, 3, 1, 2, 40), Counter32()).setMaxAccess("readonly")
clnpOutErrUnsOptions = MibScalar((1, 3, 6, 1, 3, 1, 2, 41), Counter32()).setMaxAccess("readonly")
clnpOutErrUnsVersions = MibScalar((1, 3, 6, 1, 3, 1, 2, 42), Counter32()).setMaxAccess("readonly")
clnpOutErrUnsSecurities = MibScalar((1, 3, 6, 1, 3, 1, 2, 43), Counter32()).setMaxAccess("readonly")
clnpOutErrUnsSRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 44), Counter32()).setMaxAccess("readonly")
clnpOutErrUnsRRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 45), Counter32()).setMaxAccess("readonly")
clnpOutErrInterferences = MibScalar((1, 3, 6, 1, 3, 1, 2, 46), Counter32()).setMaxAccess("readonly")
echo = MibIdentifier((1, 3, 6, 1, 3, 1, 3))
es_is = MibIdentifier((1, 3, 6, 1, 3, 1, 4)).setLabel("es-is")
esisESHins = MibScalar((1, 3, 6, 1, 3, 1, 4, 1), Counter32()).setMaxAccess("readonly")
esisESHouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 2), Counter32()).setMaxAccess("readonly")
esisISHins = MibScalar((1, 3, 6, 1, 3, 1, 4, 3), Counter32()).setMaxAccess("readonly")
esisISHouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 4), Counter32()).setMaxAccess("readonly")
esisRDUins = MibScalar((1, 3, 6, 1, 3, 1, 4, 5), Counter32()).setMaxAccess("readonly")
esisRDUouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 6), Counter32()).setMaxAccess("readonly")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("CLNS-MIB", ClnpAddress=ClnpAddress)

# Objects
mibBuilder.exportSymbols("CLNS-MIB", clns=clns, clnp=clnp, clnpForwarding=clnpForwarding, clnpDefaultLifeTime=clnpDefaultLifeTime, clnpInReceives=clnpInReceives, clnpInHdrErrors=clnpInHdrErrors, clnpInAddrErrors=clnpInAddrErrors, clnpForwPDUs=clnpForwPDUs, clnpInUnknownNLPs=clnpInUnknownNLPs, clnpInUnknownULPs=clnpInUnknownULPs, clnpInDiscards=clnpInDiscards, clnpInDelivers=clnpInDelivers, clnpOutRequests=clnpOutRequests, clnpOutDiscards=clnpOutDiscards, clnpOutNoRoutes=clnpOutNoRoutes, clnpReasmTimeout=clnpReasmTimeout, clnpReasmReqds=clnpReasmReqds, clnpReasmOKs=clnpReasmOKs, clnpReasmFails=clnpReasmFails, clnpSegOKs=clnpSegOKs, clnpSegFails=clnpSegFails, clnpSegCreates=clnpSegCreates, clnpAddrTable=clnpAddrTable, clnpAddrEntry=clnpAddrEntry, clnpAdEntAddr=clnpAdEntAddr, clnpAdEntIfIndex=clnpAdEntIfIndex, clnpAdEntReasmMaxSize=clnpAdEntReasmMaxSize, clnpRoutingTable=clnpRoutingTable, clnpRouteEntry=clnpRouteEntry, clnpRouteDest=clnpRouteDest, clnpRouteIfIndex=clnpRouteIfIndex, clnpRouteMetric1=clnpRouteMetric1, clnpRouteMetric2=clnpRouteMetric2, clnpRouteMetric3=clnpRouteMetric3, clnpRouteMetric4=clnpRouteMetric4, clnpRouteNextHop=clnpRouteNextHop, clnpRouteType=clnpRouteType, clnpRouteProto=clnpRouteProto, clnpRouteAge=clnpRouteAge, clnpRouteMetric5=clnpRouteMetric5, clnpRouteInfo=clnpRouteInfo, clnpNetToMediaTable=clnpNetToMediaTable, clnpNetToMediaEntry=clnpNetToMediaEntry, clnpNetToMediaIfIndex=clnpNetToMediaIfIndex, clnpNetToMediaPhysAddress=clnpNetToMediaPhysAddress, clnpNetToMediaNetAddress=clnpNetToMediaNetAddress, clnpNetToMediaType=clnpNetToMediaType, clnpNetToMediaAge=clnpNetToMediaAge, clnpNetToMediaHoldTime=clnpNetToMediaHoldTime, clnpMediaToNetTable=clnpMediaToNetTable, clnpMediaToNetEntry=clnpMediaToNetEntry, clnpMediaToNetIfIndex=clnpMediaToNetIfIndex, clnpMediaToNetAddress=clnpMediaToNetAddress, clnpMediaToNetPhysAddress=clnpMediaToNetPhysAddress, clnpMediaToNetType=clnpMediaToNetType, clnpMediaToNetAge=clnpMediaToNetAge, clnpMediaToNetHoldTime=clnpMediaToNetHoldTime, clnpInOpts=clnpInOpts, clnpOutOpts=clnpOutOpts, clnpRoutingDiscards=clnpRoutingDiscards, error=error, clnpInErrors=clnpInErrors, clnpOutErrors=clnpOutErrors, clnpInErrUnspecs=clnpInErrUnspecs, clnpInErrProcs=clnpInErrProcs, clnpInErrCksums=clnpInErrCksums, clnpInErrCongests=clnpInErrCongests, clnpInErrHdrs=clnpInErrHdrs, clnpInErrSegs=clnpInErrSegs, clnpInErrIncomps=clnpInErrIncomps, clnpInErrDups=clnpInErrDups, clnpInErrUnreachDsts=clnpInErrUnreachDsts, clnpInErrUnknownDsts=clnpInErrUnknownDsts, clnpInErrSRUnspecs=clnpInErrSRUnspecs, clnpInErrSRSyntaxes=clnpInErrSRSyntaxes, clnpInErrSRUnkAddrs=clnpInErrSRUnkAddrs, clnpInErrSRBadPaths=clnpInErrSRBadPaths, clnpInErrHops=clnpInErrHops, clnpInErrHopReassms=clnpInErrHopReassms, clnpInErrUnsOptions=clnpInErrUnsOptions, clnpInErrUnsVersions=clnpInErrUnsVersions, clnpInErrUnsSecurities=clnpInErrUnsSecurities, clnpInErrUnsSRs=clnpInErrUnsSRs, clnpInErrUnsRRs=clnpInErrUnsRRs, clnpInErrInterferences=clnpInErrInterferences, clnpOutErrUnspecs=clnpOutErrUnspecs, clnpOutErrProcs=clnpOutErrProcs, clnpOutErrCksums=clnpOutErrCksums, clnpOutErrCongests=clnpOutErrCongests, clnpOutErrHdrs=clnpOutErrHdrs, clnpOutErrSegs=clnpOutErrSegs, clnpOutErrIncomps=clnpOutErrIncomps, clnpOutErrDups=clnpOutErrDups, clnpOutErrUnreachDsts=clnpOutErrUnreachDsts, clnpOutErrUnknownDsts=clnpOutErrUnknownDsts, clnpOutErrSRUnspecs=clnpOutErrSRUnspecs, clnpOutErrSRSyntaxes=clnpOutErrSRSyntaxes, clnpOutErrSRUnkAddrs=clnpOutErrSRUnkAddrs, clnpOutErrSRBadPaths=clnpOutErrSRBadPaths, clnpOutErrHops=clnpOutErrHops, clnpOutErrHopReassms=clnpOutErrHopReassms, clnpOutErrUnsOptions=clnpOutErrUnsOptions, clnpOutErrUnsVersions=clnpOutErrUnsVersions, clnpOutErrUnsSecurities=clnpOutErrUnsSecurities, clnpOutErrUnsSRs=clnpOutErrUnsSRs, clnpOutErrUnsRRs=clnpOutErrUnsRRs, clnpOutErrInterferences=clnpOutErrInterferences, echo=echo, es_is=es_is, esisESHins=esisESHins, esisESHouts=esisESHouts, esisISHins=esisISHins, esisISHouts=esisISHouts, esisRDUins=esisRDUins, esisRDUouts=esisRDUouts)

