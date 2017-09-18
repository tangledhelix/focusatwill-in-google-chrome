## About

This [Alfred][] workflow will control the [focusatwill.com][faw] tab in your
Google Chrome browser. It will not bring Chrome to the front or activate the
focus@will tab.

http://www.packal.org/workflow/playpause-focuswill-google-chrome

[alfred]: https://www.alfredapp.com/
[faw]: https://www.focusatwill.com/

## Hotkey support

Hotkeys are stripped by Alfred on import, so you'll need to set what you prefer.
You may assign hotkeys for the "play/pause" and "next track" actions.

To do so, go to Alfred's preferences, find the workflow under "Workflows", and
double-click the "play" or "next" box. Then hit the hotkey combination you would
like to use.

**NOTE:** This will take over the hotkey globally! So don't use a hotkey that
you want to keep using in another program.

## Using Alfred keywords

After triggering Alfred, you can use the keyword `focus` (or `foc`). With no
argument, play/pause is assumed.

    foc play    - play/pause
    foc pause   - play/pause
    foc p       - play/pause
    foc pp      - play/pause

    foc next    - next track
    foc skip    - next track
    foc n       - next track

You can also switch genres using the `focg` keyword. Alfred will autocomplete
the genre for you, so you should only need to type a few characters to select
the genre you want. (`alph` for Alpha Chill, `eins` for Einstein's Genius, etc.)

Unfortunately it does not seem to be possible to read data from a rendered web
page into Alfred, so the list is fixed. As focus@will adds new genres, I have
to add them to the list manually.

## Compatibility notes

The workflow is now using JXA (JavaScript for Automation). JXA is available as
of Mac OS X 10.10 (Yosemite), released in October 2014. It should work on any
version of OS X / macOS from that point on.
