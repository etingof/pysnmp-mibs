#
# PySNMP MIB module PerfHist-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/PerfHist-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:25:44 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('Kaj Tesink\n              Postal:  Bellcore\n                       331 Newman Springs Road\n                       Red Bank, NJ 07701\n                       USA\n              Tel:     +1 732 758 5254\n              Fax:     +1 732 758 2269\n              E-mail:  kaj@bellcore.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions\n             to be used by systems supporting 15 minute\n             based performance history counts.')
class PerfCurrentCount(Gauge32, TextualConvention):
    pass

class PerfIntervalCount(Gauge32, TextualConvention):
    pass

class PerfTotalCount(Gauge32, TextualConvention):
    pass

mibBuilder.exportSymbols("PerfHist-TC-MIB", perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount, PerfCurrentCount=PerfCurrentCount, PYSNMP_MODULE_ID=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount)
