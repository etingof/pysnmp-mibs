# PySNMP SMI module. Autogenerated from smidump -f python APPN-DLUR-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:25:50 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( SnaControlPointName, ) = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue")

# Objects

dlurMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 5)).setRevisions(("1997-05-10 15:00",))
dlurObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 1))
dlurNodeInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 1, 1))
dlurNodeCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1))
dlurNodeCpName = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 1), SnaControlPointName()).setMaxAccess("readonly")
dlurReleaseLevel = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("readonly")
dlurAnsSupport = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("continueOrStop", 1), ("stopOnly", 2), ))).setMaxAccess("readonly")
dlurMultiSubnetSupport = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
dlurDefaultDefPrimDlusName = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 5), SnaControlPointName()).setMaxAccess("readonly")
dlurNetworkNameForwardingSupport = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
dlurNondisDlusDlurSessDeactSup = MibScalar((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
dlurDefaultDefBackupDlusTable = MibTable((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2))
dlurDefaultDefBackupDlusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1)).setIndexNames((0, "APPN-DLUR-MIB", "dlurDefaultDefBackupDlusIndex"))
dlurDefaultDefBackupDlusIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
dlurDefaultDefBackupDlusName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1, 2), SnaControlPointName()).setMaxAccess("readonly")
dlurPuInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 1, 2))
dlurPuTable = MibTable((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1))
dlurPuEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1)).setIndexNames((0, "APPN-DLUR-MIB", "dlurPuName"))
dlurPuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 17))).setMaxAccess("noaccess")
dlurPuSscpSuppliedName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
dlurPuStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,8,9,2,4,3,6,7,5,)).subtype(namedValues=namedval.NamedValues(("reset", 1), ("pendReqActpuRsp", 2), ("pendActpu", 3), ("pendActpuRsp", 4), ("active", 5), ("pendLinkact", 6), ("pendDactpuRsp", 7), ("pendInop", 8), ("pendInopActpu", 9), ))).setMaxAccess("readonly")
dlurPuAnsSupport = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("continue", 1), ("stop", 2), ))).setMaxAccess("readonly")
dlurPuLocation = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("internal", 1), ("downstream", 2), ))).setMaxAccess("readonly")
dlurPuLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
dlurPuDlusSessnStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("reset", 1), ("pendingActive", 2), ("active", 3), ("pendingInactive", 4), ))).setMaxAccess("readonly")
dlurPuActiveDlusName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
dlurPuDefPrimDlusName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 9), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
dlurPuDefBackupDlusTable = MibTable((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2))
dlurPuDefBackupDlusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1)).setIndexNames((0, "APPN-DLUR-MIB", "dlurPuDefBackupDlusPuName"), (0, "APPN-DLUR-MIB", "dlurPuDefBackupDlusIndex"))
dlurPuDefBackupDlusPuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 17))).setMaxAccess("noaccess")
dlurPuDefBackupDlusIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
dlurPuDefBackupDlusName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 3), SnaControlPointName()).setMaxAccess("readonly")
dlurDlusInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 1, 3))
dlurDlusTable = MibTable((1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1))
dlurDlusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1)).setIndexNames((0, "APPN-DLUR-MIB", "dlurDlusName"))
dlurDlusName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1, 1), SnaControlPointName()).setMaxAccess("noaccess")
dlurDlusSessnStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("reset", 1), ("pendingActive", 2), ("active", 3), ("pendingInactive", 4), ))).setMaxAccess("readonly")
dlurConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 2))
dlurCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 2, 1))
dlurGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 5, 2, 2))

# Augmentions

# Groups

dlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 5, 2, 2, 1)).setObjects(("APPN-DLUR-MIB", "dlurPuAnsSupport"), ("APPN-DLUR-MIB", "dlurDefaultDefPrimDlusName"), ("APPN-DLUR-MIB", "dlurPuLocation"), ("APPN-DLUR-MIB", "dlurReleaseLevel"), ("APPN-DLUR-MIB", "dlurPuActiveDlusName"), ("APPN-DLUR-MIB", "dlurNodeCpName"), ("APPN-DLUR-MIB", "dlurPuSscpSuppliedName"), ("APPN-DLUR-MIB", "dlurPuDefPrimDlusName"), ("APPN-DLUR-MIB", "dlurPuLsName"), ("APPN-DLUR-MIB", "dlurPuDefBackupDlusName"), ("APPN-DLUR-MIB", "dlurPuDlusSessnStatus"), ("APPN-DLUR-MIB", "dlurNetworkNameForwardingSupport"), ("APPN-DLUR-MIB", "dlurAnsSupport"), ("APPN-DLUR-MIB", "dlurDlusSessnStatus"), ("APPN-DLUR-MIB", "dlurDefaultDefBackupDlusName"), ("APPN-DLUR-MIB", "dlurPuStatus"), ("APPN-DLUR-MIB", "dlurNondisDlusDlurSessDeactSup"), ("APPN-DLUR-MIB", "dlurMultiSubnetSupport"), )

# Exports

# Module identity
mibBuilder.exportSymbols("APPN-DLUR-MIB", PYSNMP_MODULE_ID=dlurMIB)

# Objects
mibBuilder.exportSymbols("APPN-DLUR-MIB", dlurMIB=dlurMIB, dlurObjects=dlurObjects, dlurNodeInfo=dlurNodeInfo, dlurNodeCapabilities=dlurNodeCapabilities, dlurNodeCpName=dlurNodeCpName, dlurReleaseLevel=dlurReleaseLevel, dlurAnsSupport=dlurAnsSupport, dlurMultiSubnetSupport=dlurMultiSubnetSupport, dlurDefaultDefPrimDlusName=dlurDefaultDefPrimDlusName, dlurNetworkNameForwardingSupport=dlurNetworkNameForwardingSupport, dlurNondisDlusDlurSessDeactSup=dlurNondisDlusDlurSessDeactSup, dlurDefaultDefBackupDlusTable=dlurDefaultDefBackupDlusTable, dlurDefaultDefBackupDlusEntry=dlurDefaultDefBackupDlusEntry, dlurDefaultDefBackupDlusIndex=dlurDefaultDefBackupDlusIndex, dlurDefaultDefBackupDlusName=dlurDefaultDefBackupDlusName, dlurPuInfo=dlurPuInfo, dlurPuTable=dlurPuTable, dlurPuEntry=dlurPuEntry, dlurPuName=dlurPuName, dlurPuSscpSuppliedName=dlurPuSscpSuppliedName, dlurPuStatus=dlurPuStatus, dlurPuAnsSupport=dlurPuAnsSupport, dlurPuLocation=dlurPuLocation, dlurPuLsName=dlurPuLsName, dlurPuDlusSessnStatus=dlurPuDlusSessnStatus, dlurPuActiveDlusName=dlurPuActiveDlusName, dlurPuDefPrimDlusName=dlurPuDefPrimDlusName, dlurPuDefBackupDlusTable=dlurPuDefBackupDlusTable, dlurPuDefBackupDlusEntry=dlurPuDefBackupDlusEntry, dlurPuDefBackupDlusPuName=dlurPuDefBackupDlusPuName, dlurPuDefBackupDlusIndex=dlurPuDefBackupDlusIndex, dlurPuDefBackupDlusName=dlurPuDefBackupDlusName, dlurDlusInfo=dlurDlusInfo, dlurDlusTable=dlurDlusTable, dlurDlusEntry=dlurDlusEntry, dlurDlusName=dlurDlusName, dlurDlusSessnStatus=dlurDlusSessnStatus, dlurConformance=dlurConformance, dlurCompliances=dlurCompliances, dlurGroups=dlurGroups)

# Groups
mibBuilder.exportSymbols("APPN-DLUR-MIB", dlurConfGroup=dlurConfGroup)
