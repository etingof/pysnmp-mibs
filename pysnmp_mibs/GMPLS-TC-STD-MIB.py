#
# PySNMP MIB module GMPLS-TC-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/GMPLS-TC-STD-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:28:18 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gmplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 12)).setRevisions(("2007-02-28 00:00",))
if mibBuilder.loadTexts: gmplsTCStdMIB.setOrganization('IETF Common Control and Measurement Plane (CCAMP) Working Group')
if mibBuilder.loadTexts: gmplsTCStdMIB.setContactInfo('       Thomas D. Nadeau\n               Cisco Systems, Inc.\n        Email: tnadeau@cisco.com\n\n               Adrian Farrel\n               Old Dog Consulting\n        Email: adrian@olddog.co.uk\n\n        Comments about this document should be emailed directly to the\n        CCAMP working group mailing list at ccamp@ops.ietf.org')
if mibBuilder.loadTexts: gmplsTCStdMIB.setDescription('Copyright (C) The IETF Trust (2007).  This version of\n        this MIB module is part of RFC 4801; see the RFC itself for\n        full legal notices.\n\n        This MIB module defines TEXTUAL-CONVENTIONs for concepts used in\n        Generalized Multiprotocol Label Switching (GMPLS) networks.')
class GmplsFreeformLabelTC(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,64)

class GmplsLabelTypeTC(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6,)
    namedValues = NamedValues(("gmplsMplsLabel", 1), ("gmplsPortWavelengthLabel", 2), ("gmplsFreeformGeneralizedLabel", 3), ("gmplsSonetLabel", 4), ("gmplsSdhLabel", 5), ("gmplsWavebandLabel", 6),)

class GmplsSegmentDirectionTC(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("forward", 1), ("reverse", 2),)

mibBuilder.exportSymbols("GMPLS-TC-STD-MIB", PYSNMP_MODULE_ID=gmplsTCStdMIB, GmplsFreeformLabelTC=GmplsFreeformLabelTC, GmplsLabelTypeTC=GmplsLabelTypeTC, gmplsTCStdMIB=gmplsTCStdMIB, GmplsSegmentDirectionTC=GmplsSegmentDirectionTC)
