# PySNMP SMI module. Autogenerated from smidump -f python Q-BRIDGE-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:14 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( dot1dBasePort, dot1dBasePortEntry, dot1dBridge, ) = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "dot1dBasePortEntry", "dot1dBridge")
( EnabledStatus, ) = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
( TimeFilter, ) = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( MacAddress, RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")

# Types

class PortList(OctetString):
    pass

class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,4094)
    pass

class VlanIndex(Unsigned32):
    pass


# Objects

qBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 7)).setRevisions(("1999-08-25 00:00",))
qBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1))
dot1qBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 1))
dot1qVlanVersionNumber = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,)).subtype(namedValues=namedval.NamedValues(("version1", 1), ))).setMaxAccess("readonly")
dot1qMaxVlanId = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 2), VlanId()).setMaxAccess("readonly")
dot1qMaxSupportedVlans = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
dot1qNumVlans = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
dot1qGvrpStatus = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
dot1qTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 2))
dot1qFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1))
dot1qFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"))
dot1qFdbId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("noaccess")
dot1qFdbDynamicCount = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
dot1qTpFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2))
dot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
dot1qTpFdbAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
dot1qTpFdbPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
dot1qTpFdbStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,5,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5), ))).setMaxAccess("readonly")
dot1qTpGroupTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3))
dot1qTpGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "Q-BRIDGE-MIB", "dot1qTpGroupAddress"))
dot1qTpGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("noaccess")
dot1qTpGroupEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 2), PortList()).setMaxAccess("readonly")
dot1qTpGroupLearnt = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 3), PortList()).setMaxAccess("readonly")
dot1qForwardAllTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4))
dot1qForwardAllEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qForwardAllPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 1), PortList()).setMaxAccess("readonly")
dot1qForwardAllStaticPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 2), PortList()).setMaxAccess("readwrite")
dot1qForwardAllForbiddenPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 3), PortList()).setMaxAccess("readwrite")
dot1qForwardUnregisteredTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5))
dot1qForwardUnregisteredEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qForwardUnregisteredPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 1), PortList()).setMaxAccess("readonly")
dot1qForwardUnregisteredStaticPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 2), PortList()).setMaxAccess("readwrite")
dot1qForwardUnregisteredForbiddenPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 3), PortList()).setMaxAccess("readwrite")
dot1qStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 3))
dot1qStaticUnicastTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1))
dot1qStaticUnicastEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastAddress"), (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastReceivePort"))
dot1qStaticUnicastAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 1), MacAddress()).setMaxAccess("noaccess")
dot1qStaticUnicastReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
dot1qStaticUnicastAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 3), PortList()).setMaxAccess("readwrite")
dot1qStaticUnicastStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,5,1,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5), )).clone(3)).setMaxAccess("readwrite")
dot1qStaticMulticastTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2))
dot1qStaticMulticastEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastAddress"), (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastReceivePort"))
dot1qStaticMulticastAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
dot1qStaticMulticastReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
dot1qStaticMulticastStaticEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 3), PortList()).setMaxAccess("readwrite")
dot1qStaticMulticastForbiddenEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 4), PortList()).setMaxAccess("readwrite")
dot1qStaticMulticastStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,5,1,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5), )).clone(3)).setMaxAccess("readwrite")
dot1qVlan = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 4))
dot1qVlanNumDeletes = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 1), Counter32()).setMaxAccess("readonly")
dot1qVlanCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2))
dot1qVlanCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanTimeMark"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qVlanTimeMark = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 1), TimeFilter()).setMaxAccess("noaccess")
dot1qVlanIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 2), VlanIndex()).setMaxAccess("noaccess")
dot1qVlanFdbId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
dot1qVlanCurrentEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 4), PortList()).setMaxAccess("readonly")
dot1qVlanCurrentUntaggedPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 5), PortList()).setMaxAccess("readonly")
dot1qVlanStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("permanent", 2), ("dynamicGvrp", 3), ))).setMaxAccess("readonly")
dot1qVlanCreationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
dot1qVlanStaticTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3))
dot1qVlanStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qVlanStaticName = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
dot1qVlanStaticEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 2), PortList()).setMaxAccess("readwrite")
dot1qVlanForbiddenEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 3), PortList()).setMaxAccess("readwrite")
dot1qVlanStaticUntaggedPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 4), PortList()).setMaxAccess("readwrite")
dot1qVlanStaticRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
dot1qNextFreeLocalVlanIndex = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(4096, 2147483647L))).setMaxAccess("readonly")
dot1qPortVlanTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5))
dot1qPortVlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1))
dot1qPvid = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 1), VlanIndex()).setMaxAccess("readwrite")
dot1qPortAcceptableFrameTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("admitAll", 1), ("admitOnlyVlanTagged", 2), )).clone(1)).setMaxAccess("readwrite")
dot1qPortIngressFiltering = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 3), TruthValue()).setMaxAccess("readwrite")
dot1qPortGvrpStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
dot1qPortGvrpFailedRegistrations = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 5), Counter32()).setMaxAccess("readonly")
dot1qPortGvrpLastPduOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 6), MacAddress()).setMaxAccess("readonly")
dot1qPortVlanStatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6))
dot1qPortVlanStatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qTpVlanPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 1), Counter32()).setMaxAccess("readonly")
dot1qTpVlanPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 2), Counter32()).setMaxAccess("readonly")
dot1qTpVlanPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 3), Counter32()).setMaxAccess("readonly")
dot1qTpVlanPortInOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 4), Counter32()).setMaxAccess("readonly")
dot1qTpVlanPortOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 5), Counter32()).setMaxAccess("readonly")
dot1qTpVlanPortInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 6), Counter32()).setMaxAccess("readonly")
dot1qPortVlanHCStatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7))
dot1qPortVlanHCStatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
dot1qTpVlanPortHCInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 1), Counter64()).setMaxAccess("readonly")
dot1qTpVlanPortHCOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 2), Counter64()).setMaxAccess("readonly")
dot1qTpVlanPortHCInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 3), Counter64()).setMaxAccess("readonly")
dot1qLearningConstraintsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8))
dot1qLearningConstraintsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1)).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qConstraintVlan"), (0, "Q-BRIDGE-MIB", "dot1qConstraintSet"))
dot1qConstraintVlan = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 1), VlanIndex()).setMaxAccess("noaccess")
dot1qConstraintSet = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
dot1qConstraintType = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("independent", 1), ("shared", 2), ))).setMaxAccess("readwrite")
dot1qConstraintStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 4), RowStatus()).setMaxAccess("readwrite")
dot1qConstraintSetDefault = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
dot1qConstraintTypeDefault = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("independent", 1), ("shared", 2), ))).setMaxAccess("readwrite")
qBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2))
qBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2, 1))
qBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2, 2))

# Augmentions
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
dot1dBasePortEntry.registerAugmentions(("Q-BRIDGE-MIB", "dot1qPortVlanEntry"))
apply(dot1qPortVlanEntry.setIndexNames, dot1dBasePortEntry.getIndexNames())

# Groups

qBridgeFdbUnicastGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 2)).setObjects(("Q-BRIDGE-MIB", "dot1qFdbDynamicCount"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"), ("Q-BRIDGE-MIB", "dot1qTpFdbPort"), )
qBridgePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 8)).setObjects(("Q-BRIDGE-MIB", "dot1qPortAcceptableFrameTypes"), ("Q-BRIDGE-MIB", "dot1qPortGvrpStatus"), ("Q-BRIDGE-MIB", "dot1qPortIngressFiltering"), ("Q-BRIDGE-MIB", "dot1qPortGvrpLastPduOrigin"), ("Q-BRIDGE-MIB", "dot1qPvid"), ("Q-BRIDGE-MIB", "dot1qPortGvrpFailedRegistrations"), )
qBridgeFdbStaticGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 5)).setObjects(("Q-BRIDGE-MIB", "dot1qStaticMulticastStatus"), ("Q-BRIDGE-MIB", "dot1qStaticUnicastStatus"), ("Q-BRIDGE-MIB", "dot1qStaticMulticastForbiddenEgressPorts"), ("Q-BRIDGE-MIB", "dot1qStaticUnicastAllowedToGoTo"), ("Q-BRIDGE-MIB", "dot1qStaticMulticastStaticEgressPorts"), )
qBridgeFdbMulticastGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 3)).setObjects(("Q-BRIDGE-MIB", "dot1qTpGroupEgressPorts"), ("Q-BRIDGE-MIB", "dot1qTpGroupLearnt"), )
qBridgeBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 1)).setObjects(("Q-BRIDGE-MIB", "dot1qNumVlans"), ("Q-BRIDGE-MIB", "dot1qVlanVersionNumber"), ("Q-BRIDGE-MIB", "dot1qGvrpStatus"), ("Q-BRIDGE-MIB", "dot1qMaxVlanId"), ("Q-BRIDGE-MIB", "dot1qMaxSupportedVlans"), )
qBridgeServiceRequirementsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 4)).setObjects(("Q-BRIDGE-MIB", "dot1qForwardUnregisteredStaticPorts"), ("Q-BRIDGE-MIB", "dot1qForwardAllForbiddenPorts"), ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredForbiddenPorts"), ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredPorts"), ("Q-BRIDGE-MIB", "dot1qForwardAllStaticPorts"), ("Q-BRIDGE-MIB", "dot1qForwardAllPorts"), )
qBridgeVlanStaticGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 7)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStaticName"), ("Q-BRIDGE-MIB", "dot1qNextFreeLocalVlanIndex"), ("Q-BRIDGE-MIB", "dot1qVlanForbiddenEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStaticUntaggedPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStaticEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStaticRowStatus"), )
qBridgeVlanStatisticsOverflowGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 10)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortOutOverflowFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowDiscards"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowFrames"), )
qBridgeLearningConstraintDefaultGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 13)).setObjects(("Q-BRIDGE-MIB", "dot1qConstraintSetDefault"), ("Q-BRIDGE-MIB", "dot1qConstraintTypeDefault"), )
qBridgeVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 6)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanNumDeletes"), ("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qVlanCurrentEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanFdbId"), ("Q-BRIDGE-MIB", "dot1qVlanCreationTime"), ("Q-BRIDGE-MIB", "dot1qVlanCurrentUntaggedPorts"), )
qBridgeLearningConstraintsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 12)).setObjects(("Q-BRIDGE-MIB", "dot1qConstraintType"), ("Q-BRIDGE-MIB", "dot1qConstraintStatus"), )
qBridgeVlanHCStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 11)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInDiscards"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCOutFrames"), )
qBridgeVlanStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 9)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortOutFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInDiscards"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInFrames"), )

# Exports

# Module identity
mibBuilder.exportSymbols("Q-BRIDGE-MIB", PYSNMP_MODULE_ID=qBridgeMIB)

# Types
mibBuilder.exportSymbols("Q-BRIDGE-MIB", PortList=PortList, VlanId=VlanId, VlanIndex=VlanIndex)

# Objects
mibBuilder.exportSymbols("Q-BRIDGE-MIB", qBridgeMIB=qBridgeMIB, qBridgeMIBObjects=qBridgeMIBObjects, dot1qBase=dot1qBase, dot1qVlanVersionNumber=dot1qVlanVersionNumber, dot1qMaxVlanId=dot1qMaxVlanId, dot1qMaxSupportedVlans=dot1qMaxSupportedVlans, dot1qNumVlans=dot1qNumVlans, dot1qGvrpStatus=dot1qGvrpStatus, dot1qTp=dot1qTp, dot1qFdbTable=dot1qFdbTable, dot1qFdbEntry=dot1qFdbEntry, dot1qFdbId=dot1qFdbId, dot1qFdbDynamicCount=dot1qFdbDynamicCount, dot1qTpFdbTable=dot1qTpFdbTable, dot1qTpFdbEntry=dot1qTpFdbEntry, dot1qTpFdbAddress=dot1qTpFdbAddress, dot1qTpFdbPort=dot1qTpFdbPort, dot1qTpFdbStatus=dot1qTpFdbStatus, dot1qTpGroupTable=dot1qTpGroupTable, dot1qTpGroupEntry=dot1qTpGroupEntry, dot1qTpGroupAddress=dot1qTpGroupAddress, dot1qTpGroupEgressPorts=dot1qTpGroupEgressPorts, dot1qTpGroupLearnt=dot1qTpGroupLearnt, dot1qForwardAllTable=dot1qForwardAllTable, dot1qForwardAllEntry=dot1qForwardAllEntry, dot1qForwardAllPorts=dot1qForwardAllPorts, dot1qForwardAllStaticPorts=dot1qForwardAllStaticPorts, dot1qForwardAllForbiddenPorts=dot1qForwardAllForbiddenPorts, dot1qForwardUnregisteredTable=dot1qForwardUnregisteredTable, dot1qForwardUnregisteredEntry=dot1qForwardUnregisteredEntry, dot1qForwardUnregisteredPorts=dot1qForwardUnregisteredPorts, dot1qForwardUnregisteredStaticPorts=dot1qForwardUnregisteredStaticPorts, dot1qForwardUnregisteredForbiddenPorts=dot1qForwardUnregisteredForbiddenPorts, dot1qStatic=dot1qStatic, dot1qStaticUnicastTable=dot1qStaticUnicastTable, dot1qStaticUnicastEntry=dot1qStaticUnicastEntry, dot1qStaticUnicastAddress=dot1qStaticUnicastAddress, dot1qStaticUnicastReceivePort=dot1qStaticUnicastReceivePort, dot1qStaticUnicastAllowedToGoTo=dot1qStaticUnicastAllowedToGoTo, dot1qStaticUnicastStatus=dot1qStaticUnicastStatus, dot1qStaticMulticastTable=dot1qStaticMulticastTable, dot1qStaticMulticastEntry=dot1qStaticMulticastEntry, dot1qStaticMulticastAddress=dot1qStaticMulticastAddress, dot1qStaticMulticastReceivePort=dot1qStaticMulticastReceivePort, dot1qStaticMulticastStaticEgressPorts=dot1qStaticMulticastStaticEgressPorts, dot1qStaticMulticastForbiddenEgressPorts=dot1qStaticMulticastForbiddenEgressPorts, dot1qStaticMulticastStatus=dot1qStaticMulticastStatus, dot1qVlan=dot1qVlan, dot1qVlanNumDeletes=dot1qVlanNumDeletes, dot1qVlanCurrentTable=dot1qVlanCurrentTable, dot1qVlanCurrentEntry=dot1qVlanCurrentEntry, dot1qVlanTimeMark=dot1qVlanTimeMark, dot1qVlanIndex=dot1qVlanIndex, dot1qVlanFdbId=dot1qVlanFdbId, dot1qVlanCurrentEgressPorts=dot1qVlanCurrentEgressPorts, dot1qVlanCurrentUntaggedPorts=dot1qVlanCurrentUntaggedPorts, dot1qVlanStatus=dot1qVlanStatus, dot1qVlanCreationTime=dot1qVlanCreationTime, dot1qVlanStaticTable=dot1qVlanStaticTable, dot1qVlanStaticEntry=dot1qVlanStaticEntry, dot1qVlanStaticName=dot1qVlanStaticName, dot1qVlanStaticEgressPorts=dot1qVlanStaticEgressPorts, dot1qVlanForbiddenEgressPorts=dot1qVlanForbiddenEgressPorts, dot1qVlanStaticUntaggedPorts=dot1qVlanStaticUntaggedPorts, dot1qVlanStaticRowStatus=dot1qVlanStaticRowStatus, dot1qNextFreeLocalVlanIndex=dot1qNextFreeLocalVlanIndex, dot1qPortVlanTable=dot1qPortVlanTable, dot1qPortVlanEntry=dot1qPortVlanEntry, dot1qPvid=dot1qPvid, dot1qPortAcceptableFrameTypes=dot1qPortAcceptableFrameTypes, dot1qPortIngressFiltering=dot1qPortIngressFiltering, dot1qPortGvrpStatus=dot1qPortGvrpStatus, dot1qPortGvrpFailedRegistrations=dot1qPortGvrpFailedRegistrations, dot1qPortGvrpLastPduOrigin=dot1qPortGvrpLastPduOrigin, dot1qPortVlanStatisticsTable=dot1qPortVlanStatisticsTable, dot1qPortVlanStatisticsEntry=dot1qPortVlanStatisticsEntry, dot1qTpVlanPortInFrames=dot1qTpVlanPortInFrames, dot1qTpVlanPortOutFrames=dot1qTpVlanPortOutFrames, dot1qTpVlanPortInDiscards=dot1qTpVlanPortInDiscards, dot1qTpVlanPortInOverflowFrames=dot1qTpVlanPortInOverflowFrames, dot1qTpVlanPortOutOverflowFrames=dot1qTpVlanPortOutOverflowFrames, dot1qTpVlanPortInOverflowDiscards=dot1qTpVlanPortInOverflowDiscards, dot1qPortVlanHCStatisticsTable=dot1qPortVlanHCStatisticsTable, dot1qPortVlanHCStatisticsEntry=dot1qPortVlanHCStatisticsEntry, dot1qTpVlanPortHCInFrames=dot1qTpVlanPortHCInFrames, dot1qTpVlanPortHCOutFrames=dot1qTpVlanPortHCOutFrames, dot1qTpVlanPortHCInDiscards=dot1qTpVlanPortHCInDiscards, dot1qLearningConstraintsTable=dot1qLearningConstraintsTable, dot1qLearningConstraintsEntry=dot1qLearningConstraintsEntry, dot1qConstraintVlan=dot1qConstraintVlan, dot1qConstraintSet=dot1qConstraintSet, dot1qConstraintType=dot1qConstraintType, dot1qConstraintStatus=dot1qConstraintStatus, dot1qConstraintSetDefault=dot1qConstraintSetDefault, dot1qConstraintTypeDefault=dot1qConstraintTypeDefault, qBridgeConformance=qBridgeConformance, qBridgeGroups=qBridgeGroups, qBridgeCompliances=qBridgeCompliances)

# Groups
mibBuilder.exportSymbols("Q-BRIDGE-MIB", qBridgeFdbUnicastGroup=qBridgeFdbUnicastGroup, qBridgePortGroup=qBridgePortGroup, qBridgeFdbStaticGroup=qBridgeFdbStaticGroup, qBridgeFdbMulticastGroup=qBridgeFdbMulticastGroup, qBridgeBaseGroup=qBridgeBaseGroup, qBridgeServiceRequirementsGroup=qBridgeServiceRequirementsGroup, qBridgeVlanStaticGroup=qBridgeVlanStaticGroup, qBridgeVlanStatisticsOverflowGroup=qBridgeVlanStatisticsOverflowGroup, qBridgeLearningConstraintDefaultGroup=qBridgeLearningConstraintDefaultGroup, qBridgeVlanGroup=qBridgeVlanGroup, qBridgeLearningConstraintsGroup=qBridgeLearningConstraintsGroup, qBridgeVlanHCStatisticsGroup=qBridgeVlanHCStatisticsGroup, qBridgeVlanStatisticsGroup=qBridgeVlanStatisticsGroup)
