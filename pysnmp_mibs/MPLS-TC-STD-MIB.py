#
# PySNMP MIB module MPLS-TC-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/MPLS-TC-STD-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:28:18 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, transmission, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "transmission", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 1)).setRevisions(("2004-06-03 00:00",))
if mibBuilder.loadTexts: mplsTCStdMIB.setOrganization('IETF Multiprotocol Label Switching (MPLS) Working\n              Group.')
if mibBuilder.loadTexts: mplsTCStdMIB.setContactInfo('        Thomas D. Nadeau\n                        Cisco Systems, Inc.\n                        tnadeau@cisco.com\n\n                        Joan Cucchiara\n                        Marconi Communications, Inc.\n                        jcucchiara@mindspring.com\n\n                        Cheenu Srinivasan\n                        Bloomberg L.P.\n                        cheenu@bloomberg.net\n\n                        Arun Viswanathan\n                        Force10 Networks, Inc.\n                        arunv@force10networks.com\n\n                        Hans Sjostrand\n                        ipUnplugged\n                        hans@ipunplugged.com\n\n                        Kireeti Kompella\n                        Juniper Networks\n                        kireeti@juniper.net\n\n             Email comments to the MPLS WG Mailing List at\n             mpls@uu.net.')
if mibBuilder.loadTexts: mplsTCStdMIB.setDescription('Copyright (C) The Internet Society (2004). The\n              initial version of this MIB module was published\n              in RFC 3811. For full legal notices see the RFC\n              itself or see:\n              http://www.ietf.org/copyrights/ianamib.html\n\n              This MIB module defines TEXTUAL-CONVENTIONs\n              for concepts used in Multiprotocol Label\n              Switching (MPLS) networks.')
mplsStdMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166))
class MplsAtmVcIdentifier(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(32,65535)

class MplsBitRate(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295),)
class MplsBurstSize(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class MplsExtendedTunnelId(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class MplsLabel(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class MplsLabelDistributionMethod(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2),)

class MplsLdpIdentifier(OctetString, TextualConvention):
    displayHint = '1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(6,6)
    fixedLength = 6

class MplsLsrIdentifier(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(4,4)
    fixedLength = 4

class MplsLdpLabelType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3),)

class MplsLSPID(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(2,2),ValueSizeConstraint(6,6),)
class MplsLspType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("unknown", 1), ("terminatingLsp", 2), ("originatingLsp", 3), ("crossConnectingLsp", 4),)

class MplsOwner(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmp", 3), ("ldp", 4), ("crldp", 5), ("rsvpTe", 6), ("policyAgent", 7),)

class MplsPathIndexOrZero(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class MplsPathIndex(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class MplsRetentionMode(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("conservative", 1), ("liberal", 2),)

class MplsTunnelAffinity(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class MplsTunnelIndex(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class MplsTunnelInstanceIndex(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535),ValueRangeConstraint(65536,4294967295),)
class TeHopAddressType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5,)
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("asnumber", 3), ("unnum", 4), ("lspid", 5),)

class TeHopAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)

class TeHopAddressAS(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(4,4)
    fixedLength = 4

class TeHopAddressUnnum(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(4,4)
    fixedLength = 4

mibBuilder.exportSymbols("MPLS-TC-STD-MIB", MplsBurstSize=MplsBurstSize, MplsLdpIdentifier=MplsLdpIdentifier, MplsLdpLabelType=MplsLdpLabelType, TeHopAddressType=TeHopAddressType, MplsLsrIdentifier=MplsLsrIdentifier, MplsTunnelIndex=MplsTunnelIndex, MplsLSPID=MplsLSPID, MplsBitRate=MplsBitRate, MplsPathIndex=MplsPathIndex, MplsLabelDistributionMethod=MplsLabelDistributionMethod, mplsTCStdMIB=mplsTCStdMIB, MplsLabel=MplsLabel, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsOwner=MplsOwner, mplsStdMIB=mplsStdMIB, TeHopAddressUnnum=TeHopAddressUnnum, TeHopAddressAS=TeHopAddressAS, MplsRetentionMode=MplsRetentionMode, MplsPathIndexOrZero=MplsPathIndexOrZero, TeHopAddress=TeHopAddress, MplsTunnelAffinity=MplsTunnelAffinity, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, PYSNMP_MODULE_ID=mplsTCStdMIB, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsLspType=MplsLspType)
