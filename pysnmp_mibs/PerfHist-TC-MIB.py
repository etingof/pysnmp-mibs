# PySNMP SMI module. Autogenerated from smidump -f python PerfHist-TC-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:59 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class PerfCurrentCount(Gauge32):
    pass

class PerfIntervalCount(Gauge32):
    pass

class PerfTotalCount(Gauge32):
    pass


# Objects

perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfCurrentCount=PerfCurrentCount, PerfIntervalCount=PerfIntervalCount, PerfTotalCount=PerfTotalCount)

# Objects
mibBuilder.exportSymbols("PerfHist-TC-MIB", perfHistTCMIB=perfHistTCMIB)
