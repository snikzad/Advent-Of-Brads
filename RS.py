import fractions
import itertools
import sys
'''
Richard Sowers 2016-06-17
makes list of integer pairs [m_x,m_y] corresponding
to slopes m_y/m_x (including 1/0 and -1/0)
must have |m_x|+|m_y|<=N
Usage
python RationalSlopes.py 5
gives integer pairs for N=5
'''


def RationalSlopes(N):
	def toDouble(myFraction):
		return float(myFraction)
	m_y_range=range(-N,N+1)
	m_x_range=range(1,N)
	square=list(itertools.product(m_x_range,m_y_range))
	Diamond = [fractions.Fraction(m_y,m_x) for [m_x,m_y] in square
		if (abs(m_x)+abs(m_y)<=N)]
		#disallow /0's 
	DiamondSet=list(frozenset(Diamond))
	DiamondSet.sort(key=toDouble)
	newsquare=[[F.denominator,F.numerator] for F in DiamondSet]
	newsquare=[[0,-1]]+newsquare+[[0,1]]	
	return newsquare


