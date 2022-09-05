from pathlib import Path
import random
from string import *
import os

os.chdir('insert path here')
clues = 'questions.txt'

def randomizer():

    [oldFile.unlink() for oldFile in Path('Insert path here/folder name').glob("*") if oldFile.is_file()] 

    inClues = open(clues, 'rt')
    lineList = inClues.read().splitlines()

    os.chdir('Insert path here/folder name to save to')

    qty = int(input('How many different sheets would you like? '))

    for i in range(0, qty):
        random.shuffle(lineList)
        output = f'sheet{i + 1}.txt'
        with open(output, 'w') as outClues:
            outClues.write('\t\t\t\tCS Club Scavenger Hunt\n\n\n')
            outClues.write('Team Name:_____________________________________________\n\n')
            for num in range(0, len(lineList)):
                outClues.write(f'{num + 1}. {lineList[num]}\n\n\n')    

    inClues.close()
    outClues.close()

    print('Done!')

randomizer()

