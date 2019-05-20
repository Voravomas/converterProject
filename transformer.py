def mover(path_in, path_out):
    """
    str, str -> None
    A function that moves file from one destination to another.
    """
    import os
    os.rename(path_in, path_out)


def baseCopy(path_in, path_out):
    """
    str, str -> none
    A function that copies file.
    """
    import shutil
    shutil.copy(path_in, path_out)


def baseDel(path):
    """
    str -> None
    A function that removes file.
    """
    import os
    exists = os.path.isfile(path)
    if exists:
        os.remove(path)
