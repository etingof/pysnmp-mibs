# PySNMP SMI module. Autogenerated from smidump -f python Finisher-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:25:59 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( hrDeviceIndex, ) = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
( FinAttributeTypeTC, FinDeviceTypeTC, ) = mibBuilder.importSymbols("IANA-FINISHER-MIB", "FinAttributeTypeTC", "FinDeviceTypeTC")
( PrtInputTypeTC, PrtMarkerSuppliesTypeTC, ) = mibBuilder.importSymbols("IANA-PRINTER-MIB", "PrtInputTypeTC", "PrtMarkerSuppliesTypeTC")
( PresentOnOff, PrtCapacityUnitTC, PrtLocalizedDescriptionStringTC, PrtMarkerSuppliesClassTC, PrtMarkerSuppliesSupplyUnitTC, PrtMediaUnitTC, PrtSubUnitStatusTC, printmib, prtMIBConformance, ) = mibBuilder.importSymbols("Printer-MIB", "PresentOnOff", "PrtCapacityUnitTC", "PrtLocalizedDescriptionStringTC", "PrtMarkerSuppliesClassTC", "PrtMarkerSuppliesSupplyUnitTC", "PrtMediaUnitTC", "PrtSubUnitStatusTC", "printmib", "prtMIBConformance")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")

# Objects

finMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 2, 6))
finDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 30))
finDeviceTable = MibTable((1, 3, 6, 1, 2, 1, 43, 30, 1))
finDeviceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 30, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"))
finDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
finDeviceType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 2), FinDeviceTypeTC()).setMaxAccess("readonly")
finDevicePresentOnOff = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 3), PresentOnOff()).setMaxAccess("readwrite")
finDeviceCapacityUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 4), PrtCapacityUnitTC()).setMaxAccess("readonly")
finDeviceMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readwrite")
finDeviceCurrentCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readwrite")
finDeviceAssociatedMediaPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 7), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
finDeviceAssociatedOutputs = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 8), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
finDeviceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 9), PrtSubUnitStatusTC()).setMaxAccess("readonly")
finDeviceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 10), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
finSupply = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 31))
finSupplyTable = MibTable((1, 3, 6, 1, 2, 1, 43, 31, 1))
finSupplyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 31, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyIndex"))
finSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
finSupplyDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
finSupplyClass = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 3), PrtMarkerSuppliesClassTC()).setMaxAccess("readonly")
finSupplyType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 4), PrtMarkerSuppliesTypeTC()).setMaxAccess("readonly")
finSupplyDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 5), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
finSupplyUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 6), PrtMarkerSuppliesSupplyUnitTC()).setMaxAccess("readonly")
finSupplyMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readwrite")
finSupplyCurrentLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-3, 2147483647L)).clone(-2)).setMaxAccess("readwrite")
finSupplyColorName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
finSupplyMediaInput = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 32))
finSupplyMediaInputTable = MibTable((1, 3, 6, 1, 2, 1, 43, 32, 1))
finSupplyMediaInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 32, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyMediaInputIndex"))
finSupplyMediaInputIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
finSupplyMediaInputDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
finSupplyMediaInputSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
finSupplyMediaInputType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 4), PrtInputTypeTC()).setMaxAccess("readonly")
finSupplyMediaInputDimUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 5), PrtMediaUnitTC()).setMaxAccess("readonly")
finSupplyMediaInputMediaDimFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L))).setMaxAccess("readwrite")
finSupplyMediaInputMediaDimXFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L))).setMaxAccess("readwrite")
finSupplyMediaInputStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 8), PrtSubUnitStatusTC()).setMaxAccess("readonly")
finSupplyMediaInputMediaName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
finSupplyMediaInputName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
finSupplyMediaInputDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 11), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
finSupplyMediaInputSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 12), PresentOnOff()).setMaxAccess("readwrite")
finSupplyMediaInputMediaWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
finSupplyMediaInputMediaThickness = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L))).setMaxAccess("readwrite")
finSupplyMediaInputMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 15), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
finDeviceAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 33))
finDeviceAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 43, 33, 1))
finDeviceAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 33, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"), (0, "Finisher-MIB", "finDeviceAttributeTypeIndex"), (0, "Finisher-MIB", "finDeviceAttributeInstanceIndex"))
finDeviceAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 1), FinAttributeTypeTC()).setMaxAccess("noaccess")
finDeviceAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
finDeviceAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readwrite")
finDeviceAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readwrite")
finisherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 111)).setRevisions(("2004-06-02 00:00",))

# Augmentions

# Groups

finDeviceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 1)).setObjects(("Finisher-MIB", "finDeviceStatus"), ("Finisher-MIB", "finDeviceDescription"), ("Finisher-MIB", "finDevicePresentOnOff"), ("Finisher-MIB", "finDeviceMaxCapacity"), ("Finisher-MIB", "finDeviceCapacityUnit"), ("Finisher-MIB", "finDeviceAssociatedMediaPaths"), ("Finisher-MIB", "finDeviceAssociatedOutputs"), ("Finisher-MIB", "finDeviceCurrentCapacity"), ("Finisher-MIB", "finDeviceType"), )
finDeviceAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 4)).setObjects(("Finisher-MIB", "finDeviceAttributeValueAsInteger"), ("Finisher-MIB", "finDeviceAttributeValueAsOctets"), )
finSupplyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 2)).setObjects(("Finisher-MIB", "finSupplyCurrentLevel"), ("Finisher-MIB", "finSupplyDeviceIndex"), ("Finisher-MIB", "finSupplyClass"), ("Finisher-MIB", "finSupplyMaxCapacity"), ("Finisher-MIB", "finSupplyColorName"), ("Finisher-MIB", "finSupplyDescription"), ("Finisher-MIB", "finSupplyUnit"), ("Finisher-MIB", "finSupplyType"), )
finSupplyMediaInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 3)).setObjects(("Finisher-MIB", "finSupplyMediaInputDeviceIndex"), ("Finisher-MIB", "finSupplyMediaInputMediaDimXFeedDir"), ("Finisher-MIB", "finSupplyMediaInputMediaName"), ("Finisher-MIB", "finSupplyMediaInputType"), ("Finisher-MIB", "finSupplyMediaInputDescription"), ("Finisher-MIB", "finSupplyMediaInputSecurity"), ("Finisher-MIB", "finSupplyMediaInputDimUnit"), ("Finisher-MIB", "finSupplyMediaInputMediaType"), ("Finisher-MIB", "finSupplyMediaInputSupplyIndex"), ("Finisher-MIB", "finSupplyMediaInputMediaDimFeedDir"), ("Finisher-MIB", "finSupplyMediaInputMediaWeight"), ("Finisher-MIB", "finSupplyMediaInputName"), ("Finisher-MIB", "finSupplyMediaInputMediaThickness"), ("Finisher-MIB", "finSupplyMediaInputStatus"), )

# Exports

# Module identity
mibBuilder.exportSymbols("Finisher-MIB", PYSNMP_MODULE_ID=finisherMIB)

# Objects
mibBuilder.exportSymbols("Finisher-MIB", finMIBGroups=finMIBGroups, finDevice=finDevice, finDeviceTable=finDeviceTable, finDeviceEntry=finDeviceEntry, finDeviceIndex=finDeviceIndex, finDeviceType=finDeviceType, finDevicePresentOnOff=finDevicePresentOnOff, finDeviceCapacityUnit=finDeviceCapacityUnit, finDeviceMaxCapacity=finDeviceMaxCapacity, finDeviceCurrentCapacity=finDeviceCurrentCapacity, finDeviceAssociatedMediaPaths=finDeviceAssociatedMediaPaths, finDeviceAssociatedOutputs=finDeviceAssociatedOutputs, finDeviceStatus=finDeviceStatus, finDeviceDescription=finDeviceDescription, finSupply=finSupply, finSupplyTable=finSupplyTable, finSupplyEntry=finSupplyEntry, finSupplyIndex=finSupplyIndex, finSupplyDeviceIndex=finSupplyDeviceIndex, finSupplyClass=finSupplyClass, finSupplyType=finSupplyType, finSupplyDescription=finSupplyDescription, finSupplyUnit=finSupplyUnit, finSupplyMaxCapacity=finSupplyMaxCapacity, finSupplyCurrentLevel=finSupplyCurrentLevel, finSupplyColorName=finSupplyColorName, finSupplyMediaInput=finSupplyMediaInput, finSupplyMediaInputTable=finSupplyMediaInputTable, finSupplyMediaInputEntry=finSupplyMediaInputEntry, finSupplyMediaInputIndex=finSupplyMediaInputIndex, finSupplyMediaInputDeviceIndex=finSupplyMediaInputDeviceIndex, finSupplyMediaInputSupplyIndex=finSupplyMediaInputSupplyIndex, finSupplyMediaInputType=finSupplyMediaInputType, finSupplyMediaInputDimUnit=finSupplyMediaInputDimUnit, finSupplyMediaInputMediaDimFeedDir=finSupplyMediaInputMediaDimFeedDir, finSupplyMediaInputMediaDimXFeedDir=finSupplyMediaInputMediaDimXFeedDir, finSupplyMediaInputStatus=finSupplyMediaInputStatus, finSupplyMediaInputMediaName=finSupplyMediaInputMediaName, finSupplyMediaInputName=finSupplyMediaInputName, finSupplyMediaInputDescription=finSupplyMediaInputDescription, finSupplyMediaInputSecurity=finSupplyMediaInputSecurity, finSupplyMediaInputMediaWeight=finSupplyMediaInputMediaWeight, finSupplyMediaInputMediaThickness=finSupplyMediaInputMediaThickness, finSupplyMediaInputMediaType=finSupplyMediaInputMediaType, finDeviceAttribute=finDeviceAttribute, finDeviceAttributeTable=finDeviceAttributeTable, finDeviceAttributeEntry=finDeviceAttributeEntry, finDeviceAttributeTypeIndex=finDeviceAttributeTypeIndex, finDeviceAttributeInstanceIndex=finDeviceAttributeInstanceIndex, finDeviceAttributeValueAsInteger=finDeviceAttributeValueAsInteger, finDeviceAttributeValueAsOctets=finDeviceAttributeValueAsOctets, finisherMIB=finisherMIB)

# Groups
mibBuilder.exportSymbols("Finisher-MIB", finDeviceGroup=finDeviceGroup, finDeviceAttributeGroup=finDeviceAttributeGroup, finSupplyGroup=finSupplyGroup, finSupplyMediaInputGroup=finSupplyMediaInputGroup)
