# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-ACC-SERVER-MIB
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
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 1)).setRevisions(("2006-08-21 00:00","1999-06-11 00:00",))
if mibBuilder.loadTexts: radiusAccServMIB.setOrganization("IETF RADIUS Extensions Working Group.")
if mibBuilder.loadTexts: radiusAccServMIB.setContactInfo(" Bernard Aboba\nMicrosoft\nOne Microsoft Way\nRedmond, WA  98052\nUS\n\n\n\nPhone: +1 425 936 6605\nEMail: bernarda@microsoft.com")
if mibBuilder.loadTexts: radiusAccServMIB.setDescription("The MIB module for entities implementing the server\nside of the Remote Authentication Dial-In User\nService (RADIUS) accounting protocol.  Copyright (C)\nThe Internet Society (2006).  This version of this\nMIB module is part of RFC 4671; see the RFC itself\nfor full legal notices.")
radiusAccServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1))
radiusAccServ = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1))
radiusAccServIdent = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServIdent.setDescription("The implementation identification string for the\nRADIUS accounting server software in use on the\nsystem, for example, 'FNS-2.1'.")
radiusAccServUpTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServUpTime.setDescription("If the server has a persistent state (e.g., a\nprocess), this value will be the time elapsed (in\nhundredths of a second) since the server process was\nstarted.  For software without persistent state, this\nvalue will be zero.")
radiusAccServResetTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServResetTime.setDescription("If the server has a persistent state (e.g., a process)\nand supports a 'reset' operation (e.g., can be told to\nre-read configuration files), this value will be the\ntime elapsed (in hundredths of a second) since the\nserver was 'reset.'  For software that does not\nhave persistence or does not support a 'reset'\noperation, this value will be zero.")
radiusAccServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusAccServConfigReset.setDescription("Status/action object to reinitialize any persistent\nserver state.  When set to reset(2), any persistent\nserver state (such as a process) is reinitialized as\nif the server had just been started.  This value will\nnever be returned by a read operation.  When read,\none of the following values will be returned:\n    other(1) - server in some unknown state;\n    initializing(3) - server (re)initializing;\n    running(4) - server currently running.")
radiusAccServTotalRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalRequests.setDescription("The number of packets received on the\naccounting port.")
radiusAccServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalInvalidRequests.setDescription("The number of RADIUS Accounting-Request packets\nreceived from unknown addresses.")
radiusAccServTotalDupRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalDupRequests.setDescription("The number of duplicate RADIUS Accounting-Request\npackets received.")
radiusAccServTotalResponses = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalResponses.setDescription("The number of RADIUS Accounting-Response packets\nsent.")
radiusAccServTotalMalformedRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalMalformedRequests.setDescription("The number of malformed RADIUS Accounting-Request\npackets received.  Bad authenticators or unknown\ntypes are not included as malformed Access-Requests.")
radiusAccServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalBadAuthenticators.setDescription("The number of RADIUS Accounting-Request packets\nthat contained an invalid authenticator.")
radiusAccServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalPacketsDropped.setDescription("The number of incoming packets silently discarded\nfor a reason other than malformed, bad authenticators,\nor unknown types.")
radiusAccServTotalNoRecords = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalNoRecords.setDescription("The number of RADIUS Accounting-Request packets\nthat were received and responded to but not\nrecorded.")
radiusAccServTotalUnknownTypes = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAccServTotalUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received.")
radiusAccClientTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14))
if mibBuilder.loadTexts: radiusAccClientTable.setDescription("The (conceptual) table listing the RADIUS accounting\nclients with which the server shares a secret.")
radiusAccClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1)).setIndexNames((0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientIndex"))
if mibBuilder.loadTexts: radiusAccClientEntry.setDescription("An entry (conceptual row) representing a RADIUS\naccounting client with which the server shares a\nsecret.")
radiusAccClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAccClientIndex.setDescription("A number uniquely identifying each RADIUS accounting\nclient with which this server communicates.")
radiusAccClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientAddress.setDescription("The NAS-IP-Address of the RADIUS accounting client\n\n\n\nreferred to in this table entry.")
radiusAccClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientID.setDescription("The NAS-Identifier of the RADIUS accounting client\nreferred to in this table entry.  This is not\nnecessarily the same as sysName in MIB II.")
radiusAccServPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServPacketsDropped.setDescription("The number of incoming packets received\nfrom this client and silently discarded\nfor a reason other than malformed, bad\nauthenticators, or unknown types.")
radiusAccServRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServRequests.setDescription("The number of packets received from this\nclient on the accounting port.")
radiusAccServDupRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServDupRequests.setDescription("The number of duplicate RADIUS Accounting-Request\npackets received from this client.")
radiusAccServResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServResponses.setDescription("The number of RADIUS Accounting-Response packets\nsent to this client.")
radiusAccServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServBadAuthenticators.setDescription("The number of RADIUS Accounting-Request packets\nthat contained invalid authenticators received\nfrom this client.")
radiusAccServMalformedRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServMalformedRequests.setDescription("The number of malformed RADIUS Accounting-Request\npackets that were received from this client.\nBad authenticators and unknown types\nare not included as malformed Accounting-Requests.")
radiusAccServNoRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServNoRecords.setDescription("The number of RADIUS Accounting-Request packets\nthat were received and responded to but not\nrecorded.")
radiusAccServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this client.")
radiusAccClientExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15))
if mibBuilder.loadTexts: radiusAccClientExtTable.setDescription("The (conceptual) table listing the RADIUS accounting\nclients with which the server shares a secret.")
radiusAccClientExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1)).setIndexNames((0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientExtIndex"))
if mibBuilder.loadTexts: radiusAccClientExtEntry.setDescription("An entry (conceptual row) representing a RADIUS\naccounting client with which the server shares a\nsecret.")
radiusAccClientExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAccClientExtIndex.setDescription("A number uniquely identifying each RADIUS accounting\nclient with which this server communicates.")
radiusAccClientInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInetAddressType.setDescription("The type of address format used for the\nradiusAccClientInetAddress object.")
radiusAccClientInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientInetAddress.setDescription("The IP address of the RADIUS accounting\nclient referred to in this table entry, using\nthe IPv6 address format.")
radiusAccClientExtID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccClientExtID.setDescription("The NAS-Identifier of the RADIUS accounting client\nreferred to in this table entry.  This is not\nnecessarily the same as sysName in MIB II.")
radiusAccServExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtPacketsDropped.setDescription("The number of incoming packets received from this\nclient and silently discarded for a reason other\nthan malformed, bad authenticators, or unknown types.\nThis counter may experience a discontinuity when the\nRADIUS Accounting Server module within the managed\nentity is reinitialized, as indicated by the current\nvalue of radiusAccServerCounterDiscontinuity.")
radiusAccServExtRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtRequests.setDescription("The number of packets received from this\nclient on the accounting port.  This counter\nmay experience a discontinuity when the\nRADIUS Accounting Server module within the\nmanaged entity is reinitialized, as indicated by\nthe current value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServExtDupRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtDupRequests.setDescription("The number of duplicate RADIUS Accounting-Request\npackets received from this client.  This counter\n\n\n\nmay experience a discontinuity when the RADIUS\nAccounting Server module within the managed\nentity is reinitialized, as indicated by the\ncurrent value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServExtResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtResponses.setDescription("The number of RADIUS Accounting-Response packets\nsent to this client.  This counter may experience\na discontinuity when the RADIUS Accounting Server\nmodule within the managed entity is reinitialized,\nas indicated by the current value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtBadAuthenticators.setDescription("The number of RADIUS Accounting-Request packets\nthat contained invalid authenticators received\nfrom this client.  This counter may experience a\ndiscontinuity when the RADIUS Accounting Server\nmodule within the managed entity is reinitialized,\nas indicated by the current value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServExtMalformedRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtMalformedRequests.setDescription("The number of malformed RADIUS Accounting-Request\npackets that were received from this client.\nBad authenticators and unknown types are not\n\n\n\nincluded as malformed Accounting-Requests.  This\ncounter may experience a discontinuity when the\nRADIUS Accounting Server module within the managed\nentity is reinitialized, as indicated by the current\nvalue of radiusAccServerCounterDiscontinuity.")
radiusAccServExtNoRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtNoRecords.setDescription("The number of RADIUS Accounting-Request packets\nthat were received and responded to but not\nrecorded.  This counter may experience a\ndiscontinuity when the RADIUS Accounting Server\nmodule within the managed entity is reinitialized,\nas indicated by the current value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServExtUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this client.  This counter may\nexperience a discontinuity when the RADIUS Accounting\nServer module within the managed entity is\nreinitialized, as indicated by the current value of\nradiusAccServerCounterDiscontinuity.")
radiusAccServerCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAccServerCounterDiscontinuity.setDescription("The number of centiseconds since the last\ndiscontinuity in the RADIUS Accounting Server\ncounters.  A discontinuity may be the result of\na reinitialization of the RADIUS Accounting Server\n\n\n\nmodule within the managed entity.")
radiusAccServMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2))
radiusAccServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1))
radiusAccServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2))

# Augmentions

# Groups

radiusAccServMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientAddress"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientID"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"), )
if mibBuilder.loadTexts: radiusAccServMIBGroup.setDescription("The collection of objects providing management of\na RADIUS Accounting Server.")
radiusAccServExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 2)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServerCounterDiscontinuity"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddressType"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddress"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientExtID"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"), )
if mibBuilder.loadTexts: radiusAccServExtMIBGroup.setDescription("The collection of objects providing management of\na RADIUS Accounting Server.")

# Compliances

radiusAccServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 1)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServMIBGroup"), )
if mibBuilder.loadTexts: radiusAccServMIBCompliance.setDescription("The compliance statement for accounting servers\nimplementing the RADIUS Accounting Server MIB.\nImplementation of this module is for IPv4-only\nentities, or for backwards compatibility use with\nentities that support both IPv4 and IPv6.")
radiusAccServExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 2)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServExtMIBGroup"), )
if mibBuilder.loadTexts: radiusAccServExtMIBCompliance.setDescription("The compliance statement for accounting\nservers implementing the RADIUS Accounting\nServer IPv6 Extensions MIB.  Implementation of\nthis module is for entities that support IPv6,\nor support IPv4 and IPv6.")

# Exports

# Module identity
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", PYSNMP_MODULE_ID=radiusAccServMIB)

# Objects
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusMIB=radiusMIB, radiusAccounting=radiusAccounting, radiusAccServMIB=radiusAccServMIB, radiusAccServMIBObjects=radiusAccServMIBObjects, radiusAccServ=radiusAccServ, radiusAccServIdent=radiusAccServIdent, radiusAccServUpTime=radiusAccServUpTime, radiusAccServResetTime=radiusAccServResetTime, radiusAccServConfigReset=radiusAccServConfigReset, radiusAccServTotalRequests=radiusAccServTotalRequests, radiusAccServTotalInvalidRequests=radiusAccServTotalInvalidRequests, radiusAccServTotalDupRequests=radiusAccServTotalDupRequests, radiusAccServTotalResponses=radiusAccServTotalResponses, radiusAccServTotalMalformedRequests=radiusAccServTotalMalformedRequests, radiusAccServTotalBadAuthenticators=radiusAccServTotalBadAuthenticators, radiusAccServTotalPacketsDropped=radiusAccServTotalPacketsDropped, radiusAccServTotalNoRecords=radiusAccServTotalNoRecords, radiusAccServTotalUnknownTypes=radiusAccServTotalUnknownTypes, radiusAccClientTable=radiusAccClientTable, radiusAccClientEntry=radiusAccClientEntry, radiusAccClientIndex=radiusAccClientIndex, radiusAccClientAddress=radiusAccClientAddress, radiusAccClientID=radiusAccClientID, radiusAccServPacketsDropped=radiusAccServPacketsDropped, radiusAccServRequests=radiusAccServRequests, radiusAccServDupRequests=radiusAccServDupRequests, radiusAccServResponses=radiusAccServResponses, radiusAccServBadAuthenticators=radiusAccServBadAuthenticators, radiusAccServMalformedRequests=radiusAccServMalformedRequests, radiusAccServNoRecords=radiusAccServNoRecords, radiusAccServUnknownTypes=radiusAccServUnknownTypes, radiusAccClientExtTable=radiusAccClientExtTable, radiusAccClientExtEntry=radiusAccClientExtEntry, radiusAccClientExtIndex=radiusAccClientExtIndex, radiusAccClientInetAddressType=radiusAccClientInetAddressType, radiusAccClientInetAddress=radiusAccClientInetAddress, radiusAccClientExtID=radiusAccClientExtID, radiusAccServExtPacketsDropped=radiusAccServExtPacketsDropped, radiusAccServExtRequests=radiusAccServExtRequests, radiusAccServExtDupRequests=radiusAccServExtDupRequests, radiusAccServExtResponses=radiusAccServExtResponses, radiusAccServExtBadAuthenticators=radiusAccServExtBadAuthenticators, radiusAccServExtMalformedRequests=radiusAccServExtMalformedRequests, radiusAccServExtNoRecords=radiusAccServExtNoRecords, radiusAccServExtUnknownTypes=radiusAccServExtUnknownTypes, radiusAccServerCounterDiscontinuity=radiusAccServerCounterDiscontinuity, radiusAccServMIBConformance=radiusAccServMIBConformance, radiusAccServMIBCompliances=radiusAccServMIBCompliances, radiusAccServMIBGroups=radiusAccServMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusAccServMIBGroup=radiusAccServMIBGroup, radiusAccServExtMIBGroup=radiusAccServExtMIBGroup)

# Compliances
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusAccServMIBCompliance=radiusAccServMIBCompliance, radiusAccServExtMIBCompliance=radiusAccServExtMIBCompliance)
