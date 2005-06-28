# PySNMP SMI module. Autogenerated from smidump -f python RFC1381-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:31:04 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Types

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,2147483647L)
    pass

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass


# Objects

lapb = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16))
lapbAdmnTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 1))
lapbAdmnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 1, 1)).setIndexNames((0, "RFC1381-MIB", "lapbAdmnIndex"))
lapbAdmnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 1)).setColumnInitializer(MibVariable((), IfIndexType()).setMaxAccess("readonly"))
lapbAdmnStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("dte", 1), ("dce", 2), ("dxe", 3), )).clone(1)).setMaxAccess("readwrite"))
lapbAdmnControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("modulo8", 1), ("modulo128", 2), )).clone(1)).setMaxAccess("readwrite"))
lapbAdmnTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 4)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 5)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite"))
lapbAdmnReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite"))
lapbAdmnN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(20)).setMaxAccess("readwrite"))
lapbAdmnT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 9)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 10)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 11)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 12)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbAdmnActionInitiate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 13)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,5,1,2,)).subtype(namedValues=namedval.NamedValues(("sendSABM", 1), ("sendDISC", 2), ("sendDM", 3), ("none", 4), ("other", 5), )).clone(1)).setMaxAccess("readwrite"))
lapbAdmnActionRecvDM = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 14)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("sendSABM", 1), ("sendDISC", 2), ("other", 3), )).clone(1)).setMaxAccess("readwrite"))
lapbOperTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 2))
lapbOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 2, 1)).setIndexNames((0, "RFC1381-MIB", "lapbOperIndex"))
lapbOperIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 1)).setColumnInitializer(MibVariable((), IfIndexType()).setMaxAccess("readonly"))
lapbOperStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("dte", 1), ("dce", 2), ("dxe", 3), ))).setMaxAccess("readonly"))
lapbOperControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("modulo8", 1), ("modulo128", 2), ))).setMaxAccess("readonly"))
lapbOperTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 4)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readonly"))
lapbOperReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 5)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readonly"))
lapbOperTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127))).setMaxAccess("readonly"))
lapbOperReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127))).setMaxAccess("readonly"))
lapbOperN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
lapbOperT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 9)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readonly"))
lapbOperT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 10)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readonly"))
lapbOperT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 11)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readonly"))
lapbOperT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 12)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
lapbOperPortId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 13)).setColumnInitializer(MibVariable((), ObjectIdentifier()).setMaxAccess("readonly"))
lapbOperProtocolVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 14)).setColumnInitializer(MibVariable((), ObjectIdentifier()).setMaxAccess("readonly"))
lapbFlowTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 3))
lapbFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 3, 1)).setIndexNames((0, "RFC1381-MIB", "lapbFlowIfIndex"))
lapbFlowIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 1)).setColumnInitializer(MibVariable((), IfIndexType()).setMaxAccess("readonly"))
lapbFlowStateChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
lapbFlowChangeReason = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(12,5,7,8,1,9,13,2,4,11,10,6,3,)).subtype(namedValues=namedval.NamedValues(("notStarted", 1), ("frmrReceived", 10), ("frmrSent", 11), ("n2Timeout", 12), ("other", 13), ("abmEntered", 2), ("abmeEntered", 3), ("abmReset", 4), ("abmeReset", 5), ("dmReceived", 6), ("dmSent", 7), ("discReceived", 8), ("discSent", 9), ))).setMaxAccess("readonly"))
lapbFlowCurrentMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,6,1,8,13,12,10,11,5,2,16,15,9,14,4,17,7,)).subtype(namedValues=namedval.NamedValues(("disconnected", 1), ("bothStationsBusy", 10), ("waitingAckStationBusy", 11), ("waitingAckRemoteBusy", 12), ("waitingAckBothBusy", 13), ("rejFrameSentRemoteBusy", 14), ("xidFrameSent", 15), ("error", 16), ("other", 17), ("linkSetup", 2), ("frameReject", 3), ("disconnectRequest", 4), ("informationTransfer", 5), ("rejFrameSent", 6), ("waitingAcknowledgement", 7), ("stationBusy", 8), ("remoteStationBusy", 9), ))).setMaxAccess("readonly"))
lapbFlowBusyDefers = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
lapbFlowRejOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
lapbFlowRejInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
lapbFlowT1Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
lapbFlowFrmrSent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 9)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 7))).setMaxAccess("readonly"))
lapbFlowFrmrReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 10)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 7))).setMaxAccess("readonly"))
lapbFlowXidReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 11)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 8206))).setMaxAccess("readonly"))
lapbXidTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 4))
lapbXidEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 4, 1)).setIndexNames((0, "RFC1381-MIB", "lapbXidIndex"))
lapbXidIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 1)).setColumnInitializer(MibVariable((), IfIndexType()).setMaxAccess("readonly"))
lapbXidAdRIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 2)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite"))
lapbXidAdRAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 3)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite"))
lapbXidParameterUniqueIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 4)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite"))
lapbXidGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 5)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite"))
lapbXidPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 6)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite"))
lapbXidUserDataSubfield = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 7)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 8206)).clone('')).setMaxAccess("readwrite"))
lapbProtocolVersion = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5))
lapbProtocolIso7776v1986 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 1))
lapbProtocolCcittV1980 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 2))
lapbProtocolCcittV1984 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 3))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("RFC1381-MIB", IfIndexType=IfIndexType, PositiveInteger=PositiveInteger)

# Objects
mibBuilder.exportSymbols("RFC1381-MIB", lapb=lapb, lapbAdmnTable=lapbAdmnTable, lapbAdmnEntry=lapbAdmnEntry, lapbAdmnIndex=lapbAdmnIndex, lapbAdmnStationType=lapbAdmnStationType, lapbAdmnControlField=lapbAdmnControlField, lapbAdmnTransmitN1FrameSize=lapbAdmnTransmitN1FrameSize, lapbAdmnReceiveN1FrameSize=lapbAdmnReceiveN1FrameSize, lapbAdmnTransmitKWindowSize=lapbAdmnTransmitKWindowSize, lapbAdmnReceiveKWindowSize=lapbAdmnReceiveKWindowSize, lapbAdmnN2RxmitCount=lapbAdmnN2RxmitCount, lapbAdmnT1AckTimer=lapbAdmnT1AckTimer, lapbAdmnT2AckDelayTimer=lapbAdmnT2AckDelayTimer, lapbAdmnT3DisconnectTimer=lapbAdmnT3DisconnectTimer, lapbAdmnT4IdleTimer=lapbAdmnT4IdleTimer, lapbAdmnActionInitiate=lapbAdmnActionInitiate, lapbAdmnActionRecvDM=lapbAdmnActionRecvDM, lapbOperTable=lapbOperTable, lapbOperEntry=lapbOperEntry, lapbOperIndex=lapbOperIndex, lapbOperStationType=lapbOperStationType, lapbOperControlField=lapbOperControlField, lapbOperTransmitN1FrameSize=lapbOperTransmitN1FrameSize, lapbOperReceiveN1FrameSize=lapbOperReceiveN1FrameSize, lapbOperTransmitKWindowSize=lapbOperTransmitKWindowSize, lapbOperReceiveKWindowSize=lapbOperReceiveKWindowSize, lapbOperN2RxmitCount=lapbOperN2RxmitCount, lapbOperT1AckTimer=lapbOperT1AckTimer, lapbOperT2AckDelayTimer=lapbOperT2AckDelayTimer, lapbOperT3DisconnectTimer=lapbOperT3DisconnectTimer, lapbOperT4IdleTimer=lapbOperT4IdleTimer, lapbOperPortId=lapbOperPortId, lapbOperProtocolVersionId=lapbOperProtocolVersionId, lapbFlowTable=lapbFlowTable, lapbFlowEntry=lapbFlowEntry, lapbFlowIfIndex=lapbFlowIfIndex, lapbFlowStateChanges=lapbFlowStateChanges, lapbFlowChangeReason=lapbFlowChangeReason, lapbFlowCurrentMode=lapbFlowCurrentMode, lapbFlowBusyDefers=lapbFlowBusyDefers, lapbFlowRejOutPkts=lapbFlowRejOutPkts, lapbFlowRejInPkts=lapbFlowRejInPkts, lapbFlowT1Timeouts=lapbFlowT1Timeouts, lapbFlowFrmrSent=lapbFlowFrmrSent, lapbFlowFrmrReceived=lapbFlowFrmrReceived, lapbFlowXidReceived=lapbFlowXidReceived, lapbXidTable=lapbXidTable, lapbXidEntry=lapbXidEntry, lapbXidIndex=lapbXidIndex, lapbXidAdRIdentifier=lapbXidAdRIdentifier, lapbXidAdRAddress=lapbXidAdRAddress, lapbXidParameterUniqueIdentifier=lapbXidParameterUniqueIdentifier, lapbXidGroupAddress=lapbXidGroupAddress, lapbXidPortNumber=lapbXidPortNumber, lapbXidUserDataSubfield=lapbXidUserDataSubfield, lapbProtocolVersion=lapbProtocolVersion, lapbProtocolIso7776v1986=lapbProtocolIso7776v1986, lapbProtocolCcittV1980=lapbProtocolCcittV1980, lapbProtocolCcittV1984=lapbProtocolCcittV1984)
