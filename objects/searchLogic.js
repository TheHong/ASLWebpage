class Searcher {
    // Takes care of both the search bar and the dropdown

    constructor() {
        console.log("Search bar constructed");
        this.words = loadData();
        this.maxDropdownSize = 15;

    }

    createBar() {
        document.getElementById("theSearchBar").innerHTML = '<input type="text" placeholder="Search.." id="searchField" onkeyup="searcher.filterFunction()">'
    }

    filterFunction() {
        var noResultStr = "No Translation Available";
        var hasResult = 0;
        var dropdown = document.getElementById("theDropdown");
        var input = document.getElementById("searchField").value;
        var priorityWords = [], similarWords = [];

        this.clearDropdown();

        // Show items that are relevant to the user input
        if (input != "") {
            for (var i = 0; i < this.words.length && priorityWords.length <= this.maxDropdownSize; i++) {
                if (this.words[i].english.toUpperCase().indexOf(input.toUpperCase()) > -1 && input != noResultStr) {
                    if (this.words[i].english.toUpperCase()[0] == input.toUpperCase()[0]) {
                        priorityWords.push(this.words[i]);
                    } else {
                        similarWords.push(this.words[i]);
                    }
                    hasResult = 1;
                }
            }
            if (!hasResult) {
                this.showItem(new Word(noResultStr, "", ""), dropdown);
            } else {
                var i;
                for (i = 0; i < priorityWords.length; i++) {
                    this.showItem(priorityWords[i], dropdown);
                }
                for (i = 0; i < similarWords.length && i < this.maxDropdownSize - priorityWords.length; i++) {
                    this.showItem(similarWords[i], dropdown);
                }
            }
        }
    }

    showItem(word, dropdown) {
        var newItem = document.createElement('a');
        var newLabel = document.createTextNode(word.english);
        newItem.appendChild(newLabel);
        newItem.title = word.chinese;
        newItem.href = word.url;
        newItem.target = "webframe";
        newItem.onclick = this.clearDropdown;
        dropdown.appendChild(newItem);
    }

    clearDropdown() {
        // Use jQuery to reset the drop down
        $("#theDropdown").empty();
    }
}