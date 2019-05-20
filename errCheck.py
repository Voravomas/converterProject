def correctName(fileName):
    """
    str -> bool
    A function that checks, whether filename is true.
    >>> correctName("me.csv")
    True
    >>> correctName("mec.sv")
    False
    """
    if fileName.endswith(".csv"):
        return True
    return False


def mainCheck(fileName):
    """
    str -> str
    str -> bool
    A function that checks all errors that may happen in a file.
    >>> mainCheck("main.cdf")
    "Invalid file name"
    >>> mainCheck("main.csv")
    False
    """
    if correctName(fileName) == False:
        return "Invalid file name"
    return False
