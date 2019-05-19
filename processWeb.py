from temp.hash_table import HashTable


def hasher(theDict):
    """
    dict -> DictADT
    A function that transforms dict into Dict ADT.
    """
    n = 36
    types = ["th", "td", "table"]
    attributes = ["font-family", "font-style", "font-size", "font-weight",
                  "border",
                  "border-collapse", "width", "height", "text-align",
                  "vertical-align", "padding", "color"]
    preferences = HashTable(n)
    if theDict["default_style"] == "on":
        preferences.insert("th, font-family", "222")
        preferences.insert("table, border", "1px solid black")
        preferences.insert("th, font-size", "20px")
        for typer in types:
            for attr in attributes:
                key = typer + ", " + attr
                try:
                    preferences.search(key)
                except TypeError:
                    preferences.insert(key, "-")
    else:
        for typer in types:
            for attr in attributes:
                key = typer + ", " + attr
                val = theDict[key]
                preferences.insert(key, val)
    return preferences
