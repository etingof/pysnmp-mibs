#
# PySNMP MIB module T11-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/T11-TC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:32:17 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11TcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 136)).setRevisions(("2006-03-02 00:00",))
if mibBuilder.loadTexts: t11TcMIB.setOrganization('T11')
if mibBuilder.loadTexts: t11TcMIB.setContactInfo('     Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  Phone: +1 408 853-9172\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA USA 95134\n                  Phone: +1 408-526-5260\n                  EMail: kzm@cisco.com')
if mibBuilder.loadTexts: t11TcMIB.setDescription('This module defines textual conventions used in T11 MIBs.\n\n           Copyright (C) The Internet Society (2006).  This version\n           of this MIB module is part of RFC 4439;  see the RFC\n           itself for full legal notices.')
class T11FabricIndex(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4095)

mibBuilder.exportSymbols("T11-TC-MIB", T11FabricIndex=T11FabricIndex, t11TcMIB=t11TcMIB, PYSNMP_MODULE_ID=t11TcMIB)
