#
# PySNMP MIB module SNMPv2-TC-v1 (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/SNMPv2-TC-v1
# Produced by pysmi-0.0.3 at Wed Jul  1 22:27:02 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class PhysAddress(OctetString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(6,6)
    fixedLength = 6

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("true", 1), ("false", 2),)

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class AutonomousType(ObjectIdentifier):
    pass

class InstancePointer(ObjectIdentifier):
    pass

class VariablePointer(ObjectIdentifier):
    pass

class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6,)
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6),)

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(11,11)
    fixedLength = 11

class StorageType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3), ("permanent", 4), ("readOnly", 5),)

class TDomain(ObjectIdentifier):
    pass

class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)

mibBuilder.exportSymbols("SNMPv2-TC-v1", InstancePointer=InstancePointer, TDomain=TDomain, MacAddress=MacAddress, PhysAddress=PhysAddress, TimeStamp=TimeStamp, TimeInterval=TimeInterval, TestAndIncr=TestAndIncr, DateAndTime=DateAndTime, RowPointer=RowPointer, StorageType=StorageType, AutonomousType=AutonomousType, RowStatus=RowStatus, VariablePointer=VariablePointer, TruthValue=TruthValue, DisplayString=DisplayString, TAddress=TAddress)
