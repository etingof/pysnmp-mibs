# PySNMP SMI module. Autogenerated from smidump -f python DOCS-IF-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:43 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndexOrZero, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "transmission")
( MacAddress, RowStatus, TextualConvention, TimeInterval, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TimeInterval", "TimeStamp", "TruthValue")

# Types

class TenthdB(TextualConvention, Integer32):
    pass

class TenthdBmV(TextualConvention, Integer32):
    pass


# Objects

docsIfMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 127))
docsIfMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 1))
docsIfBaseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 1, 1))
docsIfDownstreamChannelTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1))
docsIfDownstreamChannelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfDownChannelId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly"))
docsIfDownChannelFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite"))
docsIfDownChannelWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16000000))).setMaxAccess("readwrite"))
docsIfDownChannelModulation = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,2,3,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("other", 2), ("qam64", 3), ("qam256", 4), ))).setMaxAccess("readwrite"))
docsIfDownChannelInterleave = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,1,3,2,5,6,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("other", 2), ("taps8Increment16", 3), ("taps16Increment8", 4), ("taps32Increment4", 5), ("taps64Increment2", 6), ("taps128Increment1", 7), ))).setMaxAccess("readwrite"))
docsIfDownChannelPower = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), TenthdBmV()).setMaxAccess("readwrite"))
docsIfUpstreamChannelTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2))
docsIfUpstreamChannelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfUpChannelId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly"))
docsIfUpChannelFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite"))
docsIfUpChannelWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 20000000))).setMaxAccess("readwrite"))
docsIfUpChannelModulationProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
docsIfUpChannelSlotSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
docsIfUpChannelTxTimingOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
docsIfUpChannelRangingBackoffStart = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readwrite"))
docsIfUpChannelRangingBackoffEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readwrite"))
docsIfUpChannelTxBackoffStart = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readwrite"))
docsIfUpChannelTxBackoffEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readwrite"))
docsIfQosProfileTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3))
docsIfQosProfileEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1)).setIndexNames((0, "DOCS-IF-MIB", "docsIfQosProfIndex"))
docsIfQosProfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16383))).setMaxAccess("noaccess"))
docsIfQosProfPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7)).clone(0)).setMaxAccess("readwrite"))
docsIfQosProfMaxUpBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 100000000)).clone(0)).setMaxAccess("readwrite"))
docsIfQosProfGuarUpBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 100000000)).clone(0)).setMaxAccess("readwrite"))
docsIfQosProfMaxDownBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 100000000)).clone(0)).setMaxAccess("readwrite"))
docsIfQosProfMaxTxBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readwrite"))
docsIfQosProfBaselinePrivacy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 7)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
docsIfQosProfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 3, 1, 8)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
docsIfSignalQualityTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4))
docsIfSignalQualityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfSigQIncludesContention = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
docsIfSigQUnerroreds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfSigQCorrecteds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfSigQUncorrectables = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 5)).setColumnInitializer(MibVariable((), TenthdB()).setMaxAccess("readonly"))
docsIfSigQMicroreflections = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly"))
docsIfSigQEqualizationData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 1, 4, 1, 7)).setColumnInitializer(MibVariable((), OctetString()).setMaxAccess("readonly"))
docsIfCmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 1, 2))
docsIfCmMacTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1))
docsIfCmMacEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfCmCmtsAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), MacAddress()).setMaxAccess("readonly"))
docsIfCmCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Bits().subtype(namedValues=namedval.NamedValues(("atmCells", 0), ("concatenation", 1), ))).setMaxAccess("readonly"))
docsIfCmRangingRespTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readwrite"))
docsIfCmRangingTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
docsIfCmStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2))
docsIfCmStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfCmStatusValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,4,3,8,5,12,2,1,10,6,13,11,9,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("paramTransferComplete", 10), ("registrationComplete", 11), ("operational", 12), ("accessDenied", 13), ("notReady", 2), ("notSynchronized", 3), ("phySynchronized", 4), ("usParametersAcquired", 5), ("rangingComplete", 6), ("ipComplete", 7), ("todEstablished", 8), ("securityEstablished", 9), ))).setMaxAccess("readonly"))
docsIfCmStatusCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 2)).setColumnInitializer(MibVariable((), OctetString()).setMaxAccess("readonly"))
docsIfCmStatusTxPower = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 3)).setColumnInitializer(MibVariable((), TenthdBmV()).setMaxAccess("readonly"))
docsIfCmStatusResets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusLostSyncs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusInvalidMaps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusInvalidUcds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusInvalidRangingResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusInvalidRegistrationResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusT1Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusT2Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusT3Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusT4Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmStatusRangingAborteds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 2, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3))
docsIfCmServiceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-IF-MIB", "docsIfCmServiceId"))
docsIfCmServiceId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16383))).setMaxAccess("noaccess"))
docsIfCmServiceQosProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16383))).setMaxAccess("readonly"))
docsIfCmServiceTxSlotsImmed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceTxSlotsDed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceTxRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceTxExceededs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceRqRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmServiceRqExceededs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 2, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 1, 3))
docsIfCmtsMacTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1))
docsIfCmtsMacEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfCmtsCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), Bits().subtype(namedValues=namedval.NamedValues(("atmCells", 0), ("concatenation", 1), ))).setMaxAccess("readonly"))
docsIfCmtsSyncInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 200))).setMaxAccess("readwrite"))
docsIfCmtsUcdInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2000))).setMaxAccess("readwrite"))
docsIfCmtsMaxServiceIds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16383))).setMaxAccess("readonly"))
docsIfCmtsInsertionInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readwrite"))
docsIfCmtsInvitedRangingAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite"))
docsIfCmtsInsertInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
docsIfCmtsStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2))
docsIfCmtsStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsIfCmtsStatusInvalidRangeReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsStatusRangingAborteds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsStatusInvalidRegReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsStatusFailedRegReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsStatusInvalidDataReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsStatusT5Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 2, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsCmStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3))
docsIfCmtsCmStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1)).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"))
docsIfCmtsCmStatusIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
docsIfCmtsCmStatusMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 2)).setColumnInitializer(MibVariable((), MacAddress()).setMaxAccess("readonly"))
docsIfCmtsCmStatusIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
docsIfCmtsCmStatusDownChannelIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 4)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readonly"))
docsIfCmtsCmStatusUpChannelIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 5)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readonly"))
docsIfCmtsCmStatusRxPower = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 6)).setColumnInitializer(MibVariable((), TenthdBmV()).setMaxAccess("readonly"))
docsIfCmtsCmStatusTimingOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 7)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
docsIfCmtsCmStatusEqualizationData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 8)).setColumnInitializer(MibVariable((), OctetString()).setMaxAccess("readonly"))
docsIfCmtsCmStatusValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,5,1,4,3,6,7,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ranging", 2), ("rangingAborted", 3), ("rangingComplete", 4), ("ipComplete", 5), ("registrationComplete", 6), ("accessDenied", 7), ))).setMaxAccess("readonly"))
docsIfCmtsCmStatusUnerroreds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsCmStatusCorrecteds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsCmStatusUncorrectables = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsCmStatusSignalNoise = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 13)).setColumnInitializer(MibVariable((), TenthdB()).setMaxAccess("readonly"))
docsIfCmtsCmStatusMicroreflections = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 3, 1, 14)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly"))
docsIfCmtsServiceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4))
docsIfCmtsServiceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-IF-MIB", "docsIfCmtsServiceId"))
docsIfCmtsServiceId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16383))).setMaxAccess("noaccess"))
docsIfCmtsServiceCmStatusIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
docsIfCmtsServiceAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("destroyed", 3), ))).setMaxAccess("readwrite"))
docsIfCmtsServiceQosProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 4)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16383))).setMaxAccess("readonly"))
docsIfCmtsServiceCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 5)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
docsIfCmtsServiceInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsServiceInPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 4, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
docsIfCmtsModulationTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5))
docsIfCmtsModulationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1)).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsModIndex"), (0, "DOCS-IF-MIB", "docsIfCmtsModIntervalUsageCode"))
docsIfCmtsModIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
docsIfCmtsModIntervalUsageCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,6,1,2,4,5,)).subtype(namedValues=namedval.NamedValues(("request", 1), ("requestData", 2), ("initialRanging", 3), ("periodicRanging", 4), ("shortData", 5), ("longData", 6), ))).setMaxAccess("noaccess"))
docsIfCmtsModControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 3)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
docsIfCmtsModType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("qpsk", 2), ("qam16", 3), )).clone(2)).setMaxAccess("readwrite"))
docsIfCmtsModPreambleLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 5)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite"))
docsIfCmtsModDifferentialEncoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 6)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
docsIfCmtsModFECErrorCorrection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 10)).clone(0)).setMaxAccess("readwrite"))
docsIfCmtsModFECCodewordLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255)).clone(32)).setMaxAccess("readwrite"))
docsIfCmtsModScramblerSeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 9)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 32767)).clone(0)).setMaxAccess("readwrite"))
docsIfCmtsModMaxBurstSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 10)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readwrite"))
docsIfCmtsModGuardTimeSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 11)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
docsIfCmtsModLastCodewordShortened = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 12)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
docsIfCmtsModScrambler = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 5, 1, 13)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
docsIfCmtsQosProfilePermissions = MibVariable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 6), Bits().subtype(namedValues=namedval.NamedValues(("createByManagement", 0), ("updateByManagement", 1), ("createByModems", 2), ))).setMaxAccess("readwrite")
docsIfCmtsMacToCmTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7))
docsIfCmtsMacToCmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1)).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmMac"))
docsIfCmtsCmMac = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1, 1)).setColumnInitializer(MibVariable((), MacAddress()).setMaxAccess("noaccess"))
docsIfCmtsCmPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 1, 3, 7, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
docsIfNotification = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 2))
docsIfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 3))
docsIfCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 3, 1))
docsIfGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 3, 2))

# Augmentions

# Groups

docsIfCmtsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 3)).setObjects(("DOCS-IF-MIB", "docsIfCmtsStatusInvalidRegReqs"), ("DOCS-IF-MIB", "docsIfCmtsStatusInvalidDataReqs"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusRxPower"), ("DOCS-IF-MIB", "docsIfCmtsServiceInPackets"), ("DOCS-IF-MIB", "docsIfCmtsServiceAdminStatus"), ("DOCS-IF-MIB", "docsIfCmtsModFECErrorCorrection"), ("DOCS-IF-MIB", "docsIfCmtsSyncInterval"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusTimingOffset"), ("DOCS-IF-MIB", "docsIfCmtsServiceQosProfile"), ("DOCS-IF-MIB", "docsIfCmtsStatusFailedRegReqs"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusEqualizationData"), ("DOCS-IF-MIB", "docsIfCmtsModScramblerSeed"), ("DOCS-IF-MIB", "docsIfCmtsModType"), ("DOCS-IF-MIB", "docsIfCmtsStatusInvalidRangeReqs"), ("DOCS-IF-MIB", "docsIfCmtsModFECCodewordLength"), ("DOCS-IF-MIB", "docsIfCmtsModScrambler"), ("DOCS-IF-MIB", "docsIfCmtsModGuardTimeSize"), ("DOCS-IF-MIB", "docsIfCmtsCapabilities"), ("DOCS-IF-MIB", "docsIfCmtsCmPtr"), ("DOCS-IF-MIB", "docsIfCmtsModDifferentialEncoding"), ("DOCS-IF-MIB", "docsIfCmtsModLastCodewordShortened"), ("DOCS-IF-MIB", "docsIfCmtsModPreambleLen"), ("DOCS-IF-MIB", "docsIfCmtsMaxServiceIds"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"), ("DOCS-IF-MIB", "docsIfCmtsQosProfilePermissions"), ("DOCS-IF-MIB", "docsIfCmtsInvitedRangingAttempts"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusCorrecteds"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusUnerroreds"), ("DOCS-IF-MIB", "docsIfCmtsUcdInterval"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusUncorrectables"), ("DOCS-IF-MIB", "docsIfCmtsServiceInOctets"), ("DOCS-IF-MIB", "docsIfCmtsServiceCmStatusIndex"), ("DOCS-IF-MIB", "docsIfCmtsStatusRangingAborteds"), ("DOCS-IF-MIB", "docsIfCmtsServiceCreateTime"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusIpAddress"), ("DOCS-IF-MIB", "docsIfCmtsModMaxBurstSize"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMicroreflections"), ("DOCS-IF-MIB", "docsIfCmtsStatusT5Timeouts"), ("DOCS-IF-MIB", "docsIfCmtsModControl"), ("DOCS-IF-MIB", "docsIfCmtsInsertInterval"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusSignalNoise"), )
docsIfCmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 2)).setObjects(("DOCS-IF-MIB", "docsIfCmServiceTxRetries"), ("DOCS-IF-MIB", "docsIfCmServiceTxSlotsImmed"), ("DOCS-IF-MIB", "docsIfCmStatusT3Timeouts"), ("DOCS-IF-MIB", "docsIfCmStatusT1Timeouts"), ("DOCS-IF-MIB", "docsIfCmStatusInvalidUcds"), ("DOCS-IF-MIB", "docsIfCmStatusValue"), ("DOCS-IF-MIB", "docsIfCmStatusInvalidRangingResponses"), ("DOCS-IF-MIB", "docsIfCmStatusRangingAborteds"), ("DOCS-IF-MIB", "docsIfCmCapabilities"), ("DOCS-IF-MIB", "docsIfCmStatusCode"), ("DOCS-IF-MIB", "docsIfCmServiceRqRetries"), ("DOCS-IF-MIB", "docsIfCmServiceTxExceededs"), ("DOCS-IF-MIB", "docsIfCmServiceRqExceededs"), ("DOCS-IF-MIB", "docsIfCmStatusT4Timeouts"), ("DOCS-IF-MIB", "docsIfCmStatusResets"), ("DOCS-IF-MIB", "docsIfCmStatusLostSyncs"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-IF-MIB", "docsIfCmServiceQosProfile"), ("DOCS-IF-MIB", "docsIfCmRangingTimeout"), ("DOCS-IF-MIB", "docsIfCmStatusTxPower"), ("DOCS-IF-MIB", "docsIfCmStatusT2Timeouts"), ("DOCS-IF-MIB", "docsIfCmServiceTxSlotsDed"), ("DOCS-IF-MIB", "docsIfCmStatusInvalidMaps"), ("DOCS-IF-MIB", "docsIfCmStatusInvalidRegistrationResponses"), )
docsIfObsoleteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 4)).setObjects(("DOCS-IF-MIB", "docsIfCmtsInsertionInterval"), ("DOCS-IF-MIB", "docsIfCmRangingRespTimeout"), )
docsIfBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 3, 2, 1)).setObjects(("DOCS-IF-MIB", "docsIfQosProfStatus"), ("DOCS-IF-MIB", "docsIfSigQSignalNoise"), ("DOCS-IF-MIB", "docsIfUpChannelSlotSize"), ("DOCS-IF-MIB", "docsIfQosProfPriority"), ("DOCS-IF-MIB", "docsIfQosProfMaxUpBandwidth"), ("DOCS-IF-MIB", "docsIfDownChannelWidth"), ("DOCS-IF-MIB", "docsIfDownChannelFrequency"), ("DOCS-IF-MIB", "docsIfUpChannelTxBackoffStart"), ("DOCS-IF-MIB", "docsIfUpChannelTxTimingOffset"), ("DOCS-IF-MIB", "docsIfQosProfMaxTxBurst"), ("DOCS-IF-MIB", "docsIfSigQEqualizationData"), ("DOCS-IF-MIB", "docsIfUpChannelWidth"), ("DOCS-IF-MIB", "docsIfUpChannelModulationProfile"), ("DOCS-IF-MIB", "docsIfUpChannelRangingBackoffStart"), ("DOCS-IF-MIB", "docsIfUpChannelId"), ("DOCS-IF-MIB", "docsIfSigQUnerroreds"), ("DOCS-IF-MIB", "docsIfQosProfMaxDownBandwidth"), ("DOCS-IF-MIB", "docsIfQosProfGuarUpBandwidth"), ("DOCS-IF-MIB", "docsIfSigQMicroreflections"), ("DOCS-IF-MIB", "docsIfUpChannelFrequency"), ("DOCS-IF-MIB", "docsIfQosProfBaselinePrivacy"), ("DOCS-IF-MIB", "docsIfUpChannelTxBackoffEnd"), ("DOCS-IF-MIB", "docsIfDownChannelInterleave"), ("DOCS-IF-MIB", "docsIfSigQIncludesContention"), ("DOCS-IF-MIB", "docsIfDownChannelPower"), ("DOCS-IF-MIB", "docsIfSigQUncorrectables"), ("DOCS-IF-MIB", "docsIfDownChannelModulation"), ("DOCS-IF-MIB", "docsIfSigQCorrecteds"), ("DOCS-IF-MIB", "docsIfDownChannelId"), ("DOCS-IF-MIB", "docsIfUpChannelRangingBackoffEnd"), )

# Exports

# Types
mibBuilder.exportSymbols("DOCS-IF-MIB", TenthdB=TenthdB, TenthdBmV=TenthdBmV)

# Objects
mibBuilder.exportSymbols("DOCS-IF-MIB", docsIfMib=docsIfMib, docsIfMibObjects=docsIfMibObjects, docsIfBaseObjects=docsIfBaseObjects, docsIfDownstreamChannelTable=docsIfDownstreamChannelTable, docsIfDownstreamChannelEntry=docsIfDownstreamChannelEntry, docsIfDownChannelId=docsIfDownChannelId, docsIfDownChannelFrequency=docsIfDownChannelFrequency, docsIfDownChannelWidth=docsIfDownChannelWidth, docsIfDownChannelModulation=docsIfDownChannelModulation, docsIfDownChannelInterleave=docsIfDownChannelInterleave, docsIfDownChannelPower=docsIfDownChannelPower, docsIfUpstreamChannelTable=docsIfUpstreamChannelTable, docsIfUpstreamChannelEntry=docsIfUpstreamChannelEntry, docsIfUpChannelId=docsIfUpChannelId, docsIfUpChannelFrequency=docsIfUpChannelFrequency, docsIfUpChannelWidth=docsIfUpChannelWidth, docsIfUpChannelModulationProfile=docsIfUpChannelModulationProfile, docsIfUpChannelSlotSize=docsIfUpChannelSlotSize, docsIfUpChannelTxTimingOffset=docsIfUpChannelTxTimingOffset, docsIfUpChannelRangingBackoffStart=docsIfUpChannelRangingBackoffStart, docsIfUpChannelRangingBackoffEnd=docsIfUpChannelRangingBackoffEnd, docsIfUpChannelTxBackoffStart=docsIfUpChannelTxBackoffStart, docsIfUpChannelTxBackoffEnd=docsIfUpChannelTxBackoffEnd, docsIfQosProfileTable=docsIfQosProfileTable, docsIfQosProfileEntry=docsIfQosProfileEntry, docsIfQosProfIndex=docsIfQosProfIndex, docsIfQosProfPriority=docsIfQosProfPriority, docsIfQosProfMaxUpBandwidth=docsIfQosProfMaxUpBandwidth, docsIfQosProfGuarUpBandwidth=docsIfQosProfGuarUpBandwidth, docsIfQosProfMaxDownBandwidth=docsIfQosProfMaxDownBandwidth, docsIfQosProfMaxTxBurst=docsIfQosProfMaxTxBurst, docsIfQosProfBaselinePrivacy=docsIfQosProfBaselinePrivacy, docsIfQosProfStatus=docsIfQosProfStatus, docsIfSignalQualityTable=docsIfSignalQualityTable, docsIfSignalQualityEntry=docsIfSignalQualityEntry, docsIfSigQIncludesContention=docsIfSigQIncludesContention, docsIfSigQUnerroreds=docsIfSigQUnerroreds, docsIfSigQCorrecteds=docsIfSigQCorrecteds, docsIfSigQUncorrectables=docsIfSigQUncorrectables, docsIfSigQSignalNoise=docsIfSigQSignalNoise, docsIfSigQMicroreflections=docsIfSigQMicroreflections, docsIfSigQEqualizationData=docsIfSigQEqualizationData, docsIfCmObjects=docsIfCmObjects, docsIfCmMacTable=docsIfCmMacTable, docsIfCmMacEntry=docsIfCmMacEntry, docsIfCmCmtsAddress=docsIfCmCmtsAddress, docsIfCmCapabilities=docsIfCmCapabilities, docsIfCmRangingRespTimeout=docsIfCmRangingRespTimeout, docsIfCmRangingTimeout=docsIfCmRangingTimeout, docsIfCmStatusTable=docsIfCmStatusTable, docsIfCmStatusEntry=docsIfCmStatusEntry, docsIfCmStatusValue=docsIfCmStatusValue, docsIfCmStatusCode=docsIfCmStatusCode, docsIfCmStatusTxPower=docsIfCmStatusTxPower, docsIfCmStatusResets=docsIfCmStatusResets, docsIfCmStatusLostSyncs=docsIfCmStatusLostSyncs, docsIfCmStatusInvalidMaps=docsIfCmStatusInvalidMaps, docsIfCmStatusInvalidUcds=docsIfCmStatusInvalidUcds, docsIfCmStatusInvalidRangingResponses=docsIfCmStatusInvalidRangingResponses, docsIfCmStatusInvalidRegistrationResponses=docsIfCmStatusInvalidRegistrationResponses, docsIfCmStatusT1Timeouts=docsIfCmStatusT1Timeouts, docsIfCmStatusT2Timeouts=docsIfCmStatusT2Timeouts, docsIfCmStatusT3Timeouts=docsIfCmStatusT3Timeouts, docsIfCmStatusT4Timeouts=docsIfCmStatusT4Timeouts, docsIfCmStatusRangingAborteds=docsIfCmStatusRangingAborteds, docsIfCmServiceTable=docsIfCmServiceTable, docsIfCmServiceEntry=docsIfCmServiceEntry, docsIfCmServiceId=docsIfCmServiceId, docsIfCmServiceQosProfile=docsIfCmServiceQosProfile, docsIfCmServiceTxSlotsImmed=docsIfCmServiceTxSlotsImmed, docsIfCmServiceTxSlotsDed=docsIfCmServiceTxSlotsDed, docsIfCmServiceTxRetries=docsIfCmServiceTxRetries, docsIfCmServiceTxExceededs=docsIfCmServiceTxExceededs, docsIfCmServiceRqRetries=docsIfCmServiceRqRetries, docsIfCmServiceRqExceededs=docsIfCmServiceRqExceededs, docsIfCmtsObjects=docsIfCmtsObjects, docsIfCmtsMacTable=docsIfCmtsMacTable, docsIfCmtsMacEntry=docsIfCmtsMacEntry, docsIfCmtsCapabilities=docsIfCmtsCapabilities, docsIfCmtsSyncInterval=docsIfCmtsSyncInterval, docsIfCmtsUcdInterval=docsIfCmtsUcdInterval, docsIfCmtsMaxServiceIds=docsIfCmtsMaxServiceIds, docsIfCmtsInsertionInterval=docsIfCmtsInsertionInterval, docsIfCmtsInvitedRangingAttempts=docsIfCmtsInvitedRangingAttempts, docsIfCmtsInsertInterval=docsIfCmtsInsertInterval, docsIfCmtsStatusTable=docsIfCmtsStatusTable, docsIfCmtsStatusEntry=docsIfCmtsStatusEntry, docsIfCmtsStatusInvalidRangeReqs=docsIfCmtsStatusInvalidRangeReqs, docsIfCmtsStatusRangingAborteds=docsIfCmtsStatusRangingAborteds, docsIfCmtsStatusInvalidRegReqs=docsIfCmtsStatusInvalidRegReqs, docsIfCmtsStatusFailedRegReqs=docsIfCmtsStatusFailedRegReqs, docsIfCmtsStatusInvalidDataReqs=docsIfCmtsStatusInvalidDataReqs, docsIfCmtsStatusT5Timeouts=docsIfCmtsStatusT5Timeouts, docsIfCmtsCmStatusTable=docsIfCmtsCmStatusTable, docsIfCmtsCmStatusEntry=docsIfCmtsCmStatusEntry, docsIfCmtsCmStatusIndex=docsIfCmtsCmStatusIndex, docsIfCmtsCmStatusMacAddress=docsIfCmtsCmStatusMacAddress, docsIfCmtsCmStatusIpAddress=docsIfCmtsCmStatusIpAddress, docsIfCmtsCmStatusDownChannelIfIndex=docsIfCmtsCmStatusDownChannelIfIndex, docsIfCmtsCmStatusUpChannelIfIndex=docsIfCmtsCmStatusUpChannelIfIndex, docsIfCmtsCmStatusRxPower=docsIfCmtsCmStatusRxPower, docsIfCmtsCmStatusTimingOffset=docsIfCmtsCmStatusTimingOffset, docsIfCmtsCmStatusEqualizationData=docsIfCmtsCmStatusEqualizationData, docsIfCmtsCmStatusValue=docsIfCmtsCmStatusValue, docsIfCmtsCmStatusUnerroreds=docsIfCmtsCmStatusUnerroreds, docsIfCmtsCmStatusCorrecteds=docsIfCmtsCmStatusCorrecteds, docsIfCmtsCmStatusUncorrectables=docsIfCmtsCmStatusUncorrectables, docsIfCmtsCmStatusSignalNoise=docsIfCmtsCmStatusSignalNoise, docsIfCmtsCmStatusMicroreflections=docsIfCmtsCmStatusMicroreflections, docsIfCmtsServiceTable=docsIfCmtsServiceTable, docsIfCmtsServiceEntry=docsIfCmtsServiceEntry, docsIfCmtsServiceId=docsIfCmtsServiceId, docsIfCmtsServiceCmStatusIndex=docsIfCmtsServiceCmStatusIndex, docsIfCmtsServiceAdminStatus=docsIfCmtsServiceAdminStatus, docsIfCmtsServiceQosProfile=docsIfCmtsServiceQosProfile, docsIfCmtsServiceCreateTime=docsIfCmtsServiceCreateTime, docsIfCmtsServiceInOctets=docsIfCmtsServiceInOctets, docsIfCmtsServiceInPackets=docsIfCmtsServiceInPackets, docsIfCmtsModulationTable=docsIfCmtsModulationTable, docsIfCmtsModulationEntry=docsIfCmtsModulationEntry, docsIfCmtsModIndex=docsIfCmtsModIndex, docsIfCmtsModIntervalUsageCode=docsIfCmtsModIntervalUsageCode, docsIfCmtsModControl=docsIfCmtsModControl, docsIfCmtsModType=docsIfCmtsModType, docsIfCmtsModPreambleLen=docsIfCmtsModPreambleLen, docsIfCmtsModDifferentialEncoding=docsIfCmtsModDifferentialEncoding, docsIfCmtsModFECErrorCorrection=docsIfCmtsModFECErrorCorrection, docsIfCmtsModFECCodewordLength=docsIfCmtsModFECCodewordLength)
mibBuilder.exportSymbols("DOCS-IF-MIB", docsIfCmtsModScramblerSeed=docsIfCmtsModScramblerSeed, docsIfCmtsModMaxBurstSize=docsIfCmtsModMaxBurstSize, docsIfCmtsModGuardTimeSize=docsIfCmtsModGuardTimeSize, docsIfCmtsModLastCodewordShortened=docsIfCmtsModLastCodewordShortened, docsIfCmtsModScrambler=docsIfCmtsModScrambler, docsIfCmtsQosProfilePermissions=docsIfCmtsQosProfilePermissions, docsIfCmtsMacToCmTable=docsIfCmtsMacToCmTable, docsIfCmtsMacToCmEntry=docsIfCmtsMacToCmEntry, docsIfCmtsCmMac=docsIfCmtsCmMac, docsIfCmtsCmPtr=docsIfCmtsCmPtr, docsIfNotification=docsIfNotification, docsIfConformance=docsIfConformance, docsIfCompliances=docsIfCompliances, docsIfGroups=docsIfGroups)

# Groups
mibBuilder.exportSymbols("DOCS-IF-MIB", docsIfCmtsGroup=docsIfCmtsGroup, docsIfCmGroup=docsIfCmGroup, docsIfObsoleteGroup=docsIfObsoleteGroup, docsIfBasicGroup=docsIfBasicGroup)