import re
import sys

# Easy way to get this list updated:
# Open focusatwill player in browser. Open console, then paste this:
#
# let _clist; window.faw.channelList.forEach(function(e){_clist += `"${e.name}": ${e.id},\n`}); console.log(_clist);

genre_list = {
    "Classical Plus": 503,
    "Electro Bach": 493,
    "Acoustical Plus": 543,
    "Propeller Drone": 513,
    "Neuro Space": 483,
    "Focus Spa": 473,
    "Uptempo": 443,
    "Alpha Chill ": 153,
    "Classical Piano": 393,
    "Cinematic": 7,
    "Ambient": 3,
    "Water ": 23,
    "Baroque Piano": 423,
    "ADHD Type 1": 13,
    "Oct Beta Test": 243,
    "Cafe Focus Beta": 253,
    "Cafe Creative Beta": 263,
    "Drums & Hums Beta": 283,
    "Drums & Hums Turbo Beta": 303,
    "Drum Zone Beta": 293,
    "Drum Zone Turbo Beta": 313,
    "Hand Drums & Hums Beta": 333,
    "Hand Drums & Hums Turbo Beta": 353,
    "Kora Beta ": 363,
    "Kora Beta w/Entrainment ": 373,
}

p = re.compile("^.*" + sys.argv[1] + ".*$", re.IGNORECASE)

print '<?xml version="1.0" encoding="UTF-8"?>'
print '<items>'

for genre in genre_list:
    idx = genre_list[genre]
    if p.match(genre):
        print '    <item uid="%s" valid="YES" autocomplete="%s" type="file">' % (idx, genre)
        print '        <title>%s</title>' % genre
        print '        <icon>icon.png</icon>'
        print '        <arg>genre %s</arg>' % idx
        print '    </item>'

print '</items>'
