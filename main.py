from temp.transformer import baseDel, mover
from temp.makeHTML import webing
from temp.prefHTML import mainPref


def preMain(dictADT):
    """
    A main function that does all work. Returns True if everything is OK.
    """
    data_addr = "..\\csv\\normal.csv"

    userPref = dictADT
    mainPref("base.txt", userPref)

    sample_path = "base.txt"
    webing(sample_path, data_addr)

    path_in = "base.txt"
    path_out = "..\\resultHTML\\result.html"
    mover(path_in, path_out)

    baseDel("base.txt")
    # baseDel("resultHTML\\result.html")
    baseDel("..\\csv\\normal.csv")
    return True
