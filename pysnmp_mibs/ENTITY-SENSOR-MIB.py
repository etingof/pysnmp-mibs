# PySNMP SMI module. Autogenerated from smidump -f python ENTITY-SENSOR-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:15:25 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( entPhysicalIndex, entityPhysicalGroup, ) = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entityPhysicalGroup")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp")

# Types

class EntitySensorDataScale(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,9,15,11,6,14,4,17,7,5,13,8,10,3,12,16,2,)
    namedValues = namedval.NamedValues(("yocto", 1), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), )
    
class EntitySensorDataType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(5,12,11,8,10,6,4,2,3,7,1,9,)
    namedValues = namedval.NamedValues(("other", 1), ("rpm", 10), ("cmm", 11), ("truthvalue", 12), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), )
    
class EntitySensorPrecision(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(-8,9)
    
class EntitySensorStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,3,2,)
    namedValues = namedval.NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3), )
    
class EntitySensorValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(-1000000000,1000000000)
    

# Objects

entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 99)).setRevisions(("2002-12-16 00:00",))
if mibBuilder.loadTexts: entitySensorMIB.setOrganization("IETF Entity MIB Working Group")
if mibBuilder.loadTexts: entitySensorMIB.setContactInfo("        Andy Bierman\nCisco Systems, Inc.\nTel: +1 408-527-3711\nE-mail: abierman@cisco.com\nPostal: 170 West Tasman Drive\nSan Jose, CA USA 95134\n\nDan Romascanu\nAvaya Inc.\nTel: +972-3-645-8414\nEmail: dromasca@avaya.com\nPostal: Atidim technology Park, Bldg. #3\nTel Aviv, Israel, 61131\n\nK.C. Norseth\nL-3 Communications\nTel: +1 801-594-2809\nEmail: kenyon.c.norseth@L-3com.com\nPostal: 640 N. 2200 West.\n\n\n\nSalt Lake City, Utah 84116-0850\n\nSend comments to <entmib@ietf.org>\nMailing list subscription info:\nhttp://www.ietf.org/mailman/listinfo/entmib ")
if mibBuilder.loadTexts: entitySensorMIB.setDescription("This module defines Entity MIB extensions for physical\nsensors.\n\nCopyright (C) The Internet Society (2002). This version\nof this MIB module is part of RFC 3433; see the RFC\nitself for full legal notices.")
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 1))
entPhySensorTable = MibTable((1, 3, 6, 1, 2, 1, 99, 1, 1))
if mibBuilder.loadTexts: entPhySensorTable.setDescription("This table contains one row per physical sensor represented\nby an associated row in the entPhysicalTable.")
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 99, 1, 1, 1)).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setDescription("Information about a particular physical sensor.\n\n\n\n\n\nAn entry in this table describes the present reading of a\nsensor, the measurement units and scale, and sensor\noperational status.\n\nEntries are created in this table by the agent.  An entry\nfor each physical sensor SHOULD be created at the same time\nas the associated entPhysicalEntry.  An entry SHOULD be\ndestroyed if the associated entPhysicalEntry is destroyed.")
entPhySensorType = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setDescription("The type of data returned by the associated\nentPhySensorValue object.\n\nThis object SHOULD be set by the agent during entry\ncreation, and the value SHOULD NOT change during operation.")
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setDescription("The exponent to apply to values returned by the associated\nentPhySensorValue object.\n\nThis object SHOULD be set by the agent during entry\ncreation, and the value SHOULD NOT change during operation.")
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setDescription("The number of decimal places of precision in fixed-point\nsensor values returned by the associated entPhySensorValue\nobject.\n\nThis object SHOULD be set to '0' when the associated\nentPhySensorType value is not a fixed-point type: e.g.,\n'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.\n\nThis object SHOULD be set by the agent during entry\ncreation, and the value SHOULD NOT change during operation.")
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setDescription("The most recent measurement obtained by the agent for this\nsensor.\n\nTo correctly interpret the value of this object, the\nassociated entPhySensorType, entPhySensorScale, and\nentPhySensorPrecision objects must also be examined.")
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setDescription("The operational status of the sensor.")
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setDescription("A textual description of the data units that should be used\nin the display of entPhySensorValue.")
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setDescription("The value of sysUpTime at the time the status and/or value\nof this sensor was last obtained by the agent.")
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setDescription("An indication of the frequency that the agent updates the\nassociated entPhySensorValue object, representing in\nmilliseconds.\n\nThe value zero indicates:\n\n    - the sensor value is updated on demand (e.g.,\n      when polled by the agent for a get-request),\n    - the sensor value is updated when the sensor\n      value changes (event-driven),\n    - the agent does not know the update rate.")
entitySensorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3))
entitySensorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 1))
entitySensorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 2))

# Augmentions

# Groups

entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 99, 3, 2, 1)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorScale"), ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"), ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"), ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"), ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"), ("ENTITY-SENSOR-MIB", "entPhySensorType"), ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"), )
if mibBuilder.loadTexts: entitySensorValueGroup.setDescription("A collection of objects representing physical entity sensor\ninformation.")

# Compliances

entitySensorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 99, 3, 1, 1)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("ENTITY-SENSOR-MIB", "entitySensorValueGroup"), )
if mibBuilder.loadTexts: entitySensorCompliance.setDescription("Describes the requirements for conformance to the Entity\nSensor MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", PYSNMP_MODULE_ID=entitySensorMIB)

# Types
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", EntitySensorDataScale=EntitySensorDataScale, EntitySensorDataType=EntitySensorDataType, EntitySensorPrecision=EntitySensorPrecision, EntitySensorStatus=EntitySensorStatus, EntitySensorValue=EntitySensorValue)

# Objects
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", entitySensorMIB=entitySensorMIB, entitySensorObjects=entitySensorObjects, entPhySensorTable=entPhySensorTable, entPhySensorEntry=entPhySensorEntry, entPhySensorType=entPhySensorType, entPhySensorScale=entPhySensorScale, entPhySensorPrecision=entPhySensorPrecision, entPhySensorValue=entPhySensorValue, entPhySensorOperStatus=entPhySensorOperStatus, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, entitySensorConformance=entitySensorConformance, entitySensorCompliances=entitySensorCompliances, entitySensorGroups=entitySensorGroups)

# Groups
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", entitySensorValueGroup=entitySensorValueGroup)

# Compliances
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", entitySensorCompliance=entitySensorCompliance)
