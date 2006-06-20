# PySNMP SMI module. Autogenerated from smidump -f python TOKENRING-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 21:10:22 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( MacAddress, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeStamp")

# Objects

dot5 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 9)).setRevisions(("1994-10-23 11:50",))
dot5Table = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 1))
dot5Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 1, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5IfIndex"))
dot5IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
dot5Commands = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,4,)).subtype(namedValues=namedval.NamedValues(("noop", 1), ("open", 2), ("reset", 3), ("close", 4), ))).setMaxAccess("readwrite")
dot5RingStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 262143))).setMaxAccess("readonly")
dot5RingState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,1,3,5,2,4,)).subtype(namedValues=namedval.NamedValues(("opened", 1), ("closed", 2), ("opening", 3), ("closing", 4), ("openFailure", 5), ("ringFailure", 6), ))).setMaxAccess("readonly")
dot5RingOpenStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,6,3,9,8,10,1,2,4,11,7,)).subtype(namedValues=namedval.NamedValues(("noOpen", 1), ("removeReceived", 10), ("open", 11), ("badParam", 2), ("lobeFailed", 3), ("signalLoss", 4), ("insertionTimeout", 5), ("ringFailed", 6), ("beaconing", 7), ("duplicateMAC", 8), ("requestFailed", 9), ))).setMaxAccess("readonly")
dot5RingSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("oneMegabit", 2), ("fourMegabit", 3), ("sixteenMegabit", 4), ))).setMaxAccess("readwrite")
dot5UpStream = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
dot5ActMonParticipate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readwrite")
dot5Functional = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 9), MacAddress()).setMaxAccess("readwrite")
dot5LastBeaconSent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
dot5StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 2))
dot5StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 2, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5StatsIfIndex"))
dot5StatsIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
dot5StatsLineErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 2), Counter32()).setMaxAccess("readonly")
dot5StatsBurstErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 3), Counter32()).setMaxAccess("readonly")
dot5StatsACErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 4), Counter32()).setMaxAccess("readonly")
dot5StatsAbortTransErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 5), Counter32()).setMaxAccess("readonly")
dot5StatsInternalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 6), Counter32()).setMaxAccess("readonly")
dot5StatsLostFrameErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 7), Counter32()).setMaxAccess("readonly")
dot5StatsReceiveCongestions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 8), Counter32()).setMaxAccess("readonly")
dot5StatsFrameCopiedErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 9), Counter32()).setMaxAccess("readonly")
dot5StatsTokenErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 10), Counter32()).setMaxAccess("readonly")
dot5StatsSoftErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 11), Counter32()).setMaxAccess("readonly")
dot5StatsHardErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 12), Counter32()).setMaxAccess("readonly")
dot5StatsSignalLoss = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 13), Counter32()).setMaxAccess("readonly")
dot5StatsTransmitBeacons = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 14), Counter32()).setMaxAccess("readonly")
dot5StatsRecoverys = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 15), Counter32()).setMaxAccess("readonly")
dot5StatsLobeWires = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 16), Counter32()).setMaxAccess("readonly")
dot5StatsRemoves = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 17), Counter32()).setMaxAccess("readonly")
dot5StatsSingles = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 18), Counter32()).setMaxAccess("readonly")
dot5StatsFreqErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 19), Counter32()).setMaxAccess("readonly")
dot5Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3))
dot5TestInsertFunc = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3, 1))
dot5TestFullDuplexLoopBack = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3, 2))
dot5ChipSets = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4))
dot5ChipSetIBM16 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 1))
dot5ChipSetTItms380 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 2))
dot5ChipSetTItms380c16 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 3))
dot5TimerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 5))
dot5TimerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 5, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5TimerIfIndex"))
dot5TimerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 1), Integer32()).setMaxAccess("readonly")
dot5TimerReturnRepeat = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 2), Integer32()).setMaxAccess("readonly")
dot5TimerHolding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 3), Integer32()).setMaxAccess("readonly")
dot5TimerQueuePDU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 4), Integer32()).setMaxAccess("readonly")
dot5TimerValidTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 5), Integer32()).setMaxAccess("readonly")
dot5TimerNoToken = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 6), Integer32()).setMaxAccess("readonly")
dot5TimerActiveMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 7), Integer32()).setMaxAccess("readonly")
dot5TimerStandbyMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 8), Integer32()).setMaxAccess("readonly")
dot5TimerErrorReport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 9), Integer32()).setMaxAccess("readonly")
dot5TimerBeaconTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 10), Integer32()).setMaxAccess("readonly")
dot5TimerBeaconReceive = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 11), Integer32()).setMaxAccess("readonly")
dot5Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6))
dot5Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6, 1))
dot5Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6, 2))

# Augmentions

# Groups

dot5StateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 1)).setObjects(("TOKENRING-MIB", "dot5RingOpenStatus"), ("TOKENRING-MIB", "dot5ActMonParticipate"), ("TOKENRING-MIB", "dot5Functional"), ("TOKENRING-MIB", "dot5Commands"), ("TOKENRING-MIB", "dot5LastBeaconSent"), ("TOKENRING-MIB", "dot5RingSpeed"), ("TOKENRING-MIB", "dot5RingState"), ("TOKENRING-MIB", "dot5RingStatus"), ("TOKENRING-MIB", "dot5UpStream"), )
dot5StatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 2)).setObjects(("TOKENRING-MIB", "dot5StatsRecoverys"), ("TOKENRING-MIB", "dot5StatsHardErrors"), ("TOKENRING-MIB", "dot5StatsACErrors"), ("TOKENRING-MIB", "dot5StatsRemoves"), ("TOKENRING-MIB", "dot5StatsFrameCopiedErrors"), ("TOKENRING-MIB", "dot5StatsSoftErrors"), ("TOKENRING-MIB", "dot5StatsBurstErrors"), ("TOKENRING-MIB", "dot5StatsTokenErrors"), ("TOKENRING-MIB", "dot5StatsLineErrors"), ("TOKENRING-MIB", "dot5StatsSignalLoss"), ("TOKENRING-MIB", "dot5StatsSingles"), ("TOKENRING-MIB", "dot5StatsLostFrameErrors"), ("TOKENRING-MIB", "dot5StatsTransmitBeacons"), ("TOKENRING-MIB", "dot5StatsFreqErrors"), ("TOKENRING-MIB", "dot5StatsLobeWires"), ("TOKENRING-MIB", "dot5StatsAbortTransErrors"), ("TOKENRING-MIB", "dot5StatsInternalErrors"), ("TOKENRING-MIB", "dot5StatsReceiveCongestions"), )

# Exports

# Module identity
mibBuilder.exportSymbols("TOKENRING-MIB", PYSNMP_MODULE_ID=dot5)

# Objects
mibBuilder.exportSymbols("TOKENRING-MIB", dot5=dot5, dot5Table=dot5Table, dot5Entry=dot5Entry, dot5IfIndex=dot5IfIndex, dot5Commands=dot5Commands, dot5RingStatus=dot5RingStatus, dot5RingState=dot5RingState, dot5RingOpenStatus=dot5RingOpenStatus, dot5RingSpeed=dot5RingSpeed, dot5UpStream=dot5UpStream, dot5ActMonParticipate=dot5ActMonParticipate, dot5Functional=dot5Functional, dot5LastBeaconSent=dot5LastBeaconSent, dot5StatsTable=dot5StatsTable, dot5StatsEntry=dot5StatsEntry, dot5StatsIfIndex=dot5StatsIfIndex, dot5StatsLineErrors=dot5StatsLineErrors, dot5StatsBurstErrors=dot5StatsBurstErrors, dot5StatsACErrors=dot5StatsACErrors, dot5StatsAbortTransErrors=dot5StatsAbortTransErrors, dot5StatsInternalErrors=dot5StatsInternalErrors, dot5StatsLostFrameErrors=dot5StatsLostFrameErrors, dot5StatsReceiveCongestions=dot5StatsReceiveCongestions, dot5StatsFrameCopiedErrors=dot5StatsFrameCopiedErrors, dot5StatsTokenErrors=dot5StatsTokenErrors, dot5StatsSoftErrors=dot5StatsSoftErrors, dot5StatsHardErrors=dot5StatsHardErrors, dot5StatsSignalLoss=dot5StatsSignalLoss, dot5StatsTransmitBeacons=dot5StatsTransmitBeacons, dot5StatsRecoverys=dot5StatsRecoverys, dot5StatsLobeWires=dot5StatsLobeWires, dot5StatsRemoves=dot5StatsRemoves, dot5StatsSingles=dot5StatsSingles, dot5StatsFreqErrors=dot5StatsFreqErrors, dot5Tests=dot5Tests, dot5TestInsertFunc=dot5TestInsertFunc, dot5TestFullDuplexLoopBack=dot5TestFullDuplexLoopBack, dot5ChipSets=dot5ChipSets, dot5ChipSetIBM16=dot5ChipSetIBM16, dot5ChipSetTItms380=dot5ChipSetTItms380, dot5ChipSetTItms380c16=dot5ChipSetTItms380c16, dot5TimerTable=dot5TimerTable, dot5TimerEntry=dot5TimerEntry, dot5TimerIfIndex=dot5TimerIfIndex, dot5TimerReturnRepeat=dot5TimerReturnRepeat, dot5TimerHolding=dot5TimerHolding, dot5TimerQueuePDU=dot5TimerQueuePDU, dot5TimerValidTransmit=dot5TimerValidTransmit, dot5TimerNoToken=dot5TimerNoToken, dot5TimerActiveMon=dot5TimerActiveMon, dot5TimerStandbyMon=dot5TimerStandbyMon, dot5TimerErrorReport=dot5TimerErrorReport, dot5TimerBeaconTransmit=dot5TimerBeaconTransmit, dot5TimerBeaconReceive=dot5TimerBeaconReceive, dot5Conformance=dot5Conformance, dot5Groups=dot5Groups, dot5Compliances=dot5Compliances)

# Groups
mibBuilder.exportSymbols("TOKENRING-MIB", dot5StateGroup=dot5StateGroup, dot5StatsGroup=dot5StatsGroup)
