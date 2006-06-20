# PySNMP SMI module. Autogenerated from smidump -f python NET-SNMP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:13 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "enterprises")

# Objects

netSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072)).setRevisions(("2002-01-30 00:00",))
netSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1))
netSnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3))
netSnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1))
netSnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2))
netSnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3))
netSnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4))
netSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 0))
netSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 1))
netSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5))
netSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 1))
netSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 2))
netSnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999))
netSnmpPlaypen = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999, 9999))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NET-SNMP-MIB", PYSNMP_MODULE_ID=netSnmp)

# Objects
mibBuilder.exportSymbols("NET-SNMP-MIB", netSnmp=netSnmp, netSnmpObjects=netSnmpObjects, netSnmpEnumerations=netSnmpEnumerations, netSnmpModuleIDs=netSnmpModuleIDs, netSnmpAgentOIDs=netSnmpAgentOIDs, netSnmpDomains=netSnmpDomains, netSnmpNotificationPrefix=netSnmpNotificationPrefix, netSnmpNotifications=netSnmpNotifications, netSnmpNotificationObjects=netSnmpNotificationObjects, netSnmpConformance=netSnmpConformance, netSnmpCompliances=netSnmpCompliances, netSnmpGroups=netSnmpGroups, netSnmpExperimental=netSnmpExperimental, netSnmpPlaypen=netSnmpPlaypen)

