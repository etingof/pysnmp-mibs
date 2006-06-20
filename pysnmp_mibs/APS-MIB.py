# PySNMP SMI module. Autogenerated from smidump -f python APS-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:09:58 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( RowStatus, StorageType, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "TimeStamp")

# Types

class ApsControlCommand(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,)
    namedValues = namedval.NamedValues(("noCmd", 1), ("lockoutWorkingChannel", 2), ("clearLockoutWorkingChannel", 3), )
    pass

class ApsK1K2(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(2,2)
    pass

class ApsSwitchCommand(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(6,2,3,7,5,1,4,8,)
    namedValues = namedval.NamedValues(("noCmd", 1), ("clear", 2), ("lockoutOfProtection", 3), ("forcedSwitchWorkToProtect", 4), ("forcedSwitchProtectToWork", 5), ("manualSwitchWorkToProtect", 6), ("manualSwitchProtectToWork", 7), ("exercise", 8), )
    pass


# Objects

apsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 49)).setRevisions(("2003-02-28 00:00",))
apsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 1))
apsConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 1, 1))
apsConfigGroups = MibScalar((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
apsConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2))
apsConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1)).setIndexNames((1, "APS-MIB", "apsConfigName"))
apsConfigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
apsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
apsConfigMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,2,3,)).subtype(namedValues=namedval.NamedValues(("onePlusOne", 1), ("oneToN", 2), ("onePlusOneCompatible", 3), ("onePlusOneOptimized", 4), )).clone(1)).setMaxAccess("readcreate")
apsConfigRevert = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("nonrevertive", 1), ("revertive", 2), )).clone(1)).setMaxAccess("readcreate")
apsConfigDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("unidirectional", 1), ("bidirectional", 2), )).clone(1)).setMaxAccess("readcreate")
apsConfigExtraTraffic = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
apsConfigSdBerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(5, 9)).clone(5)).setMaxAccess("readcreate")
apsConfigSfBerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(3, 5)).clone(3)).setMaxAccess("readcreate")
apsConfigWaitToRestore = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 720)).clone(300)).setMaxAccess("readcreate")
apsConfigCreationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 10), TimeStamp()).setMaxAccess("readonly")
apsConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 11), StorageType()).setMaxAccess("readcreate")
apsStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 2))
apsStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1))
apsStatusK1K2Rcv = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 1), ApsK1K2()).setMaxAccess("readonly")
apsStatusK1K2Trans = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 2), ApsK1K2()).setMaxAccess("readonly")
apsStatusCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 3), Bits().subtype(namedValues=namedval.NamedValues(("modeMismatch", 0), ("channelMismatch", 1), ("psbf", 2), ("feplf", 3), ("extraTraffic", 4), ))).setMaxAccess("readonly")
apsStatusModeMismatches = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
apsStatusChannelMismatches = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
apsStatusPSBFs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
apsStatusFEPLFs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
apsStatusSwitchedChannel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
apsStatusDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 9), TimeStamp()).setMaxAccess("readonly")
apsMap = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 1, 3))
apsChanLTEs = MibScalar((1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
apsMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2))
apsMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
apsMapGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
apsMapChanNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 14))).setMaxAccess("readonly")
apsChanConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 4))
apsChanConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1)).setIndexNames((0, "APS-MIB", "apsChanConfigGroupName"), (0, "APS-MIB", "apsChanConfigNumber"))
apsChanConfigGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
apsChanConfigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 14))).setMaxAccess("noaccess")
apsChanConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
apsChanConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
apsChanConfigPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("low", 1), ("high", 2), )).clone(1)).setMaxAccess("readcreate")
apsChanConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 6), StorageType()).setMaxAccess("readcreate")
apsCommandTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 5))
apsCommandEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1)).setIndexNames((0, "APS-MIB", "apsChanConfigGroupName"), (0, "APS-MIB", "apsChanConfigNumber"))
apsCommandSwitch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1, 1), ApsSwitchCommand()).setMaxAccess("readwrite")
apsCommandControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1, 2), ApsControlCommand()).setMaxAccess("readwrite")
apsChanStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 49, 1, 6))
apsChanStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1))
apsChanStatusCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("lockedOut", 0), ("sd", 1), ("sf", 2), ("switched", 3), ("wtr", 4), ))).setMaxAccess("readonly")
apsChanStatusSignalDegrades = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
apsChanStatusSignalFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
apsChanStatusSwitchovers = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
apsChanStatusLastSwitchover = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 5), TimeStamp()).setMaxAccess("readonly")
apsChanStatusSwitchoverSeconds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
apsChanStatusDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 7), TimeStamp()).setMaxAccess("readonly")
apsNotificationEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 49, 1, 7), Bits().subtype(namedValues=namedval.NamedValues(("switchover", 0), ("modeMismatch", 1), ("channelMismatch", 2), ("psbf", 3), ("feplf", 4), )).clone(())).setMaxAccess("readwrite")
apsMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 2))
apsNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 2, 0))
apsMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 3))
apsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 3, 1))
apsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 49, 3, 2))

# Augmentions
apsConfigEntry.registerAugmentions(("APS-MIB", "apsStatusEntry"))
apply(apsStatusEntry.setIndexNames, apsConfigEntry.getIndexNames())
apsChanConfigEntry.registerAugmentions(("APS-MIB", "apsChanStatusEntry"))
apply(apsChanStatusEntry.setIndexNames, apsChanConfigEntry.getIndexNames())

# Notifications

apsEventFEPLF = NotificationType((1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 5)).setObjects(("APS-MIB", "apsStatusFEPLFs"), ("APS-MIB", "apsStatusCurrent"), )
apsEventSwitchover = NotificationType((1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 1)).setObjects(("APS-MIB", "apsChanStatusCurrent"), ("APS-MIB", "apsChanStatusSwitchovers"), )
apsEventModeMismatch = NotificationType((1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 2)).setObjects(("APS-MIB", "apsStatusModeMismatches"), ("APS-MIB", "apsStatusCurrent"), )
apsEventChannelMismatch = NotificationType((1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 3)).setObjects(("APS-MIB", "apsStatusCurrent"), ("APS-MIB", "apsStatusChannelMismatches"), )
apsEventPSBF = NotificationType((1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 4)).setObjects(("APS-MIB", "apsStatusPSBFs"), ("APS-MIB", "apsStatusCurrent"), )

# Groups

apsConfigGeneral = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 1)).setObjects(("APS-MIB", "apsConfigRowStatus"), ("APS-MIB", "apsConfigDirection"), ("APS-MIB", "apsConfigMode"), ("APS-MIB", "apsConfigSfBerThreshold"), ("APS-MIB", "apsConfigRevert"), ("APS-MIB", "apsConfigSdBerThreshold"), ("APS-MIB", "apsNotificationEnable"), ("APS-MIB", "apsConfigExtraTraffic"), ("APS-MIB", "apsConfigCreationTime"), ("APS-MIB", "apsConfigStorageType"), )
apsCommandOneToN = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 4)).setObjects(("APS-MIB", "apsCommandControl"), ("APS-MIB", "apsCommandSwitch"), )
apsConfigWtr = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 2)).setObjects(("APS-MIB", "apsConfigWaitToRestore"), )
apsStatusGeneral = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 5)).setObjects(("APS-MIB", "apsStatusK1K2Rcv"), ("APS-MIB", "apsStatusCurrent"), ("APS-MIB", "apsStatusSwitchedChannel"), ("APS-MIB", "apsStatusFEPLFs"), ("APS-MIB", "apsStatusModeMismatches"), ("APS-MIB", "apsStatusChannelMismatches"), ("APS-MIB", "apsStatusPSBFs"), ("APS-MIB", "apsStatusDiscontinuityTime"), ("APS-MIB", "apsStatusK1K2Trans"), )
apsCommandOnePlusOne = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 3)).setObjects(("APS-MIB", "apsCommandSwitch"), )
apsEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 10)).setObjects(("APS-MIB", "apsEventFEPLF"), ("APS-MIB", "apsEventSwitchover"), ("APS-MIB", "apsEventModeMismatch"), ("APS-MIB", "apsEventChannelMismatch"), ("APS-MIB", "apsEventPSBF"), )
apsChanOneToN = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 7)).setObjects(("APS-MIB", "apsChanConfigPriority"), )
apsMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 9)).setObjects(("APS-MIB", "apsMapChanNumber"), ("APS-MIB", "apsMapGroupName"), )
apsChanGeneral = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 6)).setObjects(("APS-MIB", "apsChanStatusSignalDegrades"), ("APS-MIB", "apsChanStatusCurrent"), ("APS-MIB", "apsChanStatusLastSwitchover"), ("APS-MIB", "apsChanStatusSwitchoverSeconds"), ("APS-MIB", "apsChanStatusDiscontinuityTime"), ("APS-MIB", "apsChanConfigIfIndex"), ("APS-MIB", "apsChanConfigStorageType"), ("APS-MIB", "apsChanConfigRowStatus"), ("APS-MIB", "apsChanStatusSwitchovers"), ("APS-MIB", "apsChanStatusSignalFailures"), )
apsTotalsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 8)).setObjects(("APS-MIB", "apsChanLTEs"), ("APS-MIB", "apsConfigGroups"), )

# Exports

# Module identity
mibBuilder.exportSymbols("APS-MIB", PYSNMP_MODULE_ID=apsMIB)

# Types
mibBuilder.exportSymbols("APS-MIB", ApsControlCommand=ApsControlCommand, ApsK1K2=ApsK1K2, ApsSwitchCommand=ApsSwitchCommand)

# Objects
mibBuilder.exportSymbols("APS-MIB", apsMIB=apsMIB, apsMIBObjects=apsMIBObjects, apsConfig=apsConfig, apsConfigGroups=apsConfigGroups, apsConfigTable=apsConfigTable, apsConfigEntry=apsConfigEntry, apsConfigName=apsConfigName, apsConfigRowStatus=apsConfigRowStatus, apsConfigMode=apsConfigMode, apsConfigRevert=apsConfigRevert, apsConfigDirection=apsConfigDirection, apsConfigExtraTraffic=apsConfigExtraTraffic, apsConfigSdBerThreshold=apsConfigSdBerThreshold, apsConfigSfBerThreshold=apsConfigSfBerThreshold, apsConfigWaitToRestore=apsConfigWaitToRestore, apsConfigCreationTime=apsConfigCreationTime, apsConfigStorageType=apsConfigStorageType, apsStatusTable=apsStatusTable, apsStatusEntry=apsStatusEntry, apsStatusK1K2Rcv=apsStatusK1K2Rcv, apsStatusK1K2Trans=apsStatusK1K2Trans, apsStatusCurrent=apsStatusCurrent, apsStatusModeMismatches=apsStatusModeMismatches, apsStatusChannelMismatches=apsStatusChannelMismatches, apsStatusPSBFs=apsStatusPSBFs, apsStatusFEPLFs=apsStatusFEPLFs, apsStatusSwitchedChannel=apsStatusSwitchedChannel, apsStatusDiscontinuityTime=apsStatusDiscontinuityTime, apsMap=apsMap, apsChanLTEs=apsChanLTEs, apsMapTable=apsMapTable, apsMapEntry=apsMapEntry, apsMapGroupName=apsMapGroupName, apsMapChanNumber=apsMapChanNumber, apsChanConfigTable=apsChanConfigTable, apsChanConfigEntry=apsChanConfigEntry, apsChanConfigGroupName=apsChanConfigGroupName, apsChanConfigNumber=apsChanConfigNumber, apsChanConfigRowStatus=apsChanConfigRowStatus, apsChanConfigIfIndex=apsChanConfigIfIndex, apsChanConfigPriority=apsChanConfigPriority, apsChanConfigStorageType=apsChanConfigStorageType, apsCommandTable=apsCommandTable, apsCommandEntry=apsCommandEntry, apsCommandSwitch=apsCommandSwitch, apsCommandControl=apsCommandControl, apsChanStatusTable=apsChanStatusTable, apsChanStatusEntry=apsChanStatusEntry, apsChanStatusCurrent=apsChanStatusCurrent, apsChanStatusSignalDegrades=apsChanStatusSignalDegrades, apsChanStatusSignalFailures=apsChanStatusSignalFailures, apsChanStatusSwitchovers=apsChanStatusSwitchovers, apsChanStatusLastSwitchover=apsChanStatusLastSwitchover, apsChanStatusSwitchoverSeconds=apsChanStatusSwitchoverSeconds, apsChanStatusDiscontinuityTime=apsChanStatusDiscontinuityTime, apsNotificationEnable=apsNotificationEnable, apsMIBNotifications=apsMIBNotifications, apsNotificationsPrefix=apsNotificationsPrefix, apsMIBConformance=apsMIBConformance, apsGroups=apsGroups, apsCompliances=apsCompliances)

# Notifications
mibBuilder.exportSymbols("APS-MIB", apsEventFEPLF=apsEventFEPLF, apsEventSwitchover=apsEventSwitchover, apsEventModeMismatch=apsEventModeMismatch, apsEventChannelMismatch=apsEventChannelMismatch, apsEventPSBF=apsEventPSBF)

# Groups
mibBuilder.exportSymbols("APS-MIB", apsConfigGeneral=apsConfigGeneral, apsCommandOneToN=apsCommandOneToN, apsConfigWtr=apsConfigWtr, apsStatusGeneral=apsStatusGeneral, apsCommandOnePlusOne=apsCommandOnePlusOne, apsEventGroup=apsEventGroup, apsChanOneToN=apsChanOneToN, apsMapGroup=apsMapGroup, apsChanGeneral=apsChanGeneral, apsTotalsGroup=apsTotalsGroup)
