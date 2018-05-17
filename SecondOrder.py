from music21 import *

# Random Notes for Testing
noteA = note.Note('A4')
noteB = note.Note('B4')
noteC = note.Note('C4')
noteD = note.Note('D4')
noteE = note.Note('E4')
noteF = note.Note('F4')
noteG = note.Note('G4')

def main():
    # 2nd Order Markov List
    secondOrderList = {}
    
    # Adds Notes to Array
    secondList = []
    secondList.append(noteA)
    secondList.append(noteB)
    secondList.append(noteC)
    secondList.append(noteD)
    secondList.append(noteE)
    secondList.append(noteF)
    secondList.append(noteG)
    secondList.append(noteA)
    secondList.append(noteB)
    secondList.append(noteC)
     
    # Counts the number of transitions
    i = 0
    for notes in secondList:
        if i == 0:
            i += 1
            firstNote = notes
        elif i == 1:
            i += 1
            secondNote = notes
        else:
            transition = firstNote.name + '->' + secondNote.name + '->' + notes.name
            if transition in secondOrderList:
                secondOrderList[transition] += 1
            else:
                secondOrderList[transition] = 1
            firstNote = secondNote
            secondNote = notes
    print(secondOrderList)
        
if __name__ == '__main__':
    main()