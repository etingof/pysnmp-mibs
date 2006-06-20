# PySNMP SMI module. Autogenerated from smidump -f python DOT12-IF-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:02 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")

# Objects

dot12MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 45)).setRevisions(("1996-02-22 04:52",))
dot12MIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 45, 1))
dot12ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 45, 1, 1))
dot12ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
dot12CurrentFramingType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("frameType88023", 1), ("frameType88025", 2), ("frameTypeUnknown", 3), ))).setMaxAccess("readonly")
dot12DesiredFramingType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("frameType88023", 1), ("frameType88025", 2), ("frameTypeEither", 3), ))).setMaxAccess("readwrite")
dot12FramingCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("frameType88023", 1), ("frameType88025", 2), ("frameTypeEither", 3), ))).setMaxAccess("readonly")
dot12DesiredPromiscStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("singleAddressMode", 1), ("promiscuousMode", 2), ))).setMaxAccess("readwrite")
dot12TrainingVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
dot12LastTrainingConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("readonly")
dot12Commands = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,4,)).subtype(namedValues=namedval.NamedValues(("noOp", 1), ("open", 2), ("reset", 3), ("close", 4), ))).setMaxAccess("readwrite")
dot12Status = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,6,5,2,)).subtype(namedValues=namedval.NamedValues(("opened", 1), ("closed", 2), ("opening", 3), ("openFailure", 5), ("linkFailure", 6), ))).setMaxAccess("readonly")
dot12ControlMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("masterMode", 1), ("slaveMode", 2), ("learn", 3), ))).setMaxAccess("readwrite")
dot12StatTable = MibTable((1, 3, 6, 1, 2, 1, 10, 45, 1, 2))
dot12StatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
dot12InHighPriorityFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
dot12InHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
dot12InNormPriorityFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
dot12InNormPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
dot12InIPMErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
dot12InOversizeFrameErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
dot12InDataErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
dot12InNullAddressedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
dot12OutHighPriorityFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
dot12OutHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
dot12TransitionIntoTrainings = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
dot12HCInHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
dot12HCInNormPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
dot12HCOutHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
dot12Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 45, 2))
dot12Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 45, 2, 1))
dot12Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 45, 2, 2))

# Augmentions

# Groups

dot12StatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 2)).setObjects(("DOT12-IF-MIB", "dot12InHighPriorityOctets"), ("DOT12-IF-MIB", "dot12OutHighPriorityOctets"), ("DOT12-IF-MIB", "dot12HCInHighPriorityOctets"), ("DOT12-IF-MIB", "dot12InNullAddressedFrames"), ("DOT12-IF-MIB", "dot12HCInNormPriorityOctets"), ("DOT12-IF-MIB", "dot12TransitionIntoTrainings"), ("DOT12-IF-MIB", "dot12InOversizeFrameErrors"), ("DOT12-IF-MIB", "dot12InDataErrors"), ("DOT12-IF-MIB", "dot12InIPMErrors"), ("DOT12-IF-MIB", "dot12HCOutHighPriorityOctets"), ("DOT12-IF-MIB", "dot12InNormPriorityFrames"), ("DOT12-IF-MIB", "dot12OutHighPriorityFrames"), ("DOT12-IF-MIB", "dot12InHighPriorityFrames"), ("DOT12-IF-MIB", "dot12InNormPriorityOctets"), )
dot12ConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 1)).setObjects(("DOT12-IF-MIB", "dot12Status"), ("DOT12-IF-MIB", "dot12CurrentFramingType"), ("DOT12-IF-MIB", "dot12ControlMode"), ("DOT12-IF-MIB", "dot12Commands"), ("DOT12-IF-MIB", "dot12DesiredPromiscStatus"), ("DOT12-IF-MIB", "dot12TrainingVersion"), ("DOT12-IF-MIB", "dot12LastTrainingConfig"), ("DOT12-IF-MIB", "dot12FramingCapability"), ("DOT12-IF-MIB", "dot12DesiredFramingType"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DOT12-IF-MIB", PYSNMP_MODULE_ID=dot12MIB)

# Objects
mibBuilder.exportSymbols("DOT12-IF-MIB", dot12MIB=dot12MIB, dot12MIBObjects=dot12MIBObjects, dot12ConfigTable=dot12ConfigTable, dot12ConfigEntry=dot12ConfigEntry, dot12CurrentFramingType=dot12CurrentFramingType, dot12DesiredFramingType=dot12DesiredFramingType, dot12FramingCapability=dot12FramingCapability, dot12DesiredPromiscStatus=dot12DesiredPromiscStatus, dot12TrainingVersion=dot12TrainingVersion, dot12LastTrainingConfig=dot12LastTrainingConfig, dot12Commands=dot12Commands, dot12Status=dot12Status, dot12ControlMode=dot12ControlMode, dot12StatTable=dot12StatTable, dot12StatEntry=dot12StatEntry, dot12InHighPriorityFrames=dot12InHighPriorityFrames, dot12InHighPriorityOctets=dot12InHighPriorityOctets, dot12InNormPriorityFrames=dot12InNormPriorityFrames, dot12InNormPriorityOctets=dot12InNormPriorityOctets, dot12InIPMErrors=dot12InIPMErrors, dot12InOversizeFrameErrors=dot12InOversizeFrameErrors, dot12InDataErrors=dot12InDataErrors, dot12InNullAddressedFrames=dot12InNullAddressedFrames, dot12OutHighPriorityFrames=dot12OutHighPriorityFrames, dot12OutHighPriorityOctets=dot12OutHighPriorityOctets, dot12TransitionIntoTrainings=dot12TransitionIntoTrainings, dot12HCInHighPriorityOctets=dot12HCInHighPriorityOctets, dot12HCInNormPriorityOctets=dot12HCInNormPriorityOctets, dot12HCOutHighPriorityOctets=dot12HCOutHighPriorityOctets, dot12Conformance=dot12Conformance, dot12Compliances=dot12Compliances, dot12Groups=dot12Groups)

# Groups
mibBuilder.exportSymbols("DOT12-IF-MIB", dot12StatsGroup=dot12StatsGroup, dot12ConfigGroup=dot12ConfigGroup)
