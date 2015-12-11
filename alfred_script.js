// Alpha-quality JSX port. Feature incomplete.
// This is not used in the exported workflow yet.
//
// TODO: implement genre support

var alfredQuery = "{query}";
var alfredArgs = alfredQuery.split(" ");

var expectedUrl = "https://www.focusatwill.com/music/#player";
var Chrome = Application("Google Chrome");

function run() {

    var tab = findTab();
    if (!tab) {
        displayNotification();
        return;
    }
    
    if (["p", "pp", "play", "pause"].indexOf(alfredArgs[0]) >= 0) {
        clickPlayPause(tab);
    } else if (["n", "next", "skip"].indexOf(alfredArgs[0]) >= 0) {
        clickNextTrack(tab);
    } else if (["genre"].indexOf(alfredArgs[0]) >= 0) {
        chooseGenre(alfredArgs[1]);
    }
}

function findTab() {
    var windowIndex, tabIndex, tabUrl;
    
    for (windowIndex = 0; windowIndex < Chrome.windows.length; windowIndex++) {
        for (tabIndex = 0; tabIndex < Chrome.windows[windowIndex].tabs.length; tabIndex++) {
            tabUrl = Chrome.windows[windowIndex].tabs[tabIndex].url();
            if (tabUrl.indexOf(expectedUrl) >= 0) {
                console.log("Found it - window " + windowIndex + ", tab " + tabIndex);
                return Chrome.windows[windowIndex].tabs[tabIndex];
            }
        }
    }
    
    return false;
}

function displayNotification() {
    var me = Application.currentApplication();
    me.includeStandardAdditions = true;
    me.displayNotification("Please open the site in Chrome.", {withTitle: "focus@will not found"});
}

function clickSomething(tab, targetClass) {
    tab.execute({ javascript: "document.getElementsByClassName('" + targetClass + "')[0].click();" });
}

function clickPlayPause(tab) {
    clickSomething(tab, "play");
}

function clickNextTrack(tab) {
    clickSomething(tab, "next");
}

function chooseGenre(genre_idx) {
    tab.execute({ javascript: "document.querySelectorAll('li.genre a')[" + genre_idx + "].click();" });
}
