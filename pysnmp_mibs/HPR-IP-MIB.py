# PySNMP SMI module. Autogenerated from smidump -f python HPR-IP-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:15:34 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( SnaControlPointName, ) = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( hprCompliances, hprGroups, hprObjects, ) = mibBuilder.importSymbols("HPR-MIB", "hprCompliances", "hprGroups", "hprObjects")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")

# Types

class AppnTOSPrecedence(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec+constraint.ValueSizeConstraint(3,3)
    fixedLength = 3
    
class AppnTrafficType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,5,4,)
    namedValues = namedval.NamedValues(("low", 1), ("medium", 2), ("high", 3), ("network", 4), ("llcAndFnRoutedNlp", 5), )
    

# Objects

hprIp = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 6, 1, 5)).setRevisions(("1998-09-24 00:00",))
if mibBuilder.loadTexts: hprIp.setOrganization("IETF SNA NAU MIB WG / AIW APPN MIBs SIG")
if mibBuilder.loadTexts: hprIp.setContactInfo("\nBob Clouston\nCisco Systems\n7025 Kit Creek Road\nP.O. Box 14987\nResearch Triangle Park, NC 27709, USA\nTel:    1 919 472 2333\nE-mail: clouston@cisco.com\n\nBob Moore\nIBM Corporation\n4205 S. Miami Boulevard\nBRQA/501\nP.O. Box 12195\nResearch Triangle Park, NC 27709, USA\nTel:    1 919 254 4436\nE-mail: remoore@us.ibm.com")
if mibBuilder.loadTexts: hprIp.setDescription("The MIB module for HPR over IP.  This module contains two\ngroups:\n\n -  the HPR over IP Monitoring Group provides a count of the UDP\n    packets sent by a link station for each APPN traffic type.\n\n -  the HPR over IP Configuration Group provides for reading and\n    setting the mappings between APPN traffic types and TOS\n    Precedence settings in the IP header.  These mappings are\n    configured at the APPN port level, and are inherited by the\n    APPN connection networks and link stations associated with an\n    APPN port.  A port-level mapping can, however, be overridden\n    for a particular connection network or link station.")
hprIpActiveLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1))
if mibBuilder.loadTexts: hprIpActiveLsTable.setDescription("The HPR/IP active link station table.  This table provides\ncounts of the number of UDP packets sent for each APPN\ntraffic type.")
hprIpActiveLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpActiveLsLsName"), (0, "HPR-IP-MIB", "hprIpActiveLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpActiveLsEntry.setDescription("Entry of the HPR/IP link station table.")
hprIpActiveLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 10))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpActiveLsLsName.setDescription("Administratively assigned name for the link station.  If this\nobject has the same value as the appnLsName in the APPN MIB,\nthen the two objects are referring to the same APPN link\nstation.")
hprIpActiveLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 2), AppnTrafficType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpActiveLsAppnTrafficType.setDescription("APPN traffic type being sent through the link station.")
hprIpActiveLsUdpPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hprIpActiveLsUdpPackets.setDescription("The count of outgoing UDP packets carrying this type of APPN\ntraffic.  A discontinuity in the counter is indicated by the\nappnLsCounterDisconTime object in the APPN MIB.")
hprIpAppnPortTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2))
if mibBuilder.loadTexts: hprIpAppnPortTable.setDescription("The HPR/IP APPN port table.  This table supports reading and\nsetting the mapping between APPN traffic types and TOS\nPrecedence settings for all the link stations at this APPN\nport.  This mapping can be overridden for an individual link\nstation or an individual connection network via, respectively,\nthe hprIpLsTOSPrecedence and the hprIpCnTOSPrecedence objects.")
hprIpAppnPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpAppnPortName"), (0, "HPR-IP-MIB", "hprIpAppnPortAppnTrafficType"))
if mibBuilder.loadTexts: hprIpAppnPortEntry.setDescription("Entry of the HPR/IP APPN port table.  Entries exist for\nevery APPN port defined to support HPR over IP.")
hprIpAppnPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 10))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpAppnPortName.setDescription("Administratively assigned name for this APPN port.  If this\nobject has the same value as the appnPortName in the APPN MIB,\nthen the two objects are referring to the same APPN port.")
hprIpAppnPortAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 2), AppnTrafficType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpAppnPortAppnTrafficType.setDescription("APPN traffic type sent through the port.")
hprIpAppnPortTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 3), AppnTOSPrecedence()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hprIpAppnPortTOSPrecedence.setDescription("A setting for the three TOS Precedence bits in the IP Type of\nService field for this APPN traffic type.\n\nWhen this value is changed via a Set operation, the new setting\nfor the TOS Precedence bits takes effect immediately, rather\nthan waiting for some event such as reinitialization of the\nport or of the APPN node itself.")
hprIpLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3))
if mibBuilder.loadTexts: hprIpLsTable.setDescription("The HPR/IP link station table.  Values for TOS Precedence at\nthe link station level override those at the level of the\ncontaining port.  If there is no entry in this table for a\ngiven link station, then that link station inherits its TOS\nPrecedence values from its port.")
hprIpLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpLsLsName"), (0, "HPR-IP-MIB", "hprIpLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpLsEntry.setDescription("Entry of the HPR/IP link station table.")
hprIpLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 10))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpLsLsName.setDescription("Administratively assigned name for the link station.  If this\nobject has the same value as the appnLsName in the APPN MIB,\nthen the two objects are referring to the same APPN link\nstation.")
hprIpLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 2), AppnTrafficType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpLsAppnTrafficType.setDescription("APPN traffic type sent through the link station.")
hprIpLsTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsTOSPrecedence.setDescription("A setting for the three TOS Precedence bits in the IP Type of\nService field for this APPN traffic type.\n\nWhen this value is changed via a Set operation, the new setting\nfor the TOS Precedence bits takes effect immediately, rather\nthan waiting for some event such as reinitialization of the\nport or of the APPN node itself.")
hprIpLsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsRowStatus.setDescription("This object allows entries to be created and deleted in the\nhprIpLsTable.  As soon as an entry becomes active, the mapping\nbetween APPN traffic types and TOS Precedence settings that it\nspecifies becomes effective.\n\nThe value of the other accessible object in this entry,\nhprIpLsTOSPrecedence, can be changed via a Set operation when\nthis object's value is active(1).\n\nAn entry in this table is deleted by setting this object to\ndestroy(6).  Deleting an entry in this table causes the\nlink station to revert to the default TOS Precedence\nmapping for its port.")
hprIpCnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4))
if mibBuilder.loadTexts: hprIpCnTable.setDescription("The HPR/IP connection network table.  Values for TOS\nPrecedence at the connection network level override those at\nthe level of the containing port.  If there is no entry in\nthis table for a given connection network, then that\nconnection network inherits its TOS Precedence values from\nits port.\n\nA node may have connections to a given connection network\nthrough multiple ports.  There is no provision in the HPR-IP\narchitecture for variations in TOS Precedence values for\na single connection network based on the port through which\ntraffic is flowing to the connection network.  Thus an entry\nin this table overrides the port-level settings for all the\nports through which the node can reach the connection\nnetwork.")
hprIpCnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpCnVrnName"), (0, "HPR-IP-MIB", "hprIpCnAppnTrafficType"))
if mibBuilder.loadTexts: hprIpCnEntry.setDescription("Entry of the HPR/IP connection network table.")
hprIpCnVrnName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 1), SnaControlPointName()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpCnVrnName.setDescription("SNA control point name of the virtual routing node (VRN) that\nidentifies the connection network in the APPN topology\ndatabase.  If this object has the same value as the appnVrnName\nin the APPN MIB, then the two objects are referring\nto the same APPN VRN.")
hprIpCnAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 2), AppnTrafficType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hprIpCnAppnTrafficType.setDescription("APPN traffic type sent to this connection network.")
hprIpCnTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnTOSPrecedence.setDescription("A setting for the three TOS Precedence bits in the IP Type of\nService field for this APPN traffic type.  This setting applies\nto all traffic sent to this connection network by this node,\nregardless of the port through which the traffic is sent.\n\nWhen this value is changed via a Set operation, the new setting\nfor the TOS Precedence bits takes effect immediately, rather\nthan waiting for some event such as reinitialization of a\nport or of the APPN node itself.")
hprIpCnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnRowStatus.setDescription("This object allows entries to be created and deleted in the\nhprIpCnTable.  As soon as an entry becomes active, the mapping\nbetween APPN traffic types and TOS Precedence settings that it\nspecifies becomes effective.\n\nThe value of the other accessible object in this entry,\nhprIpCnTOSPrecedence, can be changed via a Set operation when\nthis object's value is active(1).\n\nAn entry in this table is deleted by setting this object to\ndestroy(6).  Deleting an entry in this table causes the\nconnection network to revert to the default TOS Precedence\nmapping for each port through which it is accessed.")

# Augmentions

# Groups

hprIpMonitoringGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 5)).setObjects(("HPR-IP-MIB", "hprIpActiveLsUdpPackets"), )
if mibBuilder.loadTexts: hprIpMonitoringGroup.setDescription("An object for counting outgoing HPR/IP traffic for each APPN\ntraffic type.")
hprIpConfigurationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 6)).setObjects(("HPR-IP-MIB", "hprIpLsTOSPrecedence"), ("HPR-IP-MIB", "hprIpCnTOSPrecedence"), ("HPR-IP-MIB", "hprIpAppnPortTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsRowStatus"), ("HPR-IP-MIB", "hprIpCnRowStatus"), )
if mibBuilder.loadTexts: hprIpConfigurationGroup.setDescription("A collection of HPR/IP objects representing the mappings\nbetween APPN traffic types and TOS Precedence bits at the APPN\nport, APPN link station, and APPN connection network levels.")

# Compliances

hprIpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 6, 2, 1, 2)).setObjects(("HPR-IP-MIB", "hprIpMonitoringGroup"), ("HPR-IP-MIB", "hprIpConfigurationGroup"), )
if mibBuilder.loadTexts: hprIpCompliance.setDescription("Compliance statement for the HPR over IP MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("HPR-IP-MIB", PYSNMP_MODULE_ID=hprIp)

# Types
mibBuilder.exportSymbols("HPR-IP-MIB", AppnTOSPrecedence=AppnTOSPrecedence, AppnTrafficType=AppnTrafficType)

# Objects
mibBuilder.exportSymbols("HPR-IP-MIB", hprIp=hprIp, hprIpActiveLsTable=hprIpActiveLsTable, hprIpActiveLsEntry=hprIpActiveLsEntry, hprIpActiveLsLsName=hprIpActiveLsLsName, hprIpActiveLsAppnTrafficType=hprIpActiveLsAppnTrafficType, hprIpActiveLsUdpPackets=hprIpActiveLsUdpPackets, hprIpAppnPortTable=hprIpAppnPortTable, hprIpAppnPortEntry=hprIpAppnPortEntry, hprIpAppnPortName=hprIpAppnPortName, hprIpAppnPortAppnTrafficType=hprIpAppnPortAppnTrafficType, hprIpAppnPortTOSPrecedence=hprIpAppnPortTOSPrecedence, hprIpLsTable=hprIpLsTable, hprIpLsEntry=hprIpLsEntry, hprIpLsLsName=hprIpLsLsName, hprIpLsAppnTrafficType=hprIpLsAppnTrafficType, hprIpLsTOSPrecedence=hprIpLsTOSPrecedence, hprIpLsRowStatus=hprIpLsRowStatus, hprIpCnTable=hprIpCnTable, hprIpCnEntry=hprIpCnEntry, hprIpCnVrnName=hprIpCnVrnName, hprIpCnAppnTrafficType=hprIpCnAppnTrafficType, hprIpCnTOSPrecedence=hprIpCnTOSPrecedence, hprIpCnRowStatus=hprIpCnRowStatus)

# Groups
mibBuilder.exportSymbols("HPR-IP-MIB", hprIpMonitoringGroup=hprIpMonitoringGroup, hprIpConfigurationGroup=hprIpConfigurationGroup)

# Compliances
mibBuilder.exportSymbols("HPR-IP-MIB", hprIpCompliance=hprIpCompliance)
