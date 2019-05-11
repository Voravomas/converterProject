part1 = "<!DOCTYPE html>\n<html>\n<head>\n<style>\n"
part2 = "</style>\n</head>\n<body>\n"

types = ["th", "td", "table"]
attributes = ["font-family", "font-style", "font-size", "font_weight", "border",
              "border-collapse", "width", "height", "text-align",
              "vertical-align", "padding", "color"]


def makePref(pref):
    """
    A function that makes a td, th, table tags in html file
    and html file itself.
    """
    th = "th {"
    td = "td {"
    table = "table {"
    for typer in types:
        for attr in attributes:
            key = typer + ", " + attr
            val = pref.search(key)
            if val == "None":
                continue
            else:
                if typer == "th":
                    th += attr + ": " + val + ";\n"
                if typer == "td":
                    td += attr + ": " + val + ";\n"
                if typer == "table":
                    table += attr + ": " + val + ";\n"
    th += "}"
    td += "}"
    table += "}"
    if th == "th {}":
        th = ""
    if td == "td {}":
        td = ""
    if table == "table {}":
        table = ""
    mainText = part1 + table + "\n" + th + "\n" + td + part2
    return mainText


def writePref(path, text):
    """
    str, str -> None
    A function that writes text into a file.
    """
    with open(path, "w") as f:
        f.write(text)


def mainPref(link, dictADT):
    """
    str, HashTable -> None
    A main function that makes base of html file based on user preferences.
    """
    baseHTML = makePref(dictADT)
    writePref(link, baseHTML)

