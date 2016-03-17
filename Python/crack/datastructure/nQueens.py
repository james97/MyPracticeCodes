

def conflict(state, nextX): 
            nextY = len(state)
            for i in range(nextY):
                if (abs(state[i]-nextX) in (0,nextY-i)):
                    return True
            return False


def queens(num=8,state=()):
            for pos in range(num):
                if not conflict(state,pos):
                    if len(state)==num-1:
                        yield(pos,)
                    else:
                        for result in queens(num,state+(pos,)):
                            yield (pos,)+result


def isQueenSafe(currentStep, pos):
	currLength = len(currentStep)
	for i in range(currLength):
		if (abs(pos - currentStep[i]) in (0, currLength -i)):
			return False
	return True      

def nQueens(num = 8, currentStep = ()):
	for pos in range(num):
		if isQueenSafe(currentStep,pos):
			if len(currentStep) == num -1:
				yield (pos,)
			else:
				print currentStep
				for result in nQueens(num, currentStep+(pos,)):
					yield (pos,)+ result
			                 

for i in nQueens(4,):
	print i