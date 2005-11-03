# PySNMP SMI module. Autogenerated from smidump -f python RSVP-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:18 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( BitRate, BurstSize, MessageSize, Port, Protocol, QosService, SessionNumber, SessionType, intSrvFlowStatus, ) = mibBuilder.importSymbols("INTEGRATED-SERVICES-MIB", "BitRate", "BurstSize", "MessageSize", "Port", "Protocol", "QosService", "SessionNumber", "SessionType", "intSrvFlowStatus")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, TextualConvention, TestAndIncr, TimeInterval, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TestAndIncr", "TimeInterval", "TimeStamp", "TruthValue")

# Types

class RefreshInterval(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class RsvpEncapsulation(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,)
    namedValues = namedval.NamedValues(("ip", 1), ("udp", 2), ("both", 3), )
    pass


# Objects

rsvp = ModuleIdentity((1, 3, 6, 1, 2, 1, 51)).setRevisions(("1995-11-03 05:00",))
rsvpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 1))
rsvpSessionTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 1))
rsvpSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 1, 1)).setIndexNames((0, "RSVP-MIB", "rsvpSessionNumber"))
rsvpSessionNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 1), SessionNumber()).setMaxAccess("noaccess")
rsvpSessionType = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 2), SessionType()).setMaxAccess("readonly")
rsvpSessionDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readonly")
rsvpSessionDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
rsvpSessionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 5), Protocol()).setMaxAccess("readonly")
rsvpSessionPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 6), Port()).setMaxAccess("readonly")
rsvpSessionSenders = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
rsvpSessionReceivers = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
rsvpSessionRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
rsvpSenderTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 2))
rsvpSenderEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 2, 1)).setIndexNames((0, "RSVP-MIB", "rsvpSessionNumber"), (0, "RSVP-MIB", "rsvpSenderNumber"))
rsvpSenderNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 1), SessionNumber()).setMaxAccess("noaccess")
rsvpSenderType = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 2), SessionType()).setMaxAccess("readwrite")
rsvpSenderDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpSenderDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
rsvpSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
rsvpSenderProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 7), Protocol()).setMaxAccess("readwrite")
rsvpSenderDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 8), Port()).setMaxAccess("readwrite")
rsvpSenderPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 9), Port()).setMaxAccess("readwrite")
rsvpSenderFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
rsvpSenderHopAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpSenderHopLih = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
rsvpSenderInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 13), InterfaceIndex()).setMaxAccess("readwrite")
rsvpSenderTSpecRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 14), BitRate()).setMaxAccess("readwrite")
rsvpSenderTSpecPeakRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 15), BitRate()).setMaxAccess("readwrite")
rsvpSenderTSpecBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 16), BurstSize()).setMaxAccess("readwrite")
rsvpSenderTSpecMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 17), MessageSize()).setMaxAccess("readwrite")
rsvpSenderTSpecMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 18), MessageSize()).setMaxAccess("readwrite")
rsvpSenderInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 19), RefreshInterval()).setMaxAccess("readwrite")
rsvpSenderRSVPHop = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 20), TruthValue()).setMaxAccess("readwrite")
rsvpSenderLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 21), TimeStamp()).setMaxAccess("readonly")
rsvpSenderPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 22), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 65536))).setMaxAccess("readwrite")
rsvpSenderAdspecBreak = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 23), TruthValue()).setMaxAccess("readwrite")
rsvpSenderAdspecHopCount = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderAdspecPathBw = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 25), BitRate()).setMaxAccess("readwrite")
rsvpSenderAdspecMinLatency = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 26), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 27), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedSvc = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 28), TruthValue()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedBreak = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 29), TruthValue()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedCtot = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 30), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedDtot = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 31), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedCsum = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 32), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedDsum = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 33), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedHopCount = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 34), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedPathBw = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 35), BitRate()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedMinLatency = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 36), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecGuaranteedMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 37), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadSvc = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 38), TruthValue()).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadBreak = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 39), TruthValue()).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadHopCount = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadPathBw = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 41), BitRate()).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadMinLatency = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 42), Integer32()).setMaxAccess("readwrite")
rsvpSenderAdspecCtrlLoadMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 43), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
rsvpSenderStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 44), RowStatus()).setMaxAccess("readwrite")
rsvpSenderTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 45), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
rsvpSenderOutInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 3))
rsvpSenderOutInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 3, 1)).setIndexNames((0, "RSVP-MIB", "rsvpSessionNumber"), (0, "RSVP-MIB", "rsvpSenderNumber"), (0, "IF-MIB", "ifIndex"))
rsvpSenderOutInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 3, 1, 1), RowStatus()).setMaxAccess("readonly")
rsvpResvTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 4))
rsvpResvEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 4, 1)).setIndexNames((0, "RSVP-MIB", "rsvpSessionNumber"), (0, "RSVP-MIB", "rsvpResvNumber"))
rsvpResvNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 1), SessionNumber()).setMaxAccess("noaccess")
rsvpResvType = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 2), SessionType()).setMaxAccess("readwrite")
rsvpResvDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpResvSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpResvDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
rsvpResvSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
rsvpResvProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 7), Protocol()).setMaxAccess("readwrite")
rsvpResvDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 8), Port()).setMaxAccess("readwrite")
rsvpResvPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 9), Port()).setMaxAccess("readwrite")
rsvpResvHopAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
rsvpResvHopLih = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 11), Integer32()).setMaxAccess("readwrite")
rsvpResvInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 12), InterfaceIndex()).setMaxAccess("readwrite")
rsvpResvService = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 13), QosService()).setMaxAccess("readwrite")
rsvpResvTSpecRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 14), BitRate()).setMaxAccess("readwrite")
rsvpResvTSpecPeakRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 15), BitRate()).setMaxAccess("readwrite")
rsvpResvTSpecBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 16), BurstSize()).setMaxAccess("readwrite")
rsvpResvTSpecMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 17), MessageSize()).setMaxAccess("readwrite")
rsvpResvTSpecMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 18), MessageSize()).setMaxAccess("readwrite")
rsvpResvRSpecRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 19), BitRate()).setMaxAccess("readwrite")
rsvpResvRSpecSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 20), Integer32()).setMaxAccess("readwrite")
rsvpResvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 21), RefreshInterval()).setMaxAccess("readwrite")
rsvpResvScope = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 22), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 65536))).setMaxAccess("readwrite")
rsvpResvShared = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 23), TruthValue()).setMaxAccess("readwrite")
rsvpResvExplicit = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 24), TruthValue()).setMaxAccess("readwrite")
rsvpResvRSVPHop = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 25), TruthValue()).setMaxAccess("readwrite")
rsvpResvLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 26), TimeStamp()).setMaxAccess("readonly")
rsvpResvPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 27), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 65536))).setMaxAccess("readwrite")
rsvpResvStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 28), RowStatus()).setMaxAccess("readwrite")
rsvpResvTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 29), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
rsvpResvFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 30), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
rsvpResvFwdTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 5))
rsvpResvFwdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 5, 1)).setIndexNames((0, "RSVP-MIB", "rsvpSessionNumber"), (0, "RSVP-MIB", "rsvpResvFwdNumber"))
rsvpResvFwdNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 1), SessionNumber()).setMaxAccess("noaccess")
rsvpResvFwdType = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 2), SessionType()).setMaxAccess("readonly")
rsvpResvFwdDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readonly")
rsvpResvFwdSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readonly")
rsvpResvFwdDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
rsvpResvFwdSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
rsvpResvFwdProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 7), Protocol()).setMaxAccess("readonly")
rsvpResvFwdDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 8), Port()).setMaxAccess("readonly")
rsvpResvFwdPort = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 9), Port()).setMaxAccess("readonly")
rsvpResvFwdHopAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readonly")
rsvpResvFwdHopLih = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 11), Integer32()).setMaxAccess("readonly")
rsvpResvFwdInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 12), InterfaceIndex()).setMaxAccess("readonly")
rsvpResvFwdService = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 13), QosService()).setMaxAccess("readonly")
rsvpResvFwdTSpecRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 14), BitRate()).setMaxAccess("readonly")
rsvpResvFwdTSpecPeakRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 15), BitRate()).setMaxAccess("readonly")
rsvpResvFwdTSpecBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 16), BurstSize()).setMaxAccess("readonly")
rsvpResvFwdTSpecMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 17), MessageSize()).setMaxAccess("readonly")
rsvpResvFwdTSpecMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 18), MessageSize()).setMaxAccess("readonly")
rsvpResvFwdRSpecRate = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 19), BitRate()).setMaxAccess("readonly")
rsvpResvFwdRSpecSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 20), Integer32()).setMaxAccess("readonly")
rsvpResvFwdInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 21), RefreshInterval()).setMaxAccess("readonly")
rsvpResvFwdScope = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 22), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 65536))).setMaxAccess("readonly")
rsvpResvFwdShared = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 23), TruthValue()).setMaxAccess("readonly")
rsvpResvFwdExplicit = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 24), TruthValue()).setMaxAccess("readonly")
rsvpResvFwdRSVPHop = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 25), TruthValue()).setMaxAccess("readonly")
rsvpResvFwdLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 26), TimeStamp()).setMaxAccess("readonly")
rsvpResvFwdPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 27), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 65536))).setMaxAccess("readonly")
rsvpResvFwdStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 28), RowStatus()).setMaxAccess("readwrite")
rsvpResvFwdTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 29), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
rsvpResvFwdFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 30), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
rsvpIfTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 6))
rsvpIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 6, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
rsvpIfUdpNbrs = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 1), Gauge32()).setMaxAccess("readonly")
rsvpIfIpNbrs = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 2), Gauge32()).setMaxAccess("readonly")
rsvpIfNbrs = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 3), Gauge32()).setMaxAccess("readonly")
rsvpIfRefreshBlockadeMultiple = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65536)).clone(4)).setMaxAccess("readwrite")
rsvpIfRefreshMultiple = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65536)).clone(3)).setMaxAccess("readwrite")
rsvpIfTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readwrite")
rsvpIfRefreshInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 7), TimeInterval()).setMaxAccess("readwrite")
rsvpIfRouteDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 8), TimeInterval()).setMaxAccess("readwrite")
rsvpIfEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 9), TruthValue()).setMaxAccess("readwrite")
rsvpIfUdpRequired = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 10), TruthValue()).setMaxAccess("readwrite")
rsvpIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 11), RowStatus()).setMaxAccess("readwrite")
rsvpNbrTable = MibTable((1, 3, 6, 1, 2, 1, 51, 1, 7))
rsvpNbrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 51, 1, 7, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RSVP-MIB", "rsvpNbrAddress"))
rsvpNbrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("noaccess")
rsvpNbrProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 2), RsvpEncapsulation()).setMaxAccess("readwrite")
rsvpNbrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 3), RowStatus()).setMaxAccess("readwrite")
rsvpGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 2))
rsvpBadPackets = MibScalar((1, 3, 6, 1, 2, 1, 51, 2, 1), Gauge32()).setMaxAccess("readonly")
rsvpSenderNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 51, 2, 2), TestAndIncr()).setMaxAccess("readwrite")
rsvpResvNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 51, 2, 3), TestAndIncr()).setMaxAccess("readwrite")
rsvpResvFwdNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 51, 2, 4), TestAndIncr()).setMaxAccess("readwrite")
rsvpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 3))
rsvpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 3, 0))
rsvpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 4))
rsvpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 4, 1))
rsvpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 51, 4, 2))

# Augmentions

# Notifications

newFlow = NotificationType((1, 3, 6, 1, 2, 1, 51, 3, 0, 1)).setObjects(("RSVP-MIB", "rsvpResvFwdStatus"), ("RSVP-MIB", "rsvpSessionDestAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"), ("RSVP-MIB", "rsvpSenderStatus"), ("RSVP-MIB", "rsvpResvStatus"), )
lostFlow = NotificationType((1, 3, 6, 1, 2, 1, 51, 3, 0, 2)).setObjects(("RSVP-MIB", "rsvpResvFwdStatus"), ("RSVP-MIB", "rsvpSessionDestAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"), ("RSVP-MIB", "rsvpSenderStatus"), ("RSVP-MIB", "rsvpResvStatus"), )

# Groups

rsvpNbrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 7)).setObjects(("RSVP-MIB", "rsvpNbrProtocol"), ("RSVP-MIB", "rsvpNbrStatus"), )
rsvpNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 8)).setObjects(("RSVP-MIB", "newFlow"), ("RSVP-MIB", "lostFlow"), )
rsvpResvGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 3)).setObjects(("RSVP-MIB", "rsvpResvNewIndex"), ("RSVP-MIB", "rsvpResvStatus"), ("RSVP-MIB", "rsvpResvShared"), ("RSVP-MIB", "rsvpResvHopAddr"), ("RSVP-MIB", "rsvpResvDestPort"), ("RSVP-MIB", "rsvpResvPolicy"), ("RSVP-MIB", "rsvpResvService"), ("RSVP-MIB", "rsvpResvTSpecMaxTU"), ("RSVP-MIB", "rsvpResvInterval"), ("RSVP-MIB", "rsvpResvScope"), ("RSVP-MIB", "rsvpResvTSpecPeakRate"), ("RSVP-MIB", "rsvpResvProtocol"), ("RSVP-MIB", "rsvpResvTSpecMinTU"), ("RSVP-MIB", "rsvpResvRSpecRate"), ("RSVP-MIB", "rsvpResvType"), ("RSVP-MIB", "rsvpResvRSVPHop"), ("RSVP-MIB", "rsvpResvTSpecRate"), ("RSVP-MIB", "rsvpResvDestAddr"), ("RSVP-MIB", "rsvpResvSenderAddr"), ("RSVP-MIB", "rsvpResvRSpecSlack"), ("RSVP-MIB", "rsvpResvInterface"), ("RSVP-MIB", "rsvpResvTSpecBurst"), ("RSVP-MIB", "rsvpResvPort"), ("RSVP-MIB", "rsvpResvLastChange"), ("RSVP-MIB", "rsvpResvExplicit"), ("RSVP-MIB", "rsvpResvDestAddrLength"), ("RSVP-MIB", "rsvpResvSenderAddrLength"), ("RSVP-MIB", "rsvpResvHopLih"), )
rsvpSessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 1)).setObjects(("RSVP-MIB", "rsvpSessionSenders"), ("RSVP-MIB", "rsvpSessionDestAddrLength"), ("RSVP-MIB", "rsvpSessionReceivers"), ("RSVP-MIB", "rsvpSessionDestAddr"), ("RSVP-MIB", "rsvpSessionType"), ("RSVP-MIB", "rsvpSessionPort"), ("RSVP-MIB", "rsvpSessionRequests"), ("RSVP-MIB", "rsvpSessionProtocol"), )
rsvpIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 6)).setObjects(("RSVP-MIB", "rsvpIfIpNbrs"), ("RSVP-MIB", "rsvpIfEnabled"), ("RSVP-MIB", "rsvpIfRefreshInterval"), ("RSVP-MIB", "rsvpIfTTL"), ("RSVP-MIB", "rsvpIfNbrs"), ("RSVP-MIB", "rsvpIfUdpNbrs"), ("RSVP-MIB", "rsvpIfUdpRequired"), ("RSVP-MIB", "rsvpIfRefreshBlockadeMultiple"), ("RSVP-MIB", "rsvpIfRefreshMultiple"), ("RSVP-MIB", "rsvpIfStatus"), ("RSVP-MIB", "rsvpIfRouteDelay"), )
rsvpResvFwdGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 4)).setObjects(("RSVP-MIB", "rsvpResvFwdExplicit"), ("RSVP-MIB", "rsvpResvFwdTSpecMaxTU"), ("RSVP-MIB", "rsvpResvFwdLastChange"), ("RSVP-MIB", "rsvpResvFwdTSpecRate"), ("RSVP-MIB", "rsvpResvFwdNewIndex"), ("RSVP-MIB", "rsvpResvFwdTSpecMinTU"), ("RSVP-MIB", "rsvpResvFwdHopLih"), ("RSVP-MIB", "rsvpResvFwdDestPort"), ("RSVP-MIB", "rsvpResvFwdRSpecRate"), ("RSVP-MIB", "rsvpResvFwdDestAddrLength"), ("RSVP-MIB", "rsvpResvFwdShared"), ("RSVP-MIB", "rsvpResvFwdStatus"), ("RSVP-MIB", "rsvpResvFwdSenderAddrLength"), ("RSVP-MIB", "rsvpResvFwdTSpecPeakRate"), ("RSVP-MIB", "rsvpResvFwdProtocol"), ("RSVP-MIB", "rsvpResvFwdScope"), ("RSVP-MIB", "rsvpResvFwdRSVPHop"), ("RSVP-MIB", "rsvpResvFwdSenderAddr"), ("RSVP-MIB", "rsvpResvFwdInterval"), ("RSVP-MIB", "rsvpResvFwdHopAddr"), ("RSVP-MIB", "rsvpResvFwdPort"), ("RSVP-MIB", "rsvpResvFwdPolicy"), ("RSVP-MIB", "rsvpResvFwdInterface"), ("RSVP-MIB", "rsvpResvFwdDestAddr"), ("RSVP-MIB", "rsvpResvFwdService"), ("RSVP-MIB", "rsvpResvFwdTSpecBurst"), ("RSVP-MIB", "rsvpResvFwdRSpecSlack"), ("RSVP-MIB", "rsvpResvFwdType"), )
rsvpSenderGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 51, 4, 1, 2)).setObjects(("RSVP-MIB", "rsvpSenderInterval"), ("RSVP-MIB", "rsvpSenderAdspecBreak"), ("RSVP-MIB", "rsvpSenderAdspecHopCount"), ("RSVP-MIB", "rsvpSenderHopAddr"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedMtu"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadMtu"), ("RSVP-MIB", "rsvpSenderInterface"), ("RSVP-MIB", "rsvpSenderTSpecMaxTU"), ("RSVP-MIB", "rsvpSenderAdspecPathBw"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedDsum"), ("RSVP-MIB", "rsvpSenderTSpecBurst"), ("RSVP-MIB", "rsvpSenderAddr"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadBreak"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedCtot"), ("RSVP-MIB", "rsvpSenderStatus"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadPathBw"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedDtot"), ("RSVP-MIB", "rsvpSenderAddrLength"), ("RSVP-MIB", "rsvpSenderAdspecMinLatency"), ("RSVP-MIB", "rsvpSenderTSpecRate"), ("RSVP-MIB", "rsvpSenderTSpecMinTU"), ("RSVP-MIB", "rsvpSenderDestPort"), ("RSVP-MIB", "rsvpSenderNewIndex"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedCsum"), ("RSVP-MIB", "rsvpSenderDestAddr"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadHopCount"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedBreak"), ("RSVP-MIB", "rsvpSenderPort"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedHopCount"), ("RSVP-MIB", "rsvpSenderAdspecMtu"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedMinLatency"), ("RSVP-MIB", "rsvpSenderDestAddrLength"), ("RSVP-MIB", "rsvpSenderHopLih"), ("RSVP-MIB", "rsvpSenderPolicy"), ("RSVP-MIB", "rsvpSenderType"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedPathBw"), ("RSVP-MIB", "rsvpSenderProtocol"), ("RSVP-MIB", "rsvpSenderTSpecPeakRate"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadMinLatency"), ("RSVP-MIB", "rsvpSenderLastChange"), ("RSVP-MIB", "rsvpSenderRSVPHop"), ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadSvc"), ("RSVP-MIB", "rsvpSenderAdspecGuaranteedSvc"), )

# Exports

# Module identity
mibBuilder.exportSymbols("RSVP-MIB", PYSNMP_MODULE_ID=rsvp)

# Types
mibBuilder.exportSymbols("RSVP-MIB", RefreshInterval=RefreshInterval, RsvpEncapsulation=RsvpEncapsulation)

# Objects
mibBuilder.exportSymbols("RSVP-MIB", rsvp=rsvp, rsvpObjects=rsvpObjects, rsvpSessionTable=rsvpSessionTable, rsvpSessionEntry=rsvpSessionEntry, rsvpSessionNumber=rsvpSessionNumber, rsvpSessionType=rsvpSessionType, rsvpSessionDestAddr=rsvpSessionDestAddr, rsvpSessionDestAddrLength=rsvpSessionDestAddrLength, rsvpSessionProtocol=rsvpSessionProtocol, rsvpSessionPort=rsvpSessionPort, rsvpSessionSenders=rsvpSessionSenders, rsvpSessionReceivers=rsvpSessionReceivers, rsvpSessionRequests=rsvpSessionRequests, rsvpSenderTable=rsvpSenderTable, rsvpSenderEntry=rsvpSenderEntry, rsvpSenderNumber=rsvpSenderNumber, rsvpSenderType=rsvpSenderType, rsvpSenderDestAddr=rsvpSenderDestAddr, rsvpSenderAddr=rsvpSenderAddr, rsvpSenderDestAddrLength=rsvpSenderDestAddrLength, rsvpSenderAddrLength=rsvpSenderAddrLength, rsvpSenderProtocol=rsvpSenderProtocol, rsvpSenderDestPort=rsvpSenderDestPort, rsvpSenderPort=rsvpSenderPort, rsvpSenderFlowId=rsvpSenderFlowId, rsvpSenderHopAddr=rsvpSenderHopAddr, rsvpSenderHopLih=rsvpSenderHopLih, rsvpSenderInterface=rsvpSenderInterface, rsvpSenderTSpecRate=rsvpSenderTSpecRate, rsvpSenderTSpecPeakRate=rsvpSenderTSpecPeakRate, rsvpSenderTSpecBurst=rsvpSenderTSpecBurst, rsvpSenderTSpecMinTU=rsvpSenderTSpecMinTU, rsvpSenderTSpecMaxTU=rsvpSenderTSpecMaxTU, rsvpSenderInterval=rsvpSenderInterval, rsvpSenderRSVPHop=rsvpSenderRSVPHop, rsvpSenderLastChange=rsvpSenderLastChange, rsvpSenderPolicy=rsvpSenderPolicy, rsvpSenderAdspecBreak=rsvpSenderAdspecBreak, rsvpSenderAdspecHopCount=rsvpSenderAdspecHopCount, rsvpSenderAdspecPathBw=rsvpSenderAdspecPathBw, rsvpSenderAdspecMinLatency=rsvpSenderAdspecMinLatency, rsvpSenderAdspecMtu=rsvpSenderAdspecMtu, rsvpSenderAdspecGuaranteedSvc=rsvpSenderAdspecGuaranteedSvc, rsvpSenderAdspecGuaranteedBreak=rsvpSenderAdspecGuaranteedBreak, rsvpSenderAdspecGuaranteedCtot=rsvpSenderAdspecGuaranteedCtot, rsvpSenderAdspecGuaranteedDtot=rsvpSenderAdspecGuaranteedDtot, rsvpSenderAdspecGuaranteedCsum=rsvpSenderAdspecGuaranteedCsum, rsvpSenderAdspecGuaranteedDsum=rsvpSenderAdspecGuaranteedDsum, rsvpSenderAdspecGuaranteedHopCount=rsvpSenderAdspecGuaranteedHopCount, rsvpSenderAdspecGuaranteedPathBw=rsvpSenderAdspecGuaranteedPathBw, rsvpSenderAdspecGuaranteedMinLatency=rsvpSenderAdspecGuaranteedMinLatency, rsvpSenderAdspecGuaranteedMtu=rsvpSenderAdspecGuaranteedMtu, rsvpSenderAdspecCtrlLoadSvc=rsvpSenderAdspecCtrlLoadSvc, rsvpSenderAdspecCtrlLoadBreak=rsvpSenderAdspecCtrlLoadBreak, rsvpSenderAdspecCtrlLoadHopCount=rsvpSenderAdspecCtrlLoadHopCount, rsvpSenderAdspecCtrlLoadPathBw=rsvpSenderAdspecCtrlLoadPathBw, rsvpSenderAdspecCtrlLoadMinLatency=rsvpSenderAdspecCtrlLoadMinLatency, rsvpSenderAdspecCtrlLoadMtu=rsvpSenderAdspecCtrlLoadMtu, rsvpSenderStatus=rsvpSenderStatus, rsvpSenderTTL=rsvpSenderTTL, rsvpSenderOutInterfaceTable=rsvpSenderOutInterfaceTable, rsvpSenderOutInterfaceEntry=rsvpSenderOutInterfaceEntry, rsvpSenderOutInterfaceStatus=rsvpSenderOutInterfaceStatus, rsvpResvTable=rsvpResvTable, rsvpResvEntry=rsvpResvEntry, rsvpResvNumber=rsvpResvNumber, rsvpResvType=rsvpResvType, rsvpResvDestAddr=rsvpResvDestAddr, rsvpResvSenderAddr=rsvpResvSenderAddr, rsvpResvDestAddrLength=rsvpResvDestAddrLength, rsvpResvSenderAddrLength=rsvpResvSenderAddrLength, rsvpResvProtocol=rsvpResvProtocol, rsvpResvDestPort=rsvpResvDestPort, rsvpResvPort=rsvpResvPort, rsvpResvHopAddr=rsvpResvHopAddr, rsvpResvHopLih=rsvpResvHopLih, rsvpResvInterface=rsvpResvInterface, rsvpResvService=rsvpResvService, rsvpResvTSpecRate=rsvpResvTSpecRate, rsvpResvTSpecPeakRate=rsvpResvTSpecPeakRate, rsvpResvTSpecBurst=rsvpResvTSpecBurst, rsvpResvTSpecMinTU=rsvpResvTSpecMinTU, rsvpResvTSpecMaxTU=rsvpResvTSpecMaxTU, rsvpResvRSpecRate=rsvpResvRSpecRate, rsvpResvRSpecSlack=rsvpResvRSpecSlack, rsvpResvInterval=rsvpResvInterval, rsvpResvScope=rsvpResvScope, rsvpResvShared=rsvpResvShared, rsvpResvExplicit=rsvpResvExplicit, rsvpResvRSVPHop=rsvpResvRSVPHop, rsvpResvLastChange=rsvpResvLastChange, rsvpResvPolicy=rsvpResvPolicy, rsvpResvStatus=rsvpResvStatus, rsvpResvTTL=rsvpResvTTL, rsvpResvFlowId=rsvpResvFlowId, rsvpResvFwdTable=rsvpResvFwdTable, rsvpResvFwdEntry=rsvpResvFwdEntry, rsvpResvFwdNumber=rsvpResvFwdNumber, rsvpResvFwdType=rsvpResvFwdType, rsvpResvFwdDestAddr=rsvpResvFwdDestAddr, rsvpResvFwdSenderAddr=rsvpResvFwdSenderAddr, rsvpResvFwdDestAddrLength=rsvpResvFwdDestAddrLength, rsvpResvFwdSenderAddrLength=rsvpResvFwdSenderAddrLength, rsvpResvFwdProtocol=rsvpResvFwdProtocol, rsvpResvFwdDestPort=rsvpResvFwdDestPort, rsvpResvFwdPort=rsvpResvFwdPort, rsvpResvFwdHopAddr=rsvpResvFwdHopAddr, rsvpResvFwdHopLih=rsvpResvFwdHopLih, rsvpResvFwdInterface=rsvpResvFwdInterface, rsvpResvFwdService=rsvpResvFwdService, rsvpResvFwdTSpecRate=rsvpResvFwdTSpecRate, rsvpResvFwdTSpecPeakRate=rsvpResvFwdTSpecPeakRate, rsvpResvFwdTSpecBurst=rsvpResvFwdTSpecBurst, rsvpResvFwdTSpecMinTU=rsvpResvFwdTSpecMinTU, rsvpResvFwdTSpecMaxTU=rsvpResvFwdTSpecMaxTU, rsvpResvFwdRSpecRate=rsvpResvFwdRSpecRate, rsvpResvFwdRSpecSlack=rsvpResvFwdRSpecSlack, rsvpResvFwdInterval=rsvpResvFwdInterval, rsvpResvFwdScope=rsvpResvFwdScope, rsvpResvFwdShared=rsvpResvFwdShared, rsvpResvFwdExplicit=rsvpResvFwdExplicit, rsvpResvFwdRSVPHop=rsvpResvFwdRSVPHop, rsvpResvFwdLastChange=rsvpResvFwdLastChange, rsvpResvFwdPolicy=rsvpResvFwdPolicy, rsvpResvFwdStatus=rsvpResvFwdStatus, rsvpResvFwdTTL=rsvpResvFwdTTL, rsvpResvFwdFlowId=rsvpResvFwdFlowId, rsvpIfTable=rsvpIfTable)
mibBuilder.exportSymbols("RSVP-MIB", rsvpIfEntry=rsvpIfEntry, rsvpIfUdpNbrs=rsvpIfUdpNbrs, rsvpIfIpNbrs=rsvpIfIpNbrs, rsvpIfNbrs=rsvpIfNbrs, rsvpIfRefreshBlockadeMultiple=rsvpIfRefreshBlockadeMultiple, rsvpIfRefreshMultiple=rsvpIfRefreshMultiple, rsvpIfTTL=rsvpIfTTL, rsvpIfRefreshInterval=rsvpIfRefreshInterval, rsvpIfRouteDelay=rsvpIfRouteDelay, rsvpIfEnabled=rsvpIfEnabled, rsvpIfUdpRequired=rsvpIfUdpRequired, rsvpIfStatus=rsvpIfStatus, rsvpNbrTable=rsvpNbrTable, rsvpNbrEntry=rsvpNbrEntry, rsvpNbrAddress=rsvpNbrAddress, rsvpNbrProtocol=rsvpNbrProtocol, rsvpNbrStatus=rsvpNbrStatus, rsvpGenObjects=rsvpGenObjects, rsvpBadPackets=rsvpBadPackets, rsvpSenderNewIndex=rsvpSenderNewIndex, rsvpResvNewIndex=rsvpResvNewIndex, rsvpResvFwdNewIndex=rsvpResvFwdNewIndex, rsvpNotificationsPrefix=rsvpNotificationsPrefix, rsvpNotifications=rsvpNotifications, rsvpConformance=rsvpConformance, rsvpGroups=rsvpGroups, rsvpCompliances=rsvpCompliances)

# Notifications
mibBuilder.exportSymbols("RSVP-MIB", newFlow=newFlow, lostFlow=lostFlow)

# Groups
mibBuilder.exportSymbols("RSVP-MIB", rsvpNbrGroup=rsvpNbrGroup, rsvpNotificationGroup=rsvpNotificationGroup, rsvpResvGroup=rsvpResvGroup, rsvpSessionGroup=rsvpSessionGroup, rsvpIfGroup=rsvpIfGroup, rsvpResvFwdGroup=rsvpResvFwdGroup, rsvpSenderGroup=rsvpSenderGroup)
