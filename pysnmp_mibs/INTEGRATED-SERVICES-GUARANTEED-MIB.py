# PySNMP SMI module. Autogenerated from smidump -f python INTEGRATED-SERVICES-GUARANTEED-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:04 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( intSrv, ) = mibBuilder.importSymbols("INTEGRATED-SERVICES-MIB", "intSrv")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus")

# Objects

intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 5)).setRevisions(("1995-11-03 05:00",))
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 1))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 5, 1, 1))
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
intSrvGuaranteedIfBacklog = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 268435455))).setMaxAccess("readwrite")
intSrvGuaranteedIfDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 268435455))).setMaxAccess("readwrite")
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 268435455))).setMaxAccess("readwrite")
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3))
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 2))

# Augmentions

# Groups

intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 5, 3, 1, 2)).setObjects(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfDelay"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfBacklog"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"), )

# Exports

# Module identity
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", PYSNMP_MODULE_ID=intSrvGuaranteed)

# Objects
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteedIfBacklog=intSrvGuaranteedIfBacklog, intSrvGuaranteedIfDelay=intSrvGuaranteedIfDelay, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances)

# Groups
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup)
