import re

genre_list = {
    "Classical": 0,
    "Focus Spa": 1,
    "Up Tempo": 2,
    "Alpha Chill": 3,
    "Acoustical": 4,
    "Cinematic": 5,
    "Ambient": 6,
    "Water": 7,
    "Baroque Piano": 8,
    "ADHD Type 1": 9,
    "Oct Beta Test": 10,
    "Cafe Focus Beta": 11,
    "Cafe Creative Beta": 12,
    "Drums &amp; Hums Beta": 13,
    "Drums &amp; Hums Turbo Beta": 14,
    "Drum Zone Beta": 15,
    "Drum Zone Turbo Beta": 16,
    "Hand Drums &amp; Hums Beta": 17,
    "Hand Drums &amp; Hums Turbo Beta": 18
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
