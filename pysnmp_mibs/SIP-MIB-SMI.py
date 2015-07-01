#
# PySNMP MIB module SIP-MIB-SMI (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/SIP-MIB-SMI
# Produced by pysmi-0.0.3 at Wed Jul  1 22:31:53 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 9998))
if mibBuilder.loadTexts: sipMIB.setOrganization('IETF SIP Working Group, SIP MIB Team')
if mibBuilder.loadTexts: sipMIB.setContactInfo('SIP MIB Team email: sip-mib@egroups.com \n\n                 Co-editor  Kevin Lingle \n                            Cisco Systems, Inc. \n                 postal:    7025 Kit Creek Road \n\nLingle/Maeng/Walker                                                  5 \nInternet Draft            SIP-MIB                          July, 2000 \n\n                            P.O. Box 14987 \n                            Research Triangle Park, NC 27709 \n                            USA \n                 email:     klingle@cisco.com \n                 phone:     +1-919-392-2029 \n\n                 Co-editor  Joon Maeng \n                            VTEL Corporation \n                 postal:    108 Wild Basin Rd. \n                            Austin, TX 78746 \n                            USA \n                 email:     joon_maeng@vtel.com \n                 phone:     +1-512-437-4567 \n\n                 Co-editor  Dave Walker \n                            SS8 Networks, Inc. \n                 postal:    80 Hines Road \n                            Kanata, ON  K2K 2T8 \n                            Canada \n                 email:     drwalker@ss8networks.com \n                 phone:     +1 613 592 2100')
if mibBuilder.loadTexts: sipMIB.setDescription('Initial version of Session Initiation Protocol (SIP) \n                 MIB module that defines base OID for all other \n                 SIP-related MIB Modules.')
mibBuilder.exportSymbols("SIP-MIB-SMI", sipMIB=sipMIB, PYSNMP_MODULE_ID=sipMIB)
