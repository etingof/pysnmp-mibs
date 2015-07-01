#
# PySNMP MIB module ADSL-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/ADSL-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:25:44 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, transmission, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "transmission", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94))
adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2)).setRevisions(("1999-08-19 00:00",))
if mibBuilder.loadTexts: adsltcmib.setOrganization('IETF ADSL MIB Working Group')
if mibBuilder.loadTexts: adsltcmib.setContactInfo('\n       Gregory Bathrick\n       AG Communication Systems\n       A Subsidiary of Lucent Technologies\n       2500 W Utopia Rd.\n       Phoenix, AZ 85027 USA\n       Tel: +1 602-582-7679\n       Fax: +1 602-582-7697\n       E-mail: bathricg@agcs.com\n\n       Faye Ly\n       Copper Mountain Networks\n       Norcal Office\n       2470 Embarcadero Way\n       Palo Alto, CA 94303\n       Tel: +1 650-858-8500\n       Fax: +1 650-858-8085\n       E-Mail: faye@coppermountain.com\n       IETF ADSL MIB Working Group (adsl@xlist.agcs.com)\n       ')
if mibBuilder.loadTexts: adsltcmib.setDescription('The MIB module which provides a ADSL\n           Line Coding Textual Convention to be used\n           by ADSL Lines.')
class AdslLineCodingType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4),)

class AdslPerfCurrDayCount(Gauge32, TextualConvention):
    pass

class AdslPerfPrevDayCount(Gauge32, TextualConvention):
    pass

class AdslPerfTimeElapsed(Gauge32, TextualConvention):
    pass

mibBuilder.exportSymbols("ADSL-TC-MIB", AdslPerfCurrDayCount=AdslPerfCurrDayCount, PYSNMP_MODULE_ID=adsltcmib, AdslLineCodingType=AdslLineCodingType, AdslPerfPrevDayCount=AdslPerfPrevDayCount, adslMIB=adslMIB, AdslPerfTimeElapsed=AdslPerfTimeElapsed, adsltcmib=adsltcmib)
