# PySNMP SMI module. Autogenerated from smidump -f python FR-ATM-PVC-SERVICE-IWF-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:47 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( atmVclEntry, ) = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
( AtmVcIdentifier, AtmVpIdentifier, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp")

# Objects

frAtmIwfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 86))
frAtmIwfMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 1))
frAtmIwfConnIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 86, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
frAtmIwfConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 2))
frAtmIwfConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 2, 1)).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndex"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtmPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVpi"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVci"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFrPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDlci"))
frAtmIwfConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
frAtmIwfConnAtmPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
frAtmIwfConnVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
frAtmIwfConnVci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("noaccess"))
frAtmIwfConnFrPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
frAtmIwfConnDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(16, 4194303))).setMaxAccess("noaccess"))
frAtmIwfConnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
frAtmIwfConnAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readwrite"))
frAtmIwfConnAtm2FrOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly"))
frAtmIwfConnAtm2FrLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
frAtmIwfConnFr2AtmOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly"))
frAtmIwfConnFr2AtmLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
frAtmIwfConnectionDescriptor = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readwrite"))
frAtmIwfConnFailedFrameTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnOverSizedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnFailedAal5PduTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnOverSizedSDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 17)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnCrcErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 18)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnSarTimeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
frAtmIwfConnectionDescriptorIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 86, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
frAtmIwfConnectionDescriptorTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 4))
frAtmIwfConnectionDescriptorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 4, 1)).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndex"))
frAtmIwfConnectionDescriptorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
frAtmIwfConnDescriptorRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
frAtmIwfConnDeToClpMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3), )).clone(1)).setMaxAccess("readwrite"))
frAtmIwfConnClpToDeMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3), )).clone(1)).setMaxAccess("readwrite"))
frAtmIwfConnCongestionMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("mode1", 1), ("mode2", 2), )).clone(1)).setMaxAccess("readwrite"))
frAtmIwfConnEncapsulationMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 6)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("transparentMode", 1), ("translationMode", 2), ("translationModeAll", 3), )).clone(1)).setMaxAccess("readwrite"))
frAtmIwfConnEncapsulationMappings = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 7)).setColumnInitializer(MibVariable((), Bits().subtype(namedValues=namedval.NamedValues(("none", 0), ("bridgedPdus", 1), ("bridged802dot6", 2), ("bPdus", 3), ("routedIp", 4), ("routedOsi", 5), ("otherRouted", 6), ("x25Iso8202", 7), ("q933q2931", 8), )).clone(("none",))).setMaxAccess("readwrite"))
frAtmIwfConnFragAndReassEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 8)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readwrite"))
frAtmIwfConnArpTranslationEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readwrite"))
frAtmIwfVclTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 5))
frAtmIwfVclEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 5, 1))
frAtmIwfVclCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 5, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
frAtmIwfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2))
frAtmIwfTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2, 0))
frAtmIwfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3))
frAtmIwfGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 1))
frAtmIwfCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 2))

# Augmentions
atmVclEntry, = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
atmVclEntry.registerAugmentions(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclEntry"))
apply(frAtmIwfVclEntry.setIndexNames, atmVclEntry.getIndexNames())

# Notifications

frAtmIwfConnStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 86, 2, 0, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), )

# Groups

frAtmIwfConnectionDescriptorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 2)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCongestionMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnClpToDeMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndexNext"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnArpTranslationEnabled"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFragAndReassEnabled"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDescriptorRowStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDeToClpMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappings"), )
frAtmIwfNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 4)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnStatusChange"), )
frAtmIwfAtmVclTableAugmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 3)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclCrossConnectIdentifier"), )
frAtmIwfBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedFrames"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptor"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedSDUs"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCrcErrors"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedFrameTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnRowStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnSarTimeOuts"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedAal5PduTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndexNext"), )

# Exports

# Objects
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfMIB=frAtmIwfMIB, frAtmIwfMIBObjects=frAtmIwfMIBObjects, frAtmIwfConnIndexNext=frAtmIwfConnIndexNext, frAtmIwfConnectionTable=frAtmIwfConnectionTable, frAtmIwfConnectionEntry=frAtmIwfConnectionEntry, frAtmIwfConnIndex=frAtmIwfConnIndex, frAtmIwfConnAtmPort=frAtmIwfConnAtmPort, frAtmIwfConnVpi=frAtmIwfConnVpi, frAtmIwfConnVci=frAtmIwfConnVci, frAtmIwfConnFrPort=frAtmIwfConnFrPort, frAtmIwfConnDlci=frAtmIwfConnDlci, frAtmIwfConnRowStatus=frAtmIwfConnRowStatus, frAtmIwfConnAdminStatus=frAtmIwfConnAdminStatus, frAtmIwfConnAtm2FrOperStatus=frAtmIwfConnAtm2FrOperStatus, frAtmIwfConnAtm2FrLastChange=frAtmIwfConnAtm2FrLastChange, frAtmIwfConnFr2AtmOperStatus=frAtmIwfConnFr2AtmOperStatus, frAtmIwfConnFr2AtmLastChange=frAtmIwfConnFr2AtmLastChange, frAtmIwfConnectionDescriptor=frAtmIwfConnectionDescriptor, frAtmIwfConnFailedFrameTranslate=frAtmIwfConnFailedFrameTranslate, frAtmIwfConnOverSizedFrames=frAtmIwfConnOverSizedFrames, frAtmIwfConnFailedAal5PduTranslate=frAtmIwfConnFailedAal5PduTranslate, frAtmIwfConnOverSizedSDUs=frAtmIwfConnOverSizedSDUs, frAtmIwfConnCrcErrors=frAtmIwfConnCrcErrors, frAtmIwfConnSarTimeOuts=frAtmIwfConnSarTimeOuts, frAtmIwfConnectionDescriptorIndexNext=frAtmIwfConnectionDescriptorIndexNext, frAtmIwfConnectionDescriptorTable=frAtmIwfConnectionDescriptorTable, frAtmIwfConnectionDescriptorEntry=frAtmIwfConnectionDescriptorEntry, frAtmIwfConnectionDescriptorIndex=frAtmIwfConnectionDescriptorIndex, frAtmIwfConnDescriptorRowStatus=frAtmIwfConnDescriptorRowStatus, frAtmIwfConnDeToClpMappingMode=frAtmIwfConnDeToClpMappingMode, frAtmIwfConnClpToDeMappingMode=frAtmIwfConnClpToDeMappingMode, frAtmIwfConnCongestionMappingMode=frAtmIwfConnCongestionMappingMode, frAtmIwfConnEncapsulationMappingMode=frAtmIwfConnEncapsulationMappingMode, frAtmIwfConnEncapsulationMappings=frAtmIwfConnEncapsulationMappings, frAtmIwfConnFragAndReassEnabled=frAtmIwfConnFragAndReassEnabled, frAtmIwfConnArpTranslationEnabled=frAtmIwfConnArpTranslationEnabled, frAtmIwfVclTable=frAtmIwfVclTable, frAtmIwfVclEntry=frAtmIwfVclEntry, frAtmIwfVclCrossConnectIdentifier=frAtmIwfVclCrossConnectIdentifier, frAtmIwfTraps=frAtmIwfTraps, frAtmIwfTrapsPrefix=frAtmIwfTrapsPrefix, frAtmIwfConformance=frAtmIwfConformance, frAtmIwfGroups=frAtmIwfGroups, frAtmIwfCompliances=frAtmIwfCompliances)

# Notifications
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfConnStatusChange=frAtmIwfConnStatusChange)

# Groups
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfConnectionDescriptorGroup=frAtmIwfConnectionDescriptorGroup, frAtmIwfNotificationsGroup=frAtmIwfNotificationsGroup, frAtmIwfAtmVclTableAugmentGroup=frAtmIwfAtmVclTableAugmentGroup, frAtmIwfBasicGroup=frAtmIwfBasicGroup)