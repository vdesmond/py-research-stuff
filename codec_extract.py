import codecs


def get_file_bom_encodig(filename):
    with open(filename, "rb") as openfileobject:
        line = str(openfileobject.readline())
        if line[2:14] == str(codecs.BOM_UTF8).split("'")[1]:
            return "utf_8"
        if line[2:10] == str(codecs.BOM_UTF16_BE).split("'")[1]:
            return "utf_16"
        if line[2:10] == str(codecs.BOM_UTF16_LE).split("'")[1]:
            return "utf_16"
        if line[2:18] == str(codecs.BOM_UTF32_BE).split("'")[1]:
            return "utf_32"
        if line[2:18] == str(codecs.BOM_UTF32_LE).split("'")[1]:
            return "utf_32"
    return ""


def get_all_file_encoding(filename):
    encoding_list = []
    encodings = (
        "utf_8",
        "utf_16",
        "utf_16_le",
        "utf_16_be",
        "utf_32",
        "utf_32_be",
        "utf_32_le",
        "cp850",
        "cp437",
        "cp852",
        "cp1252",
        "cp1250",
        "ascii",
        "utf_8_sig",
        "big5",
        "big5hkscs",
        "cp037",
        "cp424",
        "cp500",
        "cp720",
        "cp737",
        "cp775",
        "cp855",
        "cp856",
        "cp857",
        "cp858",
        "cp860",
        "cp861",
        "cp862",
        "cp863",
        "cp864",
        "cp865",
        "cp866",
        "cp869",
        "cp874",
        "cp875",
        "cp932",
        "cp949",
        "cp950",
        "cp1006",
        "cp1026",
        "cp1140",
        "cp1251",
        "cp1253",
        "cp1254",
        "cp1255",
        "cp1256",
        "cp1257",
        "cp1258",
        "euc_jp",
        "euc_jis_2004",
        "euc_jisx0213",
        "euc_kr",
        "gb2312",
        "gbk",
        "gb18030",
        "hz",
        "iso2022_jp",
        "iso2022_jp_1",
        "iso2022_jp_2",
        "iso2022_jp_2004",
        "iso2022_jp_3",
        "iso2022_jp_ext",
        "iso2022_kr",
        "latin_1",
        "iso8859_2",
        "iso8859_3",
        "iso8859_4",
        "iso8859_5",
        "iso8859_6",
        "iso8859_7",
        "iso8859_8",
        "iso8859_9",
        "iso8859_10",
        "iso8859_13",
        "iso8859_14",
        "iso8859_15",
        "iso8859_16",
        "johab",
        "koi8_r",
        "koi8_u",
        "mac_cyrillic",
        "mac_greek",
        "mac_iceland",
        "mac_latin2",
        "mac_roman",
        "mac_turkish",
        "ptcp154",
        "shift_jis",
        "shift_jis_2004",
        "shift_jisx0213",
    )
    for e in encodings:
        try:
            fh = codecs.open(filename, "r", encoding=e)
            fh.readlines()
        except UnicodeDecodeError:
            fh.close()
        except UnicodeError:
            fh.close()
        else:
            encoding_list.append([e])
            fh.close()
            continue
    return encoding_list


def get_file_encoding(filename):
    file_encoding = get_file_bom_encodig(filename)
    if file_encoding != "":
        return file_encoding
    encoding_list = get_all_file_encoding(filename)
    file_encoding = str(encoding_list[0][0])
    if file_encoding[-3:] == "_be" or file_encoding[-3:] == "_le":
        file_encoding = file_encoding[:-3]
    return file_encoding
