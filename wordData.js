class Word {
    constructor(english, chinese, url) {
        this.english = english;
        this.chinese = chinese;
        this.url = url;
    }
}

// function loadData() {
//     var rawFile = new XMLHttpRequest();
//     rawFile.open("GET", "links.txt", false);
//     rawFile.onreadystatechange = function () {
//         if (rawFile.readyState === 4) {
//             if (rawFile.status === 200 || rawFile.status == 0) {
//                 var allText = rawFile.responseText;
//                 alert(allText);
//             }
//         }
//     }
//     rawFile.send(null);
// }

function loadData() {
    return [
        new Word("Bob", "temp", "url1"),
        new Word("BOBB", "我", "url2"),
        new Word("ABAB", "tt", "dfs")
    ];
}





