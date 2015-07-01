#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:29:31 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipv6FlowLabelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 103)).setRevisions(("2003-08-28 00:00",))
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setOrganization('IETF Operations and Management Area')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setContactInfo('Bert Wijnen (Editor)\n                      Lucent Technologies\n                      Schagen 33\n                      3461 GL Linschoten\n                      Netherlands\n                      Phone: +31 348-407-775\n                      EMail: bwijnen@lucent.com\n\n                      Send comments to <mibs@ops.ietf.org>.\n                     ')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setDescription('This MIB module provides commonly used textual\n                      conventions for IPv6 Flow Labels.\n\n                      Copyright (C) The Internet Society (2003).  This\n                      version of this MIB module is part of RFC 3595,\n                      see the RFC itself for full legal notices.\n                     ')
class IPv6FlowLabel(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,1048575)

class IPv6FlowLabelOrAny(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575),)
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", IPv6FlowLabelOrAny=IPv6FlowLabelOrAny, ipv6FlowLabelMIB=ipv6FlowLabelMIB, IPv6FlowLabel=IPv6FlowLabel, PYSNMP_MODULE_ID=ipv6FlowLabelMIB)
