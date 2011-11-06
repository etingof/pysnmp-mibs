# PySNMP SMI module. Autogenerated from smidump -f python PPP-IP-NCP-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:16:01 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

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
if mibBuilder.loadTexts: pppIpTable.setDescription("Table containing the IP parameters and\nstatistics for the local PPP entity.")
pppIpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppIpEntry.setDescription("IPCP status information for a particular PPP\nlink.")
pppIpOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("opened", 1), ("not-opened", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIpOperStatus.setDescription("The operational status of the IP network\nprotocol. If the value of this object is up\nthen the finite state machine for the IP\nnetwork protocol has reached the Opened state.")
pppIpLocalToRemoteCompressionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIpLocalToRemoteCompressionProtocol.setDescription("The IP compression protocol that the local\nPPP-IP entity uses when sending packets to the\nremote PPP-IP entity. The value of this object\nis meaningful only when the link has reached\nthe open state (pppIpOperStatus is opened).")
pppIpRemoteToLocalCompressionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIpRemoteToLocalCompressionProtocol.setDescription("The IP compression protocol that the remote\nPPP-IP entity uses when sending packets to the\nlocal PPP-IP entity. The value of this object\nis meaningful only when the link has reached\nthe open state (pppIpOperStatus is opened).")
pppIpRemoteMaxSlotId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIpRemoteMaxSlotId.setDescription("The Max-Slot-Id parameter that the remote node\nhas advertised and that is in use on the link.\nIf vj-tcp header compression is not in use on\nthe link then the value of this object shall be\n0. The value of this object is meaningful only\nwhen the link has reached the open state\n(pppIpOperStatus is opened).")
pppIpLocalMaxSlotId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIpLocalMaxSlotId.setDescription("The Max-Slot-Id parameter that the local node\nhas advertised and that is in use on the link.\nIf vj-tcp header compression is not in use on\nthe link then the value of this object shall be\n0. The value of this object is meaningful only\nwhen the link has reached the open state\n(pppIpOperStatus is opened).")
pppIpConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 3, 2))
if mibBuilder.loadTexts: pppIpConfigTable.setDescription("Table containing configuration variables for\nthe IPCP for the local PPP entity.")
pppIpConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppIpConfigEntry.setDescription("IPCP information for a particular PPP link.")
pppIpConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("open", 1), ("close", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppIpConfigAdminStatus.setDescription("The immediate desired status of the IP network\nprotocol. Setting this object to open will\ninject an administrative open event into the IP\nnetwork protocol's finite state machine.\nSetting this object to close will inject an\nadministrative close event into the IP network\nprotocol's finite state machine.")
pppIpConfigCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("vj-tcp", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppIpConfigCompression.setDescription("If none(1) then the local node will not\nattempt to negotiate any IP Compression option.\nOtherwise, the local node will attempt to\nnegotiate compression mode indicated by the\nenumerated value. Changing this object will\nhave effect when the link is next restarted.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-IP-NCP-MIB", pppIp=pppIp, pppIpTable=pppIpTable, pppIpEntry=pppIpEntry, pppIpOperStatus=pppIpOperStatus, pppIpLocalToRemoteCompressionProtocol=pppIpLocalToRemoteCompressionProtocol, pppIpRemoteToLocalCompressionProtocol=pppIpRemoteToLocalCompressionProtocol, pppIpRemoteMaxSlotId=pppIpRemoteMaxSlotId, pppIpLocalMaxSlotId=pppIpLocalMaxSlotId, pppIpConfigTable=pppIpConfigTable, pppIpConfigEntry=pppIpConfigEntry, pppIpConfigAdminStatus=pppIpConfigAdminStatus, pppIpConfigCompression=pppIpConfigCompression)

