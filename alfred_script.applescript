on alfred_script(q)

    set AppleScript's text item delimiters to {" "}

    tell application "Google Chrome"
        
        if q is "" or q is "p" or q is "pp" or q is "play" or q is "pause" then
            set buttonClass to "play"
            set execCode to "$('." & buttonClass & "').first().click()"
        else if q is "next" or q is "skip" or q is "n" then
            set buttonClass to "next"
            set execCode to "$('." & buttonClass & "').first().click()"
        else
            set argList to every text item of q
            if item 1 of argList is "genre" then
                set execCode to "$('li.genre a')[" & item 2 of argList & "].click();"
            end if
        end if
        
        set seenPlayerTab to 0
        
        set thisWindowIndex to 1
        repeat with thisWindow in windows
            
            set thisTabIndex to 1
            repeat with thisTab in tabs of thisWindow
                
                if URL of thisTab starts with "https://www.focusatwill.com/" then
                    set seenPlayerTab to 1
                    exit repeat
                end if
                
                set thisTabIndex to thisTabIndex + 1
                
            end repeat
            
            if seenPlayerTab is greater than 0 then
                tell tab thisTabIndex of window thisWindowIndex
                    execute javascript execCode
                end tell
                exit repeat
            end if
            
            set thisWindowIndex to thisWindowIndex + 1
            
        end repeat
        
        if seenPlayerTab is 0 then
            set newTab to make new tab at end of tabs of window 1
            set URL of newTab to "https://www.focusatwill.com/music/#player"
            delay 5
            tell newTab
                execute javascript execCode
            end tell
        end if
        
    end tell
end alfred_script
