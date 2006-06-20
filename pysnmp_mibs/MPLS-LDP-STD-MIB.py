# PySNMP SMI module. Autogenerated from smidump -f python MPLS-LDP-STD-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:12 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( IndexInteger, IndexIntegerNextFree, ) = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "IndexIntegerNextFree")
( InetAddress, InetAddressPrefixLength, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType", "InetPortNumber")
( MplsIndexType, ) = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "MplsIndexType")
( MplsLabelDistributionMethod, MplsLdpIdentifier, MplsLdpLabelType, MplsLspType, MplsLsrIdentifier, MplsRetentionMode, mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabelDistributionMethod", "MplsLdpIdentifier", "MplsLdpLabelType", "MplsLspType", "MplsLsrIdentifier", "MplsRetentionMode", "mplsStdMIB")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TimeInterval, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TimeInterval", "TimeStamp", "TruthValue")

# Objects

mplsLdpStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 4)).setRevisions(("2004-06-03 00:00",))
mplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 0))
mplsLdpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1))
mplsLdpLsrObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1))
mplsLdpLsrId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1, 1), MplsLsrIdentifier()).setMaxAccess("readonly")
mplsLdpLsrLoopDetectionCapable = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,5,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("other", 2), ("hopCount", 3), ("pathVector", 4), ("hopCountAndPathVector", 5), ))).setMaxAccess("readonly")
mplsLdpEntityObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2))
mplsLdpEntityLastChange = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
mplsLdpEntityIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 2), IndexIntegerNextFree()).setMaxAccess("readonly")
mplsLdpEntityTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3))
mplsLdpEntityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"))
mplsLdpEntityLdpId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 1), MplsLdpIdentifier()).setMaxAccess("noaccess")
mplsLdpEntityIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 2), IndexInteger()).setMaxAccess("noaccess")
mplsLdpEntityProtocolVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
mplsLdpEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("enable", 1), ("disable", 2), )).clone(1)).setMaxAccess("readcreate")
mplsLdpEntityOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3), ))).setMaxAccess("readonly")
mplsLdpEntityTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 6), InetPortNumber()).setMaxAccess("readcreate")
mplsLdpEntityUdpDscPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
mplsLdpEntityMaxPduLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 8), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(256, 65535))).setMaxAccess("readcreate")
mplsLdpEntityKeepAliveHoldTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 9), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
mplsLdpEntityHelloHoldTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 10), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
mplsLdpEntityInitSessionThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 100)).clone(8)).setMaxAccess("readcreate")
mplsLdpEntityLabelDistMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 12), MplsLabelDistributionMethod()).setMaxAccess("readcreate")
mplsLdpEntityLabelRetentionMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 13), MplsRetentionMode()).setMaxAccess("readcreate")
mplsLdpEntityPathVectorLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
mplsLdpEntityHopCountLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readcreate")
mplsLdpEntityTransportAddrKind = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 16), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("interface", 1), ("loopback", 2), )).clone(2)).setMaxAccess("readcreate")
mplsLdpEntityTargetPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 17), TruthValue()).setMaxAccess("readcreate")
mplsLdpEntityTargetPeerAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 18), InetAddressType()).setMaxAccess("readcreate")
mplsLdpEntityTargetPeerAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 19), InetAddress()).setMaxAccess("readcreate")
mplsLdpEntityLabelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 20), MplsLdpLabelType()).setMaxAccess("readcreate")
mplsLdpEntityDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 21), TimeStamp()).setMaxAccess("readonly")
mplsLdpEntityStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 22), StorageType()).setMaxAccess("readcreate")
mplsLdpEntityRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 23), RowStatus()).setMaxAccess("readcreate")
mplsLdpEntityStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4))
mplsLdpEntityStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1))
mplsLdpEntityStatsSessionAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsSessionRejectedNoHelloErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsSessionRejectedAdErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsSessionRejectedMaxPduErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsSessionRejectedLRErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsBadLdpIdentifierErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsBadPduLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsBadMessageLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsBadTlvLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsMalformedTlvValueErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsKeepAliveTimerExpErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsShutdownReceivedNotifications = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
mplsLdpEntityStatsShutdownSentNotifications = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 13), Counter32()).setMaxAccess("readonly")
mplsLdpSessionObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3))
mplsLdpPeerLastChange = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 1), TimeStamp()).setMaxAccess("readonly")
mplsLdpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2))
mplsLdpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"))
mplsLdpPeerLdpId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 1), MplsLdpIdentifier()).setMaxAccess("noaccess")
mplsLdpPeerLabelDistMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 2), MplsLabelDistributionMethod()).setMaxAccess("readonly")
mplsLdpPeerPathVectorLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
mplsLdpPeerTransportAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
mplsLdpPeerTransportAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
mplsLdpSessionTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3))
mplsLdpSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1))
mplsLdpSessionStateLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 1), TimeStamp()).setMaxAccess("readonly")
mplsLdpSessionState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,1,5,2,)).subtype(namedValues=namedval.NamedValues(("nonexistent", 1), ("initialized", 2), ("openrec", 3), ("opensent", 4), ("operational", 5), ))).setMaxAccess("readonly")
mplsLdpSessionRole = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("active", 2), ("passive", 3), ))).setMaxAccess("readonly")
mplsLdpSessionProtocolVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 4), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
mplsLdpSessionKeepAliveHoldTimeRem = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 5), TimeInterval()).setMaxAccess("readonly")
mplsLdpSessionKeepAliveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 6), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
mplsLdpSessionMaxPduLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 7), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
mplsLdpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
mplsLdpSessionStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4))
mplsLdpSessionStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1))
mplsLdpSessionStatsUnknownMesTypeErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1, 1), Counter32()).setMaxAccess("readonly")
mplsLdpSessionStatsUnknownTlvErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1, 2), Counter32()).setMaxAccess("readonly")
mplsLdpHelloAdjacencyObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5))
mplsLdpHelloAdjacencyTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1))
mplsLdpHelloAdjacencyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyIndex"))
mplsLdpHelloAdjacencyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
mplsLdpHelloAdjacencyHoldTimeRem = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 2), TimeInterval()).setMaxAccess("readonly")
mplsLdpHelloAdjacencyHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
mplsLdpHelloAdjacencyType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("link", 1), ("targeted", 2), ))).setMaxAccess("readonly")
mplsInSegmentLdpLspTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6))
mplsInSegmentLdpLspEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspIndex"))
mplsInSegmentLdpLspIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 1), MplsIndexType()).setMaxAccess("noaccess")
mplsInSegmentLdpLspLabelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 2), MplsLdpLabelType()).setMaxAccess("readonly")
mplsInSegmentLdpLspType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 3), MplsLspType()).setMaxAccess("readonly")
mplsOutSegmentLdpLspTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7))
mplsOutSegmentLdpLspEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspIndex"))
mplsOutSegmentLdpLspIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 1), MplsIndexType()).setMaxAccess("noaccess")
mplsOutSegmentLdpLspLabelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 2), MplsLdpLabelType()).setMaxAccess("readonly")
mplsOutSegmentLdpLspType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 3), MplsLspType()).setMaxAccess("readonly")
mplsFecObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8))
mplsFecLastChange = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 1), TimeStamp()).setMaxAccess("readonly")
mplsFecIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 2), IndexIntegerNextFree()).setMaxAccess("readonly")
mplsFecTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3))
mplsFecEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsFecIndex"))
mplsFecIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 1), IndexInteger()).setMaxAccess("noaccess")
mplsFecType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("prefix", 1), ("hostAddress", 2), ))).setMaxAccess("readcreate")
mplsFecAddrPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 3), InetAddressPrefixLength()).setMaxAccess("readcreate")
mplsFecAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 4), InetAddressType()).setMaxAccess("readcreate")
mplsFecAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 5), InetAddress()).setMaxAccess("readcreate")
mplsFecStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
mplsFecRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
mplsLdpLspFecLastChange = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 9), TimeStamp()).setMaxAccess("readonly")
mplsLdpLspFecTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10))
mplsLdpLspFecEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecSegment"), (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecSegmentIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecIndex"))
mplsLdpLspFecSegment = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("inSegment", 1), ("outSegment", 2), ))).setMaxAccess("noaccess")
mplsLdpLspFecSegmentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 2), MplsIndexType()).setMaxAccess("noaccess")
mplsLdpLspFecIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 3), IndexInteger()).setMaxAccess("noaccess")
mplsLdpLspFecStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 4), StorageType()).setMaxAccess("readcreate")
mplsLdpLspFecRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 5), RowStatus()).setMaxAccess("readcreate")
mplsLdpSessionPeerAddrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11))
mplsLdpSessionPeerAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpSessionPeerAddrIndex"))
mplsLdpSessionPeerAddrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
mplsLdpSessionPeerNextHopAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 2), InetAddressType()).setMaxAccess("readonly")
mplsLdpSessionPeerNextHopAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 3), InetAddress()).setMaxAccess("readonly")
mplsLdpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 2))
mplsLdpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1))
mplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 2))

# Augmentions
mplsLdpPeerEntry.registerAugmentions(("MPLS-LDP-STD-MIB", "mplsLdpSessionEntry"))
apply(mplsLdpSessionEntry.setIndexNames, mplsLdpPeerEntry.getIndexNames())
mplsLdpEntityEntry.registerAugmentions(("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsEntry"))
apply(mplsLdpEntityStatsEntry.setIndexNames, mplsLdpEntityEntry.getIndexNames())
mplsLdpPeerEntry.registerAugmentions(("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsEntry"))
apply(mplsLdpSessionStatsEntry.setIndexNames, mplsLdpPeerEntry.getIndexNames())

# Notifications

mplsLdpSessionDown = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 4)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpSessionState"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"), )
mplsLdpInitSessionThresholdExceeded = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 1)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpEntityInitSessionThreshold"), )
mplsLdpSessionUp = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 3)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpSessionState"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"), )
mplsLdpPathVectorLimitMismatch = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 2)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpPeerPathVectorLimit"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityPathVectorLimit"), )

# Groups

mplsLdpGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 1)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpSessionPeerNextHopAddrType"), ("MPLS-LDP-STD-MIB", "mplsLdpLsrId"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityTransportAddrKind"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityKeepAliveHoldTimer"), ("MPLS-LDP-STD-MIB", "mplsFecRowStatus"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadMessageLengthErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpPeerLabelDistMethod"), ("MPLS-LDP-STD-MIB", "mplsLdpPeerTransportAddrType"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityInitSessionThreshold"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionPeerNextHopAddr"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedLRErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityIndexNext"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadPduLengthErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityProtocolVersion"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeerAddrType"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionMaxPduLength"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityUdpDscPort"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadTlvLengthErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityHelloHoldTimer"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelType"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityOperStatus"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeerAddr"), ("MPLS-LDP-STD-MIB", "mplsFecLastChange"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsShutdownSentNotifications"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityHopCountLimit"), ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyHoldTime"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionRole"), ("MPLS-LDP-STD-MIB", "mplsFecIndexNext"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelDistMethod"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityDiscontinuityTime"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedMaxPduErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelRetentionMode"), ("MPLS-LDP-STD-MIB", "mplsLdpPeerLastChange"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionKeepAliveHoldTimeRem"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeer"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionProtocolVersion"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsShutdownReceivedNotifications"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityLastChange"), ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyType"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadLdpIdentifierErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityTcpPort"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionState"), ("MPLS-LDP-STD-MIB", "mplsLdpPeerPathVectorLimit"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsKeepAliveTimerExpErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsMalformedTlvValueErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityRowStatus"), ("MPLS-LDP-STD-MIB", "mplsLdpLsrLoopDetectionCapable"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedAdErrors"), ("MPLS-LDP-STD-MIB", "mplsFecAddrType"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityPathVectorLimit"), ("MPLS-LDP-STD-MIB", "mplsFecAddrPrefixLength"), ("MPLS-LDP-STD-MIB", "mplsFecAddr"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedNoHelloErrors"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionStateLastChange"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStorageType"), ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyHoldTimeRem"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityMaxPduLength"), ("MPLS-LDP-STD-MIB", "mplsLdpPeerTransportAddr"), ("MPLS-LDP-STD-MIB", "mplsFecStorageType"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityAdminStatus"), ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionAttempts"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionKeepAliveTime"), ("MPLS-LDP-STD-MIB", "mplsFecType"), )
mplsLdpNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 3)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpSessionDown"), ("MPLS-LDP-STD-MIB", "mplsLdpInitSessionThresholdExceeded"), ("MPLS-LDP-STD-MIB", "mplsLdpSessionUp"), ("MPLS-LDP-STD-MIB", "mplsLdpPathVectorLimitMismatch"), )
mplsLdpLspGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 2)).setObjects(("MPLS-LDP-STD-MIB", "mplsLdpLspFecLastChange"), ("MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspType"), ("MPLS-LDP-STD-MIB", "mplsLdpLspFecRowStatus"), ("MPLS-LDP-STD-MIB", "mplsLdpLspFecStorageType"), ("MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspLabelType"), ("MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspType"), ("MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspLabelType"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-LDP-STD-MIB", PYSNMP_MODULE_ID=mplsLdpStdMIB)

# Objects
mibBuilder.exportSymbols("MPLS-LDP-STD-MIB", mplsLdpStdMIB=mplsLdpStdMIB, mplsLdpNotifications=mplsLdpNotifications, mplsLdpObjects=mplsLdpObjects, mplsLdpLsrObjects=mplsLdpLsrObjects, mplsLdpLsrId=mplsLdpLsrId, mplsLdpLsrLoopDetectionCapable=mplsLdpLsrLoopDetectionCapable, mplsLdpEntityObjects=mplsLdpEntityObjects, mplsLdpEntityLastChange=mplsLdpEntityLastChange, mplsLdpEntityIndexNext=mplsLdpEntityIndexNext, mplsLdpEntityTable=mplsLdpEntityTable, mplsLdpEntityEntry=mplsLdpEntityEntry, mplsLdpEntityLdpId=mplsLdpEntityLdpId, mplsLdpEntityIndex=mplsLdpEntityIndex, mplsLdpEntityProtocolVersion=mplsLdpEntityProtocolVersion, mplsLdpEntityAdminStatus=mplsLdpEntityAdminStatus, mplsLdpEntityOperStatus=mplsLdpEntityOperStatus, mplsLdpEntityTcpPort=mplsLdpEntityTcpPort, mplsLdpEntityUdpDscPort=mplsLdpEntityUdpDscPort, mplsLdpEntityMaxPduLength=mplsLdpEntityMaxPduLength, mplsLdpEntityKeepAliveHoldTimer=mplsLdpEntityKeepAliveHoldTimer, mplsLdpEntityHelloHoldTimer=mplsLdpEntityHelloHoldTimer, mplsLdpEntityInitSessionThreshold=mplsLdpEntityInitSessionThreshold, mplsLdpEntityLabelDistMethod=mplsLdpEntityLabelDistMethod, mplsLdpEntityLabelRetentionMode=mplsLdpEntityLabelRetentionMode, mplsLdpEntityPathVectorLimit=mplsLdpEntityPathVectorLimit, mplsLdpEntityHopCountLimit=mplsLdpEntityHopCountLimit, mplsLdpEntityTransportAddrKind=mplsLdpEntityTransportAddrKind, mplsLdpEntityTargetPeer=mplsLdpEntityTargetPeer, mplsLdpEntityTargetPeerAddrType=mplsLdpEntityTargetPeerAddrType, mplsLdpEntityTargetPeerAddr=mplsLdpEntityTargetPeerAddr, mplsLdpEntityLabelType=mplsLdpEntityLabelType, mplsLdpEntityDiscontinuityTime=mplsLdpEntityDiscontinuityTime, mplsLdpEntityStorageType=mplsLdpEntityStorageType, mplsLdpEntityRowStatus=mplsLdpEntityRowStatus, mplsLdpEntityStatsTable=mplsLdpEntityStatsTable, mplsLdpEntityStatsEntry=mplsLdpEntityStatsEntry, mplsLdpEntityStatsSessionAttempts=mplsLdpEntityStatsSessionAttempts, mplsLdpEntityStatsSessionRejectedNoHelloErrors=mplsLdpEntityStatsSessionRejectedNoHelloErrors, mplsLdpEntityStatsSessionRejectedAdErrors=mplsLdpEntityStatsSessionRejectedAdErrors, mplsLdpEntityStatsSessionRejectedMaxPduErrors=mplsLdpEntityStatsSessionRejectedMaxPduErrors, mplsLdpEntityStatsSessionRejectedLRErrors=mplsLdpEntityStatsSessionRejectedLRErrors, mplsLdpEntityStatsBadLdpIdentifierErrors=mplsLdpEntityStatsBadLdpIdentifierErrors, mplsLdpEntityStatsBadPduLengthErrors=mplsLdpEntityStatsBadPduLengthErrors, mplsLdpEntityStatsBadMessageLengthErrors=mplsLdpEntityStatsBadMessageLengthErrors, mplsLdpEntityStatsBadTlvLengthErrors=mplsLdpEntityStatsBadTlvLengthErrors, mplsLdpEntityStatsMalformedTlvValueErrors=mplsLdpEntityStatsMalformedTlvValueErrors, mplsLdpEntityStatsKeepAliveTimerExpErrors=mplsLdpEntityStatsKeepAliveTimerExpErrors, mplsLdpEntityStatsShutdownReceivedNotifications=mplsLdpEntityStatsShutdownReceivedNotifications, mplsLdpEntityStatsShutdownSentNotifications=mplsLdpEntityStatsShutdownSentNotifications, mplsLdpSessionObjects=mplsLdpSessionObjects, mplsLdpPeerLastChange=mplsLdpPeerLastChange, mplsLdpPeerTable=mplsLdpPeerTable, mplsLdpPeerEntry=mplsLdpPeerEntry, mplsLdpPeerLdpId=mplsLdpPeerLdpId, mplsLdpPeerLabelDistMethod=mplsLdpPeerLabelDistMethod, mplsLdpPeerPathVectorLimit=mplsLdpPeerPathVectorLimit, mplsLdpPeerTransportAddrType=mplsLdpPeerTransportAddrType, mplsLdpPeerTransportAddr=mplsLdpPeerTransportAddr, mplsLdpSessionTable=mplsLdpSessionTable, mplsLdpSessionEntry=mplsLdpSessionEntry, mplsLdpSessionStateLastChange=mplsLdpSessionStateLastChange, mplsLdpSessionState=mplsLdpSessionState, mplsLdpSessionRole=mplsLdpSessionRole, mplsLdpSessionProtocolVersion=mplsLdpSessionProtocolVersion, mplsLdpSessionKeepAliveHoldTimeRem=mplsLdpSessionKeepAliveHoldTimeRem, mplsLdpSessionKeepAliveTime=mplsLdpSessionKeepAliveTime, mplsLdpSessionMaxPduLength=mplsLdpSessionMaxPduLength, mplsLdpSessionDiscontinuityTime=mplsLdpSessionDiscontinuityTime, mplsLdpSessionStatsTable=mplsLdpSessionStatsTable, mplsLdpSessionStatsEntry=mplsLdpSessionStatsEntry, mplsLdpSessionStatsUnknownMesTypeErrors=mplsLdpSessionStatsUnknownMesTypeErrors, mplsLdpSessionStatsUnknownTlvErrors=mplsLdpSessionStatsUnknownTlvErrors, mplsLdpHelloAdjacencyObjects=mplsLdpHelloAdjacencyObjects, mplsLdpHelloAdjacencyTable=mplsLdpHelloAdjacencyTable, mplsLdpHelloAdjacencyEntry=mplsLdpHelloAdjacencyEntry, mplsLdpHelloAdjacencyIndex=mplsLdpHelloAdjacencyIndex, mplsLdpHelloAdjacencyHoldTimeRem=mplsLdpHelloAdjacencyHoldTimeRem, mplsLdpHelloAdjacencyHoldTime=mplsLdpHelloAdjacencyHoldTime, mplsLdpHelloAdjacencyType=mplsLdpHelloAdjacencyType, mplsInSegmentLdpLspTable=mplsInSegmentLdpLspTable, mplsInSegmentLdpLspEntry=mplsInSegmentLdpLspEntry, mplsInSegmentLdpLspIndex=mplsInSegmentLdpLspIndex, mplsInSegmentLdpLspLabelType=mplsInSegmentLdpLspLabelType, mplsInSegmentLdpLspType=mplsInSegmentLdpLspType, mplsOutSegmentLdpLspTable=mplsOutSegmentLdpLspTable, mplsOutSegmentLdpLspEntry=mplsOutSegmentLdpLspEntry, mplsOutSegmentLdpLspIndex=mplsOutSegmentLdpLspIndex, mplsOutSegmentLdpLspLabelType=mplsOutSegmentLdpLspLabelType, mplsOutSegmentLdpLspType=mplsOutSegmentLdpLspType, mplsFecObjects=mplsFecObjects, mplsFecLastChange=mplsFecLastChange, mplsFecIndexNext=mplsFecIndexNext, mplsFecTable=mplsFecTable, mplsFecEntry=mplsFecEntry, mplsFecIndex=mplsFecIndex, mplsFecType=mplsFecType, mplsFecAddrPrefixLength=mplsFecAddrPrefixLength, mplsFecAddrType=mplsFecAddrType, mplsFecAddr=mplsFecAddr, mplsFecStorageType=mplsFecStorageType, mplsFecRowStatus=mplsFecRowStatus, mplsLdpLspFecLastChange=mplsLdpLspFecLastChange, mplsLdpLspFecTable=mplsLdpLspFecTable, mplsLdpLspFecEntry=mplsLdpLspFecEntry, mplsLdpLspFecSegment=mplsLdpLspFecSegment, mplsLdpLspFecSegmentIndex=mplsLdpLspFecSegmentIndex, mplsLdpLspFecIndex=mplsLdpLspFecIndex, mplsLdpLspFecStorageType=mplsLdpLspFecStorageType, mplsLdpLspFecRowStatus=mplsLdpLspFecRowStatus, mplsLdpSessionPeerAddrTable=mplsLdpSessionPeerAddrTable, mplsLdpSessionPeerAddrEntry=mplsLdpSessionPeerAddrEntry, mplsLdpSessionPeerAddrIndex=mplsLdpSessionPeerAddrIndex, mplsLdpSessionPeerNextHopAddrType=mplsLdpSessionPeerNextHopAddrType, mplsLdpSessionPeerNextHopAddr=mplsLdpSessionPeerNextHopAddr, mplsLdpConformance=mplsLdpConformance, mplsLdpGroups=mplsLdpGroups, mplsLdpCompliances=mplsLdpCompliances)

# Notifications
mibBuilder.exportSymbols("MPLS-LDP-STD-MIB", mplsLdpSessionDown=mplsLdpSessionDown, mplsLdpInitSessionThresholdExceeded=mplsLdpInitSessionThresholdExceeded, mplsLdpSessionUp=mplsLdpSessionUp, mplsLdpPathVectorLimitMismatch=mplsLdpPathVectorLimitMismatch)

# Groups
mibBuilder.exportSymbols("MPLS-LDP-STD-MIB", mplsLdpGeneralGroup=mplsLdpGeneralGroup, mplsLdpNotificationsGroup=mplsLdpNotificationsGroup, mplsLdpLspGroup=mplsLdpLspGroup)
