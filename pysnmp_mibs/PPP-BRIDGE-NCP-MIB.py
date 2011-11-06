# PySNMP SMI module. Autogenerated from smidump -f python PPP-BRIDGE-NCP-MIB
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

pppBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 4))
pppBridgeTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 1))
if mibBuilder.loadTexts: pppBridgeTable.setDescription("Table containing the parameters and statistics\nfor the local PPP entity that are related to\nthe operation of Bridging over the PPP.")
pppBridgeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppBridgeEntry.setDescription("Bridging information for a particular PPP\nlink.")
pppBridgeOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("opened", 1), ("not-opened", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeOperStatus.setDescription("The operational status of the Bridge network\nprotocol. If the value of this object is up\nthen the finite state machine for the Bridge\nnetwork protocol has reached the Opened state.")
pppBridgeLocalToRemoteTinygramCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeLocalToRemoteTinygramCompression.setDescription("Indicates whether the local node will perform\nTinygram Compression when sending packets to\nthe remote entity. If false then the local\nentity will not perform Tinygram Compression.\nIf true then the local entity will perform\nTinygram Compression. The value of this object\nis meaningful only when the link has reached\nthe open state (pppBridgeOperStatus is\nopened).")
pppBridgeRemoteToLocalTinygramCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeRemoteToLocalTinygramCompression.setDescription("If false(1) then the remote entity is not\nexpected to perform Tinygram Compression. If\ntrue then the remote entity is expected to\nperform Tinygram Compression. The value of this\nobject is meaningful only when the link has\nreached the open state (pppBridgeOperStatus is\nopened).")
pppBridgeLocalToRemoteLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeLocalToRemoteLanId.setDescription("Indicates whether the local node will include\nthe LAN Identification field in transmitted\npackets or not. If false(1) then the local node\nwill not transmit this field, true(2) means\nthat the field will be transmitted. The value\nof this object is meaningful only when the link\nhas reached the open state (pppBridgeOperStatus\nis opened).")
pppBridgeRemoteToLocalLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeRemoteToLocalLanId.setDescription("Indicates whether the remote node has\nindicated that it will include the LAN\nIdentification field in transmitted packets or\nnot. If false(1) then the field will not be\ntransmitted, if true(2) then the field will be\ntransmitted. The value of this object is\nmeaningful only when the link has reached the\nopen state (pppBridgeOperStatus is opened).")
pppBridgeConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 2))
if mibBuilder.loadTexts: pppBridgeConfigTable.setDescription("Table containing the parameters and statistics\nfor the local PPP entity that are related to\nthe operation of Bridging over the PPP.")
pppBridgeConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppBridgeConfigEntry.setDescription("Bridging Configuration information for a\nparticular PPP link.")
pppBridgeConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("open", 1), ("close", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeConfigAdminStatus.setDescription("The immediate desired status of the Bridging\nnetwork protocol. Setting this object to open\nwill inject an administrative open event into\nthe Bridging network protocol's finite state\nmachine. Setting this object to close will\ninject an administrative close event into the\nBridging network protocol's finite state\nmachine.")
pppBridgeConfigTinygram = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeConfigTinygram.setDescription("If false then the local BNCP entity will not\ninitiate the Tinygram Compression Option\nNegotiation. If true then the local BNCP entity\nwill initiate negotiation of this option.")
pppBridgeConfigRingId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeConfigRingId.setDescription("If false then the local PPP Entity will not\ninitiate a Remote Ring Identification Option\nnegotiation. If true then the local PPP entity\nwill intiate this negotiation. This MIB object\nis relevant only if the interface is for 802.5\nToken Ring bridging.")
pppBridgeConfigLineId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeConfigLineId.setDescription("If false then the local PPP Entity is not to\ninitiate a Line Identification Option\nnegotiation. If true then the local PPP entity\nwill intiate this negotiation. This MIB object\nis relevant only if the interface is for 802.5\nToken Ring bridging.")
pppBridgeConfigLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeConfigLanId.setDescription("If false then the local BNCP entity will not\ninitiate the LAN Identification Option\nNegotiation. If true then the local BNCP entity\nwill initiate negotiation of this option.")
pppBridgeMediaTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 3))
if mibBuilder.loadTexts: pppBridgeMediaTable.setDescription("Table identifying which MAC media types are\nenabled for the Bridging NCPs.")
pppBridgeMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaMacType"))
if mibBuilder.loadTexts: pppBridgeMediaEntry.setDescription("Status of a specific MAC Type for a specific\nPPP Link.")
pppBridgeMediaMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeMediaMacType.setDescription("The MAC type for which this entry in the\npppBridgeMediaTable is providing status\ninformation. Valid values for this object are\ndefined in Section 6.6 MAC Type Support\nSelection of RFC1220 (Bridging Point-to-Point\nProtocol).")
pppBridgeMediaLocalStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("accept", 1), ("dont-accept", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeMediaLocalStatus.setDescription("Indicates whether the local PPP Bridging\nEntity will accept packets of the protocol type\nidentified in pppBridgeMediaMacType on the PPP\nlink identified by ifIndex or not. If this\nobject is accept then any packets of the\nindicated MAC type will be received and\nproperly processed. If this object is dont-\naccept then received packets of the indicated\nMAC type will not be properly processed.")
pppBridgeMediaRemoteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("accept", 1), ("dont-accept", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppBridgeMediaRemoteStatus.setDescription("Indicates whether the local PPP Bridging\nEntity believes that the remote PPP Bridging\nEntity will accept packets of the protocol type\nidentified in pppBridgeMediaMacType on the PPP\nlink identified by ifIndex or not.")
pppBridgeMediaConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 4))
if mibBuilder.loadTexts: pppBridgeMediaConfigTable.setDescription("Table identifying which MAC media types are\nenabled for the Bridging NCPs.")
pppBridgeMediaConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaConfigMacType"))
if mibBuilder.loadTexts: pppBridgeMediaConfigEntry.setDescription("Status of a specific MAC Type for a specific\nPPP Link.")
pppBridgeMediaConfigMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeMediaConfigMacType.setDescription("The MAC type for which this entry in the\npppBridgeMediaConfigTable is providing status\ninformation. Valid values for this object are\ndefined in Section 6.6 MAC Type Support\nSelection of RFC1220 (Bridging Point-to-Point\nProtocol).")
pppBridgeMediaConfigLocalStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("accept", 1), ("dont-accept", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppBridgeMediaConfigLocalStatus.setDescription("Indicates whether the local PPP Bridging\nEntity should accept packets of the protocol\ntype identified in pppBridgeMediaConfigMacType\non the PPP link identified by ifIndex or not.\nSetting this object to the value dont-accept\nhas the affect of invalidating the\ncorresponding entry in the\npppBridgeMediaConfigTable object. It is an\nimplementation-specific matter as to whether\nthe agent removes an invalidated entry from the\ntable. Accordingly, management stations must be\nprepared to receive tabular information from\nagents that corresponds to entries not\ncurrently in use. Changing this object will\nhave effect when the link is next restarted.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-BRIDGE-NCP-MIB", pppBridge=pppBridge, pppBridgeTable=pppBridgeTable, pppBridgeEntry=pppBridgeEntry, pppBridgeOperStatus=pppBridgeOperStatus, pppBridgeLocalToRemoteTinygramCompression=pppBridgeLocalToRemoteTinygramCompression, pppBridgeRemoteToLocalTinygramCompression=pppBridgeRemoteToLocalTinygramCompression, pppBridgeLocalToRemoteLanId=pppBridgeLocalToRemoteLanId, pppBridgeRemoteToLocalLanId=pppBridgeRemoteToLocalLanId, pppBridgeConfigTable=pppBridgeConfigTable, pppBridgeConfigEntry=pppBridgeConfigEntry, pppBridgeConfigAdminStatus=pppBridgeConfigAdminStatus, pppBridgeConfigTinygram=pppBridgeConfigTinygram, pppBridgeConfigRingId=pppBridgeConfigRingId, pppBridgeConfigLineId=pppBridgeConfigLineId, pppBridgeConfigLanId=pppBridgeConfigLanId, pppBridgeMediaTable=pppBridgeMediaTable, pppBridgeMediaEntry=pppBridgeMediaEntry, pppBridgeMediaMacType=pppBridgeMediaMacType, pppBridgeMediaLocalStatus=pppBridgeMediaLocalStatus, pppBridgeMediaRemoteStatus=pppBridgeMediaRemoteStatus, pppBridgeMediaConfigTable=pppBridgeMediaConfigTable, pppBridgeMediaConfigEntry=pppBridgeMediaConfigEntry, pppBridgeMediaConfigMacType=pppBridgeMediaConfigMacType, pppBridgeMediaConfigLocalStatus=pppBridgeMediaConfigLocalStatus)

