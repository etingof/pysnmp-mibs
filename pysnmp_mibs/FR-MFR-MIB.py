# PySNMP SMI module. Autogenerated from smidump -f python FR-MFR-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:47 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( RowStatus, TextualConvention, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TestAndIncr")

# Types

class MfrBundleLinkState(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,5,4,1,6,7,2,8,)
    namedValues = namedval.NamedValues(("mfrBundleLinkStateAddSent", 1), ("mfrBundleLinkStateAddRx", 2), ("mfrBundleLinkStateAddAckRx", 3), ("mfrBundleLinkStateUp", 4), ("mfrBundleLinkStateIdlePending", 5), ("mfrBundleLinkStateIdle", 6), ("mfrBundleLinkStateDown", 7), ("mfrBundleLinkStateDownIdle", 8), )
    pass


# Objects

mfrMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 47))
mfrMibScalarObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 1))
mfrBundleMaxNumBundles = MibVariable((1, 3, 6, 1, 2, 1, 10, 47, 1, 1), Integer32()).setMaxAccess("readonly")
mfrBundleNextIndex = MibVariable((1, 3, 6, 1, 2, 1, 10, 47, 1, 2), TestAndIncr()).setMaxAccess("readwrite")
mfrMibBundleObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 2))
mfrBundleTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 2, 3))
mfrBundleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1)).setIndexNames((0, "FR-MFR-MIB", "mfrBundleIndex"))
mfrBundleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
mfrBundleIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
mfrBundleRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 3)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mfrBundleNearEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 4)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readwrite"))
mfrBundleFragmentation = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("enable", 1), ("disable", 2), )).clone(2)).setMaxAccess("readwrite"))
mfrBundleMaxFragSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 8184)).clone(-1)).setMaxAccess("readwrite"))
mfrBundleTimerHello = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 180)).clone(10)).setMaxAccess("readwrite"))
mfrBundleTimerAck = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 10)).clone(4)).setMaxAccess("readwrite"))
mfrBundleCountMaxRetry = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 9)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 5)).clone(2)).setMaxAccess("readwrite"))
mfrBundleActivationClass = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 10)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("mfrBundleActivationClassA", 1), ("mfrBundleActivationClassB", 2), ("mfrBundleActivationClassC", 3), ("mfrBundleActivationClassD", 4), )).clone(1)).setMaxAccess("readwrite"))
mfrBundleThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 11)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L)).clone(-1)).setMaxAccess("readwrite"))
mfrBundleMaxDiffDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 12)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L)).clone(-1)).setMaxAccess("readwrite"))
mfrBundleSeqNumSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 13)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("seqNumSize12bit", 1), ("seqNumSize24bit", 2), )).clone(1)).setMaxAccess("readwrite"))
mfrBundleMaxBundleLinks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 14)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
mfrBundleLinksConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 15)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
mfrBundleLinksActive = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 16)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly"))
mfrBundleBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 17)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mfrBundleFarEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 18)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
mfrBundleResequencingErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleIfIndexMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 2, 4))
mfrBundleIfIndexMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
mfrBundleIfIndexMappingIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
mfrMibBundleLinkObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 3))
mfrBundleLinkTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 3, 1))
mfrBundleLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
mfrBundleLinkRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mfrBundleLinkConfigBundleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite"))
mfrBundleLinkNearEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readwrite"))
mfrBundleLinkState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), MfrBundleLinkState()).setMaxAccess("readonly"))
mfrBundleLinkFarEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
mfrBundleLinkFarEndBundleName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
mfrBundleLinkDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly"))
mfrBundleLinkFramesControlTx = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkFramesControlRx = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkFramesControlInvalid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkTimerExpiredCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkLoopbackSuspected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkUnexpectedSequence = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrBundleLinkMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mfrMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 4))
mfrMibTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 4, 0))
mfrMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5))
mfrMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5, 1))
mfrMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5, 2))

# Augmentions

# Notifications

mfrMibTrapBundleLinkMismatch = NotificationType((1, 3, 6, 1, 2, 1, 10, 47, 4, 0, 1)).setObjects(("FR-MFR-MIB", "mfrBundleFarEndName"), ("FR-MFR-MIB", "mfrBundleLinkNearEndName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndName"), ("FR-MFR-MIB", "mfrBundleNearEndName"), )

# Groups

mfrMibBundleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 1)).setObjects(("FR-MFR-MIB", "mfrBundleBandwidth"), ("FR-MFR-MIB", "mfrBundleIfIndexMappingIndex"), ("FR-MFR-MIB", "mfrBundleThreshold"), ("FR-MFR-MIB", "mfrBundleFarEndName"), ("FR-MFR-MIB", "mfrBundleSeqNumSize"), ("FR-MFR-MIB", "mfrBundleRowStatus"), ("FR-MFR-MIB", "mfrBundleCountMaxRetry"), ("FR-MFR-MIB", "mfrBundleResequencingErrors"), ("FR-MFR-MIB", "mfrBundleLinksActive"), ("FR-MFR-MIB", "mfrBundleNearEndName"), ("FR-MFR-MIB", "mfrBundleMaxDiffDelay"), ("FR-MFR-MIB", "mfrBundleTimerAck"), ("FR-MFR-MIB", "mfrBundleTimerHello"), ("FR-MFR-MIB", "mfrBundleMaxNumBundles"), ("FR-MFR-MIB", "mfrBundleMaxFragSize"), ("FR-MFR-MIB", "mfrBundleActivationClass"), ("FR-MFR-MIB", "mfrBundleNextIndex"), ("FR-MFR-MIB", "mfrBundleLinksConfigured"), ("FR-MFR-MIB", "mfrBundleMaxBundleLinks"), ("FR-MFR-MIB", "mfrBundleIfIndex"), ("FR-MFR-MIB", "mfrBundleFragmentation"), )
mfrMibTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 3)).setObjects(("FR-MFR-MIB", "mfrMibTrapBundleLinkMismatch"), )
mfrMibBundleLinkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 2)).setObjects(("FR-MFR-MIB", "mfrBundleLinkLoopbackSuspected"), ("FR-MFR-MIB", "mfrBundleLinkRowStatus"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlInvalid"), ("FR-MFR-MIB", "mfrBundleLinkNearEndName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"), ("FR-MFR-MIB", "mfrBundleLinkDelay"), ("FR-MFR-MIB", "mfrBundleLinkUnexpectedSequence"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlTx"), ("FR-MFR-MIB", "mfrBundleLinkMismatch"), ("FR-MFR-MIB", "mfrBundleLinkConfigBundleIndex"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlRx"), ("FR-MFR-MIB", "mfrBundleLinkFarEndName"), ("FR-MFR-MIB", "mfrBundleLinkState"), ("FR-MFR-MIB", "mfrBundleLinkTimerExpiredCount"), )

# Exports

# Types
mibBuilder.exportSymbols("FR-MFR-MIB", MfrBundleLinkState=MfrBundleLinkState)

# Objects
mibBuilder.exportSymbols("FR-MFR-MIB", mfrMib=mfrMib, mfrMibScalarObjects=mfrMibScalarObjects, mfrBundleMaxNumBundles=mfrBundleMaxNumBundles, mfrBundleNextIndex=mfrBundleNextIndex, mfrMibBundleObjects=mfrMibBundleObjects, mfrBundleTable=mfrBundleTable, mfrBundleEntry=mfrBundleEntry, mfrBundleIndex=mfrBundleIndex, mfrBundleIfIndex=mfrBundleIfIndex, mfrBundleRowStatus=mfrBundleRowStatus, mfrBundleNearEndName=mfrBundleNearEndName, mfrBundleFragmentation=mfrBundleFragmentation, mfrBundleMaxFragSize=mfrBundleMaxFragSize, mfrBundleTimerHello=mfrBundleTimerHello, mfrBundleTimerAck=mfrBundleTimerAck, mfrBundleCountMaxRetry=mfrBundleCountMaxRetry, mfrBundleActivationClass=mfrBundleActivationClass, mfrBundleThreshold=mfrBundleThreshold, mfrBundleMaxDiffDelay=mfrBundleMaxDiffDelay, mfrBundleSeqNumSize=mfrBundleSeqNumSize, mfrBundleMaxBundleLinks=mfrBundleMaxBundleLinks, mfrBundleLinksConfigured=mfrBundleLinksConfigured, mfrBundleLinksActive=mfrBundleLinksActive, mfrBundleBandwidth=mfrBundleBandwidth, mfrBundleFarEndName=mfrBundleFarEndName, mfrBundleResequencingErrors=mfrBundleResequencingErrors, mfrBundleIfIndexMappingTable=mfrBundleIfIndexMappingTable, mfrBundleIfIndexMappingEntry=mfrBundleIfIndexMappingEntry, mfrBundleIfIndexMappingIndex=mfrBundleIfIndexMappingIndex, mfrMibBundleLinkObjects=mfrMibBundleLinkObjects, mfrBundleLinkTable=mfrBundleLinkTable, mfrBundleLinkEntry=mfrBundleLinkEntry, mfrBundleLinkRowStatus=mfrBundleLinkRowStatus, mfrBundleLinkConfigBundleIndex=mfrBundleLinkConfigBundleIndex, mfrBundleLinkNearEndName=mfrBundleLinkNearEndName, mfrBundleLinkState=mfrBundleLinkState, mfrBundleLinkFarEndName=mfrBundleLinkFarEndName, mfrBundleLinkFarEndBundleName=mfrBundleLinkFarEndBundleName, mfrBundleLinkDelay=mfrBundleLinkDelay, mfrBundleLinkFramesControlTx=mfrBundleLinkFramesControlTx, mfrBundleLinkFramesControlRx=mfrBundleLinkFramesControlRx, mfrBundleLinkFramesControlInvalid=mfrBundleLinkFramesControlInvalid, mfrBundleLinkTimerExpiredCount=mfrBundleLinkTimerExpiredCount, mfrBundleLinkLoopbackSuspected=mfrBundleLinkLoopbackSuspected, mfrBundleLinkUnexpectedSequence=mfrBundleLinkUnexpectedSequence, mfrBundleLinkMismatch=mfrBundleLinkMismatch, mfrMibTraps=mfrMibTraps, mfrMibTrapsPrefix=mfrMibTrapsPrefix, mfrMibConformance=mfrMibConformance, mfrMibGroups=mfrMibGroups, mfrMibCompliances=mfrMibCompliances)

# Notifications
mibBuilder.exportSymbols("FR-MFR-MIB", mfrMibTrapBundleLinkMismatch=mfrMibTrapBundleLinkMismatch)

# Groups
mibBuilder.exportSymbols("FR-MFR-MIB", mfrMibBundleGroup=mfrMibBundleGroup, mfrMibTrapGroup=mfrMibTrapGroup, mfrMibBundleLinkGroup=mfrMibBundleLinkGroup)