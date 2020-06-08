class Word {
    constructor(english, chinese, url) {
        this.english = english;
        this.chinese = chinese;
        this.url = url;
    }
}

function filterFunction() {
    var words = [new Word("About", "TEMP", "url1"), new Word("BB", "TEMP", "url2")];
    var noResultStr = "No Translation Available";
    var isResultExist = 0;
    var dropdown = document.getElementById("theDropdown");
    var input = document.getElementById("searchField").value;
    var filter;

    // Use jQuery to reset the drop down
    $("#theDropdown").empty();

    // Show items that are relevant to the user input
    if (input != "") {
        for (i = 0; i < words.length; i++) {
            if (words[i].english.toUpperCase().indexOf(input.toUpperCase()) > -1 && input != noResultStr) {
                showItem(words[i], dropdown);
                isResultExist = 1;
            }
        }
        if (!isResultExist) {
            showItem(noResultStr, dropdown);
        }
    }
}
function showItem(word, dropdown) {
    var newItem = document.createElement('a');
    var newLabel = document.createTextNode(word.english);
    newItem.appendChild(newLabel);
    newItem.title = word.chinese;
    // newItem.href = word.url;
    dropdown.appendChild(newItem);
}