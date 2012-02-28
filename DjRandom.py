
SHUFFLESTATES = []
MAXUNIQSTATES = 2000
LIMIT = 40000
MUSICLIST = range(10)



import random , copy

class DjRandom():
    def __init__(self):
        pass
    
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


##def stateFulShuffle(seq):
##    seq = copy.copy(Bseq)
##    def shuffle(seq):
##        global SHUFFLESTATE
##        SHUFFLESTATE.append(copy.copy(seq))
##        c = 0
##        while True:
##            random.shuffle(seq)
##            iSeq = copy.copy(seq)
##            if iSeq not in SHUFFLESTATE:
##                if len(SHUFFLESTATE) > MAXUNIQSTATES:
##                    del(SHUFFLESTATE)
##                    SHUFFLESTATE = []
##                    break
##                SHUFFLESTATE.append(iSeq)
##                print iSeq
##                c =0
##                yield iSeq
##                
##            elif c <= LIMIT:
##                c += 1
##            else:
##                random.shuffle(seq)
##                print 'BREAK'
##                break
##            
##    return shuffle(seq).next()






        
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


