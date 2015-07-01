#
# PySNMP MIB module HCNUM-TC (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/HCNUM-TC.txt
# Produced by pysmi-0.0.3 at Wed Jul  1 22:27:30 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78)).setRevisions(("2000-06-08 00:00",))
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
if mibBuilder.loadTexts: hcnumTC.setContactInfo('        E-mail: mibs@ops.ietf.org\n                 Subscribe: majordomo@psg.com\n                   with msg body: subscribe mibs\n\n                 Andy Bierman\n                 Cisco Systems Inc.\n                 170 West Tasman Drive\n                 San Jose, CA 95134 USA\n                 +1 408-527-3711\n                 abierman@cisco.com\n\n                 Keith McCloghrie\n                 Cisco Systems Inc.\n                 170 West Tasman Drive\n                 San Jose, CA 95134 USA\n                 +1 408-526-5260\n                 kzm@cisco.com\n\n                 Randy Presuhn\n                 BMC Software, Inc.\n                 Office 1-3141\n                 2141 North First Street\n                 San Jose,  California 95131 USA\n                 +1 408 546-1006\n                 rpresuhn@bmc.com')
if mibBuilder.loadTexts: hcnumTC.setDescription('A MIB module containing textual conventions\n         for high capacity data types. This module\n         addresses an immediate need for data types not directly\n         supported in the SMIv2. This short-term solution\n         is meant to be deprecated as a long-term solution\n         is deployed.')
class CounterBasedGauge64(Counter64, TextualConvention):
    pass

class ZeroBasedCounter64(Counter64, TextualConvention):
    pass

mibBuilder.exportSymbols("HCNUM-TC", hcnumTC=hcnumTC, PYSNMP_MODULE_ID=hcnumTC, ZeroBasedCounter64=ZeroBasedCounter64, CounterBasedGauge64=CounterBasedGauge64)
