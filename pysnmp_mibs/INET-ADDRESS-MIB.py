# PySNMP SMI module. Autogenerated from smidump -f python INET-ADDRESS-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:04 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class InetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    pass

class InetAddressDNS(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,255)
    pass

class InetAddressIPv4(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(4,4)
    pass

class InetAddressIPv4z(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(8,8)
    pass

class InetAddressIPv6(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(16,16)
    pass

class InetAddressIPv6z(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(20,20)
    pass

class InetAddressPrefixLength(Unsigned32):
    pass

class InetAddressType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,0,3,1,16,2,)
    namedValues = namedval.NamedValues(("unknown", 0), ("ipv4", 1), ("dns", 16), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), )
    pass

class InetAutonomousSystemNumber(Unsigned32):
    pass

class InetPortNumber(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass


# Objects

inetAddressMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 76)).setRevisions(("2002-05-09 00:00","2000-06-08 00:00",))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("INET-ADDRESS-MIB", PYSNMP_MODULE_ID=inetAddressMIB)

# Types
mibBuilder.exportSymbols("INET-ADDRESS-MIB", InetAddress=InetAddress, InetAddressDNS=InetAddressDNS, InetAddressIPv4=InetAddressIPv4, InetAddressIPv4z=InetAddressIPv4z, InetAddressIPv6=InetAddressIPv6, InetAddressIPv6z=InetAddressIPv6z, InetAddressPrefixLength=InetAddressPrefixLength, InetAddressType=InetAddressType, InetAutonomousSystemNumber=InetAutonomousSystemNumber, InetPortNumber=InetPortNumber)

# Objects
mibBuilder.exportSymbols("INET-ADDRESS-MIB", inetAddressMIB=inetAddressMIB)

