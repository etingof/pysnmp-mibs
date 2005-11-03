# PySNMP SMI module. Autogenerated from smidump -f python VRRP-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:26:23 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( MacAddress, RowStatus, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class VrId(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,255)
    pass


# Objects

vrrpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 68)).setRevisions(("2000-03-03 00:00",))
vrrpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 0))
vrrpOperations = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 1))
vrrpNodeVersion = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 1), Integer32()).setMaxAccess("readonly")
vrrpNotificationCntl = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(1)).setMaxAccess("readwrite")
vrrpOperTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 3))
vrrpOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
vrrpOperVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1), VrId()).setMaxAccess("noaccess")
vrrpOperVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
vrrpOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("initialize", 1), ("backup", 2), ("master", 3), ))).setMaxAccess("readonly")
vrrpOperAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), )).clone(2)).setMaxAccess("readwrite")
vrrpOperPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readwrite")
vrrpOperIpAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
vrrpOperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
vrrpOperPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8), IpAddress().clone("0.0.0.0")).setMaxAccess("readwrite")
vrrpOperAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("noAuthentication", 1), ("simpleTextPassword", 2), ("ipAuthenticationHeader", 3), )).clone(1)).setMaxAccess("readwrite")
vrrpOperAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
vrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
vrrpOperPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12), TruthValue()).setMaxAccess("readwrite")
vrrpOperVirtualRouterUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
vrrpOperProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,4,)).subtype(namedValues=namedval.NamedValues(("ip", 1), ("bridge", 2), ("decnet", 3), ("other", 4), )).clone(1)).setMaxAccess("readwrite")
vrrpOperRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15), RowStatus()).setMaxAccess("readwrite")
vrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 4))
vrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "VRRP-MIB", "vrrpAssoIpAddr"))
vrrpAssoIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1), IpAddress()).setMaxAccess("noaccess")
vrrpAssoIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
vrrpTrapPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 5), IpAddress()).setMaxAccess("notifyonly")
vrrpTrapAuthErrorType = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("invalidAuthType", 1), ("authTypeMismatch", 2), ("authFailure", 3), ))).setMaxAccess("notifyonly")
vrrpStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 2))
vrrpRouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 1), Counter32()).setMaxAccess("readonly")
vrrpRouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 2), Counter32()).setMaxAccess("readonly")
vrrpRouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 3), Counter32()).setMaxAccess("readonly")
vrrpRouterStatsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 2, 4))
vrrpRouterStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 2, 4, 1))
vrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
vrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
vrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
vrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
vrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
vrrpStatsPriorityZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
vrrpStatsPriorityZeroPktsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
vrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
vrrpStatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
vrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
vrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
vrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
vrrpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3))
vrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 1))
vrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 2))

# Augmentions
vrrpOperEntry.registerAugmentions(("VRRP-MIB", "vrrpRouterStatsEntry"))
apply(vrrpRouterStatsEntry.setIndexNames, vrrpOperEntry.getIndexNames())

# Notifications

vrrpTrapNewMaster = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 1)).setObjects(("VRRP-MIB", "vrrpOperMasterIpAddr"), )
vrrpTrapAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 2)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"), )

# Groups

vrrpNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 4)).setObjects(("VRRP-MIB", "vrrpTrapNewMaster"), ("VRRP-MIB", "vrrpTrapAuthFailure"), )
vrrpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 2)).setObjects(("VRRP-MIB", "vrrpStatsPacketLengthErrors"), ("VRRP-MIB", "vrrpStatsBecomeMaster"), ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"), ("VRRP-MIB", "vrrpRouterVrIdErrors"), ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"), ("VRRP-MIB", "vrrpStatsAddressListErrors"), ("VRRP-MIB", "vrrpStatsAuthFailures"), ("VRRP-MIB", "vrrpRouterChecksumErrors"), ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"), ("VRRP-MIB", "vrrpStatsInvalidAuthType"), ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"), ("VRRP-MIB", "vrrpRouterVersionErrors"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"), ("VRRP-MIB", "vrrpStatsIpTtlErrors"), )
vrrpOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 1)).setObjects(("VRRP-MIB", "vrrpAssoIpAddrRowStatus"), ("VRRP-MIB", "vrrpOperState"), ("VRRP-MIB", "vrrpOperAuthKey"), ("VRRP-MIB", "vrrpNodeVersion"), ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"), ("VRRP-MIB", "vrrpNotificationCntl"), ("VRRP-MIB", "vrrpOperPreemptMode"), ("VRRP-MIB", "vrrpOperRowStatus"), ("VRRP-MIB", "vrrpOperAdminState"), ("VRRP-MIB", "vrrpOperIpAddrCount"), ("VRRP-MIB", "vrrpOperPrimaryIpAddr"), ("VRRP-MIB", "vrrpOperMasterIpAddr"), ("VRRP-MIB", "vrrpOperAdvertisementInterval"), ("VRRP-MIB", "vrrpOperAuthType"), ("VRRP-MIB", "vrrpOperProtocol"), ("VRRP-MIB", "vrrpOperPriority"), ("VRRP-MIB", "vrrpOperVirtualMacAddr"), )
vrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 3)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"), )

# Exports

# Module identity
mibBuilder.exportSymbols("VRRP-MIB", PYSNMP_MODULE_ID=vrrpMIB)

# Types
mibBuilder.exportSymbols("VRRP-MIB", VrId=VrId)

# Objects
mibBuilder.exportSymbols("VRRP-MIB", vrrpMIB=vrrpMIB, vrrpNotifications=vrrpNotifications, vrrpOperations=vrrpOperations, vrrpNodeVersion=vrrpNodeVersion, vrrpNotificationCntl=vrrpNotificationCntl, vrrpOperTable=vrrpOperTable, vrrpOperEntry=vrrpOperEntry, vrrpOperVrId=vrrpOperVrId, vrrpOperVirtualMacAddr=vrrpOperVirtualMacAddr, vrrpOperState=vrrpOperState, vrrpOperAdminState=vrrpOperAdminState, vrrpOperPriority=vrrpOperPriority, vrrpOperIpAddrCount=vrrpOperIpAddrCount, vrrpOperMasterIpAddr=vrrpOperMasterIpAddr, vrrpOperPrimaryIpAddr=vrrpOperPrimaryIpAddr, vrrpOperAuthType=vrrpOperAuthType, vrrpOperAuthKey=vrrpOperAuthKey, vrrpOperAdvertisementInterval=vrrpOperAdvertisementInterval, vrrpOperPreemptMode=vrrpOperPreemptMode, vrrpOperVirtualRouterUpTime=vrrpOperVirtualRouterUpTime, vrrpOperProtocol=vrrpOperProtocol, vrrpOperRowStatus=vrrpOperRowStatus, vrrpAssoIpAddrTable=vrrpAssoIpAddrTable, vrrpAssoIpAddrEntry=vrrpAssoIpAddrEntry, vrrpAssoIpAddr=vrrpAssoIpAddr, vrrpAssoIpAddrRowStatus=vrrpAssoIpAddrRowStatus, vrrpTrapPacketSrc=vrrpTrapPacketSrc, vrrpTrapAuthErrorType=vrrpTrapAuthErrorType, vrrpStatistics=vrrpStatistics, vrrpRouterChecksumErrors=vrrpRouterChecksumErrors, vrrpRouterVersionErrors=vrrpRouterVersionErrors, vrrpRouterVrIdErrors=vrrpRouterVrIdErrors, vrrpRouterStatsTable=vrrpRouterStatsTable, vrrpRouterStatsEntry=vrrpRouterStatsEntry, vrrpStatsBecomeMaster=vrrpStatsBecomeMaster, vrrpStatsAdvertiseRcvd=vrrpStatsAdvertiseRcvd, vrrpStatsAdvertiseIntervalErrors=vrrpStatsAdvertiseIntervalErrors, vrrpStatsAuthFailures=vrrpStatsAuthFailures, vrrpStatsIpTtlErrors=vrrpStatsIpTtlErrors, vrrpStatsPriorityZeroPktsRcvd=vrrpStatsPriorityZeroPktsRcvd, vrrpStatsPriorityZeroPktsSent=vrrpStatsPriorityZeroPktsSent, vrrpStatsInvalidTypePktsRcvd=vrrpStatsInvalidTypePktsRcvd, vrrpStatsAddressListErrors=vrrpStatsAddressListErrors, vrrpStatsInvalidAuthType=vrrpStatsInvalidAuthType, vrrpStatsAuthTypeMismatch=vrrpStatsAuthTypeMismatch, vrrpStatsPacketLengthErrors=vrrpStatsPacketLengthErrors, vrrpConformance=vrrpConformance, vrrpMIBCompliances=vrrpMIBCompliances, vrrpMIBGroups=vrrpMIBGroups)

# Notifications
mibBuilder.exportSymbols("VRRP-MIB", vrrpTrapNewMaster=vrrpTrapNewMaster, vrrpTrapAuthFailure=vrrpTrapAuthFailure)

# Groups
mibBuilder.exportSymbols("VRRP-MIB", vrrpNotificationGroup=vrrpNotificationGroup, vrrpStatsGroup=vrrpStatsGroup, vrrpOperGroup=vrrpOperGroup, vrrpTrapGroup=vrrpTrapGroup)
