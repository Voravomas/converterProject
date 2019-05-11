from hash_table import HashTable


def example():
    """
    None -> HashTable()
    A function that serves as an example of user preferences in table change.
    >>> example().search("th, font-family")
    222
    >>> example().search("table, border")
    1px solid black
    """
    n = 32
    types = ["th", "td", "table"]
    attributes = ["font-family", "font-style", "font-size", "font_weight",
                  "border",
                  "border-collapse", "width", "height", "text-align",
                  "vertical-align", "padding", "color"]
    preferences = HashTable(n)
    preferences.insert("th, font-family", "222")
    preferences.insert("table, border", "1px solid black")
    preferences.insert("th, font-size", "20px")
    for typer in types:
        for attr in attributes:
            key = typer + ", " + attr
            try:
                preferences.search(key)
            except TypeError:
                preferences.insert(key, "None")
    return preferences
