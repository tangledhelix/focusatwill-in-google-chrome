function run(argv) {

  const appUrl = "https://www.focusatwill.com/app/music"
  const browser = Application("Google Chrome")

  let tab

  for (let w = 0; w < browser.windows.length; w++) {
    for (let t = 0; t < browser.windows[w].tabs.length; t++) {
      if (browser.windows[w].tabs[t].url().indexOf(appUrl) >= 0) {
        tab = browser.windows[w].tabs[t]
      }
    }
  }

  if (! tab) {
    const me = Application.currentApplication()
    me.includeStandardAdditions = true
    me.displayNotification("Please open the site in Chrome.", {withTitle: "focus@will not found"})
    return
  }

  if (["p", "pp", "play", "pause"].indexOf(argv[0]) >= 0) {
    tab.url = "javascript:if(window.faw.isPlaying){window.faw.stop()}else{window.faw.play()}"
  } else if (["n", "next", "skip"].indexOf(argv[0]) >= 0) {
    tab.url = "javascript:window.faw.skip()"
  } else if (["genre"].indexOf(argv[0] >= 0)) {
    let channelId = argv[0].split(' ')[1]
    tab.url = `javascript:window.faw.channel(${channelId})`
  }
}
