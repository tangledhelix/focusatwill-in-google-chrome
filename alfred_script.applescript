on alfred_script(q)
    
    tell application "Google Chrome"
        
        if q is "" or q is "p" or q is "pp" or q is "play" or q is "pause" then
            set buttonClass to "play"
        end if
        if q is "next" or q is "skip" or q is "n" then
            set buttonClass to "next"
        end if
        set execCode to "$('." & buttonClass & "').first().click()"
        
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
        
    end tell
end alfred_script