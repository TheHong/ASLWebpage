
def getRawData(fileName: str):
    data = []
    with open(fileName, "r") as f:
        for line in f:
            data.append(line)
    return data


def writeJS(data):
    letter_break = "---" # In the raw file, breaks of the form "---A" will be present to section the data
    href_start = "href="
    href_end = '"'
    word_start = ">"
    word_end = "<"
    codeLines = ["function loadData() {", "return ["]
    for line in data:
        if line.startswith(letter_break):
            codeLines.append("//{}".format(line[len(letter_break) + 1]))
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
            word_end_loc = line.index(word_end, word_start_loc)
            word = line[word_start_loc: word_end_loc]
            # Create JS code line
            codeLines.append(
                'new Word("{0}", "{1}", "{2}"),'.format(word, url, ""))
        except ValueError:
            print("Skipped: {}".format(line))

    codeLines.append("]")
    codeLines.append("}")
    code = "\n".join(codeLines)
    # print(code)
    with open("allWords.js", "w") as f:
        f.write(code)
    
    print("JavaScript File created")


if __name__ == "__main__":
    data = getRawData("rawHTML.txt")
    writeJS(data)
