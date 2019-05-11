def webing(sample_path, data_addr):
    """
    str, str -> None
    A function that having base of an HTML file, adds it by csv file.
    """
    with open(sample_path, "a", encoding="utf-8") as txt:
        txt.write("<table>")
        with open(data_addr, "r", encoding="utf-8") as data:
            head = True
            for item in data:
                txt.write("<tr>")

                for el in item.split(","):
                    if head:
                        temp = "<th>" + el + "</th>"
                    else:
                        temp = "<td>" + el + "</td>"
                    txt.write(temp)

                txt.write("</tr>")
                head = False

        txt.write("</table>")
        txt.write("</body>")
        txt.write("</html>")
