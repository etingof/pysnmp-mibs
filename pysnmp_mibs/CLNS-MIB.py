# PySNMP SMI module. Autogenerated from smidump -f python CLNS-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:15:12 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( PhysAddress, ) = mibBuilder.importSymbols("RFC1213-MIB", "PhysAddress")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "experimental")

# Types

class ClnpAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,21)
    

# Objects

clns = MibIdentifier((1, 3, 6, 1, 3, 1))
clnp = MibIdentifier((1, 3, 6, 1, 3, 1, 1))
clnpForwarding = MibScalar((1, 3, 6, 1, 3, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("is", 1), ("es", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpForwarding.setDescription("The indication of whether this entity is active\nas an intermediate or end system.  Only\nintermediate systems will forward PDUs onward that\nare not addressed to them.")
clnpDefaultLifeTime = MibScalar((1, 3, 6, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpDefaultLifeTime.setDescription("The default value inserted into the Lifetime\nfield of the CLNP PDU header of PDUs sourced by\nthis entity.")
clnpInReceives = MibScalar((1, 3, 6, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInReceives.setDescription("The total number of input PDUs received from all\nconnected network interfaces running CLNP,\nincluding errors.")
clnpInHdrErrors = MibScalar((1, 3, 6, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInHdrErrors.setDescription("The number of input PDUs discarded due to errors\nin the CLNP header, including bad checksums,\nversion mismatch, lifetime exceeded, errors\ndiscovered in processing options, etc.")
clnpInAddrErrors = MibScalar((1, 3, 6, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInAddrErrors.setDescription("The number of input PDUs discarded because the\nNSAP address in the CLNP header's destination\nfield was not a valid NSAP to be received at this\nentity.  This count includes addresses not\nunderstood.  For end systems, this is a count of\nPDUs which arrived with a destination NSAP which\nwas not local.")
clnpForwPDUs = MibScalar((1, 3, 6, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpForwPDUs.setDescription("The number of input PDUs for which this entity\nwas not the final destination and which an attempt\nwas made to forward them onward.")
clnpInUnknownNLPs = MibScalar((1, 3, 6, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInUnknownNLPs.setDescription("The number of locally-addressed PDUs successfully\nreceived but discarded because the network layer\nprotocol was unknown or unsupported (e.g., not\nCLNP or ES-IS).")
clnpInUnknownULPs = MibScalar((1, 3, 6, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInUnknownULPs.setDescription("The number of locally-addressed PDUs successfully\nreceived but discarded because the upper layer\nprotocol was unknown or unsupported (e.g., not\nTP4).")
clnpInDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInDiscards.setDescription("The number of input CLNP PDUs for which no\nproblems were encountered to prevent their\ncontinued processing, but were discarded (e.g.,\nfor lack of buffer space).  Note that this counter\ndoes not include any PDUs discarded while awaiting\nre-assembly.")
clnpInDelivers = MibScalar((1, 3, 6, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInDelivers.setDescription("The total number of input PDUs successfully\ndelivered to the CLNS transport user.")
clnpOutRequests = MibScalar((1, 3, 6, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutRequests.setDescription("The total number of CLNP PDUs which local CLNS\nuser protocols supplied to CLNP for transmission\nrequests.  This counter does not include any PDUs\ncounted in clnpForwPDUs.")
clnpOutDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutDiscards.setDescription("The number of output CLNP PDUs for which no other\nproblem was encountered to prevent their\ntransmission but were discarded (e.g., for lack of\nbuffer space).  Note this counter includes PDUs\ncounted in clnpForwPDUs.")
clnpOutNoRoutes = MibScalar((1, 3, 6, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutNoRoutes.setDescription("The number of CLNP PDUs discarded because no\nroute could be found to transmit them to their\ndestination.  This counter includes any PDUs\ncounted in clnpForwPDUs.")
clnpReasmTimeout = MibScalar((1, 3, 6, 1, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpReasmTimeout.setDescription("The maximum number of seconds which received\nsegments are held while they are awaiting\nreassembly at this entity.")
clnpReasmReqds = MibScalar((1, 3, 6, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpReasmReqds.setDescription("The number of CLNP segments received which needed\nto be reassembled at this entity.")
clnpReasmOKs = MibScalar((1, 3, 6, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpReasmOKs.setDescription("The number of CLNP PDUs successfully re-assembled\nat this entity.")
clnpReasmFails = MibScalar((1, 3, 6, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpReasmFails.setDescription("The number of failures detected by the CLNP\nreassembly algorithm (for any reason: timed out,\nbuffer size, etc).")
clnpSegOKs = MibScalar((1, 3, 6, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpSegOKs.setDescription("The number of CLNP PDUs that have been\nsuccessfully segmented at this entity.")
clnpSegFails = MibScalar((1, 3, 6, 1, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpSegFails.setDescription("The number of CLNP PDUs that have been discarded\nbecause they needed to be fragmented at this\nentity but could not.")
clnpSegCreates = MibScalar((1, 3, 6, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpSegCreates.setDescription("The number of CLNP PDU segments that have been\ngenerated as a result of segmentation at this\nentity.")
clnpAddrTable = MibTable((1, 3, 6, 1, 3, 1, 1, 21))
if mibBuilder.loadTexts: clnpAddrTable.setDescription("The table of addressing information relevant to\nthis entity's CLNP addresses.  ")
clnpAddrEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 21, 1)).setIndexNames((0, "CLNS-MIB", "clnpAdEntAddr"))
if mibBuilder.loadTexts: clnpAddrEntry.setDescription("The addressing information for one of this\nentity's CLNP addresses.")
clnpAdEntAddr = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 1), ClnpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpAdEntAddr.setDescription("The CLNP address to which this entry's addressing\ninformation pertains.")
clnpAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpAdEntIfIndex.setDescription("The index value which uniquely identifies the\ninterface to which this entry is applicable.  The\ninterface identified by a particular value of this\nindex is the same interface as identified by the\nsame value of ifIndex.")
clnpAdEntReasmMaxSize = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 21, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpAdEntReasmMaxSize.setDescription("The size of the largest CLNP PDU which this\nentity can re-assemble from incoming CLNP\nsegmented PDUs received on this interface.")
clnpRoutingTable = MibTable((1, 3, 6, 1, 3, 1, 1, 22))
if mibBuilder.loadTexts: clnpRoutingTable.setDescription("This entity's CLNP routing table.")
clnpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 22, 1)).setIndexNames((0, "CLNS-MIB", "clnpRouteDest"))
if mibBuilder.loadTexts: clnpRouteEntry.setDescription("A route to a particular destination.")
clnpRouteDest = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 1), ClnpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteDest.setDescription("The destination CLNP address of this route.")
clnpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteIfIndex.setDescription("The index value which uniquely identifies the\nlocal interface through which the next hop of this\nroute should be reached.  The interface identified\nby a particular value of this index is the same as\nidentified by the same value of ifIndex.")
clnpRouteMetric1 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteMetric1.setDescription("The primary routing metric for this route.  The\nsemantics of this metric are determined by the\nrouting-protocol specified in the route's\nclnpRouteProto value.  If this metric is not used,\nits value should be set to -1.")
clnpRouteMetric2 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteMetric2.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the\nrouting-protocol specified in the route's\nclnpRouteProto value.  If this metric is not used,\nits value should be set to -1.")
clnpRouteMetric3 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteMetric3.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the\nrouting-protocol specified in the route's\nclnpRouteProto value.  If this metric is not used,\nits value should be set to -1.")
clnpRouteMetric4 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteMetric4.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the\nrouting-protocol specified in the route's\nclnpRouteProto value.  If this metric is not used,\nits value should be set to -1.")
clnpRouteNextHop = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 7), ClnpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteNextHop.setDescription("The CLNP address of the next hop of this route.")
clnpRouteType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("direct", 3), ("remote", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteType.setDescription("The type of route.\n\nSetting this object to the value invalid(2) has\nthe effect of invaliding the corresponding entry\nin the clnpRoutingTable.  That is, it effectively\ndissasociates the destination identified with said\nentry from the route identified with said entry.\nIt is an implementation-specific matter as to\nwhether the agent removes an invalidated entry\nfrom the table.  Accordingly, management stations\nmust be prepared to receive tabular information\nfrom agents that corresponds to entries not\ncurrently in use.  Proper interpretation of such\nentries requires examination of the relevant\nclnpRouteType object.")
clnpRouteProto = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(14,11,1,9,3,12,13,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("local", 2), ("netmgmt", 3), ("is-is", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpRouteProto.setDescription("The routing mechanism via which this route was\nlearned.  Inclusion of values for gateway routing\nprotocols is not intended to imply that hosts\nshould support those protocols.")
clnpRouteAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteAge.setDescription("The number of seconds since this route was last\nupdated or otherwise determined to be correct.\nNote that no semantics of `too old' can be implied\nexcept through knowledge of the routing protocol\nby which the route was learned.")
clnpRouteMetric5 = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpRouteMetric5.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the\nrouting-protocol specified in the route's\nclnpRouteProto value.  If this metric is not used,\nits value should be set to -1.")
clnpRouteInfo = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 22, 1, 12), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpRouteInfo.setDescription("A reference to MIB definitions specific to the\nparticular routing protocol which is responsible\nfor this route, as determined by the value\nspecified in the route's clnpRouteProto value.  If\nthis information is not present, its value should\nbe set to the OBJECT IDENTIFIER { 0 0 }, which is\na syntatically valid object identifier, and any\nconformant implementation of ASN.1 and BER must be\nable to generate and recognize this value.")
clnpNetToMediaTable = MibTable((1, 3, 6, 1, 3, 1, 1, 23))
if mibBuilder.loadTexts: clnpNetToMediaTable.setDescription("The CLNP Address Translation table used for\nmapping from CLNP addresses to physical\naddresses.")
clnpNetToMediaEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 23, 1)).setIndexNames((0, "CLNS-MIB", "clnpNetToMediaIfIndex"), (0, "CLNS-MIB", "clnpNetToMediaNetAddress"))
if mibBuilder.loadTexts: clnpNetToMediaEntry.setDescription("Each entry contains one CLNP address to\n`physical' address equivalence.")
clnpNetToMediaIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaIfIndex.setDescription("The interface on which this entry's equivalence\nis effective.  The interface identified by a\nparticular value of this index is the same\ninterface as identified by the same value of\nifIndex.")
clnpNetToMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaPhysAddress.setDescription("The media-dependent `physical' address.")
clnpNetToMediaNetAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 3), ClnpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaNetAddress.setDescription("The CLNP address corresponding to the media-\ndependent `physical' address.")
clnpNetToMediaType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaType.setDescription("The type of mapping.\n\nSetting this object to the value invalid(2) has\nthe effect of invalidating the corresponding entry\nin the clnpNetToMediaTable.  That is, it\neffectively dissassociates the interface\nidentified with said entry from the mapping\nidentified with said entry.  It is an\nimplementation-specific matter as to whether the\nagent removes an invalidated entry from the table.\nAccordingly, management stations must be prepared\nto receive tabular information from agents that\ncorresponds to entries not currently in use.\nProper interpretation of such entries requires\nexamination of the relevant clnpNetToMediaType\nobject.")
clnpNetToMediaAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaAge.setDescription("The number of seconds since this entry was last\nupdated or otherwise determined to be correct.\nNote that no semantics of `too old' can be implied\nexcept through knowledge of the type of entry.")
clnpNetToMediaHoldTime = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 23, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpNetToMediaHoldTime.setDescription("The time in seconds this entry will be valid.\nStatic entries should always report this field as\n-1.")
clnpMediaToNetTable = MibTable((1, 3, 6, 1, 3, 1, 1, 24))
if mibBuilder.loadTexts: clnpMediaToNetTable.setDescription("The CLNP Address Translation table used for\nmapping from physical addresses to CLNP\naddresses.")
clnpMediaToNetEntry = MibTableRow((1, 3, 6, 1, 3, 1, 1, 24, 1)).setIndexNames((0, "CLNS-MIB", "clnpMediaToNetIfIndex"), (0, "CLNS-MIB", "clnpMediaToNetPhysAddress"))
if mibBuilder.loadTexts: clnpMediaToNetEntry.setDescription("Each entry contains on ClnpAddress to `physical'\naddress equivalence.")
clnpMediaToNetIfIndex = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetIfIndex.setDescription("The interface on which this entry's equivalence\nis effective.  The interface identified by a\nparticular value of this index is the same\ninterface as identified by the same value of\nifIndex.")
clnpMediaToNetAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 2), ClnpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetAddress.setDescription("The ClnpAddress corresponding to the media-\ndependent `physical' address.")
clnpMediaToNetPhysAddress = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetPhysAddress.setDescription("The media-dependent `physical' address.")
clnpMediaToNetType = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,3,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetType.setDescription("The type of mapping.\n\nSetting this object to the value invalid(2) has\nthe effect of invalidating the corresponding entry\nin the clnpMediaToNetTable.  That is, it\neffectively dissassociates the interface\nidentified with said entry from the mapping\nidentified with said entry.  It is an\nimplementation-specific matter as to whether the\nagent removes an invalidated entry from the table.\nAccordingly, management stations must be prepared\nto receive tabular information from agents that\ncorresponds to entries not currently in use.\nProper interpretation of such entries requires\nexamination of the relevant clnpMediaToNetType\nobject.")
clnpMediaToNetAge = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetAge.setDescription("The number of seconds since this entry was last\nupdated or otherwise determined to be correct.\nNote that no semantics of `too old' can be implied\nexcept through knowledge of the type of entry.")
clnpMediaToNetHoldTime = MibTableColumn((1, 3, 6, 1, 3, 1, 1, 24, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clnpMediaToNetHoldTime.setDescription("The time in seconds this entry will be valid.\nStatic entries should always report this field as\n-1.")
clnpInOpts = MibScalar((1, 3, 6, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInOpts.setDescription("The number of CLNP PDU segments that have been\ninput with options at this entity.")
clnpOutOpts = MibScalar((1, 3, 6, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutOpts.setDescription("The number of CLNP PDU segments that have been\ngenerated with options by this entity.")
clnpRoutingDiscards = MibScalar((1, 3, 6, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpRoutingDiscards.setDescription("The number of routing entries which were chosen\nto be discarded even though they are valid.  One\npossible reason for discarding such an entry could\nbe to free-up buffer space for other routing\nentries.")
error = MibIdentifier((1, 3, 6, 1, 3, 1, 2))
clnpInErrors = MibScalar((1, 3, 6, 1, 3, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrors.setDescription("The number of CLNP Error PDUs received by this\nentity.")
clnpOutErrors = MibScalar((1, 3, 6, 1, 3, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrors.setDescription("The number of CLNP Error PDUs sent by this\nentity.")
clnpInErrUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnspecs.setDescription("The number of unspecified CLNP Error PDUs\nreceived by this entity.")
clnpInErrProcs = MibScalar((1, 3, 6, 1, 3, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrProcs.setDescription("The number of protocol procedure CLNP Error PDUs\nreceived by this entity.")
clnpInErrCksums = MibScalar((1, 3, 6, 1, 3, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrCksums.setDescription("The number of checksum CLNP Error PDUs received\nby this entity.")
clnpInErrCongests = MibScalar((1, 3, 6, 1, 3, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrCongests.setDescription("The number of congestion drop CLNP Error PDUs\nreceived by this entity.")
clnpInErrHdrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrHdrs.setDescription("The number of header syntax CLNP Error PDUs\nreceived by this entity.")
clnpInErrSegs = MibScalar((1, 3, 6, 1, 3, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrSegs.setDescription("The number of segmentation disallowed CLNP Error\nPDUs received by this entity.")
clnpInErrIncomps = MibScalar((1, 3, 6, 1, 3, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrIncomps.setDescription("The number of incomplete PDU CLNP Error PDUs\nreceived by this entity.")
clnpInErrDups = MibScalar((1, 3, 6, 1, 3, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrDups.setDescription("The number of duplicate option CLNP Error PDUs\nreceived by this entity.")
clnpInErrUnreachDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnreachDsts.setDescription("The number of unreachable destination CLNP Error\nPDUs received by this entity.")
clnpInErrUnknownDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnknownDsts.setDescription("The number of unknown destination CLNP Error PDUs\nreceived by this entity.")
clnpInErrSRUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrSRUnspecs.setDescription("The number of unspecified source route CLNP Error\nPDUs received by this entity.")
clnpInErrSRSyntaxes = MibScalar((1, 3, 6, 1, 3, 1, 2, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrSRSyntaxes.setDescription("The number of source route syntax CLNP Error PDUs\nreceived by this entity.")
clnpInErrSRUnkAddrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrSRUnkAddrs.setDescription("The number of source route unknown address CLNP\nError PDUs received by this entity.")
clnpInErrSRBadPaths = MibScalar((1, 3, 6, 1, 3, 1, 2, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrSRBadPaths.setDescription("The number of source route bad path CLNP Error\nPDUs received by this entity.")
clnpInErrHops = MibScalar((1, 3, 6, 1, 3, 1, 2, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrHops.setDescription("The number of hop count exceeded CLNP Error PDUs\nreceived by this entity.")
clnpInErrHopReassms = MibScalar((1, 3, 6, 1, 3, 1, 2, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrHopReassms.setDescription("The number of hop count exceeded while\nreassembling CLNP Error PDUs received by this\nentity.")
clnpInErrUnsOptions = MibScalar((1, 3, 6, 1, 3, 1, 2, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnsOptions.setDescription("The number of unsupported option CLNP Error PDUs\nreceived by this entity.")
clnpInErrUnsVersions = MibScalar((1, 3, 6, 1, 3, 1, 2, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnsVersions.setDescription("The number of version mismatch CLNP Error PDUs\nreceived by this entity.")
clnpInErrUnsSecurities = MibScalar((1, 3, 6, 1, 3, 1, 2, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnsSecurities.setDescription("The number of unsupported security option CLNP\nError PDUs received by this entity.")
clnpInErrUnsSRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnsSRs.setDescription("The number of unsupported source route option\nCLNP Error PDUs received by this entity.")
clnpInErrUnsRRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrUnsRRs.setDescription("The number of unsupported record route option\nCLNP Error PDUs received by this entity.")
clnpInErrInterferences = MibScalar((1, 3, 6, 1, 3, 1, 2, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpInErrInterferences.setDescription("The number of reassembly interference CLNP Error\nPDUs received by this entity.")
clnpOutErrUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnspecs.setDescription("The number of unspecified CLNP Error PDUs sent by\nthis entity.")
clnpOutErrProcs = MibScalar((1, 3, 6, 1, 3, 1, 2, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrProcs.setDescription("The number of protocol procedure CLNP Error PDUs\nsent by this entity.")
clnpOutErrCksums = MibScalar((1, 3, 6, 1, 3, 1, 2, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrCksums.setDescription("The number of checksum CLNP Error PDUs sent by\nthis entity.")
clnpOutErrCongests = MibScalar((1, 3, 6, 1, 3, 1, 2, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrCongests.setDescription("The number of congestion drop CLNP Error PDUs\nsent by this entity.")
clnpOutErrHdrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrHdrs.setDescription("The number of header syntax CLNP Error PDUs sent\nby this entity.")
clnpOutErrSegs = MibScalar((1, 3, 6, 1, 3, 1, 2, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrSegs.setDescription("The number of segmentation disallowed CLNP Error\nPDUs sent by this entity.")
clnpOutErrIncomps = MibScalar((1, 3, 6, 1, 3, 1, 2, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrIncomps.setDescription("The number of incomplete PDU CLNP Error PDUs sent\nby this entity.")
clnpOutErrDups = MibScalar((1, 3, 6, 1, 3, 1, 2, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrDups.setDescription("The number of duplicate option CLNP Error PDUs\nsent by this entity.")
clnpOutErrUnreachDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnreachDsts.setDescription("The number of unreachable destination CLNP Error\nPDUs sent by this entity.")
clnpOutErrUnknownDsts = MibScalar((1, 3, 6, 1, 3, 1, 2, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnknownDsts.setDescription("The number of unknown destination CLNP Error PDUs\nsent by this entity.")
clnpOutErrSRUnspecs = MibScalar((1, 3, 6, 1, 3, 1, 2, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrSRUnspecs.setDescription("The number of unspecified source route CLNP Error\nPDUs sent by this entity.")
clnpOutErrSRSyntaxes = MibScalar((1, 3, 6, 1, 3, 1, 2, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrSRSyntaxes.setDescription("The number of source route syntax CLNP Error PDUs\nsent by this entity.")
clnpOutErrSRUnkAddrs = MibScalar((1, 3, 6, 1, 3, 1, 2, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrSRUnkAddrs.setDescription("The number of source route unknown address CLNP\nError PDUs sent by this entity.")
clnpOutErrSRBadPaths = MibScalar((1, 3, 6, 1, 3, 1, 2, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrSRBadPaths.setDescription("The number of source route bad path CLNP Error\nPDUs sent by this entity.")
clnpOutErrHops = MibScalar((1, 3, 6, 1, 3, 1, 2, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrHops.setDescription("The number of hop count exceeded CLNP Error PDUs\nsent by this entity.")
clnpOutErrHopReassms = MibScalar((1, 3, 6, 1, 3, 1, 2, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrHopReassms.setDescription("The number of hop count exceeded while\nreassembling CLNP Error PDUs sent by this entity.")
clnpOutErrUnsOptions = MibScalar((1, 3, 6, 1, 3, 1, 2, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnsOptions.setDescription("The number of unsupported option CLNP Error PDUs\nsent by this entity.")
clnpOutErrUnsVersions = MibScalar((1, 3, 6, 1, 3, 1, 2, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnsVersions.setDescription("The number of version mismatch CLNP Error PDUs\nsent by this entity.")
clnpOutErrUnsSecurities = MibScalar((1, 3, 6, 1, 3, 1, 2, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnsSecurities.setDescription("The number of unsupported security option CLNP\nError PDUs sent by this entity.")
clnpOutErrUnsSRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnsSRs.setDescription("The number of unsupported source route option\nCLNP Error PDUs sent by this entity.")
clnpOutErrUnsRRs = MibScalar((1, 3, 6, 1, 3, 1, 2, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrUnsRRs.setDescription("The number of unsupported record route option\nCLNP Error PDUs sent by this entity.")
clnpOutErrInterferences = MibScalar((1, 3, 6, 1, 3, 1, 2, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clnpOutErrInterferences.setDescription("The number of reassembly interference CLNP Error\nPDUs sent by this entity.")
echo = MibIdentifier((1, 3, 6, 1, 3, 1, 3))
es_is = MibIdentifier((1, 3, 6, 1, 3, 1, 4)).setLabel("es-is")
esisESHins = MibScalar((1, 3, 6, 1, 3, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisESHins.setDescription("The number of ESH PDUs received by this entity.")
esisESHouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisESHouts.setDescription("The number of ESH PDUs sent by this entity.")
esisISHins = MibScalar((1, 3, 6, 1, 3, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisISHins.setDescription("The number of ISH PDUs received by this entity.")
esisISHouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisISHouts.setDescription("The number of ISH PDUs sent by this entity.")
esisRDUins = MibScalar((1, 3, 6, 1, 3, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisRDUins.setDescription("The number of RDU PDUs received by this entity.")
esisRDUouts = MibScalar((1, 3, 6, 1, 3, 1, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esisRDUouts.setDescription("The number of RDU PDUs sent by this entity.")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("CLNS-MIB", ClnpAddress=ClnpAddress)

# Objects
mibBuilder.exportSymbols("CLNS-MIB", clns=clns, clnp=clnp, clnpForwarding=clnpForwarding, clnpDefaultLifeTime=clnpDefaultLifeTime, clnpInReceives=clnpInReceives, clnpInHdrErrors=clnpInHdrErrors, clnpInAddrErrors=clnpInAddrErrors, clnpForwPDUs=clnpForwPDUs, clnpInUnknownNLPs=clnpInUnknownNLPs, clnpInUnknownULPs=clnpInUnknownULPs, clnpInDiscards=clnpInDiscards, clnpInDelivers=clnpInDelivers, clnpOutRequests=clnpOutRequests, clnpOutDiscards=clnpOutDiscards, clnpOutNoRoutes=clnpOutNoRoutes, clnpReasmTimeout=clnpReasmTimeout, clnpReasmReqds=clnpReasmReqds, clnpReasmOKs=clnpReasmOKs, clnpReasmFails=clnpReasmFails, clnpSegOKs=clnpSegOKs, clnpSegFails=clnpSegFails, clnpSegCreates=clnpSegCreates, clnpAddrTable=clnpAddrTable, clnpAddrEntry=clnpAddrEntry, clnpAdEntAddr=clnpAdEntAddr, clnpAdEntIfIndex=clnpAdEntIfIndex, clnpAdEntReasmMaxSize=clnpAdEntReasmMaxSize, clnpRoutingTable=clnpRoutingTable, clnpRouteEntry=clnpRouteEntry, clnpRouteDest=clnpRouteDest, clnpRouteIfIndex=clnpRouteIfIndex, clnpRouteMetric1=clnpRouteMetric1, clnpRouteMetric2=clnpRouteMetric2, clnpRouteMetric3=clnpRouteMetric3, clnpRouteMetric4=clnpRouteMetric4, clnpRouteNextHop=clnpRouteNextHop, clnpRouteType=clnpRouteType, clnpRouteProto=clnpRouteProto, clnpRouteAge=clnpRouteAge, clnpRouteMetric5=clnpRouteMetric5, clnpRouteInfo=clnpRouteInfo, clnpNetToMediaTable=clnpNetToMediaTable, clnpNetToMediaEntry=clnpNetToMediaEntry, clnpNetToMediaIfIndex=clnpNetToMediaIfIndex, clnpNetToMediaPhysAddress=clnpNetToMediaPhysAddress, clnpNetToMediaNetAddress=clnpNetToMediaNetAddress, clnpNetToMediaType=clnpNetToMediaType, clnpNetToMediaAge=clnpNetToMediaAge, clnpNetToMediaHoldTime=clnpNetToMediaHoldTime, clnpMediaToNetTable=clnpMediaToNetTable, clnpMediaToNetEntry=clnpMediaToNetEntry, clnpMediaToNetIfIndex=clnpMediaToNetIfIndex, clnpMediaToNetAddress=clnpMediaToNetAddress, clnpMediaToNetPhysAddress=clnpMediaToNetPhysAddress, clnpMediaToNetType=clnpMediaToNetType, clnpMediaToNetAge=clnpMediaToNetAge, clnpMediaToNetHoldTime=clnpMediaToNetHoldTime, clnpInOpts=clnpInOpts, clnpOutOpts=clnpOutOpts, clnpRoutingDiscards=clnpRoutingDiscards, error=error, clnpInErrors=clnpInErrors, clnpOutErrors=clnpOutErrors, clnpInErrUnspecs=clnpInErrUnspecs, clnpInErrProcs=clnpInErrProcs, clnpInErrCksums=clnpInErrCksums, clnpInErrCongests=clnpInErrCongests, clnpInErrHdrs=clnpInErrHdrs, clnpInErrSegs=clnpInErrSegs, clnpInErrIncomps=clnpInErrIncomps, clnpInErrDups=clnpInErrDups, clnpInErrUnreachDsts=clnpInErrUnreachDsts, clnpInErrUnknownDsts=clnpInErrUnknownDsts, clnpInErrSRUnspecs=clnpInErrSRUnspecs, clnpInErrSRSyntaxes=clnpInErrSRSyntaxes, clnpInErrSRUnkAddrs=clnpInErrSRUnkAddrs, clnpInErrSRBadPaths=clnpInErrSRBadPaths, clnpInErrHops=clnpInErrHops, clnpInErrHopReassms=clnpInErrHopReassms, clnpInErrUnsOptions=clnpInErrUnsOptions, clnpInErrUnsVersions=clnpInErrUnsVersions, clnpInErrUnsSecurities=clnpInErrUnsSecurities, clnpInErrUnsSRs=clnpInErrUnsSRs, clnpInErrUnsRRs=clnpInErrUnsRRs, clnpInErrInterferences=clnpInErrInterferences, clnpOutErrUnspecs=clnpOutErrUnspecs, clnpOutErrProcs=clnpOutErrProcs, clnpOutErrCksums=clnpOutErrCksums, clnpOutErrCongests=clnpOutErrCongests, clnpOutErrHdrs=clnpOutErrHdrs, clnpOutErrSegs=clnpOutErrSegs, clnpOutErrIncomps=clnpOutErrIncomps, clnpOutErrDups=clnpOutErrDups, clnpOutErrUnreachDsts=clnpOutErrUnreachDsts, clnpOutErrUnknownDsts=clnpOutErrUnknownDsts, clnpOutErrSRUnspecs=clnpOutErrSRUnspecs, clnpOutErrSRSyntaxes=clnpOutErrSRSyntaxes, clnpOutErrSRUnkAddrs=clnpOutErrSRUnkAddrs, clnpOutErrSRBadPaths=clnpOutErrSRBadPaths, clnpOutErrHops=clnpOutErrHops, clnpOutErrHopReassms=clnpOutErrHopReassms, clnpOutErrUnsOptions=clnpOutErrUnsOptions, clnpOutErrUnsVersions=clnpOutErrUnsVersions, clnpOutErrUnsSecurities=clnpOutErrUnsSecurities, clnpOutErrUnsSRs=clnpOutErrUnsSRs, clnpOutErrUnsRRs=clnpOutErrUnsRRs, clnpOutErrInterferences=clnpOutErrInterferences, echo=echo, es_is=es_is, esisESHins=esisESHins, esisESHouts=esisESHouts, esisISHins=esisISHins, esisISHouts=esisISHouts, esisRDUins=esisRDUins, esisRDUouts=esisRDUouts)

