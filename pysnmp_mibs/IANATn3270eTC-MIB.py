#
# PySNMP MIB module IANATn3270eTC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IANATn3270eTC-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:28:56 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Counter32, ModuleIdentity, ObjectIdentity, Bits, experimental, Gauge32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Counter32", "ModuleIdentity", "ObjectIdentity", "Bits", "experimental", "Gauge32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaTn3270eTcMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 61)).setRevisions(("1998-07-27 00:00",))
if mibBuilder.loadTexts: ianaTn3270eTcMib.setOrganization('IANA')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setContactInfo('Internet Assigned Numbers Authority\n\n             Postal: USC/Information Sciences Institute\n                     4676 Admiralty Way, Marina del Rey, CA 90292\n\n             Tel:    +1  310 822 1511\n             E-Mail: iana@isi.edu')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setDescription('This module defines a set of textual conventions\n            for use by the TN3270E-MIB and the TN3270E-RT-MIB.\n\n            Any additions or changes to the contents of this\n            MIB module must first be discussed on the tn3270e\n            working group list at: tn3270e@list.nih.gov\n            and approved by one of the following TN3270E\n            working group contacts:\n\n                Ed Bailey (co-chair) - elbailey@us.ibm.com\n                Michael Boe (co-chair) - mboe@cisco.com\n                Ken White - kennethw@vnet.ibm.com\n                Robert Moore - remoore@us.ibm.com\n\n            The above list of contacts can be altered with\n            the approval of the two co-chairs.\n\n            The Textual Conventions defined within this MIB have\n            no security issues associated with them unless\n            explicitly stated in their corresponding\n            DESCRIPTION clause.')
class IANATn3270eAddrType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2),)

class IANATn3270eAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class IANATn3270eClientType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)
    namedValues = NamedValues(("none", 1), ("other", 2), ("ipv4", 3), ("ipv6", 4), ("domainName", 5), ("truncDomainName", 6), ("string", 7), ("certificate", 8), ("userId", 9), ("x509dn", 10),)

class IANATn3270Functions(Bits, TextualConvention):
    namedValues = NamedValues(("transmitBinary", 0), ("timemark", 1), ("endOfRecord", 2), ("terminalType", 3), ("tn3270Regime", 4), ("scsCtlCodes", 5), ("dataStreamCtl", 6), ("responses", 7), ("bindImage", 8), ("sysreq", 9),)

class IANATn3270ResourceType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("other", 1), ("terminal", 2), ("printer", 3), ("terminalOrPrinter", 4),)

class IANATn3270DeviceType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100,)
    namedValues = NamedValues(("ibm3278d2", 1), ("ibm3278d2E", 2), ("ibm3278d3", 3), ("ibm3278d3E", 4), ("ibm3278d4", 5), ("ibm3278d4E", 6), ("ibm3278d5", 7), ("ibm3278d5E", 8), ("ibmDynamic", 9), ("ibm3287d1", 10), ("unknown", 100),)

class IANATn3270eLogData(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,2048),)
mibBuilder.exportSymbols("IANATn3270eTC-MIB", IANATn3270eAddress=IANATn3270eAddress, IANATn3270Functions=IANATn3270Functions, IANATn3270ResourceType=IANATn3270ResourceType, IANATn3270eLogData=IANATn3270eLogData, ianaTn3270eTcMib=ianaTn3270eTcMib, IANATn3270eAddrType=IANATn3270eAddrType, IANATn3270eClientType=IANATn3270eClientType, IANATn3270DeviceType=IANATn3270DeviceType, PYSNMP_MODULE_ID=ianaTn3270eTcMib)
