# PySNMP SMI module. Autogenerated from smidump -f python IANA-CHARSET-MIB
# by libsmi2pysnmp-0.0.7-alpha at Tue Jun 20 23:32:57 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANACharset(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2022,2096,1013,2036,2087,53,2059,64,75,42,2037,2042,2005,4,5,6,7,12,13,1005,2078,1008,1009,55,1006,57,2019,18,2058,30,2071,97,14,39,71,2062,2024,28,54,50,1015,44,2025,2254,2255,2252,2253,2250,2251,2065,63,93,2028,2012,27,1007,43,2014,3,2056,51,2067,2104,2010,92,80,45,2009,37,2041,66,104,15,19,22,2074,2004,69,29,1011,24,2095,58,2097,2098,72,61,2093,81,1012,82,2099,2053,113,1001,2100,2026,98,2018,2047,2046,48,2045,1016,2073,116,103,2020,77,2103,2023,21,2085,2048,34,88,2057,2040,101,8,2039,31,1014,89,2088,2084,46,2075,25,2061,23,2258,2027,112,111,110,109,83,2259,2016,99,2105,2,1003,2072,2082,95,17,62,2069,117,90,56,16,2017,100,96,2089,2038,114,79,78,41,2043,2030,2083,105,2033,2032,2031,2256,115,2076,2034,2068,2007,2000,2054,59,70,2050,1019,2049,2086,2011,2051,2052,2064,3000,2094,2257,2102,10,2013,2008,9,94,38,1018,49,2001,2044,36,11,2006,87,32,2077,2101,2081,86,67,68,76,1,2092,2070,102,2055,2021,1010,2091,85,2063,84,1017,47,2060,74,2080,2079,60,1020,1002,106,33,40,20,2015,2090,2029,52,2003,2002,91,35,73,1000,65,2035,2066,26,)
    namedValues = namedval.NamedValues(("other", 1), ("csISOLatinGreek", 10), ("csUSDK", 100), ("csUnicode", 1000), ("csUCS4", 1001), ("csUnicodeASCII", 1002), ("csUnicodeLatin1", 1003), ("csUnicodeIBM1261", 1005), ("csUnicodeIBM1268", 1006), ("csUnicodeIBM1276", 1007), ("csUnicodeIBM1264", 1008), ("csUnicodeIBM1265", 1009), ("csDKUS", 101), ("csUnicode11", 1010), ("csSCSU", 1011), ("csUTF7", 1012), ("csUTF16BE", 1013), ("csUTF16LE", 1014), ("csUTF16", 1015), ("csCESU8", 1016), ("csUTF32", 1017), ("csUTF32BE", 1018), ("csUTF32LE", 1019), ("csKSC5636", 102), ("csBOCU1", 1020), ("csUnicode11UTF7", 103), ("csISO2022CN", 104), ("csISO2022CNEXT", 105), ("csUTF8", 106), ("csISO885913", 109), ("csISOLatinHebrew", 11), ("csISO885914", 110), ("csISO885915", 111), ("csISO885916", 112), ("csGBK", 113), ("csGB18030", 114), ("csOSDEBCDICDF0415", 115), ("csOSDEBCDICDF03IRV", 116), ("csOSDEBCDICDF041", 117), ("csISOLatin5", 12), ("csISOLatin6", 13), ("csISOTextComm", 14), ("csHalfWidthKatakana", 15), ("csJISEncoding", 16), ("csShiftJIS", 17), ("csEUCPkdFmtJapanese", 18), ("csEUCFixWidJapanese", 19), ("unknown", 2), ("csISO4UnitedKingdom", 20), ("csWindows30Latin1", 2000), ("csWindows31Latin1", 2001), ("csWindows31Latin2", 2002), ("csWindows31Latin5", 2003), ("csHPRoman8", 2004), ("csAdobeStandardEncoding", 2005), ("csVenturaUS", 2006), ("csVenturaInternational", 2007), ("csDECMCS", 2008), ("csPC850Multilingual", 2009), ("csPCp852", 2010), ("csPC8CodePage437", 2011), ("csPC8DanishNorwegian", 2012), ("csPC862LatinHebrew", 2013), ("csPC8Turkish", 2014), ("csIBMSymbols", 2015), ("csIBMThai", 2016), ("csHPLegal", 2017), ("csHPPiFont", 2018), ("csHPMath8", 2019), ("csHPPSMath", 2020), ("csHPDesktop", 2021), ("csVenturaMath", 2022), ("csMicrosoftPublishing", 2023), ("csWindows31J", 2024), ("csGB2312", 2025), ("csBig5", 2026), ("csMacintosh", 2027), ("csIBM037", 2028), ("csIBM038", 2029), ("csIBM273", 2030), ("csIBM274", 2031), ("csIBM275", 2032), ("csIBM277", 2033), ("csIBM278", 2034), ("csIBM280", 2035), ("csIBM281", 2036), ("csIBM284", 2037), ("csIBM285", 2038), ("csIBM290", 2039), ("csIBM297", 2040), ("csIBM420", 2041), ("csIBM423", 2042), ("csIBM424", 2043), ("csIBM500", 2044), ("csIBM851", 2045), ("csIBM855", 2046), ("csIBM857", 2047), ("csIBM860", 2048), ("csIBM861", 2049), ("csIBM863", 2050), ("csIBM864", 2051), ("csIBM865", 2052), ("csIBM868", 2053), ("csIBM869", 2054), ("csIBM870", 2055), ("csIBM871", 2056), ("csIBM880", 2057), ("csIBM891", 2058), ("csIBM903", 2059), ("csIBBM904", 2060), ("csIBM905", 2061), ("csIBM918", 2062), ("csIBM1026", 2063), ("csIBMEBCDICATDE", 2064), ("csEBCDICATDEA", 2065), ("csEBCDICCAFR", 2066), ("csEBCDICDKNO", 2067), ("csEBCDICDKNOA", 2068), ("csEBCDICFISE", 2069), ("csEBCDICFISEA", 2070), ("csEBCDICFR", 2071), ("csEBCDICIT", 2072), ("csEBCDICPT", 2073), ("csEBCDICES", 2074), ("csEBCDICESA", 2075), ("csEBCDICESS", 2076), ("csEBCDICUK", 2077), ("csEBCDICUS", 2078), ("csUnknown8BiT", 2079), ("csMnemonic", 2080), ("csMnem", 2081), ("csVISCII", 2082), ("csVIQR", 2083), ("csKOI8R", 2084), ("csHZGB2312", 2085), ("csIBM866", 2086), ("csPC775Baltic", 2087), ("csKOI8U", 2088), ("csIBM00858", 2089), ("csIBM00924", 2090), ("csIBM01140", 2091), ("csIBM01141", 2092), ("csIBM01142", 2093), ("csIBM01143", 2094), ("csIBM01144", 2095), ("csIBM01145", 2096), ("csIBM01146", 2097), ("csIBM01147", 2098), ("csIBM01148", 2099), ("csISO11SwedishForNames", 21), ("csIBM01149", 2100), ("csBig5HKSCS", 2101), ("csIBM1047", 2102), ("csPTCP154", 2103), ("csAmiga1251", 2104), ("csKOI7switched", 2105), ("csISO15Italian", 22), ("cswindows1250", 2250), ("cswindows1251", 2251), ("cswindows1252", 2252), ("cswindows1253", 2253), ("cswindows1254", 2254), ("cswindows1255", 2255), ("cswindows1256", 2256), ("cswindows1257", 2257), ("cswindows1258", 2258), ("csTIS620", 2259), ("csISO17Spanish", 23), ("csISO21German", 24), ("csISO60DanishNorwegian", 25), ("csISO69French", 26), ("csISO10646UTF1", 27), ("csISO646basic1983", 28), ("csINVARIANT", 29), ("csASCII", 3), ("csISO2IntlRefVersion", 30), ("reserved", 3000), ("csNATSSEFI", 31), ("csNATSSEFIADD", 32), ("csNATSDANO", 33), ("csNATSDANOADD", 34), ("csISO10Swedish", 35), ("csKSC56011987", 36), ("csISO2022KR", 37), ("csEUCKR", 38), ("csISO2022JP", 39), ("csISOLatin1", 4), ("csISO2022JP2", 40), ("csISO13JISC6220jp", 41), ("csISO14JISC6220ro", 42), ("csISO16Portuguese", 43), ("csISO18Greek7Old", 44), ("csISO19LatinGreek", 45), ("csISO25French", 46), ("csISO27LatinGreek1", 47), ("csISO5427Cyrillic", 48), ("csISO42JISC62261978", 49), ("csISOLatin2", 5), ("csISO47BSViewdata", 50), ("csISO49INIS", 51), ("csISO50INIS8", 52), ("csISO51INISCyrillic", 53), ("csISO54271981", 54), ("csISO5428Greek", 55), ("csISO57GB1988", 56), ("csISO58GB231280", 57), ("csISO61Norwegian2", 58), ("csISO70VideotexSupp1", 59), ("csISOLatin3", 6), ("csISO84Portuguese2", 60), ("csISO85Spanish2", 61), ("csISO86Hungarian", 62), ("csISO87JISX0208", 63), ("csISO88Greek7", 64), ("csISO89ASMO449", 65), ("csISO90", 66), ("csISO91JISC62291984a", 67), ("csISO92JISC62991984b", 68), ("csISO93JIS62291984badd", 69), ("csISOLatin4", 7), ("csISO94JIS62291984hand", 70), ("csISO95JIS62291984handadd", 71), ("csISO96JISC62291984kana", 72), ("csISO2033", 73), ("csISO99NAPLPS", 74), ("csISO102T617bit", 75), ("csISO103T618bit", 76), ("csISO111ECMACyrillic", 77), ("csa71", 78), ("csa72", 79), ("csISOLatinCyrillic", 8), ("csISO123CSAZ24341985gr", 80), ("csISO88596E", 81), ("csISO88596I", 82), ("csISO128T101G2", 83), ("csISO88598E", 84), ("csISO88598I", 85), ("csISO139CSN369103", 86), ("csISO141JUSIB1002", 87), ("csISO143IECP271", 88), ("csISO146Serbian", 89), ("csISOLatinArabic", 9), ("csISO147Macedonian", 90), ("csISO150", 91), ("csISO151Cuba", 92), ("csISO6937Add", 93), ("csISO153GOST1976874", 94), ("csISO8859Supp", 95), ("csISO10367Box", 96), ("csISO158Lap", 97), ("csISO159JISX02121990", 98), ("csISO646Danish", 99), )
    pass


# Objects

ianaCharsetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 106)).setRevisions(("2004-06-08 00:00",))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("IANA-CHARSET-MIB", PYSNMP_MODULE_ID=ianaCharsetMIB)

# Types
mibBuilder.exportSymbols("IANA-CHARSET-MIB", IANACharset=IANACharset)

# Objects
mibBuilder.exportSymbols("IANA-CHARSET-MIB", ianaCharsetMIB=ianaCharsetMIB)

