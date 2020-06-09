"""This script takes in a formatted text file containing html elements and convert it to JS file of word objects.
The process is as follows:
1. Copy and paste html sections of lifeprint.com that corresponds to words and their respective links. This is pasted in a text file.
2. Format the text file so that it complies with the writeJS() function in this script. The result is rawHTML.txt.
3. Run this script to create a JavaScript file called allWords.JS, which can then be used by the web page to get word data in the form of word.js/Word objects.
Took around 2 hours to copy, format the text file, and tweak the code.
"""

def getRawData(fileName: str):
    """Converts a text file into a list of string where each string correspond to each row of the file.
    Some of these rows will correspond to html elements from lifeprint.com.

    Args:
        fileName (str): File path to the file

    Returns:
        list[str]
    """
    data = []
    with open(fileName, "r") as f:
        for line in f:
            data.append(line)
    return data


def writeJS(data):
    """Creates a JavaScript file to be used to output word.js/Word objects

    Args:
        data (list[str]): List of string where most of the strings correspond to html elements
    """
    # Contains the JS code as a array of strings (to be joined later into a string)
    codeLines = ["function loadData() {", "return ["]

    # How each word.js/Word object is initialized in the JS file to be generated
    js_line_format = 'new Word("{0}", "{1}", "{2}"),'

    # In the raw file, breaks of the form "@A" will be present to section the data
    letter_break = "@"

    # Characters in the html element that indicate certain info to be extracted
    url_start = "href="
    url_end = '"'
    word_start = ">"
    word_end = "<"
    extra_info_start = "["
    extra_info_end = "]"
    
    # Processing each line
    for line in data:
        # Recognizing section breaks (by letter) in the data
        if line.startswith(letter_break):
            codeLines.append("")
            codeLines.append(
                "//{} ========================================================="
                .format(line[len(letter_break)])
            )
            continue

        try:
            # Get url =========================================================
            url_start_loc = line.index(url_start) + len(url_start) + 1
            url_end_loc = line.index(url_end, url_start_loc)
            url = "https://www.lifeprint.com/asl101/" + \
                line[url_start_loc + 3: url_end_loc]

            # Get word ========================================================
            # Get first occurance of word_start_loc
            word_start_loc = line.index(
                word_start, url_start_loc) + len(word_start)
            # If word is not located at the first occurance of word_start_loc
            if line[word_start_loc] == word_end: 
                word_start_loc = line.index(
                    word_start, word_start_loc + 2) + len(word_start)
            # Extract the word
            word_end_loc = line.index(word_end, word_start_loc)
            word = line[word_start_loc: word_end_loc].lower()
            # Replace any double quotation marks (which will mess up the JS code)
            word = word.replace('"', "'")
            # Removing instances in the html that contains "-[#"
            if "-[#" in word:
                word = word[:word.index("-[#")]

            # Get extra info (if available) ===================================
            if line.find(extra_info_start, word_end_loc) != -1:
                extra_info_start_loc = line.index(
                    extra_info_start, word_end_loc) + len(extra_info_start)
                extra_info_end_loc = line.index(
                    extra_info_end, extra_info_start_loc)
                extra_info = " " + \
                    line[extra_info_start_loc - 1: extra_info_end_loc + 1]
            else:
                extra_info = ""

            # Create JS code line =============================================
            codeLines.append(
                js_line_format.format(word + extra_info, url, ""))
        except (ValueError, AssertionError):
            print("Skipped: {}".format(line))

    # Finalize codelines and create the code string
    codeLines.append("]")
    codeLines.append("}")
    code = "\n".join(codeLines)

    # Create JS file
    with open("allWords.js", "w") as f:
        f.write(code)

    print("JavaScript File created")


if __name__ == "__main__":
    data = getRawData("rawHTML.txt")
    writeJS(data)
