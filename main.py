from transformer import baseCopy, baseDel, mover
from makeHTML import webing
from errCheck import mainCheck
from prefHTML import mainPref
####
from webImitate import example
### an example of user preferences upper


def main():
    """
    A main function that does all work. Returns True if everything is OK.
    """
    sample_path = "base.txt"
    data_addr = "csv\\incorrect\\wide.csv"

    err = mainCheck(data_addr)
    if err:
        return err

    userPref = example()
    mainPref("baseCopy1.txt", userPref)

    pathBase_in = "baseCopy1.txt"
    pathBase_out = "base.txt"
    baseCopy(pathBase_in, pathBase_out)

    webing(sample_path, data_addr)

    path_in = "base.txt"
    path_out = "Templates/test2.html"
    mover(path_in, path_out)

    baseDel("baseCopy1.txt")

    from convertPDF import main1
    main1()
    baseDel("Templates/test2.html")
    return True


print(main())
