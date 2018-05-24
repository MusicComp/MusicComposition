import glob
import xml.etree.ElementTree as XML

def parse_file(filepath):
    tree = XML.parse(filepath)
    tree_root = tree.getroot()
    # chord_sections = tree_root.findall('./sections/_Chorus/segment/chords')
    chord_sections = tree_root.findall('.//chords')

    sds = []
    #fbs = []
    for chord_section in chord_sections:
        for chord in chord_section:
            sd = chord.find('sd').text
            sds.append(sd)
            #fb = chord.find('fb').text
            #fbs.append(fb)
    print(sds)
    #print(fbs)

for filename in glob.glob('./hooktheory-data/xml/*.xml'):
    print(filename)
    parse_file(filename)
    print()
