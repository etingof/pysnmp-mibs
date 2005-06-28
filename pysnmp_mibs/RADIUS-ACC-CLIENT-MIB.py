# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-ACC-CLIENT-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:31:01 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 67))
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 2))
radiusAccClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1))
radiusAccClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1))
radiusAccClientInvalidServerAddresses = MibVariable((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
radiusAccClientIdentifier = MibVariable((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
radiusAccServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3))
radiusAccServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1)).setIndexNames((0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"))
radiusAccServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
radiusAccServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
radiusAccClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
radiusAccClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
radiusAccClientRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
radiusAccClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAccClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2))
radiusAccClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1))
radiusAccClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2))

# Augmentions

# Groups

radiusAccClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPacketsDropped"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMalformedResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientTimeouts"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRoundTripTime"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientResponses"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRetransmissions"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPendingRequests"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientUnknownTypes"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientBadAuthenticators"), )

# Exports

# Objects
mibBuilder.exportSymbols("RADIUS-ACC-CLIENT-MIB", radiusMIB=radiusMIB, radiusAccounting=radiusAccounting, radiusAccClientMIB=radiusAccClientMIB, radiusAccClientMIBObjects=radiusAccClientMIBObjects, radiusAccClient=radiusAccClient, radiusAccClientInvalidServerAddresses=radiusAccClientInvalidServerAddresses, radiusAccClientIdentifier=radiusAccClientIdentifier, radiusAccServerTable=radiusAccServerTable, radiusAccServerEntry=radiusAccServerEntry, radiusAccServerIndex=radiusAccServerIndex, radiusAccServerAddress=radiusAccServerAddress, radiusAccClientServerPortNumber=radiusAccClientServerPortNumber, radiusAccClientRoundTripTime=radiusAccClientRoundTripTime, radiusAccClientRequests=radiusAccClientRequests, radiusAccClientRetransmissions=radiusAccClientRetransmissions, radiusAccClientResponses=radiusAccClientResponses, radiusAccClientMalformedResponses=radiusAccClientMalformedResponses, radiusAccClientBadAuthenticators=radiusAccClientBadAuthenticators, radiusAccClientPendingRequests=radiusAccClientPendingRequests, radiusAccClientTimeouts=radiusAccClientTimeouts, radiusAccClientUnknownTypes=radiusAccClientUnknownTypes, radiusAccClientPacketsDropped=radiusAccClientPacketsDropped, radiusAccClientMIBConformance=radiusAccClientMIBConformance, radiusAccClientMIBCompliances=radiusAccClientMIBCompliances, radiusAccClientMIBGroups=radiusAccClientMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-ACC-CLIENT-MIB", radiusAccClientMIBGroup=radiusAccClientMIBGroup)