from csv import DictReader
import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff
 
#print(random.randint(1,6))
diceResult = []
count = []
for i in range(0,100):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    diceResult.append(d1+d2)
    count.append(i)
#fig = px.bar(x=diceResult,y=count)
 
#fig = ff.create_distplot([diceResult],["result"])
#fig.show()
#print(len(diceResult))
mean = sum(diceResult)/len(diceResult)
stddev = statistics.stdev(diceResult)
median = statistics.median(diceResult)
mode = statistics.median(diceResult)

firstSdStart,firstSdEnd = mean-stddev,mean+stddev
secSdStart,secSdEnd = mean-(stddev*2),mean+(stddev*2)
thirdSdStart,thirdStEnd = mean-(stddev*3),mean+(stddev*3)
