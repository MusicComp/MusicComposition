from music21 import *

def main():
    # 1st Order Markov List
    firstOrderDict = {}


    s1 = converter.parse('invent1.mid').iter
    firstList = []
    for el in s1:
        for notes in el.notes:
            if notes.isNote:
                firstList.append(notes)

    # Counts the number of transitions from one note to another
    previousNote = None
    for currentNote in firstList:
        if previousNote != None:
            transitionName = previousNote.name + "->" + currentNote.name
            if transitionName in firstOrderDict:
                firstOrderDict[transitionName] += 1
            else:
                firstOrderDict[transitionName] = 1
        previousNote = currentNote

    print(firstOrderDict)

if __name__ == '__main__':
    main()
