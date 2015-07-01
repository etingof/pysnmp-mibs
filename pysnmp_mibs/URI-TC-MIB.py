#
# PySNMP MIB module URI-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/URI-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:33:01 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uriTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 164)).setRevisions(("2007-09-10 00:00",))
if mibBuilder.loadTexts: uriTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
if mibBuilder.loadTexts: uriTcMIB.setContactInfo('EMail: ops-area@ietf.org\n                  Home page: http://www.ops.ietf.org/')
if mibBuilder.loadTexts: uriTcMIB.setDescription('This MIB module defines textual conventions for\n            representing URIs, as defined by RFC 3986 STD 66.')
class Uri(OctetString, TextualConvention):
    displayHint = '1a'

class Uri255(OctetString, TextualConvention):
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class Uri1024(OctetString, TextualConvention):
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,1024)

mibBuilder.exportSymbols("URI-TC-MIB", Uri=Uri, Uri1024=Uri1024, PYSNMP_MODULE_ID=uriTcMIB, Uri255=Uri255, uriTcMIB=uriTcMIB)
