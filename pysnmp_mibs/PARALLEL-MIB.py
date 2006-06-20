# PySNMP SMI module. Autogenerated from smidump -f python PARALLEL-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:15 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

para = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 34)).setRevisions(("1994-05-26 17:00",))
paraNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 34, 1), Integer32()).setMaxAccess("readonly")
paraPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 2))
paraPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 2, 1)).setIndexNames((0, "PARALLEL-MIB", "paraPortIndex"))
paraPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
paraPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("centronics", 2), ("dataproducts", 3), ))).setMaxAccess("readonly")
paraPortInSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3), Integer32()).setMaxAccess("readonly")
paraPortOutSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4), Integer32()).setMaxAccess("readonly")
paraInSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 3))
paraInSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 3, 1)).setIndexNames((0, "PARALLEL-MIB", "paraInSigPortIndex"), (0, "PARALLEL-MIB", "paraInSigName"))
paraInSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
paraInSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,5,4,2,)).subtype(namedValues=namedval.NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5), ))).setMaxAccess("readonly")
paraInSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("on", 2), ("off", 3), ))).setMaxAccess("readonly")
paraInSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4), Counter32()).setMaxAccess("readonly")
paraOutSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 4))
paraOutSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 4, 1)).setIndexNames((0, "PARALLEL-MIB", "paraOutSigPortIndex"), (0, "PARALLEL-MIB", "paraOutSigName"))
paraOutSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
paraOutSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,5,4,2,)).subtype(namedValues=namedval.NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5), ))).setMaxAccess("readonly")
paraOutSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("on", 2), ("off", 3), ))).setMaxAccess("readonly")
paraOutSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4), Counter32()).setMaxAccess("readonly")
paraConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5))
paraGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 1))
paraCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 2))

# Augmentions

# Groups

paraGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 34, 5, 1, 1)).setObjects(("PARALLEL-MIB", "paraNumber"), ("PARALLEL-MIB", "paraOutSigChanges"), ("PARALLEL-MIB", "paraOutSigName"), ("PARALLEL-MIB", "paraInSigState"), ("PARALLEL-MIB", "paraInSigName"), ("PARALLEL-MIB", "paraPortOutSigNumber"), ("PARALLEL-MIB", "paraPortType"), ("PARALLEL-MIB", "paraPortIndex"), ("PARALLEL-MIB", "paraInSigChanges"), ("PARALLEL-MIB", "paraOutSigState"), ("PARALLEL-MIB", "paraOutSigPortIndex"), ("PARALLEL-MIB", "paraPortInSigNumber"), ("PARALLEL-MIB", "paraInSigPortIndex"), )

# Exports

# Module identity
mibBuilder.exportSymbols("PARALLEL-MIB", PYSNMP_MODULE_ID=para)

# Objects
mibBuilder.exportSymbols("PARALLEL-MIB", para=para, paraNumber=paraNumber, paraPortTable=paraPortTable, paraPortEntry=paraPortEntry, paraPortIndex=paraPortIndex, paraPortType=paraPortType, paraPortInSigNumber=paraPortInSigNumber, paraPortOutSigNumber=paraPortOutSigNumber, paraInSigTable=paraInSigTable, paraInSigEntry=paraInSigEntry, paraInSigPortIndex=paraInSigPortIndex, paraInSigName=paraInSigName, paraInSigState=paraInSigState, paraInSigChanges=paraInSigChanges, paraOutSigTable=paraOutSigTable, paraOutSigEntry=paraOutSigEntry, paraOutSigPortIndex=paraOutSigPortIndex, paraOutSigName=paraOutSigName, paraOutSigState=paraOutSigState, paraOutSigChanges=paraOutSigChanges, paraConformance=paraConformance, paraGroups=paraGroups, paraCompliances=paraCompliances)

# Groups
mibBuilder.exportSymbols("PARALLEL-MIB", paraGroup=paraGroup)
