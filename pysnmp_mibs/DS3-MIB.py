# PySNMP SMI module. Autogenerated from smidump -f python DS3-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:25:57 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( PerfCurrentCount, PerfIntervalCount, PerfTotalCount, ) = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue")

# Objects

ds3 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 30)).setRevisions(("1998-08-01 21:30",))
dsx3ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 5))
dsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 5, 1)).setIndexNames((0, "DS3-MIB", "dsx3LineIndex"))
dsx3LineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
dsx3TimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
dsx3ValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
dsx3LineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,6,4,3,1,8,7,2,)).subtype(namedValues=namedval.NamedValues(("dsx3other", 1), ("dsx3M23", 2), ("dsx3SYNTRAN", 3), ("dsx3CbitParity", 4), ("dsx3ClearChannel", 5), ("e3other", 6), ("e3Framed", 7), ("e3Plcp", 8), ))).setMaxAccess("readwrite")
dsx3LineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("dsx3Other", 1), ("dsx3B3ZS", 2), ("e3HDB3", 3), ))).setMaxAccess("readwrite")
dsx3SendCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,6,3,4,5,1,)).subtype(namedValues=namedval.NamedValues(("dsx3SendNoCode", 1), ("dsx3SendLineCode", 2), ("dsx3SendPayloadCode", 3), ("dsx3SendResetCode", 4), ("dsx3SendDS1LoopCode", 5), ("dsx3SendTestPattern", 6), ))).setMaxAccess("readwrite")
dsx3CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 8), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
dsx3LoopbackConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,4,6,5,2,)).subtype(namedValues=namedval.NamedValues(("dsx3NoLoop", 1), ("dsx3PayloadLoop", 2), ("dsx3LineLoop", 3), ("dsx3OtherLoop", 4), ("dsx3InwardLoop", 5), ("dsx3DualLoop", 6), ))).setMaxAccess("readwrite")
dsx3LineStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
dsx3TransmitClockSource = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3), ))).setMaxAccess("readwrite")
dsx3InvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 12), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
dsx3LineLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 13), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 64000))).setMaxAccess("readwrite")
dsx3LineStatusLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 14), TimeStamp()).setMaxAccess("readonly")
dsx3LineStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 15), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readwrite")
dsx3LoopbackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 16), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
dsx3Channelization = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 17), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabledDs1", 2), ("enabledDs2", 3), ))).setMaxAccess("readwrite")
dsx3Ds1ForRemoteLoop = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 18), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 29))).setMaxAccess("readwrite")
dsx3CurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 6))
dsx3CurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 6, 1)).setIndexNames((0, "DS3-MIB", "dsx3CurrentIndex"))
dsx3CurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3CurrentPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 9), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 10), PerfCurrentCount()).setMaxAccess("readonly")
dsx3CurrentCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 11), PerfCurrentCount()).setMaxAccess("readonly")
dsx3IntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 7))
dsx3IntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 7, 1)).setIndexNames((0, "DS3-MIB", "dsx3IntervalIndex"), (0, "DS3-MIB", "dsx3IntervalNumber"))
dsx3IntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3IntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
dsx3IntervalPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 10), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 11), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 12), PerfIntervalCount()).setMaxAccess("readonly")
dsx3IntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 13), TruthValue()).setMaxAccess("readonly")
dsx3TotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 8))
dsx3TotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 8, 1)).setIndexNames((0, "DS3-MIB", "dsx3TotalIndex"))
dsx3TotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3TotalPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 5), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 6), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 7), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 8), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 9), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 10), PerfTotalCount()).setMaxAccess("readonly")
dsx3TotalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 11), PerfTotalCount()).setMaxAccess("readonly")
dsx3FarEndConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 9))
dsx3FarEndConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 9, 1)).setIndexNames((0, "DS3-MIB", "dsx3FarEndLineIndex"))
dsx3FarEndLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3FarEndEquipCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
dsx3FarEndLocationIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 11))).setMaxAccess("readwrite")
dsx3FarEndFrameIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
dsx3FarEndUnitCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
dsx3FarEndFacilityIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 38))).setMaxAccess("readwrite")
dsx3FarEndCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 10))
dsx3FarEndCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 10, 1)).setIndexNames((0, "DS3-MIB", "dsx3FarEndCurrentIndex"))
dsx3FarEndCurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3FarEndTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
dsx3FarEndValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
dsx3FarEndCurrentCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
dsx3FarEndCurrentCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
dsx3FarEndCurrentCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
dsx3FarEndCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
dsx3FarEndInvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
dsx3FarEndIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 11))
dsx3FarEndIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 11, 1)).setIndexNames((0, "DS3-MIB", "dsx3FarEndIntervalIndex"), (0, "DS3-MIB", "dsx3FarEndIntervalNumber"))
dsx3FarEndIntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3FarEndIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
dsx3FarEndIntervalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
dsx3FarEndIntervalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
dsx3FarEndIntervalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
dsx3FarEndIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
dsx3FarEndIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 7), TruthValue()).setMaxAccess("readonly")
dsx3FarEndTotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 12))
dsx3FarEndTotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 12, 1)).setIndexNames((0, "DS3-MIB", "dsx3FarEndTotalIndex"))
dsx3FarEndTotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dsx3FarEndTotalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
dsx3FarEndTotalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
dsx3FarEndTotalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
dsx3FarEndTotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 5), PerfTotalCount()).setMaxAccess("readonly")
dsx3FracTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 13))
dsx3FracEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 13, 1)).setIndexNames((0, "DS3-MIB", "dsx3FracIndex"), (0, "DS3-MIB", "dsx3FracNumber"))
dsx3FracIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
dsx3FracNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
dsx3FracIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite")
ds3Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14))
ds3Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14, 1))
ds3Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14, 2))
ds3Traps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 15))

# Augmentions

# Notifications

dsx3LineStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 10, 30, 15, 0, 1)).setObjects(("DS3-MIB", "dsx3LineStatusLastChange"), ("DS3-MIB", "dsx3LineStatus"), )

# Groups

ds3NearEndOptionalConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 5)).setObjects(("DS3-MIB", "dsx3LineStatusLastChange"), ("DS3-MIB", "dsx3LineStatusChangeTrapEnable"), )
ds3DeprecatedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 4)).setObjects(("DS3-MIB", "dsx3IfIndex"), ("DS3-MIB", "dsx3FracNumber"), ("DS3-MIB", "dsx3FracIfIndex"), ("DS3-MIB", "dsx3FracIndex"), )
ds3NearEndOptionalTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 6)).setObjects(("DS3-MIB", "dsx3LineStatusChange"), )
ds3FarEndGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 3)).setObjects(("DS3-MIB", "dsx3FarEndFacilityIDCode"), ("DS3-MIB", "dsx3FarEndFrameIDCode"), ("DS3-MIB", "dsx3FarEndTotalCCVs"), ("DS3-MIB", "dsx3FarEndCurrentCESs"), ("DS3-MIB", "dsx3FarEndCurrentUASs"), ("DS3-MIB", "dsx3FarEndTotalUASs"), ("DS3-MIB", "dsx3FarEndIntervalNumber"), ("DS3-MIB", "dsx3FarEndCurrentCCVs"), ("DS3-MIB", "dsx3FarEndEquipCode"), ("DS3-MIB", "dsx3FarEndInvalidIntervals"), ("DS3-MIB", "dsx3FarEndTimeElapsed"), ("DS3-MIB", "dsx3FarEndTotalCESs"), ("DS3-MIB", "dsx3FarEndIntervalCCVs"), ("DS3-MIB", "dsx3FarEndLineIndex"), ("DS3-MIB", "dsx3FarEndIntervalIndex"), ("DS3-MIB", "dsx3FarEndUnitCode"), ("DS3-MIB", "dsx3FarEndValidIntervals"), ("DS3-MIB", "dsx3FarEndCurrentCSESs"), ("DS3-MIB", "dsx3FarEndLocationIDCode"), ("DS3-MIB", "dsx3FarEndIntervalUASs"), ("DS3-MIB", "dsx3FarEndTotalIndex"), ("DS3-MIB", "dsx3FarEndTotalCSESs"), ("DS3-MIB", "dsx3FarEndIntervalValidData"), ("DS3-MIB", "dsx3FarEndCurrentIndex"), ("DS3-MIB", "dsx3FarEndIntervalCESs"), ("DS3-MIB", "dsx3FarEndIntervalCSESs"), )
ds3NearEndConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 1)).setObjects(("DS3-MIB", "dsx3InvalidIntervals"), ("DS3-MIB", "dsx3ValidIntervals"), ("DS3-MIB", "dsx3LoopbackStatus"), ("DS3-MIB", "dsx3LineStatus"), ("DS3-MIB", "dsx3LineLength"), ("DS3-MIB", "dsx3Ds1ForRemoteLoop"), ("DS3-MIB", "dsx3LineCoding"), ("DS3-MIB", "dsx3TransmitClockSource"), ("DS3-MIB", "dsx3Channelization"), ("DS3-MIB", "dsx3SendCode"), ("DS3-MIB", "dsx3LineIndex"), ("DS3-MIB", "dsx3TimeElapsed"), ("DS3-MIB", "dsx3CircuitIdentifier"), ("DS3-MIB", "dsx3LoopbackConfig"), ("DS3-MIB", "dsx3LineType"), )
ds3NearEndStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 2)).setObjects(("DS3-MIB", "dsx3IntervalCSESs"), ("DS3-MIB", "dsx3CurrentLCVs"), ("DS3-MIB", "dsx3CurrentPSESs"), ("DS3-MIB", "dsx3TotalCESs"), ("DS3-MIB", "dsx3IntervalNumber"), ("DS3-MIB", "dsx3TotalCCVs"), ("DS3-MIB", "dsx3CurrentSEFSs"), ("DS3-MIB", "dsx3TotalUASs"), ("DS3-MIB", "dsx3CurrentUASs"), ("DS3-MIB", "dsx3CurrentCESs"), ("DS3-MIB", "dsx3CurrentCSESs"), ("DS3-MIB", "dsx3TotalLESs"), ("DS3-MIB", "dsx3IntervalCCVs"), ("DS3-MIB", "dsx3TotalIndex"), ("DS3-MIB", "dsx3IntervalCESs"), ("DS3-MIB", "dsx3IntervalUASs"), ("DS3-MIB", "dsx3TotalCSESs"), ("DS3-MIB", "dsx3TotalPCVs"), ("DS3-MIB", "dsx3CurrentLESs"), ("DS3-MIB", "dsx3IntervalLESs"), ("DS3-MIB", "dsx3IntervalLCVs"), ("DS3-MIB", "dsx3CurrentIndex"), ("DS3-MIB", "dsx3IntervalPCVs"), ("DS3-MIB", "dsx3CurrentCCVs"), ("DS3-MIB", "dsx3IntervalIndex"), ("DS3-MIB", "dsx3TotalPESs"), ("DS3-MIB", "dsx3TotalSEFSs"), ("DS3-MIB", "dsx3TotalLCVs"), ("DS3-MIB", "dsx3IntervalValidData"), ("DS3-MIB", "dsx3IntervalPSESs"), ("DS3-MIB", "dsx3IntervalPESs"), ("DS3-MIB", "dsx3TotalPSESs"), ("DS3-MIB", "dsx3IntervalSEFSs"), ("DS3-MIB", "dsx3CurrentPCVs"), ("DS3-MIB", "dsx3CurrentPESs"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DS3-MIB", PYSNMP_MODULE_ID=ds3)

# Objects
mibBuilder.exportSymbols("DS3-MIB", ds3=ds3, dsx3ConfigTable=dsx3ConfigTable, dsx3ConfigEntry=dsx3ConfigEntry, dsx3LineIndex=dsx3LineIndex, dsx3IfIndex=dsx3IfIndex, dsx3TimeElapsed=dsx3TimeElapsed, dsx3ValidIntervals=dsx3ValidIntervals, dsx3LineType=dsx3LineType, dsx3LineCoding=dsx3LineCoding, dsx3SendCode=dsx3SendCode, dsx3CircuitIdentifier=dsx3CircuitIdentifier, dsx3LoopbackConfig=dsx3LoopbackConfig, dsx3LineStatus=dsx3LineStatus, dsx3TransmitClockSource=dsx3TransmitClockSource, dsx3InvalidIntervals=dsx3InvalidIntervals, dsx3LineLength=dsx3LineLength, dsx3LineStatusLastChange=dsx3LineStatusLastChange, dsx3LineStatusChangeTrapEnable=dsx3LineStatusChangeTrapEnable, dsx3LoopbackStatus=dsx3LoopbackStatus, dsx3Channelization=dsx3Channelization, dsx3Ds1ForRemoteLoop=dsx3Ds1ForRemoteLoop, dsx3CurrentTable=dsx3CurrentTable, dsx3CurrentEntry=dsx3CurrentEntry, dsx3CurrentIndex=dsx3CurrentIndex, dsx3CurrentPESs=dsx3CurrentPESs, dsx3CurrentPSESs=dsx3CurrentPSESs, dsx3CurrentSEFSs=dsx3CurrentSEFSs, dsx3CurrentUASs=dsx3CurrentUASs, dsx3CurrentLCVs=dsx3CurrentLCVs, dsx3CurrentPCVs=dsx3CurrentPCVs, dsx3CurrentLESs=dsx3CurrentLESs, dsx3CurrentCCVs=dsx3CurrentCCVs, dsx3CurrentCESs=dsx3CurrentCESs, dsx3CurrentCSESs=dsx3CurrentCSESs, dsx3IntervalTable=dsx3IntervalTable, dsx3IntervalEntry=dsx3IntervalEntry, dsx3IntervalIndex=dsx3IntervalIndex, dsx3IntervalNumber=dsx3IntervalNumber, dsx3IntervalPESs=dsx3IntervalPESs, dsx3IntervalPSESs=dsx3IntervalPSESs, dsx3IntervalSEFSs=dsx3IntervalSEFSs, dsx3IntervalUASs=dsx3IntervalUASs, dsx3IntervalLCVs=dsx3IntervalLCVs, dsx3IntervalPCVs=dsx3IntervalPCVs, dsx3IntervalLESs=dsx3IntervalLESs, dsx3IntervalCCVs=dsx3IntervalCCVs, dsx3IntervalCESs=dsx3IntervalCESs, dsx3IntervalCSESs=dsx3IntervalCSESs, dsx3IntervalValidData=dsx3IntervalValidData, dsx3TotalTable=dsx3TotalTable, dsx3TotalEntry=dsx3TotalEntry, dsx3TotalIndex=dsx3TotalIndex, dsx3TotalPESs=dsx3TotalPESs, dsx3TotalPSESs=dsx3TotalPSESs, dsx3TotalSEFSs=dsx3TotalSEFSs, dsx3TotalUASs=dsx3TotalUASs, dsx3TotalLCVs=dsx3TotalLCVs, dsx3TotalPCVs=dsx3TotalPCVs, dsx3TotalLESs=dsx3TotalLESs, dsx3TotalCCVs=dsx3TotalCCVs, dsx3TotalCESs=dsx3TotalCESs, dsx3TotalCSESs=dsx3TotalCSESs, dsx3FarEndConfigTable=dsx3FarEndConfigTable, dsx3FarEndConfigEntry=dsx3FarEndConfigEntry, dsx3FarEndLineIndex=dsx3FarEndLineIndex, dsx3FarEndEquipCode=dsx3FarEndEquipCode, dsx3FarEndLocationIDCode=dsx3FarEndLocationIDCode, dsx3FarEndFrameIDCode=dsx3FarEndFrameIDCode, dsx3FarEndUnitCode=dsx3FarEndUnitCode, dsx3FarEndFacilityIDCode=dsx3FarEndFacilityIDCode, dsx3FarEndCurrentTable=dsx3FarEndCurrentTable, dsx3FarEndCurrentEntry=dsx3FarEndCurrentEntry, dsx3FarEndCurrentIndex=dsx3FarEndCurrentIndex, dsx3FarEndTimeElapsed=dsx3FarEndTimeElapsed, dsx3FarEndValidIntervals=dsx3FarEndValidIntervals, dsx3FarEndCurrentCESs=dsx3FarEndCurrentCESs, dsx3FarEndCurrentCSESs=dsx3FarEndCurrentCSESs, dsx3FarEndCurrentCCVs=dsx3FarEndCurrentCCVs, dsx3FarEndCurrentUASs=dsx3FarEndCurrentUASs, dsx3FarEndInvalidIntervals=dsx3FarEndInvalidIntervals, dsx3FarEndIntervalTable=dsx3FarEndIntervalTable, dsx3FarEndIntervalEntry=dsx3FarEndIntervalEntry, dsx3FarEndIntervalIndex=dsx3FarEndIntervalIndex, dsx3FarEndIntervalNumber=dsx3FarEndIntervalNumber, dsx3FarEndIntervalCESs=dsx3FarEndIntervalCESs, dsx3FarEndIntervalCSESs=dsx3FarEndIntervalCSESs, dsx3FarEndIntervalCCVs=dsx3FarEndIntervalCCVs, dsx3FarEndIntervalUASs=dsx3FarEndIntervalUASs, dsx3FarEndIntervalValidData=dsx3FarEndIntervalValidData, dsx3FarEndTotalTable=dsx3FarEndTotalTable, dsx3FarEndTotalEntry=dsx3FarEndTotalEntry, dsx3FarEndTotalIndex=dsx3FarEndTotalIndex, dsx3FarEndTotalCESs=dsx3FarEndTotalCESs, dsx3FarEndTotalCSESs=dsx3FarEndTotalCSESs, dsx3FarEndTotalCCVs=dsx3FarEndTotalCCVs, dsx3FarEndTotalUASs=dsx3FarEndTotalUASs, dsx3FracTable=dsx3FracTable, dsx3FracEntry=dsx3FracEntry, dsx3FracIndex=dsx3FracIndex, dsx3FracNumber=dsx3FracNumber, dsx3FracIfIndex=dsx3FracIfIndex, ds3Conformance=ds3Conformance, ds3Groups=ds3Groups, ds3Compliances=ds3Compliances, ds3Traps=ds3Traps)

# Notifications
mibBuilder.exportSymbols("DS3-MIB", dsx3LineStatusChange=dsx3LineStatusChange)

# Groups
mibBuilder.exportSymbols("DS3-MIB", ds3NearEndOptionalConfigGroup=ds3NearEndOptionalConfigGroup, ds3DeprecatedGroup=ds3DeprecatedGroup, ds3NearEndOptionalTrapGroup=ds3NearEndOptionalTrapGroup, ds3FarEndGroup=ds3FarEndGroup, ds3NearEndConfigGroup=ds3NearEndConfigGroup, ds3NearEndStatisticsGroup=ds3NearEndStatisticsGroup)
