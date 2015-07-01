#
# PySNMP MIB module IPV6-TC (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/IPV6-TC.txt
# Produced by pysmi-0.0.3 at Wed Jul  1 22:29:31 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Ipv6Address(OctetString, TextualConvention):
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(16,16)
    fixedLength = 16

class Ipv6AddressPrefix(OctetString, TextualConvention):
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,16)

class Ipv6AddressIfIdentifier(OctetString, TextualConvention):
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,8)

class Ipv6IfIndex(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,2147483647)

class Ipv6IfIndexOrZero(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6Address=Ipv6Address, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero, Ipv6IfIndex=Ipv6IfIndex)
