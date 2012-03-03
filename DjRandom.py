
states = set()
MAXRANDOMTHRESHOLD = 12





import random , copy , cPickle


class DjRandom():
    def __init__(self):
        pass


def SaveShuffleState(state):
    #hash(stateFulShuffle(x).next().__repr__())
    state = hash(state.__repr__())
    File = open("DjRandomShuffle.states","wb")
    cPickle.dump(state,File)
    File.close()

def checkIfStateExists(state):
    File = open("DjRandomShuffle.states","rb")
    states = cPickle.load(File)
    File.close()
    
    if hash(state.__repr__()) in states:
        return True
    
def stateFulShuffle(seq):
    try:
        File = open("DjRandomShuffle.states","rb")
        states = cPickle.load(File)
        File.close()        
    except IOError:
        File = open("DjRandomShuffle.states","wb")
        
        
    #global states
    counter = 0
    while counter < MAXRANDOMTHRESHOLD :
        # if more than 12 times in a raw , seq happens to exist inside states
        # that means that generously either randomness has been exausted
        # either (in other words) there are no more unique sequences left... ;) hell yeah
        if tuple(seq) in states:
            counter += 1
            random.shuffle(seq)
        elif tuple(seq) not in states:
            counter = 0
            states.add(tuple(seq))
            yield seq
#HERE signal handler function when application exits in order to save the state
#http://www.doughellmann.com/PyMOTW/signal/
    




        
def stateFullRandom(seq):
    SEQ = copy.deepcopy(seq)
    seen = set()
    while  SEQ :
        NUM = random.choice(SEQ)
        if NUM not in seen:
            try:
                seen.add(NUM)
                SEQ.pop(SEQ.index(NUM))
                yield NUM
            except IndexError:
                NUM = random.choice(SEQ)
                print 'INDEX ERROR'
        
        else:
            NUM = random.choice(SEQ)
            print 'ELSE CLAUSE'


