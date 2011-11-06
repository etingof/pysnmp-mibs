# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-AUTH-SERVER-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:16:04 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setDescription("The OID assigned to RADIUS MIB work by the IANA.")
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 1)).setRevisions(("2006-08-21 00:00","1999-06-11 00:00",))
if mibBuilder.loadTexts: radiusAuthServMIB.setOrganization("IETF RADIUS Extensions Working Group.")
if mibBuilder.loadTexts: radiusAuthServMIB.setContactInfo(" Bernard Aboba\nMicrosoft\nOne Microsoft Way\nRedmond, WA  98052\nUS\nPhone: +1 425 936 6605\n\n\n\nEMail: bernarda@microsoft.com")
if mibBuilder.loadTexts: radiusAuthServMIB.setDescription("The MIB module for entities implementing the server\nside of the Remote Authentication Dial-In User\nService (RADIUS) authentication protocol.  Copyright\n(C) The Internet Society (2006).  This version of this\nMIB module is part of RFC 4669; see the RFC itself for\nfull legal notices.")
radiusAuthServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 1))
radiusAuthServ = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1))
radiusAuthServIdent = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServIdent.setDescription("The implementation identification string for the\nRADIUS authentication server software in use on the\nsystem, for example, 'FNS-2.1'.")
radiusAuthServUpTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUpTime.setDescription("If the server has a persistent state (e.g., a\nprocess), this value will be the time elapsed (in\nhundredths of a second) since the server process\nwas started.  For software without persistent state,\nthis value will be zero.")
radiusAuthServResetTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServResetTime.setDescription("If the server has a persistent state (e.g., a process)\nand supports a 'reset' operation (e.g., can be told to\nre-read configuration files), this value will be the\ntime elapsed (in hundredths of a second) since the\nserver was 'reset.'  For software that does not\nhave persistence or does not support a 'reset'\noperation, this value will be zero.")
radiusAuthServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusAuthServConfigReset.setDescription("Status/action object to reinitialize any persistent\nserver state.  When set to reset(2), any persistent\nserver state (such as a process) is reinitialized as\nif the server had just been started.  This value will\nnever be returned by a read operation.  When read,\none of the following values will be returned:\n    other(1) - server in some unknown state;\n    initializing(3) - server (re)initializing;\n    running(4) - server currently running.")
radiusAuthServTotalAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRequests.setDescription("The number of packets received on the\n\n\n\nauthentication port.")
radiusAuthServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalInvalidRequests.setDescription("The number of RADIUS Access-Request packets\nreceived from unknown addresses.")
radiusAuthServTotalDupAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalDupAccessRequests.setDescription("The number of duplicate RADIUS Access-Request\npackets received.")
radiusAuthServTotalAccessAccepts = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalAccessAccepts.setDescription("The number of RADIUS Access-Accept packets sent.")
radiusAuthServTotalAccessRejects = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRejects.setDescription("The number of RADIUS Access-Reject packets sent.")
radiusAuthServTotalAccessChallenges = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalAccessChallenges.setDescription("The number of RADIUS Access-Challenge packets sent.")
radiusAuthServTotalMalformedAccessRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalMalformedAccessRequests.setDescription("The number of malformed RADIUS Access-Request\npackets received.  Bad authenticators\nand unknown types are not included as\nmalformed Access-Requests.")
radiusAuthServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalBadAuthenticators.setDescription("The number of RADIUS Authentication-Request packets\nthat contained invalid Message Authenticator\nattributes received.")
radiusAuthServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalPacketsDropped.setDescription("The number of incoming packets\nsilently discarded for some reason other\nthan malformed, bad authenticators or\nunknown types.")
radiusAuthServTotalUnknownTypes = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthServTotalUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received.")
radiusAuthClientTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15))
if mibBuilder.loadTexts: radiusAuthClientTable.setDescription("The (conceptual) table listing the RADIUS\nauthentication clients with which the server shares\na secret.")
radiusAuthClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1)).setIndexNames((0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"))
if mibBuilder.loadTexts: radiusAuthClientEntry.setDescription("An entry (conceptual row) representing a RADIUS\nauthentication client with which the server shares a\nsecret.")
radiusAuthClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAuthClientIndex.setDescription("A number uniquely identifying each RADIUS\nauthentication client with which this server\ncommunicates.")
radiusAuthClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAddress.setDescription("The NAS-IP-Address of the RADIUS authentication client\nreferred to in this table entry.")
radiusAuthClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientID.setDescription("The NAS-Identifier of the RADIUS authentication client\nreferred to in this table entry.  This is not\nnecessarily the same as sysName in MIB II.")
radiusAuthServAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRequests.setDescription("The number of packets received on the authentication\n\n\n\nport from this client.")
radiusAuthServDupAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServDupAccessRequests.setDescription("The number of duplicate RADIUS Access-Request\npackets received from this client.")
radiusAuthServAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessAccepts.setDescription("The number of RADIUS Access-Accept packets\nsent to this client.")
radiusAuthServAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRejects.setDescription("The number of RADIUS Access-Reject packets\nsent to this client.")
radiusAuthServAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessChallenges.setDescription("The number of RADIUS Access-Challenge packets\nsent to this client.")
radiusAuthServMalformedAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServMalformedAccessRequests.setDescription("The number of malformed RADIUS Access-Request\npackets received from this client.\nBad authenticators and unknown types are not included\nas malformed Access-Requests.")
radiusAuthServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServBadAuthenticators.setDescription("The number of RADIUS Authentication-Request packets\nthat contained invalid Message Authenticator\nattributes received from this client.")
radiusAuthServPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServPacketsDropped.setDescription("The number of incoming packets from this\nclient silently discarded for some reason other\nthan malformed, bad authenticators or\nunknown types.")
radiusAuthServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this client.")
radiusAuthClientExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16))
if mibBuilder.loadTexts: radiusAuthClientExtTable.setDescription("The (conceptual) table listing the RADIUS\nauthentication clients with which the server shares\na secret.")
radiusAuthClientExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1)).setIndexNames((0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientExtIndex"))
if mibBuilder.loadTexts: radiusAuthClientExtEntry.setDescription("An entry (conceptual row) representing a RADIUS\nauthentication client with which the server shares a\nsecret.")
radiusAuthClientExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAuthClientExtIndex.setDescription("A number uniquely identifying each RADIUS\nauthentication client with which this server\ncommunicates.")
radiusAuthClientInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientInetAddressType.setDescription("The type of address format used for the\nradiusAuthClientInetAddress object.")
radiusAuthClientInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientInetAddress.setDescription("The IP address of the RADIUS authentication\nclient referred to in this table entry, using\nthe version-neutral IP address format.")
radiusAuthClientExtID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtID.setDescription("The NAS-Identifier of the RADIUS authentication client\nreferred to in this table entry.  This is not\nnecessarily the same as sysName in MIB II.")
radiusAuthServExtAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtAccessRequests.setDescription("The number of packets received on the authentication\nport from this client.  This counter may experience a\ndiscontinuity when the RADIUS Server module within the\nmanaged entity is reinitialized, as indicated by the\ncurrent value of radiusAuthServCounterDiscontinuity.")
radiusAuthServExtDupAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtDupAccessRequests.setDescription("The number of duplicate RADIUS Access-Request\npackets received from this client.  This counter may\nexperience a discontinuity when the RADIUS Server\nmodule within the managed entity is reinitialized, as\nindicated by the current value of\nradiusAuthServCounterDiscontinuity.")
radiusAuthServExtAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtAccessAccepts.setDescription("The number of RADIUS Access-Accept packets\nsent to this client.  This counter may experience a\ndiscontinuity when the RADIUS Server module within the\nmanaged entity is reinitialized, as indicated by the\ncurrent value of radiusAuthServCounterDiscontinuity.")
radiusAuthServExtAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtAccessRejects.setDescription("The number of RADIUS Access-Reject packets\nsent to this client.  This counter may experience a\ndiscontinuity when the RADIUS Server module within the\n\n\n\nmanaged entity is reinitialized, as indicated by the\ncurrent value of radiusAuthServCounterDiscontinuity.")
radiusAuthServExtAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtAccessChallenges.setDescription("The number of RADIUS Access-Challenge packets\nsent to this client.  This counter may experience a\ndiscontinuity when the RADIUS Server module within the\nmanaged entity is reinitialized, as indicated by the\ncurrent value of radiusAuthServCounterDiscontinuity.")
radiusAuthServExtMalformedAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtMalformedAccessRequests.setDescription("The number of malformed RADIUS Access-Request\npackets received from this client.  Bad authenticators\nand unknown types are not included as malformed\nAccess-Requests.  This counter may experience a\ndiscontinuity when the RADIUS Server module within the\nmanaged entity is reinitialized, as indicated by the\ncurrent value of radiusAuthServCounterDiscontinuity.")
radiusAuthServExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtBadAuthenticators.setDescription("The number of RADIUS Authentication-Request packets\nthat contained invalid Message Authenticator\nattributes received from this client.  This counter\nmay experience a discontinuity when the RADIUS Server\nmodule within the managed entity is reinitialized, as\nindicated by the current value of\nradiusAuthServCounterDiscontinuity.")
radiusAuthServExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtPacketsDropped.setDescription("The number of incoming packets from this client\nsilently discarded for some reason other than\nmalformed, bad authenticators or unknown types.\nThis counter may experience a discontinuity when the\nRADIUS Server module within the managed entity is\nreinitialized, as indicated by the current value of\nradiusAuthServCounterDiscontinuity.")
radiusAuthServExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServExtUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this client.  This counter may\nexperience a discontinuity when the RADIUS Server\nmodule within the managed entity is reinitialized, as\nindicated by the current value of\nradiusAuthServCounterDiscontinuity.")
radiusAuthServCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServCounterDiscontinuity.setDescription("The number of centiseconds since the last\ndiscontinuity in the RADIUS Server counters.\nA discontinuity may be the result of a\nreinitialization of the RADIUS Server module\nwithin the managed entity.")
radiusAuthServMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2))
radiusAuthServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1))
radiusAuthServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2))

# Augmentions

# Groups

radiusAuthServMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"), )
if mibBuilder.loadTexts: radiusAuthServMIBGroup.setDescription("The collection of objects providing management of\na RADIUS Authentication Server.")
radiusAuthServExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2, 2)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientExtID"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtUnknownTypes"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientInetAddressType"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientInetAddress"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServCounterDiscontinuity"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"), )
if mibBuilder.loadTexts: radiusAuthServExtMIBGroup.setDescription("The collection of objects providing management of\na RADIUS Authentication Server.")

# Compliances

radiusAuthServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMIBGroup"), )
if mibBuilder.loadTexts: radiusAuthServMIBCompliance.setDescription("The compliance statement for authentication\nservers implementing the RADIUS Authentication\nServer MIB.  Implementation of this module is for\nIPv4-only entities, or for backwards compatibility\nuse with entities that support both IPv4 and\nIPv6.")
radiusAuthServMIBExtCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1, 2)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtMIBGroup"), )
if mibBuilder.loadTexts: radiusAuthServMIBExtCompliance.setDescription("The compliance statement for authentication\nservers implementing the RADIUS Authentication\nServer IPv6 Extensions MIB.  Implementation of\nthis module is for entities that support IPv6,\nor support IPv4 and IPv6.")

# Exports

# Module identity
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", PYSNMP_MODULE_ID=radiusAuthServMIB)

# Objects
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusMIB=radiusMIB, radiusAuthentication=radiusAuthentication, radiusAuthServMIB=radiusAuthServMIB, radiusAuthServMIBObjects=radiusAuthServMIBObjects, radiusAuthServ=radiusAuthServ, radiusAuthServIdent=radiusAuthServIdent, radiusAuthServUpTime=radiusAuthServUpTime, radiusAuthServResetTime=radiusAuthServResetTime, radiusAuthServConfigReset=radiusAuthServConfigReset, radiusAuthServTotalAccessRequests=radiusAuthServTotalAccessRequests, radiusAuthServTotalInvalidRequests=radiusAuthServTotalInvalidRequests, radiusAuthServTotalDupAccessRequests=radiusAuthServTotalDupAccessRequests, radiusAuthServTotalAccessAccepts=radiusAuthServTotalAccessAccepts, radiusAuthServTotalAccessRejects=radiusAuthServTotalAccessRejects, radiusAuthServTotalAccessChallenges=radiusAuthServTotalAccessChallenges, radiusAuthServTotalMalformedAccessRequests=radiusAuthServTotalMalformedAccessRequests, radiusAuthServTotalBadAuthenticators=radiusAuthServTotalBadAuthenticators, radiusAuthServTotalPacketsDropped=radiusAuthServTotalPacketsDropped, radiusAuthServTotalUnknownTypes=radiusAuthServTotalUnknownTypes, radiusAuthClientTable=radiusAuthClientTable, radiusAuthClientEntry=radiusAuthClientEntry, radiusAuthClientIndex=radiusAuthClientIndex, radiusAuthClientAddress=radiusAuthClientAddress, radiusAuthClientID=radiusAuthClientID, radiusAuthServAccessRequests=radiusAuthServAccessRequests, radiusAuthServDupAccessRequests=radiusAuthServDupAccessRequests, radiusAuthServAccessAccepts=radiusAuthServAccessAccepts, radiusAuthServAccessRejects=radiusAuthServAccessRejects, radiusAuthServAccessChallenges=radiusAuthServAccessChallenges, radiusAuthServMalformedAccessRequests=radiusAuthServMalformedAccessRequests, radiusAuthServBadAuthenticators=radiusAuthServBadAuthenticators, radiusAuthServPacketsDropped=radiusAuthServPacketsDropped, radiusAuthServUnknownTypes=radiusAuthServUnknownTypes, radiusAuthClientExtTable=radiusAuthClientExtTable, radiusAuthClientExtEntry=radiusAuthClientExtEntry, radiusAuthClientExtIndex=radiusAuthClientExtIndex, radiusAuthClientInetAddressType=radiusAuthClientInetAddressType, radiusAuthClientInetAddress=radiusAuthClientInetAddress, radiusAuthClientExtID=radiusAuthClientExtID, radiusAuthServExtAccessRequests=radiusAuthServExtAccessRequests, radiusAuthServExtDupAccessRequests=radiusAuthServExtDupAccessRequests, radiusAuthServExtAccessAccepts=radiusAuthServExtAccessAccepts, radiusAuthServExtAccessRejects=radiusAuthServExtAccessRejects, radiusAuthServExtAccessChallenges=radiusAuthServExtAccessChallenges, radiusAuthServExtMalformedAccessRequests=radiusAuthServExtMalformedAccessRequests, radiusAuthServExtBadAuthenticators=radiusAuthServExtBadAuthenticators, radiusAuthServExtPacketsDropped=radiusAuthServExtPacketsDropped, radiusAuthServExtUnknownTypes=radiusAuthServExtUnknownTypes, radiusAuthServCounterDiscontinuity=radiusAuthServCounterDiscontinuity, radiusAuthServMIBConformance=radiusAuthServMIBConformance, radiusAuthServMIBCompliances=radiusAuthServMIBCompliances, radiusAuthServMIBGroups=radiusAuthServMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusAuthServMIBGroup=radiusAuthServMIBGroup, radiusAuthServExtMIBGroup=radiusAuthServExtMIBGroup)

# Compliances
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusAuthServMIBCompliance=radiusAuthServMIBCompliance, radiusAuthServMIBExtCompliance=radiusAuthServMIBExtCompliance)
