# PySNMP SMI module. Autogenerated from smidump -f python SNA-NAU-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:19 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, InstancePointer, RowStatus, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "InstancePointer", "RowStatus", "TimeStamp")

# Objects

snanauMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34)).setRevisions(("1994-05-12 09:00",))
snanauObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1))
snaNode = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1, 1))
snaNodeAdminTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 1, 1))
snaNodeAdminEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaNodeAdminIndex"))
snaNodeAdminIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("noaccess")
snaNodeAdminName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readwrite")
snaNodeAdminType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,6,2,1,5,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("pu10", 2), ("pu20", 3), ("t21len", 4), ("endNode", 5), ("networkNode", 6), ))).setMaxAccess("readwrite")
snaNodeAdminXidFormat = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("format0", 1), ("format1", 2), ("format3", 3), ))).setMaxAccess("readwrite")
snaNodeAdminBlockNum = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(3, 3))).setMaxAccess("readwrite")
snaNodeAdminIdNum = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(5, 5))).setMaxAccess("readwrite")
snaNodeAdminEnablingMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("startup", 2), ("demand", 3), ("onlyMS", 4), ))).setMaxAccess("readwrite")
snaNodeAdminLuTermDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,3,)).subtype(namedValues=namedval.NamedValues(("unbind", 1), ("termself", 2), ("rshutd", 3), ("poweroff", 4), ))).setMaxAccess("readwrite")
snaNodeAdminMaxLu = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
snaNodeAdminHostDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
snaNodeAdminStopMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,4,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("normal", 2), ("immed", 3), ("force", 4), ))).setMaxAccess("readwrite")
snaNodeAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("inactive", 1), ("active", 2), ))).setMaxAccess("readwrite")
snaNodeAdminRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
snaNodeAdminTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 34, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
snaNodeOperTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 1, 3))
snaNodeOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1))
snaNodeOperName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
snaNodeOperType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,6,2,1,5,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("pu10", 2), ("pu20", 3), ("t21LEN", 4), ("endNode", 5), ("networkNode", 6), ))).setMaxAccess("readonly")
snaNodeOperXidFormat = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("format0", 1), ("format1", 2), ("format3", 3), ))).setMaxAccess("readonly")
snaNodeOperBlockNum = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(3, 3))).setMaxAccess("readonly")
snaNodeOperIdNum = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(5, 5))).setMaxAccess("readonly")
snaNodeOperEnablingMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("startup", 2), ("demand", 3), ("onlyMS", 4), ))).setMaxAccess("readonly")
snaNodeOperLuTermDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,3,)).subtype(namedValues=namedval.NamedValues(("unbind", 1), ("termself", 2), ("rshutd", 3), ("poweroff", 4), ))).setMaxAccess("readonly")
snaNodeOperMaxLu = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
snaNodeOperHostDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 9), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
snaNodeOperStopMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,4,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("normal", 2), ("immed", 3), ("force", 4), ))).setMaxAccess("readonly")
snaNodeOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,4,3,1,)).subtype(namedValues=namedval.NamedValues(("inactive", 1), ("active", 2), ("waiting", 3), ("stopping", 4), ))).setMaxAccess("readonly")
snaNodeOperHostSscpId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 12), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
snaNodeOperStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
snaNodeOperLastStateChange = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 14), TimeStamp()).setMaxAccess("readonly")
snaNodeOperActFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
snaNodeOperActFailureReason = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 16), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,5,2,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("linkFailure", 2), ("noResources", 3), ("badConfiguration", 4), ("internalError", 5), ))).setMaxAccess("readonly")
snaNodeOperTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 34, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
snaPu20StatsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 1, 5))
snaPu20StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaNodeAdminIndex"))
snaPu20StatsSentBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 1), Counter32()).setMaxAccess("readonly")
snaPu20StatsReceivedBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
snaPu20StatsSentPius = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
snaPu20StatsReceivedPius = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
snaPu20StatsSentNegativeResps = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
snaPu20StatsReceivedNegativeResps = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
snaPu20StatsActLus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 7), Gauge32()).setMaxAccess("readonly")
snaPu20StatsInActLus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
snaPu20StatsBindLus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 9), Gauge32()).setMaxAccess("readonly")
snaNodeLinkAdminTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 1, 6))
snaNodeLinkAdminEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaNodeAdminIndex"), (0, "SNA-NAU-MIB", "snaNodeLinkAdminIndex"))
snaNodeLinkAdminIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 1), Integer32()).setMaxAccess("noaccess")
snaNodeLinkAdminSpecific = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 2), InstancePointer()).setMaxAccess("readwrite")
snaNodeLinkAdminMaxPiu = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
snaNodeLinkAdminRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
snaNodeLinkAdminTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 34, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
snaNodeLinkOperTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 1, 8))
snaNodeLinkOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1))
snaNodeLinkOperSpecific = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 1), InstancePointer()).setMaxAccess("readonly")
snaNodeLinkOperMaxPiu = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
snaNodeLinkOperTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 34, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
snaNodeTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1, 1, 10))
snaLu = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1, 2))
snaLuAdminTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 2, 1))
snaLuAdminEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaNodeAdminIndex"), (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"))
snaLuAdminLuIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("noaccess")
snaLuAdminName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
snaLuAdminSnaName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
snaLuAdminType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,5,6,8,1,7,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("lu0", 2), ("lu1", 3), ("lu2", 4), ("lu3", 5), ("lu4", 6), ("lu62", 7), ("lu7", 8), ))).setMaxAccess("readwrite")
snaLuAdminDepType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("dependent", 1), ("independent", 2), ))).setMaxAccess("readwrite")
snaLuAdminLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))).setMaxAccess("readwrite")
snaLuAdminDisplayModel = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,10,2,4,1,5,9,8,6,7,)).subtype(namedValues=namedval.NamedValues(("invalid", 1), ("dynamic", 10), ("model2A", 2), ("model2B", 3), ("model3A", 4), ("model3B", 5), ("model4A", 6), ("model4B", 7), ("model5A", 8), ("model5B", 9), ))).setMaxAccess("readwrite")
snaLuAdminTerm = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,3,)).subtype(namedValues=namedval.NamedValues(("unbind", 1), ("termself", 2), ("rshutd", 3), ("poweroff", 4), ))).setMaxAccess("readwrite")
snaLuAdminRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
snaLuOperTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 2, 2))
snaLuOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1))
snaLuOperName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
snaLuOperSnaName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 17))).setMaxAccess("readonly")
snaLuOperType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,5,6,8,1,7,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("lu0", 2), ("lu1", 3), ("lu2", 4), ("lu3", 5), ("lu4", 6), ("lu62", 7), ("lu7", 8), ))).setMaxAccess("readonly")
snaLuOperDepType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("dependent", 1), ("independent", 2), ))).setMaxAccess("readonly")
snaLuOperLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))).setMaxAccess("readonly")
snaLuOperDisplayModel = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,10,2,4,1,5,9,8,6,7,)).subtype(namedValues=namedval.NamedValues(("invalid", 1), ("dynamic", 10), ("model2A", 2), ("model2B", 3), ("model3A", 4), ("model3B", 5), ("model4A", 6), ("model4B", 7), ("model5A", 8), ("model5B", 9), ))).setMaxAccess("readonly")
snaLuOperTerm = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,3,)).subtype(namedValues=namedval.NamedValues(("unbind", 1), ("termself", 2), ("rshutd", 3), ("poweroff", 4), ))).setMaxAccess("readonly")
snaLuOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("inactive", 1), ("active", 2), ))).setMaxAccess("readonly")
snaLuOperSessnCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
snaLuSessnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 2, 3))
snaLuSessnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaNodeAdminIndex"), (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"), (0, "SNA-NAU-MIB", "snaLuSessnRluIndex"), (0, "SNA-NAU-MIB", "snaLuSessnIndex"))
snaLuSessnRluIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
snaLuSessnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
snaLuSessnLocalApplName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
snaLuSessnRemoteLuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
snaLuSessnMaxSndRuSize = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
snaLuSessnMaxRcvRuSize = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
snaLuSessnSndPacingSize = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
snaLuSessnRcvPacingSize = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
snaLuSessnActiveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
snaLuSessnAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,)).subtype(namedValues=namedval.NamedValues(("unbound", 1), ("bound", 3), ))).setMaxAccess("readwrite")
snaLuSessnOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,3,)).subtype(namedValues=namedval.NamedValues(("unbound", 1), ("pendingBind", 2), ("bound", 3), ("pendingUnbind", 4), ))).setMaxAccess("readonly")
snaLuSessnSenseData = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 12), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
snaLuSessnTerminationRu = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("bindFailure", 2), ("unbind", 3), ))).setMaxAccess("readonly")
snaLuSessnUnbindType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 14), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
snaLuSessnLinkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 15), Integer32()).setMaxAccess("readonly")
snaLuSessnStatsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 2, 4))
snaLuSessnStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1))
snaLuSessnStatsSentBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
snaLuSessnStatsReceivedBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
snaLuSessnStatsSentRus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
snaLuSessnStatsReceivedRus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
snaLuSessnStatsSentNegativeResps = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
snaLuSessnStatsReceivedNegativeResps = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
snaLuTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1, 2, 5))
snaMgtTools = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 1, 3))
snaLuRtmTable = MibTable((1, 3, 6, 1, 2, 1, 34, 1, 3, 1))
snaLuRtmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1)).setIndexNames((0, "SNA-NAU-MIB", "snaLuRtmPuIndex"), (0, "SNA-NAU-MIB", "snaLuRtmLuIndex"))
snaLuRtmPuIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("noaccess")
snaLuRtmLuIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("noaccess")
snaLuRtmState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("off", 1), ("on", 2), ))).setMaxAccess("readonly")
snaLuRtmStateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
snaLuRtmDef = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("firstChar", 1), ("kb", 2), ("cdeb", 3), ))).setMaxAccess("readonly")
snaLuRtmBoundary1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
snaLuRtmBoundary2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
snaLuRtmBoundary3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
snaLuRtmBoundary4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
snaLuRtmCounter1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
snaLuRtmCounter2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
snaLuRtmCounter3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
snaLuRtmCounter4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
snaLuRtmOverFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
snaLuRtmObjPercent = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 15), Integer32()).setMaxAccess("readonly")
snaLuRtmObjRange = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 16), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,2,1,6,5,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("range1", 2), ("range2", 3), ("range3", 4), ("range4", 5), ("range5", 6), ))).setMaxAccess("readonly")
snaLuRtmNumTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 17), Integer32()).setMaxAccess("readonly")
snaLuRtmLastRspTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 18), Integer32()).setMaxAccess("readonly")
snaLuRtmAvgRspTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
snanauConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 2))
snanauCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 2, 1))
snanauGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 2, 2))

# Augmentions
snaLuSessnEntry.registerAugmentions(("SNA-NAU-MIB", "snaLuSessnStatsEntry"))
apply(snaLuSessnStatsEntry.setIndexNames, snaLuSessnEntry.getIndexNames())
snaNodeLinkAdminEntry.registerAugmentions(("SNA-NAU-MIB", "snaNodeLinkOperEntry"))
apply(snaNodeLinkOperEntry.setIndexNames, snaNodeLinkAdminEntry.getIndexNames())
snaLuAdminEntry.registerAugmentions(("SNA-NAU-MIB", "snaLuOperEntry"))
apply(snaLuOperEntry.setIndexNames, snaLuAdminEntry.getIndexNames())
snaNodeAdminEntry.registerAugmentions(("SNA-NAU-MIB", "snaNodeOperEntry"))
apply(snaNodeOperEntry.setIndexNames, snaNodeAdminEntry.getIndexNames())

# Notifications

snaNodeStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 1)).setObjects(("SNA-NAU-MIB", "snaNodeOperName"), ("SNA-NAU-MIB", "snaNodeOperState"), )
snaLuSessnBindFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 2)).setObjects(("SNA-NAU-MIB", "snaLuSessnSenseData"), ("SNA-NAU-MIB", "snaLuSessnOperState"), ("SNA-NAU-MIB", "snaLuSessnLocalApplName"), ("SNA-NAU-MIB", "snaLuSessnRemoteLuName"), )
snaNodeActFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 2)).setObjects(("SNA-NAU-MIB", "snaNodeOperActFailureReason"), ("SNA-NAU-MIB", "snaNodeOperName"), ("SNA-NAU-MIB", "snaNodeOperState"), )
snaLuStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 1)).setObjects(("SNA-NAU-MIB", "snaLuOperName"), ("SNA-NAU-MIB", "snaLuOperSnaName"), ("SNA-NAU-MIB", "snaLuOperState"), )

# Groups

snaLuGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 2, 2, 2)).setObjects(("SNA-NAU-MIB", "snaLuOperName"), ("SNA-NAU-MIB", "snaLuOperSnaName"), ("SNA-NAU-MIB", "snaLuAdminType"), ("SNA-NAU-MIB", "snaLuOperState"), ("SNA-NAU-MIB", "snaLuAdminRowStatus"), ("SNA-NAU-MIB", "snaLuAdminDepType"), ("SNA-NAU-MIB", "snaLuAdminTerm"), ("SNA-NAU-MIB", "snaLuOperSessnCount"), ("SNA-NAU-MIB", "snaLuOperTerm"), ("SNA-NAU-MIB", "snaLuOperType"), ("SNA-NAU-MIB", "snaLuOperLocalAddress"), ("SNA-NAU-MIB", "snaLuAdminName"), ("SNA-NAU-MIB", "snaLuAdminDisplayModel"), ("SNA-NAU-MIB", "snaLuAdminLocalAddress"), ("SNA-NAU-MIB", "snaLuOperDepType"), ("SNA-NAU-MIB", "snaLuOperDisplayModel"), ("SNA-NAU-MIB", "snaLuAdminSnaName"), )
snaMgtToolsRtmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 2, 2, 5)).setObjects(("SNA-NAU-MIB", "snaLuRtmBoundary3"), ("SNA-NAU-MIB", "snaLuRtmBoundary2"), ("SNA-NAU-MIB", "snaLuRtmBoundary1"), ("SNA-NAU-MIB", "snaLuRtmCounter3"), ("SNA-NAU-MIB", "snaLuRtmCounter4"), ("SNA-NAU-MIB", "snaLuRtmCounter1"), ("SNA-NAU-MIB", "snaLuRtmBoundary4"), ("SNA-NAU-MIB", "snaLuRtmAvgRspTime"), ("SNA-NAU-MIB", "snaLuRtmStateTime"), ("SNA-NAU-MIB", "snaLuRtmDef"), ("SNA-NAU-MIB", "snaLuRtmLastRspTime"), ("SNA-NAU-MIB", "snaLuRtmCounter2"), ("SNA-NAU-MIB", "snaLuRtmObjPercent"), ("SNA-NAU-MIB", "snaLuRtmState"), ("SNA-NAU-MIB", "snaLuRtmOverFlows"), ("SNA-NAU-MIB", "snaLuRtmObjRange"), ("SNA-NAU-MIB", "snaLuRtmNumTrans"), )
snaPu20Group = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 2, 2, 4)).setObjects(("SNA-NAU-MIB", "snaPu20StatsReceivedBytes"), ("SNA-NAU-MIB", "snaPu20StatsBindLus"), ("SNA-NAU-MIB", "snaPu20StatsSentBytes"), ("SNA-NAU-MIB", "snaPu20StatsReceivedNegativeResps"), ("SNA-NAU-MIB", "snaPu20StatsReceivedPius"), ("SNA-NAU-MIB", "snaPu20StatsActLus"), ("SNA-NAU-MIB", "snaPu20StatsSentNegativeResps"), ("SNA-NAU-MIB", "snaPu20StatsSentPius"), ("SNA-NAU-MIB", "snaPu20StatsInActLus"), )
snaNodeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 2, 2, 1)).setObjects(("SNA-NAU-MIB", "snaNodeOperXidFormat"), ("SNA-NAU-MIB", "snaNodeAdminRowStatus"), ("SNA-NAU-MIB", "snaNodeOperType"), ("SNA-NAU-MIB", "snaNodeLinkOperMaxPiu"), ("SNA-NAU-MIB", "snaNodeAdminLuTermDefault"), ("SNA-NAU-MIB", "snaNodeOperLastStateChange"), ("SNA-NAU-MIB", "snaNodeLinkAdminRowStatus"), ("SNA-NAU-MIB", "snaNodeOperStartTime"), ("SNA-NAU-MIB", "snaNodeLinkAdminTableLastChange"), ("SNA-NAU-MIB", "snaNodeLinkOperSpecific"), ("SNA-NAU-MIB", "snaNodeOperEnablingMethod"), ("SNA-NAU-MIB", "snaNodeOperLuTermDefault"), ("SNA-NAU-MIB", "snaNodeLinkOperTableLastChange"), ("SNA-NAU-MIB", "snaNodeAdminIdNum"), ("SNA-NAU-MIB", "snaNodeOperState"), ("SNA-NAU-MIB", "snaNodeAdminHostDescription"), ("SNA-NAU-MIB", "snaNodeLinkAdminMaxPiu"), ("SNA-NAU-MIB", "snaNodeLinkAdminSpecific"), ("SNA-NAU-MIB", "snaNodeOperName"), ("SNA-NAU-MIB", "snaNodeAdminEnablingMethod"), ("SNA-NAU-MIB", "snaNodeAdminXidFormat"), ("SNA-NAU-MIB", "snaNodeAdminState"), ("SNA-NAU-MIB", "snaNodeOperStopMethod"), ("SNA-NAU-MIB", "snaNodeAdminTableLastChange"), ("SNA-NAU-MIB", "snaNodeOperActFailures"), ("SNA-NAU-MIB", "snaNodeOperBlockNum"), ("SNA-NAU-MIB", "snaNodeOperTableLastChange"), ("SNA-NAU-MIB", "snaNodeOperActFailureReason"), ("SNA-NAU-MIB", "snaNodeOperHostSscpId"), ("SNA-NAU-MIB", "snaNodeAdminMaxLu"), ("SNA-NAU-MIB", "snaNodeAdminStopMethod"), ("SNA-NAU-MIB", "snaNodeAdminType"), ("SNA-NAU-MIB", "snaNodeOperMaxLu"), ("SNA-NAU-MIB", "snaNodeOperHostDescription"), ("SNA-NAU-MIB", "snaNodeAdminBlockNum"), ("SNA-NAU-MIB", "snaNodeAdminName"), ("SNA-NAU-MIB", "snaNodeOperIdNum"), )
snaSessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 2, 2, 3)).setObjects(("SNA-NAU-MIB", "snaLuSessnStatsReceivedBytes"), ("SNA-NAU-MIB", "snaLuSessnTerminationRu"), ("SNA-NAU-MIB", "snaLuSessnSndPacingSize"), ("SNA-NAU-MIB", "snaLuSessnStatsReceivedNegativeResps"), ("SNA-NAU-MIB", "snaLuSessnIndex"), ("SNA-NAU-MIB", "snaLuSessnAdminState"), ("SNA-NAU-MIB", "snaLuSessnStatsSentNegativeResps"), ("SNA-NAU-MIB", "snaLuSessnOperState"), ("SNA-NAU-MIB", "snaLuSessnStatsSentRus"), ("SNA-NAU-MIB", "snaLuSessnLocalApplName"), ("SNA-NAU-MIB", "snaLuSessnUnbindType"), ("SNA-NAU-MIB", "snaLuSessnSenseData"), ("SNA-NAU-MIB", "snaLuSessnRcvPacingSize"), ("SNA-NAU-MIB", "snaLuSessnStatsSentBytes"), ("SNA-NAU-MIB", "snaLuSessnActiveTime"), ("SNA-NAU-MIB", "snaLuSessnLinkIndex"), ("SNA-NAU-MIB", "snaLuSessnRluIndex"), ("SNA-NAU-MIB", "snaLuSessnMaxSndRuSize"), ("SNA-NAU-MIB", "snaLuSessnStatsReceivedRus"), ("SNA-NAU-MIB", "snaLuSessnMaxRcvRuSize"), ("SNA-NAU-MIB", "snaLuSessnRemoteLuName"), )

# Exports

# Module identity
mibBuilder.exportSymbols("SNA-NAU-MIB", PYSNMP_MODULE_ID=snanauMIB)

# Objects
mibBuilder.exportSymbols("SNA-NAU-MIB", snanauMIB=snanauMIB, snanauObjects=snanauObjects, snaNode=snaNode, snaNodeAdminTable=snaNodeAdminTable, snaNodeAdminEntry=snaNodeAdminEntry, snaNodeAdminIndex=snaNodeAdminIndex, snaNodeAdminName=snaNodeAdminName, snaNodeAdminType=snaNodeAdminType, snaNodeAdminXidFormat=snaNodeAdminXidFormat, snaNodeAdminBlockNum=snaNodeAdminBlockNum, snaNodeAdminIdNum=snaNodeAdminIdNum, snaNodeAdminEnablingMethod=snaNodeAdminEnablingMethod, snaNodeAdminLuTermDefault=snaNodeAdminLuTermDefault, snaNodeAdminMaxLu=snaNodeAdminMaxLu, snaNodeAdminHostDescription=snaNodeAdminHostDescription, snaNodeAdminStopMethod=snaNodeAdminStopMethod, snaNodeAdminState=snaNodeAdminState, snaNodeAdminRowStatus=snaNodeAdminRowStatus, snaNodeAdminTableLastChange=snaNodeAdminTableLastChange, snaNodeOperTable=snaNodeOperTable, snaNodeOperEntry=snaNodeOperEntry, snaNodeOperName=snaNodeOperName, snaNodeOperType=snaNodeOperType, snaNodeOperXidFormat=snaNodeOperXidFormat, snaNodeOperBlockNum=snaNodeOperBlockNum, snaNodeOperIdNum=snaNodeOperIdNum, snaNodeOperEnablingMethod=snaNodeOperEnablingMethod, snaNodeOperLuTermDefault=snaNodeOperLuTermDefault, snaNodeOperMaxLu=snaNodeOperMaxLu, snaNodeOperHostDescription=snaNodeOperHostDescription, snaNodeOperStopMethod=snaNodeOperStopMethod, snaNodeOperState=snaNodeOperState, snaNodeOperHostSscpId=snaNodeOperHostSscpId, snaNodeOperStartTime=snaNodeOperStartTime, snaNodeOperLastStateChange=snaNodeOperLastStateChange, snaNodeOperActFailures=snaNodeOperActFailures, snaNodeOperActFailureReason=snaNodeOperActFailureReason, snaNodeOperTableLastChange=snaNodeOperTableLastChange, snaPu20StatsTable=snaPu20StatsTable, snaPu20StatsEntry=snaPu20StatsEntry, snaPu20StatsSentBytes=snaPu20StatsSentBytes, snaPu20StatsReceivedBytes=snaPu20StatsReceivedBytes, snaPu20StatsSentPius=snaPu20StatsSentPius, snaPu20StatsReceivedPius=snaPu20StatsReceivedPius, snaPu20StatsSentNegativeResps=snaPu20StatsSentNegativeResps, snaPu20StatsReceivedNegativeResps=snaPu20StatsReceivedNegativeResps, snaPu20StatsActLus=snaPu20StatsActLus, snaPu20StatsInActLus=snaPu20StatsInActLus, snaPu20StatsBindLus=snaPu20StatsBindLus, snaNodeLinkAdminTable=snaNodeLinkAdminTable, snaNodeLinkAdminEntry=snaNodeLinkAdminEntry, snaNodeLinkAdminIndex=snaNodeLinkAdminIndex, snaNodeLinkAdminSpecific=snaNodeLinkAdminSpecific, snaNodeLinkAdminMaxPiu=snaNodeLinkAdminMaxPiu, snaNodeLinkAdminRowStatus=snaNodeLinkAdminRowStatus, snaNodeLinkAdminTableLastChange=snaNodeLinkAdminTableLastChange, snaNodeLinkOperTable=snaNodeLinkOperTable, snaNodeLinkOperEntry=snaNodeLinkOperEntry, snaNodeLinkOperSpecific=snaNodeLinkOperSpecific, snaNodeLinkOperMaxPiu=snaNodeLinkOperMaxPiu, snaNodeLinkOperTableLastChange=snaNodeLinkOperTableLastChange, snaNodeTraps=snaNodeTraps, snaLu=snaLu, snaLuAdminTable=snaLuAdminTable, snaLuAdminEntry=snaLuAdminEntry, snaLuAdminLuIndex=snaLuAdminLuIndex, snaLuAdminName=snaLuAdminName, snaLuAdminSnaName=snaLuAdminSnaName, snaLuAdminType=snaLuAdminType, snaLuAdminDepType=snaLuAdminDepType, snaLuAdminLocalAddress=snaLuAdminLocalAddress, snaLuAdminDisplayModel=snaLuAdminDisplayModel, snaLuAdminTerm=snaLuAdminTerm, snaLuAdminRowStatus=snaLuAdminRowStatus, snaLuOperTable=snaLuOperTable, snaLuOperEntry=snaLuOperEntry, snaLuOperName=snaLuOperName, snaLuOperSnaName=snaLuOperSnaName, snaLuOperType=snaLuOperType, snaLuOperDepType=snaLuOperDepType, snaLuOperLocalAddress=snaLuOperLocalAddress, snaLuOperDisplayModel=snaLuOperDisplayModel, snaLuOperTerm=snaLuOperTerm, snaLuOperState=snaLuOperState, snaLuOperSessnCount=snaLuOperSessnCount, snaLuSessnTable=snaLuSessnTable, snaLuSessnEntry=snaLuSessnEntry, snaLuSessnRluIndex=snaLuSessnRluIndex, snaLuSessnIndex=snaLuSessnIndex, snaLuSessnLocalApplName=snaLuSessnLocalApplName, snaLuSessnRemoteLuName=snaLuSessnRemoteLuName, snaLuSessnMaxSndRuSize=snaLuSessnMaxSndRuSize, snaLuSessnMaxRcvRuSize=snaLuSessnMaxRcvRuSize, snaLuSessnSndPacingSize=snaLuSessnSndPacingSize, snaLuSessnRcvPacingSize=snaLuSessnRcvPacingSize, snaLuSessnActiveTime=snaLuSessnActiveTime, snaLuSessnAdminState=snaLuSessnAdminState, snaLuSessnOperState=snaLuSessnOperState, snaLuSessnSenseData=snaLuSessnSenseData, snaLuSessnTerminationRu=snaLuSessnTerminationRu, snaLuSessnUnbindType=snaLuSessnUnbindType, snaLuSessnLinkIndex=snaLuSessnLinkIndex, snaLuSessnStatsTable=snaLuSessnStatsTable, snaLuSessnStatsEntry=snaLuSessnStatsEntry, snaLuSessnStatsSentBytes=snaLuSessnStatsSentBytes, snaLuSessnStatsReceivedBytes=snaLuSessnStatsReceivedBytes, snaLuSessnStatsSentRus=snaLuSessnStatsSentRus, snaLuSessnStatsReceivedRus=snaLuSessnStatsReceivedRus, snaLuSessnStatsSentNegativeResps=snaLuSessnStatsSentNegativeResps, snaLuSessnStatsReceivedNegativeResps=snaLuSessnStatsReceivedNegativeResps, snaLuTraps=snaLuTraps, snaMgtTools=snaMgtTools, snaLuRtmTable=snaLuRtmTable, snaLuRtmEntry=snaLuRtmEntry, snaLuRtmPuIndex=snaLuRtmPuIndex, snaLuRtmLuIndex=snaLuRtmLuIndex, snaLuRtmState=snaLuRtmState, snaLuRtmStateTime=snaLuRtmStateTime, snaLuRtmDef=snaLuRtmDef, snaLuRtmBoundary1=snaLuRtmBoundary1, snaLuRtmBoundary2=snaLuRtmBoundary2, snaLuRtmBoundary3=snaLuRtmBoundary3, snaLuRtmBoundary4=snaLuRtmBoundary4, snaLuRtmCounter1=snaLuRtmCounter1, snaLuRtmCounter2=snaLuRtmCounter2, snaLuRtmCounter3=snaLuRtmCounter3, snaLuRtmCounter4=snaLuRtmCounter4, snaLuRtmOverFlows=snaLuRtmOverFlows)
mibBuilder.exportSymbols("SNA-NAU-MIB", snaLuRtmObjPercent=snaLuRtmObjPercent, snaLuRtmObjRange=snaLuRtmObjRange, snaLuRtmNumTrans=snaLuRtmNumTrans, snaLuRtmLastRspTime=snaLuRtmLastRspTime, snaLuRtmAvgRspTime=snaLuRtmAvgRspTime, snanauConformance=snanauConformance, snanauCompliances=snanauCompliances, snanauGroups=snanauGroups)

# Notifications
mibBuilder.exportSymbols("SNA-NAU-MIB", snaNodeStateChangeTrap=snaNodeStateChangeTrap, snaLuSessnBindFailTrap=snaLuSessnBindFailTrap, snaNodeActFailTrap=snaNodeActFailTrap, snaLuStateChangeTrap=snaLuStateChangeTrap)

# Groups
mibBuilder.exportSymbols("SNA-NAU-MIB", snaLuGroup=snaLuGroup, snaMgtToolsRtmGroup=snaMgtToolsRtmGroup, snaPu20Group=snaPu20Group, snaNodeGroup=snaNodeGroup, snaSessionGroup=snaSessionGroup)
