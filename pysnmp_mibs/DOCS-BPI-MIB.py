# PySNMP SMI module. Autogenerated from smidump -f python DOCS-BPI-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:01 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( docsIfCmServiceId, docsIfCmtsServiceId, docsIfMib, ) = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmServiceId", "docsIfCmtsServiceId", "docsIfMib")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DateAndTime, DisplayString, MacAddress, RowStatus, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "MacAddress", "RowStatus", "TruthValue")

# Objects

docsBpiMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 127, 5)).setRevisions(("2001-03-13 00:00","2000-11-03 19:30","2000-02-16 19:30",))
docsBpiMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 1))
docsBpiCmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1))
docsBpiCmBaseTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1))
docsBpiCmBaseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsBpiCmPrivacyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
docsBpiCmPublicKey = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(270, 270))).setMaxAccess("readonly")
docsBpiCmAuthState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,4,3,5,)).subtype(namedValues=namedval.NamedValues(("authWait", 2), ("authorized", 3), ("reauthWait", 4), ("authRejectWait", 5), ))).setMaxAccess("readonly")
docsBpiCmAuthKeySequenceNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
docsBpiCmAuthExpires = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
docsBpiCmAuthReset = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
docsBpiCmAuthGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readonly")
docsBpiCmTEKGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readonly")
docsBpiCmAuthWaitTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
docsBpiCmReauthWaitTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
docsBpiCmOpWaitTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
docsBpiCmRekeyWaitTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
docsBpiCmAuthRejectWaitTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 600))).setMaxAccess("readonly")
docsBpiCmAuthRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
docsBpiCmAuthReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
docsBpiCmAuthRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
docsBpiCmAuthInvalids = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
docsBpiCmAuthRejectErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 18), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedCm", 3), ("unauthorizedSid", 4), ))).setMaxAccess("readonly")
docsBpiCmAuthRejectErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmAuthInvalidErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 20), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,6,5,3,7,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedCm", 3), ("unsolicited", 5), ("invalidKeySequence", 6), ("keyRequestAuthenticationFailure", 7), ))).setMaxAccess("readonly")
docsBpiCmAuthInvalidErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmTEKTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2))
docsBpiCmTEKEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-IF-MIB", "docsIfCmServiceId"))
docsBpiCmTEKPrivacyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
docsBpiCmTEKState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,2,4,1,5,3,)).subtype(namedValues=namedval.NamedValues(("start", 1), ("opWait", 2), ("opReauthWait", 3), ("operational", 4), ("rekeyWait", 5), ("rekeyReauthWait", 6), ))).setMaxAccess("readonly")
docsBpiCmTEKExpiresOld = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
docsBpiCmTEKExpiresNew = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
docsBpiCmTEKKeyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
docsBpiCmTEKKeyReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
docsBpiCmTEKKeyRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
docsBpiCmTEKInvalids = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
docsBpiCmTEKAuthPends = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
docsBpiCmTEKKeyRejectErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedSid", 4), ))).setMaxAccess("readonly")
docsBpiCmTEKKeyRejectErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmTEKInvalidErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,6,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("invalidKeySequence", 6), ))).setMaxAccess("readonly")
docsBpiCmTEKInvalidErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmtsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2))
docsBpiCmtsBaseTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1))
docsBpiCmtsBaseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
docsBpiCmtsDefaultAuthLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 6048000))).setMaxAccess("readwrite")
docsBpiCmtsDefaultTEKLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 604800))).setMaxAccess("readwrite")
docsBpiCmtsDefaultAuthGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readwrite")
docsBpiCmtsDefaultTEKGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readwrite")
docsBpiCmtsAuthRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthInvalids = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2))
docsBpiCmtsAuthEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-BPI-MIB", "docsBpiCmtsAuthCmMacAddress"))
docsBpiCmtsAuthCmMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("noaccess")
docsBpiCmtsAuthCmPublicKey = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(270, 270))).setMaxAccess("readonly")
docsBpiCmtsAuthCmKeySequenceNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
docsBpiCmtsAuthCmExpires = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
docsBpiCmtsAuthCmLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 6048000))).setMaxAccess("readwrite")
docsBpiCmtsAuthCmGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readonly")
docsBpiCmtsAuthCmReset = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,4,1,)).subtype(namedValues=namedval.NamedValues(("noResetRequested", 1), ("invalidateAuth", 2), ("sendAuthInvalid", 3), ("invalidateTeks", 4), ))).setMaxAccess("readwrite")
docsBpiCmtsAuthCmRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthCmReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthCmRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthCmInvalids = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
docsBpiCmtsAuthRejectErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedCm", 3), ("unauthorizedSid", 4), ))).setMaxAccess("readonly")
docsBpiCmtsAuthRejectErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmtsAuthInvalidErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 14), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,6,5,3,7,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedCm", 3), ("unsolicited", 5), ("invalidKeySequence", 6), ("keyRequestAuthenticationFailure", 7), ))).setMaxAccess("readonly")
docsBpiCmtsAuthInvalidErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 15), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmtsTEKTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3))
docsBpiCmtsTEKEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-IF-MIB", "docsIfCmtsServiceId"))
docsBpiCmtsTEKLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 604800))).setMaxAccess("readwrite")
docsBpiCmtsTEKGraceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 1800))).setMaxAccess("readonly")
docsBpiCmtsTEKExpiresOld = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
docsBpiCmtsTEKExpiresNew = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
docsBpiCmtsTEKReset = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
docsBpiCmtsKeyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
docsBpiCmtsKeyReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
docsBpiCmtsKeyRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
docsBpiCmtsTEKInvalids = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
docsBpiCmtsKeyRejectErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("unauthorizedSid", 4), ))).setMaxAccess("readonly")
docsBpiCmtsKeyRejectErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 11), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiCmtsTEKInvalidErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,6,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("invalidKeySequence", 6), ))).setMaxAccess("readonly")
docsBpiCmtsTEKInvalidErrorString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 13), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
docsBpiMulticastControl = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4))
docsBpiIpMulticastMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1))
docsBpiIpMulticastMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-BPI-MIB", "docsBpiIpMulticastAddress"), (0, "DOCS-BPI-MIB", "docsBpiIpMulticastPrefixLength"))
docsBpiIpMulticastAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 1), IpAddress()).setMaxAccess("noaccess")
docsBpiIpMulticastPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 32))).setMaxAccess("noaccess")
docsBpiIpMulticastServiceId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(8192, 16368))).setMaxAccess("readcreate")
docsBpiIpMulticastMapControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
docsBpiMulticastAuthTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2))
docsBpiMulticastAuthEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-BPI-MIB", "docsBpiMulticastServiceId"), (0, "DOCS-BPI-MIB", "docsBpiMulticastCmMacAddress"))
docsBpiMulticastServiceId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(8192, 16368))).setMaxAccess("noaccess")
docsBpiMulticastCmMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 2), MacAddress()).setMaxAccess("noaccess")
docsBpiMulticastAuthControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
docsBpiNotification = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 2))
docsBpiConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 3))
docsBpiCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 1))
docsBpiGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2))

# Augmentions

# Groups

docsBpiObsoleteObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 3)).setObjects(("DOCS-BPI-MIB", "docsBpiCmtsDefaultAuthGraceTime"), ("DOCS-BPI-MIB", "docsBpiCmtsDefaultTEKGraceTime"), )
docsBpiCmtsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 2)).setObjects(("DOCS-BPI-MIB", "docsBpiCmtsAuthCmRequests"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthReplies"), ("DOCS-BPI-MIB", "docsBpiCmtsDefaultTEKLifetime"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthRequests"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKExpiresOld"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalidErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmtsDefaultAuthLifetime"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmReset"), ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejectErrorString"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKExpiresNew"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalids"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalidErrorString"), ("DOCS-BPI-MIB", "docsBpiIpMulticastServiceId"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejects"), ("DOCS-BPI-MIB", "docsBpiIpMulticastMapControl"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKGraceTime"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejectErrorString"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalidErrorString"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmGraceTime"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalids"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmExpires"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalidErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmtsKeyRequests"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmKeySequenceNumber"), ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejects"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmReplies"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKLifetime"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmLifetime"), ("DOCS-BPI-MIB", "docsBpiCmtsKeyReplies"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejectErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmRejects"), ("DOCS-BPI-MIB", "docsBpiCmtsTEKReset"), ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejectErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmInvalids"), ("DOCS-BPI-MIB", "docsBpiMulticastAuthControl"), ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmPublicKey"), )
docsBpiCmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 1)).setObjects(("DOCS-BPI-MIB", "docsBpiCmAuthGraceTime"), ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRequests"), ("DOCS-BPI-MIB", "docsBpiCmTEKExpiresOld"), ("DOCS-BPI-MIB", "docsBpiCmTEKInvalidErrorString"), ("DOCS-BPI-MIB", "docsBpiCmAuthRejectErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmTEKKeyReplies"), ("DOCS-BPI-MIB", "docsBpiCmRekeyWaitTimeout"), ("DOCS-BPI-MIB", "docsBpiCmPrivacyEnable"), ("DOCS-BPI-MIB", "docsBpiCmOpWaitTimeout"), ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejects"), ("DOCS-BPI-MIB", "docsBpiCmAuthRejects"), ("DOCS-BPI-MIB", "docsBpiCmAuthInvalidErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmTEKGraceTime"), ("DOCS-BPI-MIB", "docsBpiCmPublicKey"), ("DOCS-BPI-MIB", "docsBpiCmAuthRejectErrorString"), ("DOCS-BPI-MIB", "docsBpiCmAuthExpires"), ("DOCS-BPI-MIB", "docsBpiCmTEKPrivacyEnable"), ("DOCS-BPI-MIB", "docsBpiCmAuthInvalids"), ("DOCS-BPI-MIB", "docsBpiCmAuthReplies"), ("DOCS-BPI-MIB", "docsBpiCmTEKInvalidErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejectErrorCode"), ("DOCS-BPI-MIB", "docsBpiCmAuthRejectWaitTimeout"), ("DOCS-BPI-MIB", "docsBpiCmAuthKeySequenceNumber"), ("DOCS-BPI-MIB", "docsBpiCmAuthRequests"), ("DOCS-BPI-MIB", "docsBpiCmTEKExpiresNew"), ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejectErrorString"), ("DOCS-BPI-MIB", "docsBpiCmAuthWaitTimeout"), ("DOCS-BPI-MIB", "docsBpiCmAuthInvalidErrorString"), ("DOCS-BPI-MIB", "docsBpiCmTEKAuthPends"), ("DOCS-BPI-MIB", "docsBpiCmAuthReset"), ("DOCS-BPI-MIB", "docsBpiCmTEKInvalids"), ("DOCS-BPI-MIB", "docsBpiCmAuthState"), ("DOCS-BPI-MIB", "docsBpiCmReauthWaitTimeout"), ("DOCS-BPI-MIB", "docsBpiCmTEKState"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DOCS-BPI-MIB", PYSNMP_MODULE_ID=docsBpiMIB)

# Objects
mibBuilder.exportSymbols("DOCS-BPI-MIB", docsBpiMIB=docsBpiMIB, docsBpiMIBObjects=docsBpiMIBObjects, docsBpiCmObjects=docsBpiCmObjects, docsBpiCmBaseTable=docsBpiCmBaseTable, docsBpiCmBaseEntry=docsBpiCmBaseEntry, docsBpiCmPrivacyEnable=docsBpiCmPrivacyEnable, docsBpiCmPublicKey=docsBpiCmPublicKey, docsBpiCmAuthState=docsBpiCmAuthState, docsBpiCmAuthKeySequenceNumber=docsBpiCmAuthKeySequenceNumber, docsBpiCmAuthExpires=docsBpiCmAuthExpires, docsBpiCmAuthReset=docsBpiCmAuthReset, docsBpiCmAuthGraceTime=docsBpiCmAuthGraceTime, docsBpiCmTEKGraceTime=docsBpiCmTEKGraceTime, docsBpiCmAuthWaitTimeout=docsBpiCmAuthWaitTimeout, docsBpiCmReauthWaitTimeout=docsBpiCmReauthWaitTimeout, docsBpiCmOpWaitTimeout=docsBpiCmOpWaitTimeout, docsBpiCmRekeyWaitTimeout=docsBpiCmRekeyWaitTimeout, docsBpiCmAuthRejectWaitTimeout=docsBpiCmAuthRejectWaitTimeout, docsBpiCmAuthRequests=docsBpiCmAuthRequests, docsBpiCmAuthReplies=docsBpiCmAuthReplies, docsBpiCmAuthRejects=docsBpiCmAuthRejects, docsBpiCmAuthInvalids=docsBpiCmAuthInvalids, docsBpiCmAuthRejectErrorCode=docsBpiCmAuthRejectErrorCode, docsBpiCmAuthRejectErrorString=docsBpiCmAuthRejectErrorString, docsBpiCmAuthInvalidErrorCode=docsBpiCmAuthInvalidErrorCode, docsBpiCmAuthInvalidErrorString=docsBpiCmAuthInvalidErrorString, docsBpiCmTEKTable=docsBpiCmTEKTable, docsBpiCmTEKEntry=docsBpiCmTEKEntry, docsBpiCmTEKPrivacyEnable=docsBpiCmTEKPrivacyEnable, docsBpiCmTEKState=docsBpiCmTEKState, docsBpiCmTEKExpiresOld=docsBpiCmTEKExpiresOld, docsBpiCmTEKExpiresNew=docsBpiCmTEKExpiresNew, docsBpiCmTEKKeyRequests=docsBpiCmTEKKeyRequests, docsBpiCmTEKKeyReplies=docsBpiCmTEKKeyReplies, docsBpiCmTEKKeyRejects=docsBpiCmTEKKeyRejects, docsBpiCmTEKInvalids=docsBpiCmTEKInvalids, docsBpiCmTEKAuthPends=docsBpiCmTEKAuthPends, docsBpiCmTEKKeyRejectErrorCode=docsBpiCmTEKKeyRejectErrorCode, docsBpiCmTEKKeyRejectErrorString=docsBpiCmTEKKeyRejectErrorString, docsBpiCmTEKInvalidErrorCode=docsBpiCmTEKInvalidErrorCode, docsBpiCmTEKInvalidErrorString=docsBpiCmTEKInvalidErrorString, docsBpiCmtsObjects=docsBpiCmtsObjects, docsBpiCmtsBaseTable=docsBpiCmtsBaseTable, docsBpiCmtsBaseEntry=docsBpiCmtsBaseEntry, docsBpiCmtsDefaultAuthLifetime=docsBpiCmtsDefaultAuthLifetime, docsBpiCmtsDefaultTEKLifetime=docsBpiCmtsDefaultTEKLifetime, docsBpiCmtsDefaultAuthGraceTime=docsBpiCmtsDefaultAuthGraceTime, docsBpiCmtsDefaultTEKGraceTime=docsBpiCmtsDefaultTEKGraceTime, docsBpiCmtsAuthRequests=docsBpiCmtsAuthRequests, docsBpiCmtsAuthReplies=docsBpiCmtsAuthReplies, docsBpiCmtsAuthRejects=docsBpiCmtsAuthRejects, docsBpiCmtsAuthInvalids=docsBpiCmtsAuthInvalids, docsBpiCmtsAuthTable=docsBpiCmtsAuthTable, docsBpiCmtsAuthEntry=docsBpiCmtsAuthEntry, docsBpiCmtsAuthCmMacAddress=docsBpiCmtsAuthCmMacAddress, docsBpiCmtsAuthCmPublicKey=docsBpiCmtsAuthCmPublicKey, docsBpiCmtsAuthCmKeySequenceNumber=docsBpiCmtsAuthCmKeySequenceNumber, docsBpiCmtsAuthCmExpires=docsBpiCmtsAuthCmExpires, docsBpiCmtsAuthCmLifetime=docsBpiCmtsAuthCmLifetime, docsBpiCmtsAuthCmGraceTime=docsBpiCmtsAuthCmGraceTime, docsBpiCmtsAuthCmReset=docsBpiCmtsAuthCmReset, docsBpiCmtsAuthCmRequests=docsBpiCmtsAuthCmRequests, docsBpiCmtsAuthCmReplies=docsBpiCmtsAuthCmReplies, docsBpiCmtsAuthCmRejects=docsBpiCmtsAuthCmRejects, docsBpiCmtsAuthCmInvalids=docsBpiCmtsAuthCmInvalids, docsBpiCmtsAuthRejectErrorCode=docsBpiCmtsAuthRejectErrorCode, docsBpiCmtsAuthRejectErrorString=docsBpiCmtsAuthRejectErrorString, docsBpiCmtsAuthInvalidErrorCode=docsBpiCmtsAuthInvalidErrorCode, docsBpiCmtsAuthInvalidErrorString=docsBpiCmtsAuthInvalidErrorString, docsBpiCmtsTEKTable=docsBpiCmtsTEKTable, docsBpiCmtsTEKEntry=docsBpiCmtsTEKEntry, docsBpiCmtsTEKLifetime=docsBpiCmtsTEKLifetime, docsBpiCmtsTEKGraceTime=docsBpiCmtsTEKGraceTime, docsBpiCmtsTEKExpiresOld=docsBpiCmtsTEKExpiresOld, docsBpiCmtsTEKExpiresNew=docsBpiCmtsTEKExpiresNew, docsBpiCmtsTEKReset=docsBpiCmtsTEKReset, docsBpiCmtsKeyRequests=docsBpiCmtsKeyRequests, docsBpiCmtsKeyReplies=docsBpiCmtsKeyReplies, docsBpiCmtsKeyRejects=docsBpiCmtsKeyRejects, docsBpiCmtsTEKInvalids=docsBpiCmtsTEKInvalids, docsBpiCmtsKeyRejectErrorCode=docsBpiCmtsKeyRejectErrorCode, docsBpiCmtsKeyRejectErrorString=docsBpiCmtsKeyRejectErrorString, docsBpiCmtsTEKInvalidErrorCode=docsBpiCmtsTEKInvalidErrorCode, docsBpiCmtsTEKInvalidErrorString=docsBpiCmtsTEKInvalidErrorString, docsBpiMulticastControl=docsBpiMulticastControl, docsBpiIpMulticastMapTable=docsBpiIpMulticastMapTable, docsBpiIpMulticastMapEntry=docsBpiIpMulticastMapEntry, docsBpiIpMulticastAddress=docsBpiIpMulticastAddress, docsBpiIpMulticastPrefixLength=docsBpiIpMulticastPrefixLength, docsBpiIpMulticastServiceId=docsBpiIpMulticastServiceId, docsBpiIpMulticastMapControl=docsBpiIpMulticastMapControl, docsBpiMulticastAuthTable=docsBpiMulticastAuthTable, docsBpiMulticastAuthEntry=docsBpiMulticastAuthEntry, docsBpiMulticastServiceId=docsBpiMulticastServiceId, docsBpiMulticastCmMacAddress=docsBpiMulticastCmMacAddress, docsBpiMulticastAuthControl=docsBpiMulticastAuthControl, docsBpiNotification=docsBpiNotification, docsBpiConformance=docsBpiConformance, docsBpiCompliances=docsBpiCompliances, docsBpiGroups=docsBpiGroups)

# Groups
mibBuilder.exportSymbols("DOCS-BPI-MIB", docsBpiObsoleteObjectsGroup=docsBpiObsoleteObjectsGroup, docsBpiCmtsGroup=docsBpiCmtsGroup, docsBpiCmGroup=docsBpiCmGroup)
