#
# PySNMP MIB module IANA-MALLOC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IANA-MALLOC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:28:52 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaMallocMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 102)).setRevisions(("2003-01-27 12:00",))
if mibBuilder.loadTexts: ianaMallocMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaMallocMIB.setContactInfo(' Internet Assigned Numbers Authority\n              Internet Corporation for Assigned Names and Numbers\n              4676 Admiralty Way, Suite 330\n              Marina del Rey, CA 90292-6601\n\n              Phone: +1 310 823 9358\n              EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaMallocMIB.setDescription('This MIB module defines the IANAscopeSource and\n            IANAmallocRangeSource textual conventions for use in MIBs\n            which need to identify ways of learning multicast scope and\n            range information.\n\n            Any additions or changes to the contents of this MIB module\n            require either publication of an RFC, or Designated Expert\n            Review as defined in the Guidelines for Writing IANA\n            Considerations Section document.  The Designated Expert will\n            be selected by the IESG Area Director(s) of the Transport\n            Area.')
class IANAscopeSource(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3), ("mzap", 4), ("madcap", 5),)

class IANAmallocRangeSource(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3),)

mibBuilder.exportSymbols("IANA-MALLOC-MIB", IANAscopeSource=IANAscopeSource, IANAmallocRangeSource=IANAmallocRangeSource, ianaMallocMIB=ianaMallocMIB, PYSNMP_MODULE_ID=ianaMallocMIB)
