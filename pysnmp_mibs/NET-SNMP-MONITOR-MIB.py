#
# PySNMP MIB module NET-SNMP-MONITOR-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/NET-SNMP-MONITOR-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:30:33 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( netSnmpObjects, netSnmpModuleIDs, ) = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 3)).setRevisions(("2002-02-09 00:00",))
if mibBuilder.loadTexts: netSnmpMonitorMIB.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setContactInfo('postal:   Wes Hardaker\n                    P.O. Box 382\n                    Davis CA  95617\n\n          email:    net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setDescription('Configured elements of the system to monitor\n\t (XXX - ugh! - need a better description!)')
nsProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 21))
nsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 22))
nsFile = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 23))
nsLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 24))
mibBuilder.exportSymbols("NET-SNMP-MONITOR-MIB", nsLog=nsLog, nsFile=nsFile, nsProcess=nsProcess, nsDisk=nsDisk, netSnmpMonitorMIB=netSnmpMonitorMIB, PYSNMP_MODULE_ID=netSnmpMonitorMIB)
