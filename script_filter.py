import re

genre_list = {
    "Classical": 0,
    "Focus Spa": 1,
    "Up Tempo": 2,
    "Alpha Chill": 3,
    "Classical Piano": 4,
    "Acoustical": 5,
    "Cinematic": 6,
    "Ambient": 7,
    "Water": 8,
    "Baroque Piano": 9,
    "ADHD Type 1": 10,
    "Oct Beta Test": 11,
    "Cafe Focus Beta": 12,
    "Cafe Creative Beta": 13,
    "Drums &amp; Hums Beta": 14,
    "Drums &amp; Hums Turbo Beta": 15,
    "Drum Zone Beta": 16,
    "Drum Zone Turbo Beta": 17,
    "Hand Drums &amp; Hums Beta": 18,
    "Hand Drums &amp; Hums Turbo Beta": 19,
    "Kora Beta": 20,
    "Kora Beta w/Entrainment": 21
}

p = re.compile('^.*{query}.*$', re.IGNORECASE)

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
