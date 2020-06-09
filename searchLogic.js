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
        var numShown = 0;
        var dropdown = document.getElementById("theDropdown");
        var input = document.getElementById("searchField").value;

        this.clearDropdown();

        // Show items that are relevant to the user input
        if (input != "") {
            for (var i = 0; i < this.words.length && numShown <= this.maxDropdownSize; i++) {
                if (this.words[i].english.toUpperCase().indexOf(input.toUpperCase()) > -1 && input != noResultStr) {
                    this.showItem(this.words[i], dropdown);
                    numShown += 1;
                }
            }
            if (!numShown > 0) {
                this.showItem(new Word(noResultStr, "", ""), dropdown);
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