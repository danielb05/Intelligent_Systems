# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # answerDiscount = 0.9
    # answerNoise = 0.2
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    # answerDiscount = None
    # answerNoise = None
    # answerLivingReward = None
    # return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'
    
    # Living Reward high enough to not be worth to go for the distant exit,
    # but low enough to not jum in the pit
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = -4.5
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    
    # Too much noise, not worth taking chances in the short path
    answerDiscount = 0.6
    answerNoise = 0.4
    answerLivingReward = -0.8
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    
    # No noise, so its safe to pass
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = -0.2
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    
    # Some noise, but too little discount for living, so better not risk to fall
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = -0.2
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    
    # Living reward positive, so its better to keep alive winning points
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 2
    return answerDiscount, answerNoise, answerLivingReward

def question6():
    answerEpsilon = None
    answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    
    # Not possible, because there ar too many possibilities of falling in the pit, so 50 interations is not enough to be 
    # highly likely (greater than 99%) to learn the optimal policy
    
    # If not possible, return 'NOT POSSIBLE'
    return 'NOT POSSIBLE'
    

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
