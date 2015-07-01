#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/IANA-ADDRESS-FAMILY-NUMBERS-MIB.txt
# Produced by pysmi-0.0.3 at Wed Jul  1 22:28:20 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72)).setRevisions(("2002-03-14 00:00", "2000-09-08 00:00", "2000-03-01 00:00", "2000-02-04 00:00", "1999-08-26 00:00",))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setContactInfo('Postal:    Internet Assigned Numbers Authority\n                      Internet Corporation for Assigned Names\n\t\t      and Numbers\n                      4676 Admiralty Way, Suite 330\n                      Marina del Rey, CA 90292-6601\n                      USA\n\n          Tel:    +1  310-823-9358\n          E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setDescription('The MIB module defines the AddressFamilyNumbers\n          textual convention.')
class AddressFamilyNumbers(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535,)
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("reserved", 65535),)

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", AddressFamilyNumbers=AddressFamilyNumbers, ianaAddressFamilyNumbers=ianaAddressFamilyNumbers, PYSNMP_MODULE_ID=ianaAddressFamilyNumbers)
