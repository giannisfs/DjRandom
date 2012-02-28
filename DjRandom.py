
SHUFFLESTATES = []
MAXUNIQSTATES = 2000
LIMIT = 40000
MUSICLIST = range(10)



import random , copy

class DjRandom():
    def __init__(self):
        pass
    
#python changes data inside lists because append just adds a pointer to the same object 
#so i will change the following function... the copy module should help... 
#but it seems it is a horrible solution to make new object as often as the most numbered operations.... 
def stateFulShuffle(seq):
    global SHUFFLESTATE
    Seq = copy.copy(seq)
    counter = 0
    seen = set()
    while counter < MAXUNIQSTATES :
        if Seq in SHUFFLESTATES:
            counter += 1
            Seq = copy.copy(Seq)
            random.shuffle(Seq)
        elif Seq not in SHUFFLESTATES:
            Seq = copy.copy(Seq)
            print Seq ,'aa'
            SHUFFLESTATES.append(Seq)
            print Seq ,'aa'
            random.shuffle(Seq)
    return #SHUFFLESTATE






        
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


