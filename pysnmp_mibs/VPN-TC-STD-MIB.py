#
# PySNMP MIB module VPN-TC-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/VPN-TC-STD-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:30:06 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vpnTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 129)).setRevisions(("2005-11-15 00:00",))
if mibBuilder.loadTexts: vpnTcMIB.setOrganization('Layer 3 Virtual Private Networks (L3VPN) Working Group.')
if mibBuilder.loadTexts: vpnTcMIB.setContactInfo('Benson Schliesser\n         bensons@savvis.net\n\n         Thomas D. Nadeau\n         tnadeau@cisco.com\n\n         This TC MIB is a product of the PPVPN\n         http://www.ietf.org/html.charters/ppvpn-charter.html\n         and subsequently the L3VPN\n         http://www.ietf.org/html.charters/l3vpn-charter.html\n         working groups.\n\n         Comments and discussion should be directed to\n         l3vpn@ietf.org')
if mibBuilder.loadTexts: vpnTcMIB.setDescription('This MIB contains TCs for VPNs.\n\n         Copyright (C) The Internet Society (2005).  This version\n         of this MIB module is part of RFC 4265;  see the RFC\n         itself for full legal notices.')
class VPNId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(7,7)
    fixedLength = 7

class VPNIdOrZero(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(7,7),)
mibBuilder.exportSymbols("VPN-TC-STD-MIB", VPNIdOrZero=VPNIdOrZero, PYSNMP_MODULE_ID=vpnTcMIB, VPNId=VPNId, vpnTcMIB=vpnTcMIB)
