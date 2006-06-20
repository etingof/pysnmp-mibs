# PySNMP SMI module. Autogenerated from smidump -f python AGENTX-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:09:55 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( TDomain, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class AgentxTAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    pass


# Objects

agentxMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 74)).setRevisions(("2000-01-10 00:00",))
agentxObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 1))
agentxGeneral = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 1, 1))
agentxDefaultTimeout = MibScalar((1, 3, 6, 1, 2, 1, 74, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(5)).setMaxAccess("readonly").setUnits("seconds")
agentxMasterAgentXVer = MibScalar((1, 3, 6, 1, 2, 1, 74, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
agentxConnection = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 1, 2))
agentxConnTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 74, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
agentxConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 74, 1, 2, 2))
agentxConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1)).setIndexNames((0, "AGENTX-MIB", "agentxConnIndex"))
agentxConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
agentxConnOpenTime = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
agentxConnTransportDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 3), TDomain()).setMaxAccess("readonly")
agentxConnTransportAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 4), AgentxTAddress()).setMaxAccess("readonly")
agentxSession = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 1, 3))
agentxSessionTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 74, 1, 3, 1), TimeStamp()).setMaxAccess("readonly")
agentxSessionTable = MibTable((1, 3, 6, 1, 2, 1, 74, 1, 3, 2))
agentxSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1)).setIndexNames((0, "AGENTX-MIB", "agentxConnIndex"), (0, "AGENTX-MIB", "agentxSessionIndex"))
agentxSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4294967295L))).setMaxAccess("noaccess")
agentxSessionObjectID = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
agentxSessionDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
agentxSessionAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readwrite")
agentxSessionOpenTime = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
agentxSessionAgentXVer = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
agentxSessionTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
agentxRegistration = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 1, 4))
agentxRegistrationTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 74, 1, 4, 1), TimeStamp()).setMaxAccess("readonly")
agentxRegistrationTable = MibTable((1, 3, 6, 1, 2, 1, 74, 1, 4, 2))
agentxRegistrationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1)).setIndexNames((0, "AGENTX-MIB", "agentxConnIndex"), (0, "AGENTX-MIB", "agentxSessionIndex"), (0, "AGENTX-MIB", "agentxRegIndex"))
agentxRegIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
agentxRegContext = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
agentxRegStart = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
agentxRegRangeSubId = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
agentxRegUpperBound = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
agentxRegPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
agentxRegTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
agentxRegInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
agentxConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 2))
agentxMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 2, 1))
agentxMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 74, 2, 2))

# Augmentions

# Groups

agentxMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 74, 2, 1, 1)).setObjects(("AGENTX-MIB", "agentxSessionDescr"), ("AGENTX-MIB", "agentxSessionAdminStatus"), ("AGENTX-MIB", "agentxConnTransportDomain"), ("AGENTX-MIB", "agentxRegPriority"), ("AGENTX-MIB", "agentxSessionTableLastChange"), ("AGENTX-MIB", "agentxSessionAgentXVer"), ("AGENTX-MIB", "agentxConnTableLastChange"), ("AGENTX-MIB", "agentxDefaultTimeout"), ("AGENTX-MIB", "agentxConnOpenTime"), ("AGENTX-MIB", "agentxSessionTimeout"), ("AGENTX-MIB", "agentxMasterAgentXVer"), ("AGENTX-MIB", "agentxSessionObjectID"), ("AGENTX-MIB", "agentxRegRangeSubId"), ("AGENTX-MIB", "agentxRegStart"), ("AGENTX-MIB", "agentxRegUpperBound"), ("AGENTX-MIB", "agentxRegContext"), ("AGENTX-MIB", "agentxRegistrationTableLastChange"), ("AGENTX-MIB", "agentxConnTransportAddress"), ("AGENTX-MIB", "agentxRegInstance"), ("AGENTX-MIB", "agentxRegTimeout"), ("AGENTX-MIB", "agentxSessionOpenTime"), )

# Exports

# Module identity
mibBuilder.exportSymbols("AGENTX-MIB", PYSNMP_MODULE_ID=agentxMIB)

# Types
mibBuilder.exportSymbols("AGENTX-MIB", AgentxTAddress=AgentxTAddress)

# Objects
mibBuilder.exportSymbols("AGENTX-MIB", agentxMIB=agentxMIB, agentxObjects=agentxObjects, agentxGeneral=agentxGeneral, agentxDefaultTimeout=agentxDefaultTimeout, agentxMasterAgentXVer=agentxMasterAgentXVer, agentxConnection=agentxConnection, agentxConnTableLastChange=agentxConnTableLastChange, agentxConnectionTable=agentxConnectionTable, agentxConnectionEntry=agentxConnectionEntry, agentxConnIndex=agentxConnIndex, agentxConnOpenTime=agentxConnOpenTime, agentxConnTransportDomain=agentxConnTransportDomain, agentxConnTransportAddress=agentxConnTransportAddress, agentxSession=agentxSession, agentxSessionTableLastChange=agentxSessionTableLastChange, agentxSessionTable=agentxSessionTable, agentxSessionEntry=agentxSessionEntry, agentxSessionIndex=agentxSessionIndex, agentxSessionObjectID=agentxSessionObjectID, agentxSessionDescr=agentxSessionDescr, agentxSessionAdminStatus=agentxSessionAdminStatus, agentxSessionOpenTime=agentxSessionOpenTime, agentxSessionAgentXVer=agentxSessionAgentXVer, agentxSessionTimeout=agentxSessionTimeout, agentxRegistration=agentxRegistration, agentxRegistrationTableLastChange=agentxRegistrationTableLastChange, agentxRegistrationTable=agentxRegistrationTable, agentxRegistrationEntry=agentxRegistrationEntry, agentxRegIndex=agentxRegIndex, agentxRegContext=agentxRegContext, agentxRegStart=agentxRegStart, agentxRegRangeSubId=agentxRegRangeSubId, agentxRegUpperBound=agentxRegUpperBound, agentxRegPriority=agentxRegPriority, agentxRegTimeout=agentxRegTimeout, agentxRegInstance=agentxRegInstance, agentxConformance=agentxConformance, agentxMIBGroups=agentxMIBGroups, agentxMIBCompliances=agentxMIBCompliances)

# Groups
mibBuilder.exportSymbols("AGENTX-MIB", agentxMIBGroup=agentxMIBGroup)
