# PySNMP SMI module. Autogenerated from smidump -f python RTP-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:16:10 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TAddress, TDomain, TestAndIncr, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TAddress", "TDomain", "TestAndIncr", "TimeStamp", "TruthValue")
( Utf8String, ) = mibBuilder.importSymbols("SYSAPPL-MIB", "Utf8String")

# Objects

rtpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 87)).setRevisions(("2000-10-02 00:00",))
if mibBuilder.loadTexts: rtpMIB.setOrganization("IETF AVT Working Group\nEmail:   rem-conf@es.net")
if mibBuilder.loadTexts: rtpMIB.setContactInfo("Mark Baugher\nPostal: Intel Corporation\n        2111 NE 25th Avenue\n        Hillsboro, OR   97124\n\n\n        United States\nTel:    +1 503 466 8406\nEmail:  mbaugher@passedge.com\n\n        Bill Strahm\nPostal: Intel Corporation\n        2111 NE 25th Avenue\n        Hillsboro, OR   97124\n        United States\nTel:    +1 503 264 4632\nEmail:  bill.strahm@intel.com\n\n        Irina Suconick\nPostal: Ennovate Networks\n        60 Codman Hill Rd.,\n        Boxboro, Ma 01719\nTel:    +1 781-505-2155\nEmail:  irina@ennovatenetworks.com")
if mibBuilder.loadTexts: rtpMIB.setDescription("The managed objects of RTP systems.  The MIB is\nstructured around three types of information.\n1. General information about RTP sessions such\n   as the session address.\n2. Information about RTP streams being sent to\n   an RTP session by a particular sender.\n3. Information about RTP streams received on an\n   RTP session by a particular receiver from a\n   particular sender.\n There are two types of RTP Systems, RTP hosts and\n RTP monitors.  As described below, certain objects\n are unique to a particular type of RTP System.   An\n RTP host may also function as an RTP monitor.\n Refer to RFC 1889, 'RTP: A Transport Protocol for\n Real-Time Applications,' section 3.0, for definitions.")
rtpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 1))
rtpSessionNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 87, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtpSessionNewIndex.setDescription("This  object  is  used  to  assign  values  to rtpSessionIndex\nas described in 'Textual Conventions  for  SMIv2'.  For an RTP\nsystem that supports the creation of rows, the  network manager\nwould read the  object,  and  then write the value back in\nthe Set that creates a new instance  of rtpSessionEntry.   If\nthe  Set  fails with the code 'inconsistentValue,' then the\nprocess must be repeated; If the Set succeeds, then the object\nis incremented, and the  new  instance  is created according to\nthe manager's directions.  However, if the RTP agent is not\nacting as a monitor, only the RTP agent may create conceptual\nrows in the RTP session table.")
rtpSessionInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 2))
if mibBuilder.loadTexts: rtpSessionInverseTable.setDescription("Maps rtpSessionDomain, rtpSessionRemAddr, and rtpSessionLocAddr\nTAddress pairs to one or more rtpSessionIndex values, each\ndescribing a row in the rtpSessionTable.  This makes it possible\nto retrieve the row(s) in the rtpSessionTable corresponding to a\ngiven session without having to walk the entire (potentially\nlarge) table.")
rtpSessionInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 2, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpSessionRemAddr"), (0, "RTP-MIB", "rtpSessionLocAddr"), (0, "RTP-MIB", "rtpSessionIndex"))
if mibBuilder.loadTexts: rtpSessionInverseEntry.setDescription("Each entry corresponds to exactly one entry in the\nrtpSessionTable - the entry containing the tuple,\nrtpSessionDomain, rtpSessionRemAddr, rtpSessionLocAddr\nand rtpSessionIndex.")
rtpSessionInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 2, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionInverseStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpSessionTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 3))
if mibBuilder.loadTexts: rtpSessionTable.setDescription("There's one entry in rtpSessionTable for each RTP session\non which packets are being sent, received, and/or\nmonitored.")
rtpSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 3, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"))
if mibBuilder.loadTexts: rtpSessionEntry.setDescription("Data in rtpSessionTable uniquely identify an RTP session.  A\nhost RTP agent MUST create a read-only row for each session to\nwhich packets are being sent or received.  Rows MUST be created\nby the RTP Agent at the start of a session when one or more\nsenders or receivers are observed.  Rows created by an RTP agent\nMUST be deleted when the session is over and there are no\nrtpRcvrEntry and no rtpSenderEntry for this session.  An RTP\nsession SHOULD be monitored to create management information on\nall RTP streams being sent or received when the\nrtpSessionMonitor has the TruthValue of 'true(1)'.  An RTP\nmonitor SHOULD permit row creation with the side effect of\ncausing the RTP System to join the multicast session for the\npurposes of gathering management information  (additional\nconceptual rows are created in the rtpRcvrTable and\nrtpSenderTable).  Thus, rtpSessionTable rows SHOULD be created\nfor RTP session monitoring purposes.  Rows created by a\nmanagement application SHOULD be deleted via SNMP operations by\n\n\nmanagement applications.  Rows created by management operations\nare deleted by management operations by setting\nrtpSessionRowStatus to 'destroy(6)'.")
rtpSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rtpSessionIndex.setDescription("The index of the conceptual row which is for SNMP purposes\nonly and has no relation to any protocol value.  There is\nno requirement that these rows are created or maintained\nsequentially.")
rtpSessionDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 2), TDomain()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionDomain.setDescription("The transport-layer protocol used for sending or receiving\nthe stream of RTP data packets on this session.\nCannot be changed if rtpSessionRowStatus is 'active'.")
rtpSessionRemAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 3), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionRemAddr.setDescription("The address to which RTP packets are sent by the RTP system.\nIn an IP multicast RTP session, this is the single address used\n\n\nby all senders and receivers of RTP session data.  In a unicast\nRTP session this is the unicast address of the remote RTP system.\n'The destination address pair may be common for all participants,\nas in the case of IP multicast, or may be different for each, as\nin the case of individual unicast network address pairs.'  See\nRFC 1889, 'RTP: A Transport Protocol for Real-Time Applications,'\nsec. 3.  The transport service is identified by rtpSessionDomain.\nFor snmpUDPDomain, this is an IP address and even-numbered UDP\nPort with the RTCP being sent on the next higher odd-numbered\nport, see RFC 1889, sec. 5.")
rtpSessionLocAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionLocAddr.setDescription("The local address used by the RTP system.  In an IP multicast\nRTP session, rtpSessionRemAddr will be the same IP multicast\naddress as rtpSessionLocAddr.  In a unicast RTP session,\nrtpSessionRemAddr and rtpSessionLocAddr will have different\nunicast addresses.  See RFC 1889, 'RTP: A Transport Protocol for\nReal-Time Applications,' sec. 3.  The transport service is\nidentified by rtpSessionDomain.  For snmpUDPDomain, this is an IP\naddress and even-numbered UDP Port with the RTCP being sent on\nthe next higher odd-numbered port, see RFC 1889, sec. 5.")
rtpSessionIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionIfIndex.setDescription("The ifIndex value is set to the corresponding value\nfrom IF-MIB (See RFC 2233, 'The Interfaces Group MIB using\nSMIv2').  This is the interface that the RTP stream is being sent\nto or received from, or in the case of an RTP Monitor the\ninterface that RTCP packets will be received on.  Cannot be\nchanged if rtpSessionRowStatus is 'active'.")
rtpSessionSenderJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionSenderJoins.setDescription("The number of senders that have been observed to have\njoined the session since this conceptual row was created\n\n\n(rtpSessionStartTime).  A sender 'joins' an RTP\nsession by sending to it.  Senders that leave and then\nre-join following an RTCP BYE (see RFC 1889, 'RTP: A\nTransport Protocol for Real-Time Applications,' sec. 6.6)\nor session timeout may be counted twice.  Every time a new\nRTP sender is detected either using RTP or RTCP, this counter\nis incremented.")
rtpSessionReceiverJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionReceiverJoins.setDescription("The number of receivers that have been been observed to\nhave joined this session since this conceptual row was\ncreated (rtpSessionStartTime).  A receiver 'joins' an RTP\nsession by sending RTCP Receiver Reports to the session.\nReceivers that leave and then re-join following an RTCP BYE\n(see RFC 1889, 'RTP: A Transport Protocol for Real-Time\nApplications,' sec. 6.6) or session timeout may be counted\ntwice.")
rtpSessionByes = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionByes.setDescription("A count of RTCP BYE (see RFC 1889, 'RTP: A Transport\nProtocol for Real-Time Applications,' sec. 6.6) messages\nreceived by this entity.")
rtpSessionStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpSessionMonitor = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSessionMonitor.setDescription("Boolean, Set to 'true(1)' if remote senders or receivers in\naddition to the local RTP System are to be monitored using RTCP.\nRTP Monitors MUST initialize to 'true(1)' and RTP Hosts SHOULD\ninitialize this 'false(2)'.  Note that because 'host monitor'\nsystems are receiving RTCP from their remote participants they\nMUST set this value to 'true(1)'.")
rtpSessionRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rtpSessionRowStatus.setDescription("Value of 'active' when RTP or RTCP messages are being\nsent or received by an RTP System.  A newly-created\nconceptual row must have the all read-create objects\ninitialized before becoming 'active'.\nA conceptual row that is in the 'notReady' or 'notInService'\nstate MAY be removed after 5  minutes.")
rtpSenderInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 4))
if mibBuilder.loadTexts: rtpSenderInverseTable.setDescription("Maps rtpSenderAddr, rtpSessionIndex, to the rtpSenderSSRC\nindex of the rtpSenderTable.  This table allows management\napplications to find entries sorted by rtpSenderAddr rather than\nsorted by rtpSessionIndex.  Given the rtpSessionDomain and\nrtpSenderAddr, a set of rtpSessionIndex and rtpSenderSSRC values\ncan be returned from a tree walk.  When rtpSessionIndex is\nspecified in the SNMP Get-Next operations, one or more\nrtpSenderSSRC values may be returned.")
rtpSenderInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 4, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpSenderAddr"), (0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpSenderSSRC"))
if mibBuilder.loadTexts: rtpSenderInverseEntry.setDescription("Each entry corresponds to exactly one entry in the\nrtpSenderTable - the entry containing the index pair,\nrtpSessionIndex, rtpSenderSSRC.")
rtpSenderInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 4, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderInverseStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpSenderTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 5))
if mibBuilder.loadTexts: rtpSenderTable.setDescription("Table of information about a sender or senders to an RTP\nSession. RTP sending hosts MUST have an entry in this table\nfor each stream being sent.  RTP receiving hosts MAY have an\nentry in this table for each sending stream being received by\nthis host.  RTP monitors MUST create an entry for each observed\nsender to a multicast RTP Session as a side-effect when a\nconceptual row in the rtpSessionTable is made 'active' by a\nmanager.")
rtpSenderEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 5, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpSenderSSRC"))
if mibBuilder.loadTexts: rtpSenderEntry.setDescription("Each entry contains information from a single RTP Sender\nSynchronization Source (SSRC, see RFC 1889 'RTP: A Transport\nProtocol for Real-Time Applications' sec.6).  The session is\nidentified to the the SNMP entity by rtpSessionIndex.\nRows are removed by the RTP agent when a BYE is received\nfrom the sender or when the sender times out (see RFC\n1889, Sec. 6.2.1) or when the rtpSessionEntry is deleted.")
rtpSenderSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rtpSenderSSRC.setDescription("The RTP SSRC, or synchronization source identifier of the\nsender.  The RTP session address plus an SSRC uniquely\nidentify a sender to an RTP session (see RFC 1889, 'RTP: A\nTransport Protocol for Real-Time Applications' sec.3).")
rtpSenderCNAME = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 2), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderCNAME.setDescription("The RTP canonical name of the sender.")
rtpSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 3), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderAddr.setDescription("The unicast transport source address of the sender.  In the\ncase of an RTP Monitor this address is the address that the\nsender is using to send its RTCP Sender Reports.")
rtpSenderPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderPackets.setDescription("Count of RTP packets sent by this sender, or observed by\n\n\nan RTP monitor, since rtpSenderStartTime.")
rtpSenderOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderOctets.setDescription("Count of non-header RTP octets sent by this sender, or observed\nby an RTP monitor, since rtpSenderStartTime.")
rtpSenderTool = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 6), Utf8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderTool.setDescription("Name of the application program source of the stream.")
rtpSenderSRs = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderSRs.setDescription("A count of the number of RTCP Sender Reports that have\nbeen sent from this sender, or observed if the RTP entity\nis a monitor, since rtpSenderStartTime.")
rtpSenderSRTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderSRTime.setDescription("rtpSenderSRTime is the value of SysUpTime at the time that\nthe last SR was received from this sender, in the case of a\nmonitor or receiving host.  Or sent by this sender, in the\ncase of a sending host.")
rtpSenderPT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderPT.setDescription("Payload type from the RTP header of the most recently received\nRTP Packet (see RFC 1889, 'RTP: A Transport Protocol for\n\n\nReal-Time Applications' sec. 5).")
rtpSenderStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpSenderStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpRcvrInverseTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 6))
if mibBuilder.loadTexts: rtpRcvrInverseTable.setDescription("Maps rtpRcvrAddr and rtpSessionIndex to the rtpRcvrSRCSSRC and\nrtpRcvrSSRC indexes of the rtpRcvrTable.  This table allows\nmanagement applications to find entries sorted by rtpRcvrAddr\nrather than by rtpSessionIndex. Given rtpSessionDomain and\nrtpRcvrAddr, a set of rtpSessionIndex, rtpRcvrSRCSSRC, and\nrtpRcvrSSRC values can be returned from a tree walk.  When\nrtpSessionIndex is specified in SNMP Get-Next operations, one or\nmore rtpRcvrSRCSSRC and rtpRcvrSSRC pairs may be returned.")
rtpRcvrInverseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 6, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionDomain"), (0, "RTP-MIB", "rtpRcvrAddr"), (0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpRcvrSRCSSRC"), (0, "RTP-MIB", "rtpRcvrSSRC"))
if mibBuilder.loadTexts: rtpRcvrInverseEntry.setDescription("Each entry corresponds to exactly one entry in the\nrtpRcvrTable - the entry containing the index pair,\nrtpSessionIndex, rtpRcvrSSRC.")
rtpRcvrInverseStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrInverseStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpRcvrTable = MibTable((1, 3, 6, 1, 2, 1, 87, 1, 7))
if mibBuilder.loadTexts: rtpRcvrTable.setDescription("Table of information about a receiver or receivers of RTP\nsession data. RTP hosts that receive RTP session packets\nMUST create an entry in this table for that receiver/sender\npair.  RTP hosts that send RTP session packets MAY create\nan entry in this table for each receiver to their stream\nusing RTCP feedback from the RTP group.  RTP monitors\ncreate an entry for each observed RTP session receiver as\na side effect when a conceptual row in the rtpSessionTable\nis made 'active' by a manager.")
rtpRcvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 87, 1, 7, 1)).setIndexNames((0, "RTP-MIB", "rtpSessionIndex"), (0, "RTP-MIB", "rtpRcvrSRCSSRC"), (0, "RTP-MIB", "rtpRcvrSSRC"))
if mibBuilder.loadTexts: rtpRcvrEntry.setDescription("Each entry contains information from a single RTP\nSynchronization Source that is receiving packets from the\nsender identified by rtpRcvrSRCSSRC (SSRC, see RFC 1889,\n'RTP: A Transport Protocol for Real-Time Applications'\nsec.6).  The session is identified to the the RTP Agent entity\nby rtpSessionIndex.  Rows are removed by the RTP agent when\na BYE is received from the sender or when the sender times\nout (see RFC 1889, Sec. 6.2.1) or when the rtpSessionEntry is\ndeleted.")
rtpRcvrSRCSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rtpRcvrSRCSSRC.setDescription("The RTP SSRC, or synchronization source identifier of the\nsender.  The RTP session address plus an SSRC uniquely\nidentify a sender or receiver of an RTP stream (see RFC\n1889, 'RTP:  A Transport Protocol for Real-Time\nApplications' sec.3).")
rtpRcvrSSRC = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 2), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rtpRcvrSSRC.setDescription("The RTP SSRC, or synchronization source identifier of the\nreceiver.  The RTP session address plus an SSRC uniquely\nidentify a receiver of an RTP stream (see RFC 1889, 'RTP:\nA Transport Protocol for Real-Time Applications' sec.3).")
rtpRcvrCNAME = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 3), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrCNAME.setDescription("The RTP canonical name of the receiver.")
rtpRcvrAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrAddr.setDescription("The unicast transport address on which the receiver is\nreceiving RTP packets and/or RTCP Receiver Reports.")
rtpRcvrRTT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRTT.setDescription("The round trip time measurement taken by the source of the\nRTP stream based on the algorithm described on sec. 6 of\nRFC 1889, 'RTP: A Transport Protocol for Real-Time\nApplications.'  This algorithm can produce meaningful\nresults when the RTP agent has the same clock as the stream\nsender (when the RTP monitor is also the sending host for the\nparticular receiver).  Otherwise, the entity should return\n'noSuchInstance' in response to queries against rtpRcvrRTT.")
rtpRcvrLostPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrLostPackets.setDescription("A count of RTP  packets lost as observed by this receiver\nsince rtpRcvrStartTime.")
rtpRcvrJitter = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrJitter.setDescription("An estimate of delay variation as observed by this\nreceiver.  (see RFC 1889, 'RTP: A Transport Protocol\nfor Real-Time Applications' sec.6.3.1 and A.8).")
rtpRcvrTool = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 8), Utf8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrTool.setDescription("Name of the application program source of the stream.")
rtpRcvrRRs = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRRs.setDescription("A count of the number of RTCP Receiver Reports that have\nbeen sent from this receiver, or observed if the RTP entity\nis a monitor, since rtpRcvrStartTime.")
rtpRcvrRRTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrRRTime.setDescription("rtpRcvrRRTime is the value of SysUpTime at the time that the\nlast RTCP Receiver Report was received from this receiver, in\nthe case of a monitor or RR receiver (the RTP Sender).  It is\nthe  value of SysUpTime at the time that the last RR was sent by\nthis receiver in the case of an RTP receiver sending the RR.")
rtpRcvrPT = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrPT.setDescription("Static or dynamic payload type from the RTP header (see\nRFC 1889, 'RTP: A Transport Protocol for Real-Time\nApplications' sec. 5).")
rtpRcvrPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrPackets.setDescription("Count of RTP packets received by this RTP host receiver\nsince rtpRcvrStartTime.")
rtpRcvrOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrOctets.setDescription("Count of non-header RTP octets received by this receiving RTP\nhost since rtpRcvrStartTime.")
rtpRcvrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtpRcvrStartTime.setDescription("The value of SysUpTime at the time that this row was\ncreated.")
rtpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2))
rtpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2, 1))
rtpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 87, 2, 2))

# Augmentions

# Groups

rtpSystemGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 1)).setObjects(("RTP-MIB", "rtpSenderPackets"), ("RTP-MIB", "rtpRcvrRRs"), ("RTP-MIB", "rtpSenderStartTime"), ("RTP-MIB", "rtpSessionMonitor"), ("RTP-MIB", "rtpSessionStartTime"), ("RTP-MIB", "rtpSenderAddr"), ("RTP-MIB", "rtpSenderSRs"), ("RTP-MIB", "rtpRcvrAddr"), ("RTP-MIB", "rtpRcvrCNAME"), ("RTP-MIB", "rtpSessionIfIndex"), ("RTP-MIB", "rtpSessionByes"), ("RTP-MIB", "rtpSessionRemAddr"), ("RTP-MIB", "rtpSessionDomain"), ("RTP-MIB", "rtpSenderOctets"), ("RTP-MIB", "rtpRcvrLostPackets"), ("RTP-MIB", "rtpSenderTool"), ("RTP-MIB", "rtpRcvrJitter"), ("RTP-MIB", "rtpSenderSRTime"), ("RTP-MIB", "rtpRcvrStartTime"), ("RTP-MIB", "rtpSenderCNAME"), ("RTP-MIB", "rtpSessionReceiverJoins"), ("RTP-MIB", "rtpRcvrRRTime"), ("RTP-MIB", "rtpSessionSenderJoins"), ("RTP-MIB", "rtpRcvrTool"), )
if mibBuilder.loadTexts: rtpSystemGroup.setDescription("Objects available to all RTP Systems.")
rtpHostGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 2)).setObjects(("RTP-MIB", "rtpRcvrPackets"), ("RTP-MIB", "rtpSenderPT"), ("RTP-MIB", "rtpSessionLocAddr"), ("RTP-MIB", "rtpRcvrRTT"), ("RTP-MIB", "rtpRcvrOctets"), ("RTP-MIB", "rtpRcvrPT"), )
if mibBuilder.loadTexts: rtpHostGroup.setDescription("Objects that are available to RTP Host systems, but may not\nbe available to RTP Monitor systems.")
rtpMonitorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 3)).setObjects(("RTP-MIB", "rtpSessionNewIndex"), ("RTP-MIB", "rtpSessionRowStatus"), )
if mibBuilder.loadTexts: rtpMonitorGroup.setDescription("Objects used to create rows in the RTP Session Table.  These\nobjects are not needed if the system does not create rows.")
rtpInverseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 87, 2, 1, 4)).setObjects(("RTP-MIB", "rtpSenderInverseStartTime"), ("RTP-MIB", "rtpRcvrInverseStartTime"), ("RTP-MIB", "rtpSessionInverseStartTime"), )
if mibBuilder.loadTexts: rtpInverseGroup.setDescription("Objects used in the Inverse Lookup Tables.")

# Compliances

rtpHostCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 87, 2, 2, 1)).setObjects(("RTP-MIB", "rtpSystemGroup"), ("RTP-MIB", "rtpHostGroup"), ("RTP-MIB", "rtpMonitorGroup"), ("RTP-MIB", "rtpInverseGroup"), )
if mibBuilder.loadTexts: rtpHostCompliance.setDescription("Host implementations MUST comply.")
rtpMonitorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 87, 2, 2, 2)).setObjects(("RTP-MIB", "rtpSystemGroup"), ("RTP-MIB", "rtpHostGroup"), ("RTP-MIB", "rtpMonitorGroup"), ("RTP-MIB", "rtpInverseGroup"), )
if mibBuilder.loadTexts: rtpMonitorCompliance.setDescription("Monitor implementations must comply.  RTP Monitors are not\nrequired to support creation or deletion.")

# Exports

# Module identity
mibBuilder.exportSymbols("RTP-MIB", PYSNMP_MODULE_ID=rtpMIB)

# Objects
mibBuilder.exportSymbols("RTP-MIB", rtpMIB=rtpMIB, rtpMIBObjects=rtpMIBObjects, rtpSessionNewIndex=rtpSessionNewIndex, rtpSessionInverseTable=rtpSessionInverseTable, rtpSessionInverseEntry=rtpSessionInverseEntry, rtpSessionInverseStartTime=rtpSessionInverseStartTime, rtpSessionTable=rtpSessionTable, rtpSessionEntry=rtpSessionEntry, rtpSessionIndex=rtpSessionIndex, rtpSessionDomain=rtpSessionDomain, rtpSessionRemAddr=rtpSessionRemAddr, rtpSessionLocAddr=rtpSessionLocAddr, rtpSessionIfIndex=rtpSessionIfIndex, rtpSessionSenderJoins=rtpSessionSenderJoins, rtpSessionReceiverJoins=rtpSessionReceiverJoins, rtpSessionByes=rtpSessionByes, rtpSessionStartTime=rtpSessionStartTime, rtpSessionMonitor=rtpSessionMonitor, rtpSessionRowStatus=rtpSessionRowStatus, rtpSenderInverseTable=rtpSenderInverseTable, rtpSenderInverseEntry=rtpSenderInverseEntry, rtpSenderInverseStartTime=rtpSenderInverseStartTime, rtpSenderTable=rtpSenderTable, rtpSenderEntry=rtpSenderEntry, rtpSenderSSRC=rtpSenderSSRC, rtpSenderCNAME=rtpSenderCNAME, rtpSenderAddr=rtpSenderAddr, rtpSenderPackets=rtpSenderPackets, rtpSenderOctets=rtpSenderOctets, rtpSenderTool=rtpSenderTool, rtpSenderSRs=rtpSenderSRs, rtpSenderSRTime=rtpSenderSRTime, rtpSenderPT=rtpSenderPT, rtpSenderStartTime=rtpSenderStartTime, rtpRcvrInverseTable=rtpRcvrInverseTable, rtpRcvrInverseEntry=rtpRcvrInverseEntry, rtpRcvrInverseStartTime=rtpRcvrInverseStartTime, rtpRcvrTable=rtpRcvrTable, rtpRcvrEntry=rtpRcvrEntry, rtpRcvrSRCSSRC=rtpRcvrSRCSSRC, rtpRcvrSSRC=rtpRcvrSSRC, rtpRcvrCNAME=rtpRcvrCNAME, rtpRcvrAddr=rtpRcvrAddr, rtpRcvrRTT=rtpRcvrRTT, rtpRcvrLostPackets=rtpRcvrLostPackets, rtpRcvrJitter=rtpRcvrJitter, rtpRcvrTool=rtpRcvrTool, rtpRcvrRRs=rtpRcvrRRs, rtpRcvrRRTime=rtpRcvrRRTime, rtpRcvrPT=rtpRcvrPT, rtpRcvrPackets=rtpRcvrPackets, rtpRcvrOctets=rtpRcvrOctets, rtpRcvrStartTime=rtpRcvrStartTime, rtpConformance=rtpConformance, rtpGroups=rtpGroups, rtpCompliances=rtpCompliances)

# Groups
mibBuilder.exportSymbols("RTP-MIB", rtpSystemGroup=rtpSystemGroup, rtpHostGroup=rtpHostGroup, rtpMonitorGroup=rtpMonitorGroup, rtpInverseGroup=rtpInverseGroup)

# Compliances
mibBuilder.exportSymbols("RTP-MIB", rtpHostCompliance=rtpHostCompliance, rtpMonitorCompliance=rtpMonitorCompliance)
