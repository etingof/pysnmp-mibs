#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:25:40 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107)).setRevisions(("2004-02-03 00:00",))
if mibBuilder.loadTexts: hcPerfHistTCMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setContactInfo('WG-email:  adslmib@ietf.org\n           Info:      https://www1.ietf.org/mailman/listinfo/adslmib\n\n           Chair:     Mike Sneed\n                      Sand Channel Systems\n           Postal:    P.O.  Box 37324\n                      Raleigh NC 27627-7324\n                      USA\n           Email:     sneedmike@hotmail.com\n           Phone:     +1 206 600 7022\n\n           Co-editor: Bob Ray\n                      PESA Switching Systems, Inc.\n           Postal:    330-A Wynn Drive\n                      Huntsville, AL 35805\n                      USA\n           Email:     rray@pesa.com\n           Phone:     +1 256 726 9200 ext.  142\n\n           Co-editor: Rajesh Abbi\n                      Alcatel USA\n           Postal:    2301 Sugar Bush Road\n                      Raleigh, NC 27612-3339\n                      USA\n           Email:     Rajesh.Abbi@alcatel.com\n           Phone:     +1 919 850 6194\n           ')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setDescription('This MIB Module provides Textual Conventions to be\n            used by systems supporting 15 minute based performance\n            history counts that require high-capacity counts.\n\n            Copyright (C) The Internet Society (2004).  This version\n            of this MIB module is part of RFC 3705: see the RFC\n            itself for full legal notices.')
class HCPerfValidIntervals(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,96)

class HCPerfInvalidIntervals(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,96)

class HCPerfTimeElapsed(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,86399)

class HCPerfIntervalThreshold(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,900)

class HCPerfCurrentCount(Counter64, TextualConvention):
    pass

class HCPerfIntervalCount(Counter64, TextualConvention):
    pass

class HCPerfTotalCount(Counter64, TextualConvention):
    pass

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfValidIntervals=HCPerfValidIntervals, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfIntervalCount=HCPerfIntervalCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfTotalCount=HCPerfTotalCount, HCPerfIntervalThreshold=HCPerfIntervalThreshold, hcPerfHistTCMIB=hcPerfHistTCMIB)
