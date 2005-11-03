# PySNMP SMI module. Autogenerated from smidump -f python HPR-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:02 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( SnaControlPointName, ) = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DateAndTime, DisplayString, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TimeStamp")

# Types

class HprNceTypes(Bits):
    namedValues = namedval.NamedValues(("controlPoint", 0), ("logicalUnit", 1), ("boundaryFunction", 2), ("routeSetup", 3), )
    pass

class HprRtpCounter(Counter32):
    pass


# Objects

hprMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 6)).setRevisions(("1997-05-14 00:00",))
hprObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1))
hprGlobal = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1, 1))
hprNodeCpName = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 1, 1), SnaControlPointName()).setMaxAccess("readonly")
hprOperatorPathSwitchSupport = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("notSupported", 1), ("switchTriggerSupported", 2), ("switchToPathSupported", 3), ))).setMaxAccess("readonly")
hprAnrRouting = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1, 2))
hprAnrsAssigned = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 1), Counter32()).setMaxAccess("readonly").setUnits("ANR labels")
hprAnrCounterState = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("notActive", 1), ("active", 2), ))).setMaxAccess("readwrite")
hprAnrCounterStateTime = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 3), DateAndTime()).setMaxAccess("readonly")
hprAnrRoutingTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4))
hprAnrRoutingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1)).setIndexNames((0, "HPR-MIB", "hprAnrLabel"))
hprAnrLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("noaccess")
hprAnrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("nce", 1), ("tg", 2), ))).setMaxAccess("readonly")
hprAnrOutTgDest = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(3, 17))).setMaxAccess("readonly")
hprAnrOutTgNum = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
hprAnrPacketsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
hprAnrCounterDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
hprTransportUser = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1, 3))
hprNceTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1))
hprNceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1)).setIndexNames((0, "HPR-MIB", "hprNceId"))
hprNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("noaccess")
hprNceType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 2), HprNceTypes()).setMaxAccess("readonly")
hprNceDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 3), HprNceTypes()).setMaxAccess("readonly")
hprNceInstanceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4))).setMaxAccess("readonly")
hprRtp = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1, 4))
hprRtpGlobe = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1))
hprRtpGlobeConnSetups = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly").setUnits("RTP connection setups")
hprRtpGlobeCtrState = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("notActive", 1), ("active", 2), ))).setMaxAccess("readwrite")
hprRtpGlobeCtrStateTime = MibScalar((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 3), DateAndTime()).setMaxAccess("readonly")
hprRtpTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2))
hprRtpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1)).setIndexNames((0, "HPR-MIB", "hprRtpLocNceId"), (0, "HPR-MIB", "hprRtpLocTcid"))
hprRtpLocNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("noaccess")
hprRtpLocTcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8))).setMaxAccess("noaccess")
hprRtpRemCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 3), SnaControlPointName()).setMaxAccess("readonly")
hprRtpRemNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
hprRtpRemTcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 5), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8))).setMaxAccess("readonly")
hprRtpPathSwitchTrigger = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("ready", 1), ("switchPathNow", 2), ))).setMaxAccess("readwrite")
hprRtpRscv = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 7), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
hprRtpTopic = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 8), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8))).setMaxAccess("readonly")
hprRtpState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,4,99,2,5,)).subtype(namedValues=namedval.NamedValues(("rtpListening", 1), ("rtpCalling", 2), ("rtpConnected", 3), ("rtpPathSwitching", 4), ("rtpDisconnecting", 5), ("other", 99), ))).setMaxAccess("readonly")
hprRtpUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
hprRtpLivenessTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
hprRtpShortReqTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
hprRtpPathSwTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
hprRtpLivenessTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 14), HprRtpCounter()).setMaxAccess("readonly")
hprRtpShortReqTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 15), HprRtpCounter()).setMaxAccess("readonly")
hprRtpMaxSendRate = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
hprRtpMinSendRate = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
hprRtpCurSendRate = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
hprRtpSmRdTripDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
hprRtpSendPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 20), HprRtpCounter()).setMaxAccess("readonly")
hprRtpRecvPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 21), HprRtpCounter()).setMaxAccess("readonly")
hprRtpSendBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 22), HprRtpCounter()).setMaxAccess("readonly")
hprRtpRecvBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 23), HprRtpCounter()).setMaxAccess("readonly")
hprRtpRetrPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 24), HprRtpCounter()).setMaxAccess("readonly")
hprRtpPacketsDiscarded = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 25), HprRtpCounter()).setMaxAccess("readonly")
hprRtpDetectGaps = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 26), HprRtpCounter()).setMaxAccess("readonly")
hprRtpRateReqSends = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 27), HprRtpCounter()).setMaxAccess("readonly")
hprRtpOkErrPathSws = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 28), HprRtpCounter()).setMaxAccess("readonly")
hprRtpBadErrPathSws = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 29), HprRtpCounter()).setMaxAccess("readonly")
hprRtpOkOpPathSws = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 30), HprRtpCounter()).setMaxAccess("readonly")
hprRtpBadOpPathSws = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 31), HprRtpCounter()).setMaxAccess("readonly")
hprRtpCounterDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 32), TimeStamp()).setMaxAccess("readonly")
hprRtpStatusTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3))
hprRtpStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1)).setIndexNames((0, "HPR-MIB", "hprRtpStatusLocNceId"), (0, "HPR-MIB", "hprRtpStatusLocTcid"), (0, "HPR-MIB", "hprRtpStatusIndex"))
hprRtpStatusLocNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("noaccess")
hprRtpStatusLocTcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8))).setMaxAccess("noaccess")
hprRtpStatusIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
hprRtpStatusStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
hprRtpStatusEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
hprRtpStatusRemCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 6), SnaControlPointName()).setMaxAccess("readonly")
hprRtpStatusRemNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 7), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
hprRtpStatusRemTcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 8), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8))).setMaxAccess("readonly")
hprRtpStatusNewRscv = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
hprRtpStatusOldRscv = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
hprRtpStatusCause = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,5,3,1,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("rtpConnFail", 2), ("locLinkFail", 3), ("remLinkFail", 4), ("operRequest", 5), ))).setMaxAccess("readonly")
hprRtpStatusLastAttemptResult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,7,3,5,6,8,2,4,)).subtype(namedValues=namedval.NamedValues(("successful", 1), ("initiatorMoving", 2), ("directorySearchFailed", 3), ("rscvCalculationFailed", 4), ("negativeRouteSetupReply", 5), ("backoutRouteSetupReply", 6), ("timeoutDuringFirstAttempt", 7), ("otherUnsuccessful", 8), ))).setMaxAccess("readonly")
hprConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 2))
hprCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 2, 1))
hprGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 6, 2, 2))

# Augmentions

# Groups

hprRtpConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 4)).setObjects(("HPR-MIB", "hprRtpSendBytes"), ("HPR-MIB", "hprRtpRateReqSends"), ("HPR-MIB", "hprRtpStatusStartTime"), ("HPR-MIB", "hprRtpRecvBytes"), ("HPR-MIB", "hprRtpStatusOldRscv"), ("HPR-MIB", "hprRtpRecvPackets"), ("HPR-MIB", "hprRtpGlobeCtrStateTime"), ("HPR-MIB", "hprRtpCurSendRate"), ("HPR-MIB", "hprRtpStatusEndTime"), ("HPR-MIB", "hprRtpStatusCause"), ("HPR-MIB", "hprRtpGlobeConnSetups"), ("HPR-MIB", "hprRtpMinSendRate"), ("HPR-MIB", "hprRtpRemCpName"), ("HPR-MIB", "hprRtpShortReqTimeouts"), ("HPR-MIB", "hprRtpOkOpPathSws"), ("HPR-MIB", "hprRtpPathSwTimer"), ("HPR-MIB", "hprRtpBadOpPathSws"), ("HPR-MIB", "hprRtpStatusRemNceId"), ("HPR-MIB", "hprRtpCounterDisconTime"), ("HPR-MIB", "hprRtpStatusLastAttemptResult"), ("HPR-MIB", "hprRtpSendPackets"), ("HPR-MIB", "hprRtpLivenessTimer"), ("HPR-MIB", "hprRtpUpTime"), ("HPR-MIB", "hprRtpStatusNewRscv"), ("HPR-MIB", "hprRtpDetectGaps"), ("HPR-MIB", "hprRtpSmRdTripDelay"), ("HPR-MIB", "hprRtpRscv"), ("HPR-MIB", "hprRtpRetrPackets"), ("HPR-MIB", "hprRtpShortReqTimer"), ("HPR-MIB", "hprRtpTopic"), ("HPR-MIB", "hprRtpRemTcid"), ("HPR-MIB", "hprRtpPathSwitchTrigger"), ("HPR-MIB", "hprRtpGlobeCtrState"), ("HPR-MIB", "hprRtpLivenessTimeouts"), ("HPR-MIB", "hprRtpPacketsDiscarded"), ("HPR-MIB", "hprRtpMaxSendRate"), ("HPR-MIB", "hprRtpStatusRemTcid"), ("HPR-MIB", "hprRtpBadErrPathSws"), ("HPR-MIB", "hprRtpOkErrPathSws"), ("HPR-MIB", "hprRtpStatusRemCpName"), ("HPR-MIB", "hprRtpState"), ("HPR-MIB", "hprRtpRemNceId"), )
hprAnrRoutingConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 2)).setObjects(("HPR-MIB", "hprAnrCounterState"), ("HPR-MIB", "hprAnrsAssigned"), ("HPR-MIB", "hprAnrType"), ("HPR-MIB", "hprAnrOutTgNum"), ("HPR-MIB", "hprAnrOutTgDest"), ("HPR-MIB", "hprAnrCounterStateTime"), ("HPR-MIB", "hprAnrCounterDisconTime"), ("HPR-MIB", "hprAnrPacketsReceived"), )
hprTransportUserConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 3)).setObjects(("HPR-MIB", "hprNceInstanceId"), ("HPR-MIB", "hprNceDefault"), ("HPR-MIB", "hprNceType"), )
hprGlobalConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 1)).setObjects(("HPR-MIB", "hprOperatorPathSwitchSupport"), ("HPR-MIB", "hprNodeCpName"), )

# Exports

# Module identity
mibBuilder.exportSymbols("HPR-MIB", PYSNMP_MODULE_ID=hprMIB)

# Types
mibBuilder.exportSymbols("HPR-MIB", HprNceTypes=HprNceTypes, HprRtpCounter=HprRtpCounter)

# Objects
mibBuilder.exportSymbols("HPR-MIB", hprMIB=hprMIB, hprObjects=hprObjects, hprGlobal=hprGlobal, hprNodeCpName=hprNodeCpName, hprOperatorPathSwitchSupport=hprOperatorPathSwitchSupport, hprAnrRouting=hprAnrRouting, hprAnrsAssigned=hprAnrsAssigned, hprAnrCounterState=hprAnrCounterState, hprAnrCounterStateTime=hprAnrCounterStateTime, hprAnrRoutingTable=hprAnrRoutingTable, hprAnrRoutingEntry=hprAnrRoutingEntry, hprAnrLabel=hprAnrLabel, hprAnrType=hprAnrType, hprAnrOutTgDest=hprAnrOutTgDest, hprAnrOutTgNum=hprAnrOutTgNum, hprAnrPacketsReceived=hprAnrPacketsReceived, hprAnrCounterDisconTime=hprAnrCounterDisconTime, hprTransportUser=hprTransportUser, hprNceTable=hprNceTable, hprNceEntry=hprNceEntry, hprNceId=hprNceId, hprNceType=hprNceType, hprNceDefault=hprNceDefault, hprNceInstanceId=hprNceInstanceId, hprRtp=hprRtp, hprRtpGlobe=hprRtpGlobe, hprRtpGlobeConnSetups=hprRtpGlobeConnSetups, hprRtpGlobeCtrState=hprRtpGlobeCtrState, hprRtpGlobeCtrStateTime=hprRtpGlobeCtrStateTime, hprRtpTable=hprRtpTable, hprRtpEntry=hprRtpEntry, hprRtpLocNceId=hprRtpLocNceId, hprRtpLocTcid=hprRtpLocTcid, hprRtpRemCpName=hprRtpRemCpName, hprRtpRemNceId=hprRtpRemNceId, hprRtpRemTcid=hprRtpRemTcid, hprRtpPathSwitchTrigger=hprRtpPathSwitchTrigger, hprRtpRscv=hprRtpRscv, hprRtpTopic=hprRtpTopic, hprRtpState=hprRtpState, hprRtpUpTime=hprRtpUpTime, hprRtpLivenessTimer=hprRtpLivenessTimer, hprRtpShortReqTimer=hprRtpShortReqTimer, hprRtpPathSwTimer=hprRtpPathSwTimer, hprRtpLivenessTimeouts=hprRtpLivenessTimeouts, hprRtpShortReqTimeouts=hprRtpShortReqTimeouts, hprRtpMaxSendRate=hprRtpMaxSendRate, hprRtpMinSendRate=hprRtpMinSendRate, hprRtpCurSendRate=hprRtpCurSendRate, hprRtpSmRdTripDelay=hprRtpSmRdTripDelay, hprRtpSendPackets=hprRtpSendPackets, hprRtpRecvPackets=hprRtpRecvPackets, hprRtpSendBytes=hprRtpSendBytes, hprRtpRecvBytes=hprRtpRecvBytes, hprRtpRetrPackets=hprRtpRetrPackets, hprRtpPacketsDiscarded=hprRtpPacketsDiscarded, hprRtpDetectGaps=hprRtpDetectGaps, hprRtpRateReqSends=hprRtpRateReqSends, hprRtpOkErrPathSws=hprRtpOkErrPathSws, hprRtpBadErrPathSws=hprRtpBadErrPathSws, hprRtpOkOpPathSws=hprRtpOkOpPathSws, hprRtpBadOpPathSws=hprRtpBadOpPathSws, hprRtpCounterDisconTime=hprRtpCounterDisconTime, hprRtpStatusTable=hprRtpStatusTable, hprRtpStatusEntry=hprRtpStatusEntry, hprRtpStatusLocNceId=hprRtpStatusLocNceId, hprRtpStatusLocTcid=hprRtpStatusLocTcid, hprRtpStatusIndex=hprRtpStatusIndex, hprRtpStatusStartTime=hprRtpStatusStartTime, hprRtpStatusEndTime=hprRtpStatusEndTime, hprRtpStatusRemCpName=hprRtpStatusRemCpName, hprRtpStatusRemNceId=hprRtpStatusRemNceId, hprRtpStatusRemTcid=hprRtpStatusRemTcid, hprRtpStatusNewRscv=hprRtpStatusNewRscv, hprRtpStatusOldRscv=hprRtpStatusOldRscv, hprRtpStatusCause=hprRtpStatusCause, hprRtpStatusLastAttemptResult=hprRtpStatusLastAttemptResult, hprConformance=hprConformance, hprCompliances=hprCompliances, hprGroups=hprGroups)

# Groups
mibBuilder.exportSymbols("HPR-MIB", hprRtpConfGroup=hprRtpConfGroup, hprAnrRoutingConfGroup=hprAnrRoutingConfGroup, hprTransportUserConfGroup=hprTransportUserConfGroup, hprGlobalConfGroup=hprGlobalConfGroup)
