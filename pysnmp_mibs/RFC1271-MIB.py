# PySNMP SMI module. Autogenerated from smidump -f python RFC1271-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:17 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Types

class EntryStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,4,)
    namedValues = namedval.NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4), )
    pass

class OwnerString(DisplayString):
    pass


# Objects

rmon = MibIdentifier((1, 3, 6, 1, 2, 1, 16))
statistics = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 1))
etherStatsTable = MibTable((1, 3, 6, 1, 2, 1, 16, 1, 1))
etherStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 1, 1, 1)).setIndexNames((0, "RFC1271-MIB", "etherStatsIndex"))
etherStatsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
etherStatsDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
etherStatsDropEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
etherStatsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
etherStatsPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
etherStatsBroadcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
etherStatsMulticastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
etherStatsCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
etherStatsUndersizePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
etherStatsOversizePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
etherStatsFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
etherStatsJabbers = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
etherStatsCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
etherStatsPkts64Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
etherStatsPkts65to127Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
etherStatsPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
etherStatsPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
etherStatsPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
etherStatsPkts1024to1518Octets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
etherStatsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 20), OwnerString()).setMaxAccess("readwrite")
etherStatsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 21), EntryStatus()).setMaxAccess("readwrite")
history = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 2))
historyControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 2, 1))
historyControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 2, 1, 1)).setIndexNames((0, "RFC1271-MIB", "historyControlIndex"))
historyControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
historyControlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
historyControlBucketsRequested = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(50)).setMaxAccess("readwrite")
historyControlBucketsGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
historyControlInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 3600)).clone(1800)).setMaxAccess("readwrite")
historyControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 6), OwnerString()).setMaxAccess("readwrite")
historyControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 7), EntryStatus()).setMaxAccess("readwrite")
etherHistoryTable = MibTable((1, 3, 6, 1, 2, 1, 16, 2, 2))
etherHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 2, 2, 1)).setIndexNames((0, "RFC1271-MIB", "etherHistoryIndex"), (0, "RFC1271-MIB", "etherHistorySampleIndex"))
etherHistoryIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
etherHistorySampleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
etherHistoryIntervalStart = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
etherHistoryDropEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
etherHistoryOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
etherHistoryPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
etherHistoryBroadcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
etherHistoryMulticastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
etherHistoryCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
etherHistoryUndersizePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
etherHistoryOversizePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
etherHistoryFragments = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
etherHistoryJabbers = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
etherHistoryCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
etherHistoryUtilization = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
alarm = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 3))
alarmTable = MibTable((1, 3, 6, 1, 2, 1, 16, 3, 1))
alarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 3, 1, 1)).setIndexNames((0, "RFC1271-MIB", "alarmIndex"))
alarmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
alarmInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
alarmVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
alarmSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("absoluteValue", 1), ("deltaValue", 2), ))).setMaxAccess("readwrite")
alarmValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
alarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3), ))).setMaxAccess("readwrite")
alarmRisingThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
alarmFallingThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
alarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
alarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
alarmOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 11), OwnerString()).setMaxAccess("readwrite")
alarmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 12), EntryStatus()).setMaxAccess("readwrite")
hosts = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 4))
hostControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 4, 1))
hostControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 4, 1, 1)).setIndexNames((0, "RFC1271-MIB", "hostControlIndex"))
hostControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostControlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
hostControlTableSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
hostControlLastDeleteTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
hostControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
hostControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 6), EntryStatus()).setMaxAccess("readwrite")
hostTable = MibTable((1, 3, 6, 1, 2, 1, 16, 4, 2))
hostEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 4, 2, 1)).setIndexNames((0, "RFC1271-MIB", "hostIndex"), (0, "RFC1271-MIB", "hostAddress"))
hostAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 1), OctetString()).setMaxAccess("readonly")
hostCreationOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 4), Counter32()).setMaxAccess("readonly")
hostOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 5), Counter32()).setMaxAccess("readonly")
hostInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 6), Counter32()).setMaxAccess("readonly")
hostOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 7), Counter32()).setMaxAccess("readonly")
hostOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 8), Counter32()).setMaxAccess("readonly")
hostOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 9), Counter32()).setMaxAccess("readonly")
hostOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 10), Counter32()).setMaxAccess("readonly")
hostTimeTable = MibTable((1, 3, 6, 1, 2, 1, 16, 4, 3))
hostTimeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 4, 3, 1)).setIndexNames((0, "RFC1271-MIB", "hostTimeIndex"), (0, "RFC1271-MIB", "hostTimeCreationOrder"))
hostTimeAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 1), OctetString()).setMaxAccess("readonly")
hostTimeCreationOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostTimeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostTimeInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 4), Counter32()).setMaxAccess("readonly")
hostTimeOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 5), Counter32()).setMaxAccess("readonly")
hostTimeInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 6), Counter32()).setMaxAccess("readonly")
hostTimeOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 7), Counter32()).setMaxAccess("readonly")
hostTimeOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 8), Counter32()).setMaxAccess("readonly")
hostTimeOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 9), Counter32()).setMaxAccess("readonly")
hostTimeOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 10), Counter32()).setMaxAccess("readonly")
hostTopN = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 5))
hostTopNControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 5, 1))
hostTopNControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 5, 1, 1)).setIndexNames((0, "RFC1271-MIB", "hostTopNControlIndex"))
hostTopNControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostTopNHostIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
hostTopNRateBase = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,2,4,6,1,3,7,)).subtype(namedValues=namedval.NamedValues(("hostTopNInPkts", 1), ("hostTopNOutPkts", 2), ("hostTopNInOctets", 3), ("hostTopNOutOctets", 4), ("hostTopNOutErrors", 5), ("hostTopNOutBroadcastPkts", 6), ("hostTopNOutMulticastPkts", 7), ))).setMaxAccess("readwrite")
hostTopNTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 4), Integer32().clone(0)).setMaxAccess("readwrite")
hostTopNDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 5), Integer32().clone(0)).setMaxAccess("readonly")
hostTopNRequestedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 6), Integer32().clone(10)).setMaxAccess("readwrite")
hostTopNGrantedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
hostTopNStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
hostTopNOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 9), OwnerString()).setMaxAccess("readwrite")
hostTopNStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 10), EntryStatus()).setMaxAccess("readwrite")
hostTopNTable = MibTable((1, 3, 6, 1, 2, 1, 16, 5, 2))
hostTopNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 5, 2, 1)).setIndexNames((0, "RFC1271-MIB", "hostTopNReport"), (0, "RFC1271-MIB", "hostTopNIndex"))
hostTopNReport = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostTopNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
hostTopNAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 3), OctetString()).setMaxAccess("readonly")
hostTopNRate = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
matrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 6))
matrixControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 6, 1))
matrixControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 6, 1, 1)).setIndexNames((0, "RFC1271-MIB", "matrixControlIndex"))
matrixControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
matrixControlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
matrixControlTableSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
matrixControlLastDeleteTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
matrixControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
matrixControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 6), EntryStatus()).setMaxAccess("readwrite")
matrixSDTable = MibTable((1, 3, 6, 1, 2, 1, 16, 6, 2))
matrixSDEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 6, 2, 1)).setIndexNames((0, "RFC1271-MIB", "matrixSDIndex"), (0, "RFC1271-MIB", "matrixSDSourceAddress"), (0, "RFC1271-MIB", "matrixSDDestAddress"))
matrixSDSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 1), OctetString()).setMaxAccess("readonly")
matrixSDDestAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 2), OctetString()).setMaxAccess("readonly")
matrixSDIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
matrixSDPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 4), Counter32()).setMaxAccess("readonly")
matrixSDOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 5), Counter32()).setMaxAccess("readonly")
matrixSDErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 6), Counter32()).setMaxAccess("readonly")
matrixDSTable = MibTable((1, 3, 6, 1, 2, 1, 16, 6, 3))
matrixDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 6, 3, 1)).setIndexNames((0, "RFC1271-MIB", "matrixDSIndex"), (0, "RFC1271-MIB", "matrixDSDestAddress"), (0, "RFC1271-MIB", "matrixDSSourceAddress"))
matrixDSSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 1), OctetString()).setMaxAccess("readonly")
matrixDSDestAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 2), OctetString()).setMaxAccess("readonly")
matrixDSIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
matrixDSPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 4), Counter32()).setMaxAccess("readonly")
matrixDSOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 5), Counter32()).setMaxAccess("readonly")
matrixDSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 6), Counter32()).setMaxAccess("readonly")
filter = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 7))
filterTable = MibTable((1, 3, 6, 1, 2, 1, 16, 7, 1))
filterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 7, 1, 1)).setIndexNames((0, "RFC1271-MIB", "filterIndex"))
filterIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
filterChannelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
filterPktDataOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 3), Integer32().clone(0)).setMaxAccess("readwrite")
filterPktData = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
filterPktDataMask = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
filterPktDataNotMask = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
filterPktStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
filterPktStatusMask = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
filterPktStatusNotMask = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
filterOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 10), OwnerString()).setMaxAccess("readwrite")
filterStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 11), EntryStatus()).setMaxAccess("readwrite")
channelTable = MibTable((1, 3, 6, 1, 2, 1, 16, 7, 2))
channelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 7, 2, 1)).setIndexNames((0, "RFC1271-MIB", "channelIndex"))
channelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
channelIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
channelAcceptType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("acceptMatched", 1), ("acceptFailed", 2), ))).setMaxAccess("readwrite")
channelDataControl = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("on", 1), ("off", 2), )).clone(2)).setMaxAccess("readwrite")
channelTurnOnEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
channelTurnOffEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
channelEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
channelEventStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("eventReady", 1), ("eventFired", 2), ("eventAlwaysReady", 3), )).clone(1)).setMaxAccess("readwrite")
channelMatches = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
channelDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 10), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
channelOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 11), OwnerString()).setMaxAccess("readwrite")
channelStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 12), EntryStatus()).setMaxAccess("readwrite")
capture = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 8))
bufferControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 8, 1))
bufferControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 8, 1, 1)).setIndexNames((0, "RFC1271-MIB", "bufferControlIndex"))
bufferControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
bufferControlChannelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
bufferControlFullStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("spaceAvailable", 1), ("full", 2), ))).setMaxAccess("readonly")
bufferControlFullAction = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("lockWhenFull", 1), ("wrapWhenFull", 2), ))).setMaxAccess("readwrite")
bufferControlCaptureSliceSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 5), Integer32().clone(100)).setMaxAccess("readwrite")
bufferControlDownloadSliceSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 6), Integer32().clone(100)).setMaxAccess("readwrite")
bufferControlDownloadOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 7), Integer32().clone(0)).setMaxAccess("readwrite")
bufferControlMaxOctetsRequested = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 8), Integer32().clone(-1)).setMaxAccess("readwrite")
bufferControlMaxOctetsGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 9), Integer32()).setMaxAccess("readonly")
bufferControlCapturedPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 10), Integer32()).setMaxAccess("readonly")
bufferControlTurnOnTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
bufferControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 12), OwnerString()).setMaxAccess("readwrite")
bufferControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 13), EntryStatus()).setMaxAccess("readwrite")
captureBufferTable = MibTable((1, 3, 6, 1, 2, 1, 16, 8, 2))
captureBufferEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 8, 2, 1)).setIndexNames((0, "RFC1271-MIB", "captureBufferControlIndex"), (0, "RFC1271-MIB", "captureBufferIndex"))
captureBufferControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
captureBufferIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 2), Integer32()).setMaxAccess("readonly")
captureBufferPacketID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 3), Integer32()).setMaxAccess("readonly")
captureBufferPacketData = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 4), OctetString()).setMaxAccess("readonly")
captureBufferPacketLength = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 5), Integer32()).setMaxAccess("readonly")
captureBufferPacketTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 6), Integer32()).setMaxAccess("readonly")
captureBufferPacketStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 7), Integer32()).setMaxAccess("readonly")
event = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 9))
eventTable = MibTable((1, 3, 6, 1, 2, 1, 16, 9, 1))
eventEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 9, 1, 1)).setIndexNames((0, "RFC1271-MIB", "eventIndex"))
eventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
eventDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
eventType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("log", 2), ("snmp-trap", 3), ("log-and-trap", 4), ))).setMaxAccess("readwrite")
eventCommunity = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
eventLastTimeSent = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
eventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 6), OwnerString()).setMaxAccess("readwrite")
eventStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 7), EntryStatus()).setMaxAccess("readwrite")
logTable = MibTable((1, 3, 6, 1, 2, 1, 16, 9, 2))
logEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 9, 2, 1)).setIndexNames((0, "RFC1271-MIB", "logEventIndex"), (0, "RFC1271-MIB", "logIndex"))
logEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
logIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 2), Integer32()).setMaxAccess("readonly")
logTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
logDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("RFC1271-MIB", EntryStatus=EntryStatus, OwnerString=OwnerString)

# Objects
mibBuilder.exportSymbols("RFC1271-MIB", rmon=rmon, statistics=statistics, etherStatsTable=etherStatsTable, etherStatsEntry=etherStatsEntry, etherStatsIndex=etherStatsIndex, etherStatsDataSource=etherStatsDataSource, etherStatsDropEvents=etherStatsDropEvents, etherStatsOctets=etherStatsOctets, etherStatsPkts=etherStatsPkts, etherStatsBroadcastPkts=etherStatsBroadcastPkts, etherStatsMulticastPkts=etherStatsMulticastPkts, etherStatsCRCAlignErrors=etherStatsCRCAlignErrors, etherStatsUndersizePkts=etherStatsUndersizePkts, etherStatsOversizePkts=etherStatsOversizePkts, etherStatsFragments=etherStatsFragments, etherStatsJabbers=etherStatsJabbers, etherStatsCollisions=etherStatsCollisions, etherStatsPkts64Octets=etherStatsPkts64Octets, etherStatsPkts65to127Octets=etherStatsPkts65to127Octets, etherStatsPkts128to255Octets=etherStatsPkts128to255Octets, etherStatsPkts256to511Octets=etherStatsPkts256to511Octets, etherStatsPkts512to1023Octets=etherStatsPkts512to1023Octets, etherStatsPkts1024to1518Octets=etherStatsPkts1024to1518Octets, etherStatsOwner=etherStatsOwner, etherStatsStatus=etherStatsStatus, history=history, historyControlTable=historyControlTable, historyControlEntry=historyControlEntry, historyControlIndex=historyControlIndex, historyControlDataSource=historyControlDataSource, historyControlBucketsRequested=historyControlBucketsRequested, historyControlBucketsGranted=historyControlBucketsGranted, historyControlInterval=historyControlInterval, historyControlOwner=historyControlOwner, historyControlStatus=historyControlStatus, etherHistoryTable=etherHistoryTable, etherHistoryEntry=etherHistoryEntry, etherHistoryIndex=etherHistoryIndex, etherHistorySampleIndex=etherHistorySampleIndex, etherHistoryIntervalStart=etherHistoryIntervalStart, etherHistoryDropEvents=etherHistoryDropEvents, etherHistoryOctets=etherHistoryOctets, etherHistoryPkts=etherHistoryPkts, etherHistoryBroadcastPkts=etherHistoryBroadcastPkts, etherHistoryMulticastPkts=etherHistoryMulticastPkts, etherHistoryCRCAlignErrors=etherHistoryCRCAlignErrors, etherHistoryUndersizePkts=etherHistoryUndersizePkts, etherHistoryOversizePkts=etherHistoryOversizePkts, etherHistoryFragments=etherHistoryFragments, etherHistoryJabbers=etherHistoryJabbers, etherHistoryCollisions=etherHistoryCollisions, etherHistoryUtilization=etherHistoryUtilization, alarm=alarm, alarmTable=alarmTable, alarmEntry=alarmEntry, alarmIndex=alarmIndex, alarmInterval=alarmInterval, alarmVariable=alarmVariable, alarmSampleType=alarmSampleType, alarmValue=alarmValue, alarmStartupAlarm=alarmStartupAlarm, alarmRisingThreshold=alarmRisingThreshold, alarmFallingThreshold=alarmFallingThreshold, alarmRisingEventIndex=alarmRisingEventIndex, alarmFallingEventIndex=alarmFallingEventIndex, alarmOwner=alarmOwner, alarmStatus=alarmStatus, hosts=hosts, hostControlTable=hostControlTable, hostControlEntry=hostControlEntry, hostControlIndex=hostControlIndex, hostControlDataSource=hostControlDataSource, hostControlTableSize=hostControlTableSize, hostControlLastDeleteTime=hostControlLastDeleteTime, hostControlOwner=hostControlOwner, hostControlStatus=hostControlStatus, hostTable=hostTable, hostEntry=hostEntry, hostAddress=hostAddress, hostCreationOrder=hostCreationOrder, hostIndex=hostIndex, hostInPkts=hostInPkts, hostOutPkts=hostOutPkts, hostInOctets=hostInOctets, hostOutOctets=hostOutOctets, hostOutErrors=hostOutErrors, hostOutBroadcastPkts=hostOutBroadcastPkts, hostOutMulticastPkts=hostOutMulticastPkts, hostTimeTable=hostTimeTable, hostTimeEntry=hostTimeEntry, hostTimeAddress=hostTimeAddress, hostTimeCreationOrder=hostTimeCreationOrder, hostTimeIndex=hostTimeIndex, hostTimeInPkts=hostTimeInPkts, hostTimeOutPkts=hostTimeOutPkts, hostTimeInOctets=hostTimeInOctets, hostTimeOutOctets=hostTimeOutOctets, hostTimeOutErrors=hostTimeOutErrors, hostTimeOutBroadcastPkts=hostTimeOutBroadcastPkts, hostTimeOutMulticastPkts=hostTimeOutMulticastPkts, hostTopN=hostTopN, hostTopNControlTable=hostTopNControlTable, hostTopNControlEntry=hostTopNControlEntry, hostTopNControlIndex=hostTopNControlIndex, hostTopNHostIndex=hostTopNHostIndex, hostTopNRateBase=hostTopNRateBase, hostTopNTimeRemaining=hostTopNTimeRemaining, hostTopNDuration=hostTopNDuration, hostTopNRequestedSize=hostTopNRequestedSize, hostTopNGrantedSize=hostTopNGrantedSize, hostTopNStartTime=hostTopNStartTime, hostTopNOwner=hostTopNOwner, hostTopNStatus=hostTopNStatus, hostTopNTable=hostTopNTable, hostTopNEntry=hostTopNEntry, hostTopNReport=hostTopNReport, hostTopNIndex=hostTopNIndex, hostTopNAddress=hostTopNAddress, hostTopNRate=hostTopNRate, matrix=matrix, matrixControlTable=matrixControlTable, matrixControlEntry=matrixControlEntry, matrixControlIndex=matrixControlIndex, matrixControlDataSource=matrixControlDataSource, matrixControlTableSize=matrixControlTableSize, matrixControlLastDeleteTime=matrixControlLastDeleteTime)
mibBuilder.exportSymbols("RFC1271-MIB", matrixControlOwner=matrixControlOwner, matrixControlStatus=matrixControlStatus, matrixSDTable=matrixSDTable, matrixSDEntry=matrixSDEntry, matrixSDSourceAddress=matrixSDSourceAddress, matrixSDDestAddress=matrixSDDestAddress, matrixSDIndex=matrixSDIndex, matrixSDPkts=matrixSDPkts, matrixSDOctets=matrixSDOctets, matrixSDErrors=matrixSDErrors, matrixDSTable=matrixDSTable, matrixDSEntry=matrixDSEntry, matrixDSSourceAddress=matrixDSSourceAddress, matrixDSDestAddress=matrixDSDestAddress, matrixDSIndex=matrixDSIndex, matrixDSPkts=matrixDSPkts, matrixDSOctets=matrixDSOctets, matrixDSErrors=matrixDSErrors, filter=filter, filterTable=filterTable, filterEntry=filterEntry, filterIndex=filterIndex, filterChannelIndex=filterChannelIndex, filterPktDataOffset=filterPktDataOffset, filterPktData=filterPktData, filterPktDataMask=filterPktDataMask, filterPktDataNotMask=filterPktDataNotMask, filterPktStatus=filterPktStatus, filterPktStatusMask=filterPktStatusMask, filterPktStatusNotMask=filterPktStatusNotMask, filterOwner=filterOwner, filterStatus=filterStatus, channelTable=channelTable, channelEntry=channelEntry, channelIndex=channelIndex, channelIfIndex=channelIfIndex, channelAcceptType=channelAcceptType, channelDataControl=channelDataControl, channelTurnOnEventIndex=channelTurnOnEventIndex, channelTurnOffEventIndex=channelTurnOffEventIndex, channelEventIndex=channelEventIndex, channelEventStatus=channelEventStatus, channelMatches=channelMatches, channelDescription=channelDescription, channelOwner=channelOwner, channelStatus=channelStatus, capture=capture, bufferControlTable=bufferControlTable, bufferControlEntry=bufferControlEntry, bufferControlIndex=bufferControlIndex, bufferControlChannelIndex=bufferControlChannelIndex, bufferControlFullStatus=bufferControlFullStatus, bufferControlFullAction=bufferControlFullAction, bufferControlCaptureSliceSize=bufferControlCaptureSliceSize, bufferControlDownloadSliceSize=bufferControlDownloadSliceSize, bufferControlDownloadOffset=bufferControlDownloadOffset, bufferControlMaxOctetsRequested=bufferControlMaxOctetsRequested, bufferControlMaxOctetsGranted=bufferControlMaxOctetsGranted, bufferControlCapturedPackets=bufferControlCapturedPackets, bufferControlTurnOnTime=bufferControlTurnOnTime, bufferControlOwner=bufferControlOwner, bufferControlStatus=bufferControlStatus, captureBufferTable=captureBufferTable, captureBufferEntry=captureBufferEntry, captureBufferControlIndex=captureBufferControlIndex, captureBufferIndex=captureBufferIndex, captureBufferPacketID=captureBufferPacketID, captureBufferPacketData=captureBufferPacketData, captureBufferPacketLength=captureBufferPacketLength, captureBufferPacketTime=captureBufferPacketTime, captureBufferPacketStatus=captureBufferPacketStatus, event=event, eventTable=eventTable, eventEntry=eventEntry, eventIndex=eventIndex, eventDescription=eventDescription, eventType=eventType, eventCommunity=eventCommunity, eventLastTimeSent=eventLastTimeSent, eventOwner=eventOwner, eventStatus=eventStatus, logTable=logTable, logEntry=logEntry, logEventIndex=logEventIndex, logIndex=logIndex, logTime=logTime, logDescription=logDescription)

