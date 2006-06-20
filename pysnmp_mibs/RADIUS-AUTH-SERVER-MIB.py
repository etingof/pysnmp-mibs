# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-AUTH-SERVER-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:17 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 67))
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 1)).setRevisions(("1999-06-11 00:00",))
radiusAuthServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 1))
radiusAuthServ = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1))
radiusAuthServIdent = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
radiusAuthServUpTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
radiusAuthServResetTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
radiusAuthServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4), ))).setMaxAccess("readwrite")
radiusAuthServTotalAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalDupAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalAccessAccepts = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalAccessRejects = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalAccessChallenges = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalMalformedAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
radiusAuthServTotalUnknownTypes = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
radiusAuthClientTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15))
radiusAuthClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1)).setIndexNames((0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"))
radiusAuthClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
radiusAuthClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 2), IpAddress()).setMaxAccess("readonly")
radiusAuthClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
radiusAuthServAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 4), Counter32()).setMaxAccess("readonly")
radiusAuthServDupAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
radiusAuthServAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
radiusAuthServAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 7), Counter32()).setMaxAccess("readonly")
radiusAuthServAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 8), Counter32()).setMaxAccess("readonly")
radiusAuthServMalformedAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 9), Counter32()).setMaxAccess("readonly")
radiusAuthServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 10), Counter32()).setMaxAccess("readonly")
radiusAuthServPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 11), Counter32()).setMaxAccess("readonly")
radiusAuthServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 12), Counter32()).setMaxAccess("readonly")
radiusAuthServMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2))
radiusAuthServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1))
radiusAuthServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2))

# Augmentions

# Groups

radiusAuthServMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"), )

# Exports

# Module identity
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", PYSNMP_MODULE_ID=radiusAuthServMIB)

# Objects
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusMIB=radiusMIB, radiusAuthentication=radiusAuthentication, radiusAuthServMIB=radiusAuthServMIB, radiusAuthServMIBObjects=radiusAuthServMIBObjects, radiusAuthServ=radiusAuthServ, radiusAuthServIdent=radiusAuthServIdent, radiusAuthServUpTime=radiusAuthServUpTime, radiusAuthServResetTime=radiusAuthServResetTime, radiusAuthServConfigReset=radiusAuthServConfigReset, radiusAuthServTotalAccessRequests=radiusAuthServTotalAccessRequests, radiusAuthServTotalInvalidRequests=radiusAuthServTotalInvalidRequests, radiusAuthServTotalDupAccessRequests=radiusAuthServTotalDupAccessRequests, radiusAuthServTotalAccessAccepts=radiusAuthServTotalAccessAccepts, radiusAuthServTotalAccessRejects=radiusAuthServTotalAccessRejects, radiusAuthServTotalAccessChallenges=radiusAuthServTotalAccessChallenges, radiusAuthServTotalMalformedAccessRequests=radiusAuthServTotalMalformedAccessRequests, radiusAuthServTotalBadAuthenticators=radiusAuthServTotalBadAuthenticators, radiusAuthServTotalPacketsDropped=radiusAuthServTotalPacketsDropped, radiusAuthServTotalUnknownTypes=radiusAuthServTotalUnknownTypes, radiusAuthClientTable=radiusAuthClientTable, radiusAuthClientEntry=radiusAuthClientEntry, radiusAuthClientIndex=radiusAuthClientIndex, radiusAuthClientAddress=radiusAuthClientAddress, radiusAuthClientID=radiusAuthClientID, radiusAuthServAccessRequests=radiusAuthServAccessRequests, radiusAuthServDupAccessRequests=radiusAuthServDupAccessRequests, radiusAuthServAccessAccepts=radiusAuthServAccessAccepts, radiusAuthServAccessRejects=radiusAuthServAccessRejects, radiusAuthServAccessChallenges=radiusAuthServAccessChallenges, radiusAuthServMalformedAccessRequests=radiusAuthServMalformedAccessRequests, radiusAuthServBadAuthenticators=radiusAuthServBadAuthenticators, radiusAuthServPacketsDropped=radiusAuthServPacketsDropped, radiusAuthServUnknownTypes=radiusAuthServUnknownTypes, radiusAuthServMIBConformance=radiusAuthServMIBConformance, radiusAuthServMIBCompliances=radiusAuthServMIBCompliances, radiusAuthServMIBGroups=radiusAuthServMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusAuthServMIBGroup=radiusAuthServMIBGroup)
