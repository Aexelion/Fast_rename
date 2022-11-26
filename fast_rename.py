import os
import re
import Fast_rename.tmp

NEW_NAME = "{series_name} - {number} {lang}.{extension}"
SELFNAME = __file__.split("\\")[-1]

SERIE_NAME = ""
DEFAULT_LANG = "vostfr"
DEFAULT_EXT = "mp4"

FORMAT_MONO_SEASON = "{name} - {nb_ep}{lang}.{ext}"
FORMAT_MULTI_SEASONS = "{name} - {nb_se}x{nb_ep}{lang}.{ext}"

#  Detection of pattern using regex
#  The file name should be in the form :
#  NAME[ -][ ][NB_SEASONx]NB_EPISODE[[ ]LANG].EXT
RE_DETECTION_STRING = r"([\w ]+)( -)? ?((\d+)x)?(\d+)( ?[a-zA-Z]*)[.]([a-zA-Z0-9]+)"


def graphical_interface():
    #TODO
    pass

def int_to_format(n:int, nb_digits=4) -> str :
    """ Format an int n to a nb_digits digits str."""
    res = "0"*nb_digits + str(n)
    return res[-nb_digits:]


if __name__ == "__main__" :
    list_files = [x for x in os.listdir() if x!=SELFNAME]
    re_detection = re.compile(RE_DETECTION_STRING)
    format_test = input("Which output format would you like to use : multi-season (1) or mono-season (2). ")
    format_str = FORMAT_MONO_SEASON if format_test=="2" else FORMAT_MULTI_SEASONS
    default_season = input("Input the default season number for episodes without one. ")
    for file in list_files :
        m = re_detection.match(file)
        if m:
            dict = {"name": m.group(1),
                "nb_se": m.group(4) or default_season,
                "nb_ep": m.group(5),
                "lang": m.group(6),
                "ext": m.group(7),
            }
            print("renaming:", file, "to:", format_str.format(**dict))
            os.rename(file, format_str.format(**dict))
            #rename_pattern(file, dict, dst_pattern)
        else:
            print("The file name:", file, "does not match the current pattern.")
            print("This program can't rename it for now...")
    input("\nAll files name have been change.\nPress enter to end this program.")
