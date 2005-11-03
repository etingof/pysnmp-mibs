# PySNMP SMI module. Autogenerated from smidump -f python INTEGRATED-SERVICES-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:04 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Types

class BitRate(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class BurstSize(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class MessageSize(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class Port(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(2,4)
    pass

class Protocol(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,255)
    pass

class QosService(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,5,)
    namedValues = namedval.NamedValues(("bestEffort", 1), ("guaranteedDelay", 2), ("controlledLoad", 5), )
    pass

class SessionNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class SessionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,255)
    pass


# Objects

intSrv = ModuleIdentity((1, 3, 6, 1, 2, 1, 52)).setRevisions(("1995-11-03 05:00",))
intSrvObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 1))
intSrvIfAttribTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 1))
intSrvIfAttribEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
intSrvIfAttribAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1), BitRate()).setMaxAccess("readonly")
intSrvIfAttribMaxAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2), BitRate()).setMaxAccess("readwrite")
intSrvIfAttribAllocatedBuffer = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3), BurstSize()).setMaxAccess("readonly")
intSrvIfAttribFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
intSrvIfAttribPropagationDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5), Integer32().clone(0)).setMaxAccess("readwrite")
intSrvIfAttribStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6), RowStatus()).setMaxAccess("readwrite")
intSrvFlowTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 2))
intSrvFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 2, 1)).setIndexNames((0, "INTEGRATED-SERVICES-MIB", "intSrvFlowNumber"))
intSrvFlowNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1), SessionNumber()).setMaxAccess("noaccess")
intSrvFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2), SessionType()).setMaxAccess("readwrite")
intSrvFlowOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("rsvp", 2), ("management", 3), ))).setMaxAccess("readwrite")
intSrvFlowDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
intSrvFlowSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
intSrvFlowDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
intSrvFlowSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
intSrvFlowProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8), Protocol()).setMaxAccess("readwrite")
intSrvFlowDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9), Port()).setMaxAccess("readwrite")
intSrvFlowPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10), Port()).setMaxAccess("readwrite")
intSrvFlowFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
intSrvFlowInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12), InterfaceIndex()).setMaxAccess("readwrite")
intSrvFlowIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 16))).setMaxAccess("readwrite")
intSrvFlowRate = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14), BitRate()).setMaxAccess("readwrite")
intSrvFlowBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15), BurstSize()).setMaxAccess("readwrite")
intSrvFlowWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16), Integer32()).setMaxAccess("readwrite")
intSrvFlowQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
intSrvFlowMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18), MessageSize()).setMaxAccess("readwrite")
intSrvFlowMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19), MessageSize()).setMaxAccess("readwrite")
intSrvFlowBestEffort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
intSrvFlowPoliced = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
intSrvFlowDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22), TruthValue()).setMaxAccess("readwrite")
intSrvFlowService = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23), QosService()).setMaxAccess("readonly")
intSrvFlowOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
intSrvFlowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25), RowStatus()).setMaxAccess("readwrite")
intSrvGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 2))
intSrvFlowNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 52, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
intSrvNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 3))
intSrvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4))
intSrvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))

# Augmentions

# Groups

intSrvFlowsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 2)).setObjects(("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowPoliced"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowIfAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowWeight"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowOwner"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowService"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowType"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddr"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddrLength"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowOrder"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowProtocol"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowInterface"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowBurst"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowQueue"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowRate"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowPort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddrLength"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowMinTU"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestPort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowBestEffort"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"), ("INTEGRATED-SERVICES-MIB", "intSrvFlowDiscard"), )
intSrvIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 1)).setObjects(("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBuffer"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribStatus"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribPropagationDelay"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBits"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribMaxAllocatedBits"), ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribFlows"), )

# Exports

# Module identity
mibBuilder.exportSymbols("INTEGRATED-SERVICES-MIB", PYSNMP_MODULE_ID=intSrv)

# Types
mibBuilder.exportSymbols("INTEGRATED-SERVICES-MIB", BitRate=BitRate, BurstSize=BurstSize, MessageSize=MessageSize, Port=Port, Protocol=Protocol, QosService=QosService, SessionNumber=SessionNumber, SessionType=SessionType)

# Objects
mibBuilder.exportSymbols("INTEGRATED-SERVICES-MIB", intSrv=intSrv, intSrvObjects=intSrvObjects, intSrvIfAttribTable=intSrvIfAttribTable, intSrvIfAttribEntry=intSrvIfAttribEntry, intSrvIfAttribAllocatedBits=intSrvIfAttribAllocatedBits, intSrvIfAttribMaxAllocatedBits=intSrvIfAttribMaxAllocatedBits, intSrvIfAttribAllocatedBuffer=intSrvIfAttribAllocatedBuffer, intSrvIfAttribFlows=intSrvIfAttribFlows, intSrvIfAttribPropagationDelay=intSrvIfAttribPropagationDelay, intSrvIfAttribStatus=intSrvIfAttribStatus, intSrvFlowTable=intSrvFlowTable, intSrvFlowEntry=intSrvFlowEntry, intSrvFlowNumber=intSrvFlowNumber, intSrvFlowType=intSrvFlowType, intSrvFlowOwner=intSrvFlowOwner, intSrvFlowDestAddr=intSrvFlowDestAddr, intSrvFlowSenderAddr=intSrvFlowSenderAddr, intSrvFlowDestAddrLength=intSrvFlowDestAddrLength, intSrvFlowSenderAddrLength=intSrvFlowSenderAddrLength, intSrvFlowProtocol=intSrvFlowProtocol, intSrvFlowDestPort=intSrvFlowDestPort, intSrvFlowPort=intSrvFlowPort, intSrvFlowFlowId=intSrvFlowFlowId, intSrvFlowInterface=intSrvFlowInterface, intSrvFlowIfAddr=intSrvFlowIfAddr, intSrvFlowRate=intSrvFlowRate, intSrvFlowBurst=intSrvFlowBurst, intSrvFlowWeight=intSrvFlowWeight, intSrvFlowQueue=intSrvFlowQueue, intSrvFlowMinTU=intSrvFlowMinTU, intSrvFlowMaxTU=intSrvFlowMaxTU, intSrvFlowBestEffort=intSrvFlowBestEffort, intSrvFlowPoliced=intSrvFlowPoliced, intSrvFlowDiscard=intSrvFlowDiscard, intSrvFlowService=intSrvFlowService, intSrvFlowOrder=intSrvFlowOrder, intSrvFlowStatus=intSrvFlowStatus, intSrvGenObjects=intSrvGenObjects, intSrvFlowNewIndex=intSrvFlowNewIndex, intSrvNotifications=intSrvNotifications, intSrvConformance=intSrvConformance, intSrvGroups=intSrvGroups, intSrvCompliances=intSrvCompliances)

# Groups
mibBuilder.exportSymbols("INTEGRATED-SERVICES-MIB", intSrvFlowsGroup=intSrvFlowsGroup, intSrvIfAttribGroup=intSrvIfAttribGroup)
