# PySNMP SMI module. Autogenerated from smidump -f python FDDI-SMT73-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:04 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Types

class FddiMACLongAddressType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(6,6)
    pass

class FddiResourceId(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class FddiSMTStationIdType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(8,8)
    pass

class FddiTimeMilli(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class FddiTimeNano(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass


# Objects

fddi = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15))
fddimib = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73))
fddimibSMT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 1))
fddimibSMTNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibSMTTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2))
fddimibSMTEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibSMTIndex"))
fddimibSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibSMTStationId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 2), FddiSMTStationIdType()).setMaxAccess("readonly")
fddimibSMTOpVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibSMTHiVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibSMTLoVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibSMTUserData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(32, 32))).setMaxAccess("readwrite")
fddimibSMTMIBVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibSMTMACCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
fddimibSMTNonMasterCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
fddimibSMTMasterCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
fddimibSMTAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
fddimibSMTConfigCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
fddimibSMTConfigPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
fddimibSMTConnectionPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(32768, 65535))).setMaxAccess("readwrite")
fddimibSMTTNotify = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(2, 30))).setMaxAccess("readwrite")
fddimibSMTStatRptPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 16), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readwrite")
fddimibSMTTraceMaxExpiration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 17), FddiTimeMilli()).setMaxAccess("readwrite")
fddimibSMTBypassPresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 18), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibSMTECMState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 19), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(8,7,6,5,4,3,2,1,)).subtype(namedValues=namedval.NamedValues(("ec0", 1), ("ec1", 2), ("ec2", 3), ("ec3", 4), ("ec4", 5), ("ec5", 6), ("ec6", 7), ("ec7", 8), ))).setMaxAccess("readonly")
fddimibSMTCFState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 20), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(11,12,13,9,10,7,8,5,6,3,4,1,2,)).subtype(namedValues=namedval.NamedValues(("cf0", 1), ("cf9", 10), ("cf10", 11), ("cf11", 12), ("cf12", 13), ("cf1", 2), ("cf2", 3), ("cf3", 4), ("cf4", 5), ("cf5", 6), ("cf6", 7), ("cf7", 8), ("cf8", 9), ))).setMaxAccess("readonly")
fddimibSMTRemoteDisconnectFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 21), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibSMTStationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 22), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("concatenated", 1), ("separated", 2), ("thru", 3), ))).setMaxAccess("readonly")
fddimibSMTPeerWrapFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 23), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibSMTTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 24), FddiTimeMilli()).setMaxAccess("readonly")
fddimibSMTTransitionTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 25), FddiTimeMilli()).setMaxAccess("readonly")
fddimibSMTStationAction = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 26), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,1,2,8,7,6,5,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("connect", 2), ("disconnect", 3), ("path-Test", 4), ("self-Test", 5), ("disable-a", 6), ("disable-b", 7), ("disable-m", 8), ))).setMaxAccess("readwrite")
fddimibMAC = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 2))
fddimibMACNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibMACTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2))
fddimibMACEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibMACSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibMACIndex"))
fddimibMACSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibMACIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibMACIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibMACFrameStatusFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
fddimibMACTMaxCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 5), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACTVXCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 6), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
fddimibMACCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,1,4,6,2,3,)).subtype(namedValues=namedval.NamedValues(("isolated", 1), ("local", 2), ("secondary", 3), ("primary", 4), ("concatenated", 5), ("thru", 6), ))).setMaxAccess("readonly")
fddimibMACUpstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 9), FddiMACLongAddressType()).setMaxAccess("readonly")
fddimibMACDownstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 10), FddiMACLongAddressType()).setMaxAccess("readonly")
fddimibMACOldUpstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 11), FddiMACLongAddressType()).setMaxAccess("readonly")
fddimibMACOldDownstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 12), FddiMACLongAddressType()).setMaxAccess("readonly")
fddimibMACDupAddressTest = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("pass", 2), ("fail", 3), ))).setMaxAccess("readonly")
fddimibMACRequestedPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
fddimibMACDownstreamPORTType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 15), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,5,2,4,3,)).subtype(namedValues=namedval.NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5), ))).setMaxAccess("readonly")
fddimibMACSMTAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 16), FddiMACLongAddressType()).setMaxAccess("readonly")
fddimibMACTReq = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 17), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACTNeg = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 18), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACTMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 19), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACTvxValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 20), FddiTimeNano()).setMaxAccess("readonly")
fddimibMACFrameCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 21), Counter32()).setMaxAccess("readonly")
fddimibMACCopiedCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 22), Counter32()).setMaxAccess("readonly")
fddimibMACTransmitCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 23), Counter32()).setMaxAccess("readonly")
fddimibMACErrorCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 24), Counter32()).setMaxAccess("readonly")
fddimibMACLostCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 25), Counter32()).setMaxAccess("readonly")
fddimibMACFrameErrorThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 26), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
fddimibMACFrameErrorRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 27), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibMACRMTState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 28), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,1,2,7,8,5,6,)).subtype(namedValues=namedval.NamedValues(("rm0", 1), ("rm1", 2), ("rm2", 3), ("rm3", 4), ("rm4", 5), ("rm5", 6), ("rm6", 7), ("rm7", 8), ))).setMaxAccess("readonly")
fddimibMACDaFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 29), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACUnaDaFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 30), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACFrameErrorFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 31), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACMAUnitdataAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 32), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACHardwarePresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 33), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACMAUnitdataEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 34), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readwrite")
fddimibMACCounters = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 3))
fddimibMACCountersTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1))
fddimibMACCountersEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibMACSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibMACIndex"))
fddimibMACTokenCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
fddimibMACTvxExpiredCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
fddimibMACNotCopiedCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
fddimibMACLateCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
fddimibMACRingOpCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
fddimibMACNotCopiedRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibMACNotCopiedFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibMACNotCopiedThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
fddimibPATH = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 4))
fddimibPATHNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibPATHTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2))
fddimibPATHEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPATHSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHIndex"))
fddimibPATHSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPATHIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibPATHTVXLowerBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 3), FddiTimeNano()).setMaxAccess("readwrite")
fddimibPATHTMaxLowerBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 4), FddiTimeNano()).setMaxAccess("readwrite")
fddimibPATHMaxTReq = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 5), FddiTimeNano()).setMaxAccess("readwrite")
fddimibPATHConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3))
fddimibPATHConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPATHConfigSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHConfigPATHIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHConfigTokenOrder"))
fddimibPATHConfigSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPATHConfigPATHIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPATHConfigTokenOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPATHConfigResourceType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,4,)).subtype(namedValues=namedval.NamedValues(("mac", 2), ("port", 4), ))).setMaxAccess("readonly")
fddimibPATHConfigResourceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPATHConfigCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,1,4,6,2,3,)).subtype(namedValues=namedval.NamedValues(("isolated", 1), ("local", 2), ("secondary", 3), ("primary", 4), ("concatenated", 5), ("thru", 6), ))).setMaxAccess("readonly")
fddimibPORT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 5))
fddimibPORTNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
fddimibPORTTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2))
fddimibPORTEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1)).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPORTSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPORTIndex"))
fddimibPORTSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPORTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
fddimibPORTMyType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,5,2,4,3,)).subtype(namedValues=namedval.NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5), ))).setMaxAccess("readonly")
fddimibPORTNeighborType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,5,2,4,3,)).subtype(namedValues=namedval.NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5), ))).setMaxAccess("readonly")
fddimibPORTConnectionPolicies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
fddimibPORTMACIndicated = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,2,1,)).subtype(namedValues=namedval.NamedValues(("tVal9FalseRVal9False", 1), ("tVal9FalseRVal9True", 2), ("tVal9TrueRVal9False", 3), ("tVal9TrueRVal9True", 4), ))).setMaxAccess("readonly")
fddimibPORTCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,5,4,3,2,1,)).subtype(namedValues=namedval.NamedValues(("ce0", 1), ("ce1", 2), ("ce2", 3), ("ce3", 4), ("ce4", 5), ("ce5", 6), ))).setMaxAccess("readonly")
fddimibPORTRequestedPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 8), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(3, 3))).setMaxAccess("readwrite")
fddimibPORTMACPlacement = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 9), FddiResourceId()).setMaxAccess("readonly")
fddimibPORTAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
fddimibPORTPMDClass = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,7,6,8,5,4,1,)).subtype(namedValues=namedval.NamedValues(("multimode", 1), ("single-mode1", 2), ("single-mode2", 3), ("sonet", 4), ("low-cost-fiber", 5), ("twisted-pair", 6), ("unknown", 7), ("unspecified", 8), ))).setMaxAccess("readonly")
fddimibPORTConnectionCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
fddimibPORTBSFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibPORTLCTFailCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 14), Counter32()).setMaxAccess("readonly")
fddimibPORTLerEstimate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(4, 15))).setMaxAccess("readonly")
fddimibPORTLemRejectCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 16), Counter32()).setMaxAccess("readonly")
fddimibPORTLemCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 17), Counter32()).setMaxAccess("readonly")
fddimibPORTLerCutoff = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 18), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(4, 15))).setMaxAccess("readwrite")
fddimibPORTLerAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 19), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(4, 15))).setMaxAccess("readwrite")
fddimibPORTConnectState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 20), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("connecting", 2), ("standby", 3), ("active", 4), ))).setMaxAccess("readonly")
fddimibPORTPCMState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 21), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(9,10,3,4,1,2,7,8,5,6,)).subtype(namedValues=namedval.NamedValues(("pc0", 1), ("pc9", 10), ("pc1", 2), ("pc2", 3), ("pc3", 4), ("pc4", 5), ("pc5", 6), ("pc6", 7), ("pc7", 8), ("pc8", 9), ))).setMaxAccess("readonly")
fddimibPORTPCWithhold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 22), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("m-m", 2), ("otherincompatible", 3), ("pathnotavailable", 4), ))).setMaxAccess("readonly")
fddimibPORTLerFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 23), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibPORTHardwarePresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 24), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readonly")
fddimibPORTAction = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 25), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,4,3,1,2,6,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("maintPORT", 2), ("enablePORT", 3), ("disablePORT", 4), ("startPORT", 5), ("stopPORT", 6), ))).setMaxAccess("readwrite")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("FDDI-SMT73-MIB", FddiMACLongAddressType=FddiMACLongAddressType, FddiResourceId=FddiResourceId, FddiSMTStationIdType=FddiSMTStationIdType, FddiTimeMilli=FddiTimeMilli, FddiTimeNano=FddiTimeNano)

# Objects
mibBuilder.exportSymbols("FDDI-SMT73-MIB", fddi=fddi, fddimib=fddimib, fddimibSMT=fddimibSMT, fddimibSMTNumber=fddimibSMTNumber, fddimibSMTTable=fddimibSMTTable, fddimibSMTEntry=fddimibSMTEntry, fddimibSMTIndex=fddimibSMTIndex, fddimibSMTStationId=fddimibSMTStationId, fddimibSMTOpVersionId=fddimibSMTOpVersionId, fddimibSMTHiVersionId=fddimibSMTHiVersionId, fddimibSMTLoVersionId=fddimibSMTLoVersionId, fddimibSMTUserData=fddimibSMTUserData, fddimibSMTMIBVersionId=fddimibSMTMIBVersionId, fddimibSMTMACCts=fddimibSMTMACCts, fddimibSMTNonMasterCts=fddimibSMTNonMasterCts, fddimibSMTMasterCts=fddimibSMTMasterCts, fddimibSMTAvailablePaths=fddimibSMTAvailablePaths, fddimibSMTConfigCapabilities=fddimibSMTConfigCapabilities, fddimibSMTConfigPolicy=fddimibSMTConfigPolicy, fddimibSMTConnectionPolicy=fddimibSMTConnectionPolicy, fddimibSMTTNotify=fddimibSMTTNotify, fddimibSMTStatRptPolicy=fddimibSMTStatRptPolicy, fddimibSMTTraceMaxExpiration=fddimibSMTTraceMaxExpiration, fddimibSMTBypassPresent=fddimibSMTBypassPresent, fddimibSMTECMState=fddimibSMTECMState, fddimibSMTCFState=fddimibSMTCFState, fddimibSMTRemoteDisconnectFlag=fddimibSMTRemoteDisconnectFlag, fddimibSMTStationStatus=fddimibSMTStationStatus, fddimibSMTPeerWrapFlag=fddimibSMTPeerWrapFlag, fddimibSMTTimeStamp=fddimibSMTTimeStamp, fddimibSMTTransitionTimeStamp=fddimibSMTTransitionTimeStamp, fddimibSMTStationAction=fddimibSMTStationAction, fddimibMAC=fddimibMAC, fddimibMACNumber=fddimibMACNumber, fddimibMACTable=fddimibMACTable, fddimibMACEntry=fddimibMACEntry, fddimibMACSMTIndex=fddimibMACSMTIndex, fddimibMACIndex=fddimibMACIndex, fddimibMACIfIndex=fddimibMACIfIndex, fddimibMACFrameStatusFunctions=fddimibMACFrameStatusFunctions, fddimibMACTMaxCapability=fddimibMACTMaxCapability, fddimibMACTVXCapability=fddimibMACTVXCapability, fddimibMACAvailablePaths=fddimibMACAvailablePaths, fddimibMACCurrentPath=fddimibMACCurrentPath, fddimibMACUpstreamNbr=fddimibMACUpstreamNbr, fddimibMACDownstreamNbr=fddimibMACDownstreamNbr, fddimibMACOldUpstreamNbr=fddimibMACOldUpstreamNbr, fddimibMACOldDownstreamNbr=fddimibMACOldDownstreamNbr, fddimibMACDupAddressTest=fddimibMACDupAddressTest, fddimibMACRequestedPaths=fddimibMACRequestedPaths, fddimibMACDownstreamPORTType=fddimibMACDownstreamPORTType, fddimibMACSMTAddress=fddimibMACSMTAddress, fddimibMACTReq=fddimibMACTReq, fddimibMACTNeg=fddimibMACTNeg, fddimibMACTMax=fddimibMACTMax, fddimibMACTvxValue=fddimibMACTvxValue, fddimibMACFrameCts=fddimibMACFrameCts, fddimibMACCopiedCts=fddimibMACCopiedCts, fddimibMACTransmitCts=fddimibMACTransmitCts, fddimibMACErrorCts=fddimibMACErrorCts, fddimibMACLostCts=fddimibMACLostCts, fddimibMACFrameErrorThreshold=fddimibMACFrameErrorThreshold, fddimibMACFrameErrorRatio=fddimibMACFrameErrorRatio, fddimibMACRMTState=fddimibMACRMTState, fddimibMACDaFlag=fddimibMACDaFlag, fddimibMACUnaDaFlag=fddimibMACUnaDaFlag, fddimibMACFrameErrorFlag=fddimibMACFrameErrorFlag, fddimibMACMAUnitdataAvailable=fddimibMACMAUnitdataAvailable, fddimibMACHardwarePresent=fddimibMACHardwarePresent, fddimibMACMAUnitdataEnable=fddimibMACMAUnitdataEnable, fddimibMACCounters=fddimibMACCounters, fddimibMACCountersTable=fddimibMACCountersTable, fddimibMACCountersEntry=fddimibMACCountersEntry, fddimibMACTokenCts=fddimibMACTokenCts, fddimibMACTvxExpiredCts=fddimibMACTvxExpiredCts, fddimibMACNotCopiedCts=fddimibMACNotCopiedCts, fddimibMACLateCts=fddimibMACLateCts, fddimibMACRingOpCts=fddimibMACRingOpCts, fddimibMACNotCopiedRatio=fddimibMACNotCopiedRatio, fddimibMACNotCopiedFlag=fddimibMACNotCopiedFlag, fddimibMACNotCopiedThreshold=fddimibMACNotCopiedThreshold, fddimibPATH=fddimibPATH, fddimibPATHNumber=fddimibPATHNumber, fddimibPATHTable=fddimibPATHTable, fddimibPATHEntry=fddimibPATHEntry, fddimibPATHSMTIndex=fddimibPATHSMTIndex, fddimibPATHIndex=fddimibPATHIndex, fddimibPATHTVXLowerBound=fddimibPATHTVXLowerBound, fddimibPATHTMaxLowerBound=fddimibPATHTMaxLowerBound, fddimibPATHMaxTReq=fddimibPATHMaxTReq, fddimibPATHConfigTable=fddimibPATHConfigTable, fddimibPATHConfigEntry=fddimibPATHConfigEntry, fddimibPATHConfigSMTIndex=fddimibPATHConfigSMTIndex, fddimibPATHConfigPATHIndex=fddimibPATHConfigPATHIndex, fddimibPATHConfigTokenOrder=fddimibPATHConfigTokenOrder, fddimibPATHConfigResourceType=fddimibPATHConfigResourceType, fddimibPATHConfigResourceIndex=fddimibPATHConfigResourceIndex, fddimibPATHConfigCurrentPath=fddimibPATHConfigCurrentPath, fddimibPORT=fddimibPORT, fddimibPORTNumber=fddimibPORTNumber, fddimibPORTTable=fddimibPORTTable, fddimibPORTEntry=fddimibPORTEntry, fddimibPORTSMTIndex=fddimibPORTSMTIndex, fddimibPORTIndex=fddimibPORTIndex, fddimibPORTMyType=fddimibPORTMyType, fddimibPORTNeighborType=fddimibPORTNeighborType, fddimibPORTConnectionPolicies=fddimibPORTConnectionPolicies, fddimibPORTMACIndicated=fddimibPORTMACIndicated, fddimibPORTCurrentPath=fddimibPORTCurrentPath, fddimibPORTRequestedPaths=fddimibPORTRequestedPaths, fddimibPORTMACPlacement=fddimibPORTMACPlacement, fddimibPORTAvailablePaths=fddimibPORTAvailablePaths, fddimibPORTPMDClass=fddimibPORTPMDClass, fddimibPORTConnectionCapabilities=fddimibPORTConnectionCapabilities, fddimibPORTBSFlag=fddimibPORTBSFlag, fddimibPORTLCTFailCts=fddimibPORTLCTFailCts, fddimibPORTLerEstimate=fddimibPORTLerEstimate, fddimibPORTLemRejectCts=fddimibPORTLemRejectCts, fddimibPORTLemCts=fddimibPORTLemCts, fddimibPORTLerCutoff=fddimibPORTLerCutoff, fddimibPORTLerAlarm=fddimibPORTLerAlarm, fddimibPORTConnectState=fddimibPORTConnectState, fddimibPORTPCMState=fddimibPORTPCMState, fddimibPORTPCWithhold=fddimibPORTPCWithhold, fddimibPORTLerFlag=fddimibPORTLerFlag, fddimibPORTHardwarePresent=fddimibPORTHardwarePresent)
mibBuilder.exportSymbols("FDDI-SMT73-MIB", fddimibPORTAction=fddimibPORTAction)

