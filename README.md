Consider 20 independent repetitions of drawing a bulb from a lot. 

Probability that the bulb drawn will work for more than 500 hrs is 0.2. 

Plot a probability distribution using python or scilab for getting k success in 20 trial


If I do something that has a constant probability of success - how many times do I need to do it to ensure that, on average, 
I'll be successful?


If you succeed with probability  ð  independently of all previous attempts, then the probability you succeed at least once 
after  ð  tries is  1â(1âð)ð . To succeed at least once on average you need

1â(1âð)ðâ¥0.5 
(1âð)ðâ¤0.5 
ðlog2(1âð)â¤â1 
ðâ¥â1log2(1âð) 

Edit: The difference between this answer and the other common answer of  1/ð  lies in the interpretation of the question, which 
is somewhat ambiguous. My answer gives  ð , the number of flips needed so that after performing  ð  trials, the probability of 
having succeeded at least once is at least  0.5 . The answer  1/ð  is the average number of trials you will perform until you 
succeed once.

The difference is easily apparent for  ð=1/2 . My solution gives the answer  ð=1  since after one trial you will have 
succeeded half the time. The average number of trials you would perform to succeed once is greater than this because the minimum 
possible number of trials you could perform is one and sometimes it takes longer than that.
