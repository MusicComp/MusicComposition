from music21 import *

def main():
    # 1st Order Markov List
    firstOrderList = {}
    
    # Breaks down MIDI and stores notes in array
    s1 = converter.parse('invent1.mid').iter
    firstList = []
    for el in s1:
        for notes in el.notes:
            if notes.isNote:
                firstList.append(notes)
    
    # Counts the number of transitions from one note to another
    i = 0
    previousNote = None
    for thing in firstList:
        if i == 0:
            i += 1
            previousNote = thing
        else:
            transitionName = previousNote.name + " goes to " + thing.name
            if transitionName in firstOrderList: 
                firstOrderList[transitionName] += 1
            else:
                firstOrderList[transitionName] = 1
            previousNote = thing

    print(firstOrderList)
        
if __name__ == '__main__':
    main()