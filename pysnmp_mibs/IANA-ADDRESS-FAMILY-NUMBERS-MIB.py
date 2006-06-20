# PySNMP SMI module. Autogenerated from smidump -f python IANA-ADDRESS-FAMILY-NUMBERS-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 23:32:57 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AddressFamilyNumbers(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(65535,4,11,10,17,15,23,13,0,8,16,20,19,9,12,1,2,22,14,21,3,24,18,6,5,7,)
    namedValues = namedval.NamedValues(("other", 0), ("ipV4", 1), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("ipV6", 2), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("reserved", 65535), ("e163", 7), ("e164", 8), ("f69", 9), )
    pass


# Objects

ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72)).setRevisions(("2002-03-14 00:00","2000-09-08 00:00","2000-03-01 00:00","2000-02-04 00:00","1999-08-26 00:00",))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", PYSNMP_MODULE_ID=ianaAddressFamilyNumbers)

# Types
mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", AddressFamilyNumbers=AddressFamilyNumbers)

# Objects
mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", ianaAddressFamilyNumbers=ianaAddressFamilyNumbers)

