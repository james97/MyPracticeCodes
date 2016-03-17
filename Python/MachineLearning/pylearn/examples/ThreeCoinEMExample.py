#########################################################################
# File Name: ThreeCoinEMExample.py
# Author: Jun M
# mail: warrior97@gmail.com
# Created Time: Tue 10 Nov 20:09:47 2015
#########################################################################
#!/usr/bin/env python
'''
This program is written to simulate the 3 coin problem. 
The 3 coin problem is flipping coinA to select Coin B or C, and then flip the
selected coin to generate a sample. Without knowing which coin is selected, 
how to use EM to estimate the probabilities for CoinB and C to get a header.
'''
import random
import math


def flipCoin(prob):
	border = random.random()
	if border < prob:
		return 1
	else:
		return 0


def coinSeqGenerator(flipAmount, prob):
	coinSeq = []
	if (flipAmount <= 0):
		return coinSeq
	else:
		for i in range(flipAmount):
			coinSeq.append(flipCoin(prob))

	return coinSeq

def threeCoinEMExample(samples):
	currCoinBprob = 0.4
	currCoinCprob = 0.8
	prevCoinBprob = 0
	prevCoinCprob = 0

	while(math.fabs(currCoinBprob - prevCoinBprob)> 0.01) and (math.fabs(currCoinCprob - prevCoinCprob)> 0.01):

		coinBHdCnt  = 0.0
		coinBTlCnt  = 0.0
		coinCHdCnt  = 0.0
		coinCTlCnt  = 0.0
		###E-step
		for sample in samples:

			hdCnt = len([x for x in sample if x == 1])
			tailCnt = len(sample) - hdCnt
			probB = currCoinBprob ** hdCnt * (1 - currCoinBprob) ** tailCnt
			probC = currCoinCprob ** hdCnt * (1 - currCoinCprob) ** tailCnt
			weightB = probB/(probB+probC)
			weightC = 1 - weightB
			#print "weights are {} and {} for B and C".format(weightB, weightC)
			coinBHdCnt += hdCnt * weightB
			coinBTlCnt += tailCnt * weightB
			coinCHdCnt += hdCnt * weightC
			coinCTlCnt += tailCnt * weightC
					###M-step
		prevCoinBprob = currCoinBprob
		prevCoinCprob = currCoinCprob
		currCoinBprob = coinBHdCnt/(coinBHdCnt + coinBTlCnt)
		currCoinCprob = coinCHdCnt/(coinCHdCnt + coinCTlCnt)
		print "current prob for B and C are:{} {} ".format(currCoinBprob, currCoinCprob)


probCoinA = 0.2  ##Coin A is used to select the other two coins
probCoinB = 0.33
probCoinC = 0.68
print "Set head probabilities of Coin A B C to {}, {} and {}".format(probCoinA,
        probCoinB, probCoinC)

sampleCoin = coinSeqGenerator(1000, probCoinA)
wholeSamples = []
for selection in sampleCoin:
	if selection == 1:
		wholeSamples.append(coinSeqGenerator(50, probCoinB))
	else:
		wholeSamples.append(coinSeqGenerator(50, probCoinC))

threeCoinEMExample(wholeSamples)

