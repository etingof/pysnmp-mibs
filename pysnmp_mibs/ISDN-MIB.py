# PySNMP SMI module. Autogenerated from smidump -f python ISDN-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:14 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( IANAifType, ) = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, RowStatus, TextualConvention, TestAndIncr, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TestAndIncr", "TimeStamp", "TruthValue")

# Types

class IsdnSignalingProtocol(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(25,6,5,17,16,7,15,14,13,12,10,11,9,20,22,21,19,1,2,24,3,8,4,23,18,)
    namedValues = NamedValues(("other", 1), ("ni2", 10), ("ni3", 11), ("vn2", 12), ("vn3", 13), ("vn4", 14), ("vn6", 15), ("kdd", 16), ("ins64", 17), ("ins1500", 18), ("itr6", 19), ("dss1", 2), ("cornet", 20), ("ts013", 21), ("ts014", 22), ("qsig", 23), ("swissnet2", 24), ("swissnet3", 25), ("etsi", 3), ("dass2", 4), ("ess4", 5), ("ess5", 6), ("dms100", 7), ("dms250", 8), ("ni1", 9), )
    

# Objects

isdnMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 20)).setRevisions(("1996-09-23 16:42",))
if mibBuilder.loadTexts: isdnMib.setOrganization("IETF ISDN MIB Working Group")
if mibBuilder.loadTexts: isdnMib.setContactInfo("        Guenter Roeck\nPostal: cisco Systems\n        170 West Tasman Drive\n        San Jose, CA 95134\n        U.S.A.\nPhone:  +1 408 527 3143\nE-mail: groeck@cisco.com")
if mibBuilder.loadTexts: isdnMib.setDescription("The MIB module to describe the\nmanagement of ISDN interfaces.")
isdnMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1))
isdnBasicRateGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 1))
isdnBasicRateTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1))
if mibBuilder.loadTexts: isdnBasicRateTable.setDescription("Table containing configuration and operational\nparameters for all physical Basic Rate\ninterfaces on this managed device.")
isdnBasicRateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnBasicRateEntry.setDescription("An entry in the ISDN Basic Rate Table.")
isdnBasicRateIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(75,76,)).subtype(namedValues=NamedValues(("isdns", 75), ("isdnu", 76), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateIfType.setDescription("The physical interface type. For 'S/T' interfaces,\nalso called 'Four-wire Basic Access Interface',\nthe value of this object is isdns(75).\nFor 'U' interfaces, also called 'Two-wire Basic\nAccess Interface', the value of this object is\nisdnu(76).")
isdnBasicRateLineTopology = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("pointToPoint", 1), ("pointToMultipoint", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateLineTopology.setDescription("The line topology to be used for this interface.\nNote that setting isdnBasicRateIfType to isdns(75)\ndoes not necessarily mean a line topology of\npoint-to-multipoint.")
isdnBasicRateIfMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("te", 1), ("nt", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateIfMode.setDescription("The physical interface mode. For TE mode, the value\nof this object is te(1). For NT mode, the value\nof this object is nt(2).")
isdnBasicRateSignalMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("active", 1), ("inactive", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateSignalMode.setDescription("The signaling channel operational mode for this interface.\nIf active(1) there is a signaling channel on this\ninterface. If inactive(2) a signaling channel is\nnot available.")
isdnBearerGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 2))
isdnBearerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1))
if mibBuilder.loadTexts: isdnBearerTable.setDescription("This table defines port specific operational, statistics\nand active call data for ISDN B channels. Each entry\nin this table describes one B (bearer) channel.")
isdnBearerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnBearerEntry.setDescription("Operational and statistics information relating to\none port. A port is a single B channel.")
isdnBearerChannelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("dialup", 1), ("leased", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBearerChannelType.setDescription("The B channel type. If the B channel is connected\nto a dialup line, this object has a value of\ndialup(1). In this case, it is controlled by\nan associated signaling channel. If the B channel\nis connected to a leased line, this object has\na value of leased(2). For leased line B channels, there\nis no signaling channel control available.")
isdnBearerOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(4,3,1,2,)).subtype(namedValues=NamedValues(("idle", 1), ("connecting", 2), ("connected", 3), ("active", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerOperStatus.setDescription("The current call control state for this port.\nidle(1):       The B channel is idle.\n               No call or call attempt is going on.\nconnecting(2): A connection attempt (outgoing call)\n               is being made on this interface.\nconnected(3):  An incoming call is in the process\n               of validation.\nactive(4):     A call is active on this interface.")
isdnBearerChannelNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerChannelNumber.setDescription("The identifier being used by a signaling protocol\nto identify this B channel, also referred to as\nB channel number. If the Agent also supports the DS0 MIB,\nthe values of isdnBearerChannelNumber and dsx0Ds0Number\nmust be identical for a given B channel.")
isdnBearerPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerPeerAddress.setDescription("The ISDN address the current or last call is or was\nconnected to.\n\nIn some cases, the format of this information can not\nbe predicted, since it largely depends on the type\nof switch or PBX the device is connected to. Therefore,\nthe detailed format of this information is not\nspecified and is implementation dependent.\n\nIf possible, the agent should supply this information\nusing the E.164 format. In this case, the number must\nstart with '+'. Otherwise, IA5 number digits must be used.\nIf the peer ISDN address is not available,\nthis object has a length of zero.")
isdnBearerPeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerPeerSubAddress.setDescription("The ISDN subaddress the current or last call is or was\nconnected to.\n\nThe subaddress is an user supplied string of up to 20\nIA5 characters and is transmitted transparently through\nthe network.\n\nIf the peer subaddress is not available, this object\nhas a length of zero.")
isdnBearerCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,4,)).subtype(namedValues=NamedValues(("unknown", 1), ("originate", 2), ("answer", 3), ("callback", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallOrigin.setDescription("The call origin for the current or last call. If since\nsystem startup there was no call on this interface,\nthis object has a value of unknown(1).")
isdnBearerInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(8,2,3,4,1,7,5,6,9,)).subtype(namedValues=NamedValues(("unknown", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerInfoType.setDescription("The Information Transfer Capability for the current\nor last call.\n\nspeech(2) refers to a non-data connection, whereas\naudio31(6) and audio7(7) refer to data mode connections.\n\nNote that Q.931, chapter 4.5.5, originally defined\naudio7(7) as '7 kHz audio' and now defines it as\n'Unrestricted digital information with tones/\nannouncements'.\n\nIf since system startup there has been no call on this\ninterface, this object has a value of unknown(1).")
isdnBearerMultirate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerMultirate.setDescription("This flag indicates if the current or last call used\nmultirate. The actual information transfer rate,\nin detail specified in octet 4.1 (rate multiplier),\nis the sum of all B channel ifSpeed values for\nthe hyperchannel.\n\nIf since system startup there was no call on this\ninterface, this object has a value of false(2).")
isdnBearerCallSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallSetupTime.setDescription("The value of sysUpTime when the ISDN setup message for\nthe current or last call was sent or received. If since\nsystem startup there has been no call on this interface,\nthis object has a value of zero.")
isdnBearerCallConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallConnectTime.setDescription("The value of sysUpTime when the ISDN connect message for\nthe current or last call was sent or received. If since\nsystem startup there has been no call on this interface,\nthis object has a value of zero.")
isdnBearerChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerChargedUnits.setDescription("The number of charged units for the current or last\nconnection. For incoming calls or if charging information\nis not supplied by the switch, the value of this object\nis zero.")
isdnSignalingGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 3))
isdnSignalingGetIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnSignalingGetIndex.setDescription("The recommended procedure for selecting a new index for\nisdnSignalingTable row creation is to GET the value of\nthis object, and then to SET the object with the same\nvalue. If the SET operation succeeds, the manager can use\nthis value as an index to create a new row in this table.")
isdnSignalingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2))
if mibBuilder.loadTexts: isdnSignalingTable.setDescription("ISDN signaling table containing configuration and\noperational parameters for all ISDN signaling\nchannels on this managed device.")
isdnSignalingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1)).setIndexNames((0, "ISDN-MIB", "isdnSignalingIndex"))
if mibBuilder.loadTexts: isdnSignalingEntry.setDescription("An entry in the ISDN Signaling Table. To create a new\nentry, only isdnSignalingProtocol needs to be specified\nbefore isdnSignalingStatus can become active(1).")
isdnSignalingIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: isdnSignalingIndex.setDescription("The index value which uniquely identifies an entry\nin the isdnSignalingTable.")
isdnSignalingIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSignalingIfIndex.setDescription("The ifIndex value of the interface associated with this\nsignaling channel.")
isdnSignalingProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 3), IsdnSignalingProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingProtocol.setDescription("The particular protocol type supported by the\nswitch providing access to the ISDN network\nto which this signaling channel is connected.")
isdnSignalingCallingAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 4), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingCallingAddress.setDescription("The ISDN Address to be assigned to this signaling\nchannel. More specifically, this is the 'Calling Address\ninformation element' as being passed to the switch\nin outgoing call setup messages.\n\nIt can be an EAZ (1TR6), a calling number (DSS1, ETSI)\nor any other number necessary to identify a signaling\ninterface. If there is no such number defined or required,\nthis is a zero length string. It is represented in\nDisplayString form.\n\nIncoming calls can also be identified by this number.\nIf the Directory Number, i.e. the Called Number in\nincoming calls, is different to this number, the\nisdnDirectoryTable has to be used to specify all\npossible Directory Numbers.\n\nThe format of this information largely depends on the type\nof switch or PBX the device is connected to. Therefore,\nthe detailed format of this information is not\nspecified and is implementation dependent.\n\nIf possible, the agent should implement this information\nusing the E.164 number format. In this case, the number\nmust start with '+'. Otherwise, IA5 number digits must\nbe used.")
isdnSignalingSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 5), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingSubAddress.setDescription("Supplementary information to the ISDN address assigned\nto this signaling channel. Usually, this is the\nsubaddress as defined in Q.931.\nIf there is no such number defined or required, this is\na zero length string.\nThe subaddress is used for incoming calls as well as\nfor outgoing calls.\nThe subaddress is an user supplied string of up to 20\nIA5 characters and is transmitted transparently through\nthe network.")
isdnSignalingBchannelCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingBchannelCount.setDescription("The total number of B channels (bearer channels)\nmanaged by this signaling channel. The default value\nof this object depends on the physical interface type\nand is either 2 for Basic Rate interfaces or\n24 (30) for Primary Rate interfaces.")
isdnSignalingInfoTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingInfoTrapEnable.setDescription("Indicates whether isdnMibCallInformation traps\nshould be generated for calls on this signaling\nchannel.")
isdnSignalingStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingStatus.setDescription("This object is used to create and delete rows in the\nisdnSignalingTable.")
isdnSignalingStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3))
if mibBuilder.loadTexts: isdnSignalingStatsTable.setDescription("ISDN signaling table containing statistics\ninformation for all ISDN signaling channels\non this managed device.\nOnly statistical information which is not already being\ncounted in the ifTable is being defined in this table.")
isdnSignalingStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1))
if mibBuilder.loadTexts: isdnSignalingStatsEntry.setDescription("An entry in the ISDN Signaling statistics Table.")
isdnSigStatsInCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsInCalls.setDescription("The number of incoming calls on this interface.")
isdnSigStatsInConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsInConnected.setDescription("The number of incoming calls on this interface\nwhich were actually connected.")
isdnSigStatsOutCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsOutCalls.setDescription("The number of outgoing calls on this interface.")
isdnSigStatsOutConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsOutConnected.setDescription("The number of outgoing calls on this interface\nwhich were actually connected.")
isdnSigStatsChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsChargedUnits.setDescription("The number of charging units on this interface since\nsystem startup.\nOnly the charging units applying to the local interface,\ni.e. for originated calls or for calls with 'Reverse\ncharging' being active, are counted here.")
isdnLapdTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4))
if mibBuilder.loadTexts: isdnLapdTable.setDescription("Table containing configuration and statistics\ninformation for all LAPD (D channel Data Link)\ninterfaces on this managed device.\nOnly statistical information which is not already being\ncounted in the ifTable is being defined in this table.")
isdnLapdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnLapdEntry.setDescription("An entry in the LAPD Table.")
isdnLapdPrimaryChannel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnLapdPrimaryChannel.setDescription("If set to true(1), this D channel is the designated\nprimary D channel if D channel backup is active.\nThere must be exactly one primary D channel\nconfigured. If D channel backup is not used, this\nobject has a value of true(1).")
isdnLapdOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("inactive", 1), ("l1Active", 2), ("l2Active", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdOperStatus.setDescription("The operational status of this interface:\n\ninactive  all layers are inactive\nl1Active  layer 1 is activated,\n          layer 2 datalink not established\nl2Active  layer 1 is activated,\n          layer 2 datalink established.")
isdnLapdPeerSabme = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdPeerSabme.setDescription("The number of peer SABME frames received on this\ninterface. This is the number of peer-initiated\nnew connections on this interface.")
isdnLapdRecvdFrmr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdRecvdFrmr.setDescription("The number of LAPD FRMR response frames received.\nThis is the number of framing errors on this\ninterface.")
isdnEndpointGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 4))
isdnEndpointGetIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnEndpointGetIndex.setDescription("The recommended procedure for selecting a new index for\nisdnEndpointTable row creation is to GET the value of\nthis object, and then to SET the object with the same\nvalue. If the SET operation succeeds, the manager can use\nthis value as an index to create a new row in this table.")
isdnEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2))
if mibBuilder.loadTexts: isdnEndpointTable.setDescription("Table containing configuration for Terminal\nEndpoints.")
isdnEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1)).setIndexNames((0, "ISDN-MIB", "isdnEndpointIndex"))
if mibBuilder.loadTexts: isdnEndpointEntry.setDescription("An entry in the Terminal Endpoint Table. The value\nof isdnEndpointIfType must be supplied for a row\nin this table to become active.")
isdnEndpointIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: isdnEndpointIndex.setDescription("The index value which uniquely identifies an entry\nin the isdnEndpointTable.")
isdnEndpointIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnEndpointIfIndex.setDescription("The ifIndex value of the interface associated with this\nTerminal Endpoint.")
isdnEndpointIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 3), IANAifType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointIfType.setDescription("The interface type for this Terminal Endpoint.\nInterface types of x25ple(40) and isdn(63) are allowed.\nThe interface type is identical to the value of\nifType in the associated ifEntry.")
isdnEndpointTeiType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("dynamic", 1), ("static", 2), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointTeiType.setDescription("The type of TEI (Terminal Endpoint Identifier)\nused for this Terminal Endpoint. In case of dynamic(1),\nthe TEI value is selected by the switch. In\ncase of static(2), a valid TEI value has to be\nentered in the isdnEndpointTeiValue object.\nThe default value for this object depends on the\ninterface type as well as the Terminal Endpoint type.\nOn Primary Rate interfaces the default value is\nstatic(2). On Basic Rate interfaces the default value\nis dynamic(1) for isdn(63) Terminal Endpoints and\nstatic(2) for x25ple(40) Terminal Endpoints.")
isdnEndpointTeiValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointTeiValue.setDescription("The TEI (Terminal Endpoint Identifier) value\nfor this Terminal Endpoint. If isdnEndpointTeiType\nis set to static(2), valid numbers are 0..63,\nwhile otherwise the value is set internally.\nThe default value of this object is 0 for static\nTEI assignment.\nThe default value for dynamic TEI assignment is also\n0 as long as no TEI has been assigned. After TEI\nassignment, the assigned TEI value is returned.")
isdnEndpointSpid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 6), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointSpid.setDescription("The Service profile IDentifier (SPID) information\nfor this Terminal Endpoint.\n\nThe SPID is composed of 9-20 numeric characters.\n\nThis information has to be defined in addition to\nthe local number for some switch protocol types,\ne.g. Bellcore NI-1 and NI-2.\n\nIf this object is not required, it is a\nzero length string.")
isdnEndpointStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointStatus.setDescription("This object is used to create and delete rows in the\nisdnEndpointTable.")
isdnDirectoryGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 5))
isdnDirectoryTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1))
if mibBuilder.loadTexts: isdnDirectoryTable.setDescription("Table containing Directory Numbers.")
isdnDirectoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1)).setIndexNames((0, "ISDN-MIB", "isdnDirectoryIndex"))
if mibBuilder.loadTexts: isdnDirectoryEntry.setDescription("An entry in the Directory Number Table. All objects\nin an entry must be set for a new row to become active.")
isdnDirectoryIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: isdnDirectoryIndex.setDescription("The index value which uniquely identifies an entry\nin the isdnDirectoryTable.")
isdnDirectoryNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectoryNumber.setDescription("A Directory Number. Directory Numbers are used\nto identify incoming calls on the signaling\nchannel given in isdnDirectorySigIndex.\n\nThe format of this information largely depends on the type\nof switch or PBX the device is connected to. Therefore,\nthe detailed format of this information is not\nspecified and is implementation dependent.\n\nIf possible, the agent should implement this information\nusing the E.164 number format. In this case, the number\nmust start with '+'. Otherwise, IA5 number digits must\nbe used.")
isdnDirectorySigIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectorySigIndex.setDescription("An index pointing to an ISDN signaling channel.\nIncoming calls are accepted on this\nsignaling channel if the isdnDirectoryNumber is\npresented as Called Number in the SETUP message.")
isdnDirectoryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectoryStatus.setDescription("This object is used to create and delete rows in the\nisdnDirectoryTable.")
isdnMibTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2))
isdnMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2, 0))
isdnMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2, 1))
isdnMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2, 2))

# Augmentions
isdnSignalingEntry.registerAugmentions(("ISDN-MIB", "isdnSignalingStatsEntry"))
isdnSignalingStatsEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())

# Notifications

isdnMibCallInformation = NotificationType((1, 3, 6, 1, 2, 1, 10, 20, 2, 0, 1)).setObjects(*(("ISDN-MIB", "isdnBearerOperStatus"), ("ISDN-MIB", "isdnBearerPeerSubAddress"), ("ISDN-MIB", "isdnBearerCallSetupTime"), ("ISDN-MIB", "isdnBearerCallOrigin"), ("ISDN-MIB", "isdnBearerPeerAddress"), ("IF-MIB", "ifIndex"), ("ISDN-MIB", "isdnBearerInfoType"), ) )
if mibBuilder.loadTexts: isdnMibCallInformation.setDescription("This trap/inform is sent to the manager under the\nfollowing condidions:\n- on incoming calls for each call which is rejected for\n  policy reasons (e.g. unknown neighbor or access\n  violation)\n- on outgoing calls whenever a call attempt is determined\n  to have ultimately failed. In the event that call retry\n  is active, then this will be after all retry attempts\n  have failed.\n- whenever a call connects. In this case, the object\n  isdnBearerCallConnectTime should be included in the\n  trap.\n\nOnly one such trap is sent in between successful or\nunsuccessful call attempts from or to a single neighbor;\nsubsequent call attempts result in no trap.\n\nIf the Dial Control MIB objects dialCtlNbrCfgId and\ndialCtlNbrCfgIndex are known by the entity generating\nthis trap, both objects should be included in the trap\nas well. The receipt of this trap with no dial neighbor\ninformation indicates that the manager must poll the\ncallHistoryTable of the Dial Control MIB to see what\nchanged.")

# Groups

isdnMibBasicRateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 1)).setObjects(*(("ISDN-MIB", "isdnBasicRateIfType"), ("ISDN-MIB", "isdnBasicRateIfMode"), ("ISDN-MIB", "isdnBasicRateLineTopology"), ("ISDN-MIB", "isdnBasicRateSignalMode"), ) )
if mibBuilder.loadTexts: isdnMibBasicRateGroup.setDescription("A collection of objects required for ISDN Basic Rate\nphysical interface configuration and statistics.")
isdnMibBearerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 2)).setObjects(*(("ISDN-MIB", "isdnBearerOperStatus"), ("ISDN-MIB", "isdnBearerPeerSubAddress"), ("ISDN-MIB", "isdnBearerCallSetupTime"), ("ISDN-MIB", "isdnBearerChannelNumber"), ("ISDN-MIB", "isdnBearerCallOrigin"), ("ISDN-MIB", "isdnBearerChannelType"), ("ISDN-MIB", "isdnBearerMultirate"), ("ISDN-MIB", "isdnBearerCallConnectTime"), ("ISDN-MIB", "isdnBearerPeerAddress"), ("ISDN-MIB", "isdnBearerChargedUnits"), ("ISDN-MIB", "isdnBearerInfoType"), ) )
if mibBuilder.loadTexts: isdnMibBearerGroup.setDescription("A collection of objects required for ISDN Bearer channel\ncontrol and statistics.")
isdnMibSignalingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 3)).setObjects(*(("ISDN-MIB", "isdnLapdPeerSabme"), ("ISDN-MIB", "isdnLapdOperStatus"), ("ISDN-MIB", "isdnSignalingCallingAddress"), ("ISDN-MIB", "isdnSigStatsOutCalls"), ("ISDN-MIB", "isdnLapdRecvdFrmr"), ("ISDN-MIB", "isdnLapdPrimaryChannel"), ("ISDN-MIB", "isdnSignalingGetIndex"), ("ISDN-MIB", "isdnSignalingStatus"), ("ISDN-MIB", "isdnSigStatsOutConnected"), ("ISDN-MIB", "isdnSigStatsChargedUnits"), ("ISDN-MIB", "isdnSignalingIfIndex"), ("ISDN-MIB", "isdnSigStatsInConnected"), ("ISDN-MIB", "isdnSigStatsInCalls"), ("ISDN-MIB", "isdnSignalingProtocol"), ("ISDN-MIB", "isdnSignalingBchannelCount"), ("ISDN-MIB", "isdnSignalingInfoTrapEnable"), ("ISDN-MIB", "isdnSignalingSubAddress"), ) )
if mibBuilder.loadTexts: isdnMibSignalingGroup.setDescription("A collection of objects required for ISDN D channel\nconfiguration and statistics.")
isdnMibEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 4)).setObjects(*(("ISDN-MIB", "isdnEndpointGetIndex"), ("ISDN-MIB", "isdnEndpointIfType"), ("ISDN-MIB", "isdnEndpointSpid"), ("ISDN-MIB", "isdnEndpointTeiType"), ("ISDN-MIB", "isdnEndpointIfIndex"), ("ISDN-MIB", "isdnEndpointTeiValue"), ("ISDN-MIB", "isdnEndpointStatus"), ) )
if mibBuilder.loadTexts: isdnMibEndpointGroup.setDescription("A collection of objects describing Terminal Endpoints.")
isdnMibDirectoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 5)).setObjects(*(("ISDN-MIB", "isdnDirectoryNumber"), ("ISDN-MIB", "isdnDirectoryStatus"), ("ISDN-MIB", "isdnDirectorySigIndex"), ) )
if mibBuilder.loadTexts: isdnMibDirectoryGroup.setDescription("A collection of objects describing directory numbers.")
isdnMibNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 6)).setObjects(*(("ISDN-MIB", "isdnMibCallInformation"), ) )
if mibBuilder.loadTexts: isdnMibNotificationsGroup.setDescription("The notifications which a ISDN MIB entity is\nrequired to implement.")

# Compliances

isdnMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 20, 2, 1, 1)).setObjects(*(("ISDN-MIB", "isdnMibEndpointGroup"), ("ISDN-MIB", "isdnMibNotificationsGroup"), ("ISDN-MIB", "isdnMibBasicRateGroup"), ("ISDN-MIB", "isdnMibDirectoryGroup"), ("ISDN-MIB", "isdnMibSignalingGroup"), ("ISDN-MIB", "isdnMibBearerGroup"), ) )
if mibBuilder.loadTexts: isdnMibCompliance.setDescription("The compliance statement for entities which implement\nthe ISDN MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ISDN-MIB", PYSNMP_MODULE_ID=isdnMib)

# Types
mibBuilder.exportSymbols("ISDN-MIB", IsdnSignalingProtocol=IsdnSignalingProtocol)

# Objects
mibBuilder.exportSymbols("ISDN-MIB", isdnMib=isdnMib, isdnMibObjects=isdnMibObjects, isdnBasicRateGroup=isdnBasicRateGroup, isdnBasicRateTable=isdnBasicRateTable, isdnBasicRateEntry=isdnBasicRateEntry, isdnBasicRateIfType=isdnBasicRateIfType, isdnBasicRateLineTopology=isdnBasicRateLineTopology, isdnBasicRateIfMode=isdnBasicRateIfMode, isdnBasicRateSignalMode=isdnBasicRateSignalMode, isdnBearerGroup=isdnBearerGroup, isdnBearerTable=isdnBearerTable, isdnBearerEntry=isdnBearerEntry, isdnBearerChannelType=isdnBearerChannelType, isdnBearerOperStatus=isdnBearerOperStatus, isdnBearerChannelNumber=isdnBearerChannelNumber, isdnBearerPeerAddress=isdnBearerPeerAddress, isdnBearerPeerSubAddress=isdnBearerPeerSubAddress, isdnBearerCallOrigin=isdnBearerCallOrigin, isdnBearerInfoType=isdnBearerInfoType, isdnBearerMultirate=isdnBearerMultirate, isdnBearerCallSetupTime=isdnBearerCallSetupTime, isdnBearerCallConnectTime=isdnBearerCallConnectTime, isdnBearerChargedUnits=isdnBearerChargedUnits, isdnSignalingGroup=isdnSignalingGroup, isdnSignalingGetIndex=isdnSignalingGetIndex, isdnSignalingTable=isdnSignalingTable, isdnSignalingEntry=isdnSignalingEntry, isdnSignalingIndex=isdnSignalingIndex, isdnSignalingIfIndex=isdnSignalingIfIndex, isdnSignalingProtocol=isdnSignalingProtocol, isdnSignalingCallingAddress=isdnSignalingCallingAddress, isdnSignalingSubAddress=isdnSignalingSubAddress, isdnSignalingBchannelCount=isdnSignalingBchannelCount, isdnSignalingInfoTrapEnable=isdnSignalingInfoTrapEnable, isdnSignalingStatus=isdnSignalingStatus, isdnSignalingStatsTable=isdnSignalingStatsTable, isdnSignalingStatsEntry=isdnSignalingStatsEntry, isdnSigStatsInCalls=isdnSigStatsInCalls, isdnSigStatsInConnected=isdnSigStatsInConnected, isdnSigStatsOutCalls=isdnSigStatsOutCalls, isdnSigStatsOutConnected=isdnSigStatsOutConnected, isdnSigStatsChargedUnits=isdnSigStatsChargedUnits, isdnLapdTable=isdnLapdTable, isdnLapdEntry=isdnLapdEntry, isdnLapdPrimaryChannel=isdnLapdPrimaryChannel, isdnLapdOperStatus=isdnLapdOperStatus, isdnLapdPeerSabme=isdnLapdPeerSabme, isdnLapdRecvdFrmr=isdnLapdRecvdFrmr, isdnEndpointGroup=isdnEndpointGroup, isdnEndpointGetIndex=isdnEndpointGetIndex, isdnEndpointTable=isdnEndpointTable, isdnEndpointEntry=isdnEndpointEntry, isdnEndpointIndex=isdnEndpointIndex, isdnEndpointIfIndex=isdnEndpointIfIndex, isdnEndpointIfType=isdnEndpointIfType, isdnEndpointTeiType=isdnEndpointTeiType, isdnEndpointTeiValue=isdnEndpointTeiValue, isdnEndpointSpid=isdnEndpointSpid, isdnEndpointStatus=isdnEndpointStatus, isdnDirectoryGroup=isdnDirectoryGroup, isdnDirectoryTable=isdnDirectoryTable, isdnDirectoryEntry=isdnDirectoryEntry, isdnDirectoryIndex=isdnDirectoryIndex, isdnDirectoryNumber=isdnDirectoryNumber, isdnDirectorySigIndex=isdnDirectorySigIndex, isdnDirectoryStatus=isdnDirectoryStatus, isdnMibTrapPrefix=isdnMibTrapPrefix, isdnMibTraps=isdnMibTraps, isdnMibCompliances=isdnMibCompliances, isdnMibGroups=isdnMibGroups)

# Notifications
mibBuilder.exportSymbols("ISDN-MIB", isdnMibCallInformation=isdnMibCallInformation)

# Groups
mibBuilder.exportSymbols("ISDN-MIB", isdnMibBasicRateGroup=isdnMibBasicRateGroup, isdnMibBearerGroup=isdnMibBearerGroup, isdnMibSignalingGroup=isdnMibSignalingGroup, isdnMibEndpointGroup=isdnMibEndpointGroup, isdnMibDirectoryGroup=isdnMibDirectoryGroup, isdnMibNotificationsGroup=isdnMibNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ISDN-MIB", isdnMibCompliance=isdnMibCompliance)
