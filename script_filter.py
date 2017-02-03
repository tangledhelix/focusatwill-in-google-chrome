import re

genre_list = {
    "Classical": 0,
    "Neuro Space": 1,
    "Focus Spa": 2,
    "Up Tempo": 3,
    "Alpha Chill": 4,
    "Classical Piano": 5,
    "Acoustical": 6,
    "Cinematic": 7,
    "Ambient": 8,
    "Water": 9,
    "Baroque Piano": 10,
    "ADHD Type 1": 11,
    "Oct Beta Test": 12,
    "Cafe Focus Beta": 13,
    "Cafe Creative Beta": 14,
    "Drums &amp; Hums Beta": 15,
    "Drums &amp; Hums Turbo Beta": 16,
    "Drum Zone Beta": 17,
    "Drum Zone Turbo Beta": 18,
    "Hand Drums &amp; Hums Beta": 19,
    "Hand Drums &amp; Hums Turbo Beta": 20,
    "Kora Beta": 21,
    "Kora Beta w/Entrainment": 22
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
