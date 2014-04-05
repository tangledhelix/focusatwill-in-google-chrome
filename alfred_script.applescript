on alfred_script(q)
    tell application "Google Chrome"

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
                exit repeat
            end if

            set thisWindowIndex to thisWindowIndex + 1

        end repeat

        tell tab thisTabIndex of window thisWindowIndex
            execute javascript "$('.play').first().click()"
        end tell

    end tell
end alfred_script
