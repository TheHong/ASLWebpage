"""This script takes in a formatted text file containing html elements and convert it to JS file of word objects.
Took around 2 hours to copy, format the text file, and tweak the code
"""


def getRawData(fileName: str):
    data = []
    with open(fileName, "r") as f:
        for line in f:
            data.append(line)
    return data


def writeJS(data):
    js_line_format = 'new Word("{0}", "{1}", "{2}"),'
    # In the raw file, breaks of the form "@A" will be present to section the data
    letter_break = "@"
    href_start = "href="
    href_end = '"'
    word_start = ">"
    word_end = "<"
    extra_info_start = "["
    extra_info_end = "]"
    codeLines = ["function loadData() {", "return ["]
    for line in data:
        if line.startswith(letter_break):
            codeLines.append("")
            codeLines.append(
                "//{} ========================================================="
                .format(line[len(letter_break)])
            )
            continue
        try:
            if line.find("approx") != -1:
                af = 2
            # Get url
            href_start_loc = line.index(href_start) + len(href_start) + 1
            href_end_loc = line.index(href_end, href_start_loc)
            url = "https://www.lifeprint.com/asl101/" + \
                line[href_start_loc + 3: href_end_loc]
            # Get word
            word_start_loc = line.index(
                word_start, href_start_loc) + len(word_start)
            if line[word_start_loc] == word_end:
                word_start_loc = line.index(
                    word_start, word_start_loc + 2) + len(word_start)
            word_end_loc = line.index(word_end, word_start_loc)
            word = line[word_start_loc: word_end_loc].lower()
            assert word != " "
            word = word.replace('"', "'")
            if "-[#" in word:
                word = word[:word.index("-[#")]
            # Get extra info (if available)
            if line.find(extra_info_start, word_end_loc) != -1:
                extra_info_start_loc = line.index(
                    extra_info_start, word_end_loc) + len(extra_info_start)
                extra_info_end_loc = line.index(
                    extra_info_end, extra_info_start_loc)
                extra_info = " " + \
                    line[extra_info_start_loc - 1: extra_info_end_loc + 1]
                # if "lexicalized" in extra_info:
                #     extra_info = ""
            else:
                extra_info = ""
            # Create JS code line
            codeLines.append(
                js_line_format.format(word + extra_info, url, ""))
        except (ValueError, AssertionError):
            print("Skipped: {}".format(line))

    codeLines.append("]")
    codeLines.append("}")
    code = "\n".join(codeLines)
    with open("allWords.js", "w") as f:
        f.write(code)

    print("JavaScript File created")


if __name__ == "__main__":
    data = getRawData("rawHTML.txt")
    writeJS(data)
