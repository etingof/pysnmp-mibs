#
# PySNMP MIB module SIP-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/SIP-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:31:50 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148)).setRevisions(("2007-04-20 00:00",))
if mibBuilder.loadTexts: sipTC.setOrganization('IETF Session Initiation Protocol Working Group')
if mibBuilder.loadTexts: sipTC.setContactInfo('SIP WG email: sip@ietf.org\n\n              Co-editor  Kevin Lingle\n                         Cisco Systems, Inc.\n              postal:    7025 Kit Creek Road\n                         P.O. Box 14987\n                         Research Triangle Park, NC 27709\n                         USA\n              email:     klingle@cisco.com\n              phone:     +1 919 476 2029\n\n              Co-editor  Joon Maeng\n              email:     jmaeng@austin.rr.com\n\n              Co-editor  Jean-Francois Mule\n                         CableLabs\n              postal:    858 Coal Creek Circle\n                         Louisville, CO 80027\n                         USA\n              email:     jf.mule@cablelabs.com\n              phone:     +1 303 661 9100\n\n              Co-editor  Dave Walker\n              email:     drwalker@rogers.com')
if mibBuilder.loadTexts: sipTC.setDescription('Session Initiation Protocol (SIP) MIB TEXTUAL-CONVENTION\n        module used by other SIP-related MIB Modules.\n\n        Copyright (C) The IETF Trust (2007).  This version of\n        this MIB module is part of RFC 4780; see the RFC itself for\n\n\n\n        full legal notices.')
class SipTCTransportProtocol(Bits, TextualConvention):
    namedValues = NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5),)

class SipTCEntityRole(Bits, TextualConvention):
    namedValues = NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4),)

class SipTCOptionTagHeaders(Bits, TextualConvention):
    namedValues = NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3),)

class SipTCMethodName(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,100)

mibBuilder.exportSymbols("SIP-TC-MIB", SipTCMethodName=SipTCMethodName, PYSNMP_MODULE_ID=sipTC, SipTCTransportProtocol=SipTCTransportProtocol, sipTC=sipTC, SipTCEntityRole=SipTCEntityRole, SipTCOptionTagHeaders=SipTCOptionTagHeaders)
