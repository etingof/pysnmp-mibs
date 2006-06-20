# PySNMP SMI module. Autogenerated from smidump -f python PPP-IP-NCP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:16 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ppp, ) = mibBuilder.importSymbols("PPP-LCP-MIB", "ppp")
( ifIndex, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex")
( Bits, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

pppIp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 3))
pppIpTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 3, 1))
pppIpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppIpOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("opened", 1), ("not-opened", 2), ))).setMaxAccess("readonly")
pppIpLocalToRemoteCompressionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), ))).setMaxAccess("readonly")
pppIpRemoteToLocalCompressionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), ))).setMaxAccess("readonly")
pppIpRemoteMaxSlotId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
pppIpLocalMaxSlotId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
pppIpConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 3, 2))
pppIpConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppIpConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("open", 1), ("close", 2), ))).setMaxAccess("readwrite")
pppIpConfigCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), )).clone(1)).setMaxAccess("readwrite")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-IP-NCP-MIB", pppIp=pppIp, pppIpTable=pppIpTable, pppIpEntry=pppIpEntry, pppIpOperStatus=pppIpOperStatus, pppIpLocalToRemoteCompressionProtocol=pppIpLocalToRemoteCompressionProtocol, pppIpRemoteToLocalCompressionProtocol=pppIpRemoteToLocalCompressionProtocol, pppIpRemoteMaxSlotId=pppIpRemoteMaxSlotId, pppIpLocalMaxSlotId=pppIpLocalMaxSlotId, pppIpConfigTable=pppIpConfigTable, pppIpConfigEntry=pppIpConfigEntry, pppIpConfigAdminStatus=pppIpConfigAdminStatus, pppIpConfigCompression=pppIpConfigCompression)

