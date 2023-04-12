# https://www.codewars.com/kata/fruit-machine/train/python
import collections
def fruit(spins, *reel):
	d = {x:10-i for i,x in enumerate(["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"])}
    cnter = collections.Counter(reel[n] for reel,n in zip(reels, spins))
    return sum(d[k]*([0,1,10][v-1]) for k,v in cnter.items()) * [1,2][cnter["Wild"] == 1]