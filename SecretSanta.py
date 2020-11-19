### Secret Santa and Secret Santa Quizmaster code

import random
import os


def generateSecretSanta(names, invalidRelationships):
    people2 = [a for a in names]
    d1 = {a:b for a,b in invalidRelationships}
    d2 = {b:a for a,b in invalidRelationships}

    validSets = False

    while not validSets:
        valid = True
        random.shuffle(people2)
        for p1, p2 in zip(names, people2):
            if p1 == p2:
                valid = False
            if p1 in d1:
                if d1[p1] == p2:
                    valid = False
            if p1 in d2:
                if d2[p1] == p2:
                    valid = False
            pairs1 = [(a, b) for a, b in zip(names, people2)]
            pairs2 = [(b, a) for a, b in zip(names, people2)]
            for a in pairs1:
                for b in pairs2:
                    if a == b:
                        valid = False
        if valid:
            validSets = True
    return [(a, b) for a,b in zip(names, people2)]


def writeMessage(pairs, path):
    for p in pairs:
        with open(path + '/{}SecretSanta.txt'.format(p[0]), 'w') as f:
            f.write('Dear {},\n\n'.format(p[0]))
            f.write('The person who you are buying a Secret Santa present for is {}.\n\nPresents can be up to £30 and are to be given out on Christmas Day.\n\nYours sincerely,\n\nSecret Santa'.format(p[1]))
    return


def writeQuizPairs(pairs, path, picture):
    for p, pic in zip(pairs, picture):
        with open(path + '/{}SecretSanta.txt'.format(p[0]), 'w') as f:
            f.write('Dear {},\n\n'.format(p[0]))
            f.write('The person who you are choosing a quiz topic for is {}.'.format(p[1]))
            if pic:
                f.write(' Their round is to be a picture round, please remember to tell them that it is.')
            f.write(' The quiz will be next Friday, please give your person the topic by the end of Tuesday.')
            f.write('\n\nYours sincerely,\n\nThe not so secret Quizmaster (Santa in disguise).')
    return


def loadPreviousEditions(path):
    files = [a for a in os.listdir(path) if 'SecretSanta' in a]
    names = [a[:-15] for a in files]

    relations = {}
    pictures = []

    for nom in names:
        relations[nom] = []
        for a in [a for a in files if nom in a]:
            with open(r'{}\{}'.format(path, a), 'r') as f:
                data = f.readlines()[2]
                for n in names:
                    if n in data:
                        relations[nom].append(n)
                        if 'picture' in data:
                            pictures.append(n)
    final = [[(key, val) for val in relations[key]] for key in relations]
    final = [item for sublist in final for item in sublist]

    return final, pictures


def getPicturePeople(names, prev):
    pos = [a for a in names if a not in prev]

    if not pos:
        counts = {key: len([a for a in prev if a == key]) for key in names}
        maxCounts = max([counts[key] for key in names])
        pos = [a for a in names if counts[a] != maxCounts]

    return random.sample(pos, 2)


if __name__ == '__main__':
    ### Important ###
    # Remember to customise the message to what you want it to be, use the deault as an example
    #################


    # Secret Santa example
    people = ['A', 'B', 'C', 'D', 'E', 'F']  # Put a list of people in here
    couples = [('A', 'B'), ('E', 'F')]  # Put a list in here of all not allowed pairings
    previous, _ = loadPreviousEditions('[Path to folder of previous messages]')  # Put the path of a folder in here which contains any previous messages you sent and don't want pairs repeating of
    forbiddenRelations = couples + previous
    pairings = generateSecretSanta(people, forbiddenRelations)  # Generate the pairings
    writeMessage(pairings, '[path to write files in]')

    # Quiz example
    people = ['A', 'B', 'C', 'D', 'E', 'F']  # Put a list of people in here
    couples = [('A', 'B'), ('E', 'F')]  # Put a list in here of all not allowed pairings
    previous, previousPictures = loadPreviousEditions('[Path to folder of previous messages]')  # Put the path of a folder in here which contains any previous messages you sent and don't want pairs repeating of
    forbiddenRelations = couples + previous
    pairings = generateSecretSanta(people, forbiddenRelations)  # Generate the pairings
    pics = getPicturePeople(people, previousPictures)
    pics = [p if p in pics else False for p in people]
    writeQuizPairs(pairings, '[path to write files in]', pics)