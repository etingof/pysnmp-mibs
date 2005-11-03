# PySNMP SMI module. Autogenerated from smidump -f python ETHER-CHIPSET-MIB
# by libsmi2pysnmp-0.0.5-alpha at Thu Nov  3 19:25:58 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( dot3, ) = mibBuilder.importSymbols("EtherLike-MIB", "dot3")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "mib-2")

# Objects

dot3ChipSets = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8))
dot3ChipSetAMD = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1))
dot3ChipSetAMD7990 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1))
dot3ChipSetAMD79900 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2))
dot3ChipSetAMD79C940 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 3))
dot3ChipSetAMD79C90 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 4))
dot3ChipSetAMD79C960 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 5))
dot3ChipSetAMD79C961 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 6))
dot3ChipSetAMD79C961A = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 7))
dot3ChipSetAMD79C965 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 8))
dot3ChipSetAMD79C970 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 9))
dot3ChipSetAMD79C970A = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 10))
dot3ChipSetAMD79C971 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 11))
dot3ChipSetAMD79C972 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 12))
dot3ChipSetIntel = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2))
dot3ChipSetIntel82586 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 1))
dot3ChipSetIntel82596 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 2))
dot3ChipSetIntel82595 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 3))
dot3ChipSetIntel82557 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 4))
dot3ChipSetIntel82558 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 5))
dot3ChipSetSeeq = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3))
dot3ChipSetSeeq8003 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 1))
dot3ChipSetSeeq80C03 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 2))
dot3ChipSetSeeq84C30 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 3))
dot3ChipSetSeeq8431 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 4))
dot3ChipSetSeeq80C300 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 5))
dot3ChipSetSeeq84C300 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 6))
dot3ChipSetSeeq84301 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 7))
dot3ChipSetSeeq84302 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 8))
dot3ChipSetSeeq8100 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 9))
dot3ChipSetNational = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4))
dot3ChipSetNational8390 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 1))
dot3ChipSetNationalSonic = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 2))
dot3ChipSetNational83901 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 3))
dot3ChipSetNational83902 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 4))
dot3ChipSetNational83905 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 5))
dot3ChipSetNational83907 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 6))
dot3ChipSetNational83916 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 7))
dot3ChipSetNational83934 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 8))
dot3ChipSetNational83936 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 9))
dot3ChipSetFujitsu = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5))
dot3ChipSetFujitsu86950 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 1))
dot3ChipSetFujitsu86960 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 2))
dot3ChipSetFujitsu86964 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 3))
dot3ChipSetFujitsu86965A = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 4))
dot3ChipSetFujitsu86965B = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 5))
dot3ChipSetDigital = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6))
dot3ChipSetDigitalDC21040 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 1))
dot3ChipSetDigital21041 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 2))
dot3ChipSetDigital21140 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 3))
dot3ChipSetDigital21143 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 4))
dot3ChipSetDigital21340 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 5))
dot3ChipSetDigital21440 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 6))
dot3ChipSetDigital21540 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 7))
dot3ChipSetTI = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7))
dot3ChipSetTIE100 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 1))
dot3ChipSetTIE110 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 2))
dot3ChipSetTIX3100 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 3))
dot3ChipSetTIX3150 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 4))
dot3ChipSetTIX3270 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 5))
dot3ChipSetToshiba = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 8))
dot3ChipSetToshibaTC35815F = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 8, 1))
dot3ChipSetLucent = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 9))
dot3ChipSetLucentATT1MX10 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 1))
dot3ChipSetLucentLUC3M08 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 2))
dot3ChipSetGalileo = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10))
dot3ChipSetGalileoGT48001 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 1))
dot3ChipSetGalileoGT48002 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 2))
dot3ChipSetGalileoGT48004 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 3))
dot3ChipSetGalileoGT48207 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 4))
dot3ChipSetGalileoGT48208 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 5))
dot3ChipSetGalileoGT48212 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 6))
dot3ChipSetJato = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 11))
dot3ChipSetJatoJT1001 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 11, 1))
dot3ChipSetXaQti = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 12))
dot3ChipSetXaQtiXQ11800FP = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 1))
dot3ChipSetXaQtiXQ18110FP = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 2))
etherChipsetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 70)).setRevisions(("1999-08-24 04:00",))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("ETHER-CHIPSET-MIB", PYSNMP_MODULE_ID=etherChipsetMIB)

# Objects
mibBuilder.exportSymbols("ETHER-CHIPSET-MIB", dot3ChipSets=dot3ChipSets, dot3ChipSetAMD=dot3ChipSetAMD, dot3ChipSetAMD7990=dot3ChipSetAMD7990, dot3ChipSetAMD79900=dot3ChipSetAMD79900, dot3ChipSetAMD79C940=dot3ChipSetAMD79C940, dot3ChipSetAMD79C90=dot3ChipSetAMD79C90, dot3ChipSetAMD79C960=dot3ChipSetAMD79C960, dot3ChipSetAMD79C961=dot3ChipSetAMD79C961, dot3ChipSetAMD79C961A=dot3ChipSetAMD79C961A, dot3ChipSetAMD79C965=dot3ChipSetAMD79C965, dot3ChipSetAMD79C970=dot3ChipSetAMD79C970, dot3ChipSetAMD79C970A=dot3ChipSetAMD79C970A, dot3ChipSetAMD79C971=dot3ChipSetAMD79C971, dot3ChipSetAMD79C972=dot3ChipSetAMD79C972, dot3ChipSetIntel=dot3ChipSetIntel, dot3ChipSetIntel82586=dot3ChipSetIntel82586, dot3ChipSetIntel82596=dot3ChipSetIntel82596, dot3ChipSetIntel82595=dot3ChipSetIntel82595, dot3ChipSetIntel82557=dot3ChipSetIntel82557, dot3ChipSetIntel82558=dot3ChipSetIntel82558, dot3ChipSetSeeq=dot3ChipSetSeeq, dot3ChipSetSeeq8003=dot3ChipSetSeeq8003, dot3ChipSetSeeq80C03=dot3ChipSetSeeq80C03, dot3ChipSetSeeq84C30=dot3ChipSetSeeq84C30, dot3ChipSetSeeq8431=dot3ChipSetSeeq8431, dot3ChipSetSeeq80C300=dot3ChipSetSeeq80C300, dot3ChipSetSeeq84C300=dot3ChipSetSeeq84C300, dot3ChipSetSeeq84301=dot3ChipSetSeeq84301, dot3ChipSetSeeq84302=dot3ChipSetSeeq84302, dot3ChipSetSeeq8100=dot3ChipSetSeeq8100, dot3ChipSetNational=dot3ChipSetNational, dot3ChipSetNational8390=dot3ChipSetNational8390, dot3ChipSetNationalSonic=dot3ChipSetNationalSonic, dot3ChipSetNational83901=dot3ChipSetNational83901, dot3ChipSetNational83902=dot3ChipSetNational83902, dot3ChipSetNational83905=dot3ChipSetNational83905, dot3ChipSetNational83907=dot3ChipSetNational83907, dot3ChipSetNational83916=dot3ChipSetNational83916, dot3ChipSetNational83934=dot3ChipSetNational83934, dot3ChipSetNational83936=dot3ChipSetNational83936, dot3ChipSetFujitsu=dot3ChipSetFujitsu, dot3ChipSetFujitsu86950=dot3ChipSetFujitsu86950, dot3ChipSetFujitsu86960=dot3ChipSetFujitsu86960, dot3ChipSetFujitsu86964=dot3ChipSetFujitsu86964, dot3ChipSetFujitsu86965A=dot3ChipSetFujitsu86965A, dot3ChipSetFujitsu86965B=dot3ChipSetFujitsu86965B, dot3ChipSetDigital=dot3ChipSetDigital, dot3ChipSetDigitalDC21040=dot3ChipSetDigitalDC21040, dot3ChipSetDigital21041=dot3ChipSetDigital21041, dot3ChipSetDigital21140=dot3ChipSetDigital21140, dot3ChipSetDigital21143=dot3ChipSetDigital21143, dot3ChipSetDigital21340=dot3ChipSetDigital21340, dot3ChipSetDigital21440=dot3ChipSetDigital21440, dot3ChipSetDigital21540=dot3ChipSetDigital21540, dot3ChipSetTI=dot3ChipSetTI, dot3ChipSetTIE100=dot3ChipSetTIE100, dot3ChipSetTIE110=dot3ChipSetTIE110, dot3ChipSetTIX3100=dot3ChipSetTIX3100, dot3ChipSetTIX3150=dot3ChipSetTIX3150, dot3ChipSetTIX3270=dot3ChipSetTIX3270, dot3ChipSetToshiba=dot3ChipSetToshiba, dot3ChipSetToshibaTC35815F=dot3ChipSetToshibaTC35815F, dot3ChipSetLucent=dot3ChipSetLucent, dot3ChipSetLucentATT1MX10=dot3ChipSetLucentATT1MX10, dot3ChipSetLucentLUC3M08=dot3ChipSetLucentLUC3M08, dot3ChipSetGalileo=dot3ChipSetGalileo, dot3ChipSetGalileoGT48001=dot3ChipSetGalileoGT48001, dot3ChipSetGalileoGT48002=dot3ChipSetGalileoGT48002, dot3ChipSetGalileoGT48004=dot3ChipSetGalileoGT48004, dot3ChipSetGalileoGT48207=dot3ChipSetGalileoGT48207, dot3ChipSetGalileoGT48208=dot3ChipSetGalileoGT48208, dot3ChipSetGalileoGT48212=dot3ChipSetGalileoGT48212, dot3ChipSetJato=dot3ChipSetJato, dot3ChipSetJatoJT1001=dot3ChipSetJatoJT1001, dot3ChipSetXaQti=dot3ChipSetXaQti, dot3ChipSetXaQtiXQ11800FP=dot3ChipSetXaQtiXQ11800FP, dot3ChipSetXaQtiXQ18110FP=dot3ChipSetXaQtiXQ18110FP, etherChipsetMIB=etherChipsetMIB)

