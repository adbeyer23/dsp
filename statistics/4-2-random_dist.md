```{r test-python, engine='python'}
import numpy 
import thinkplot
% matplotlib inline
numbers = [numpy.random.random() for x in range(1000)]
import thinkstats2
numbers_pmf = thinkstats2.Pmf(numbers)
cdf = thinkstats2.Cdf(numbers)
thinkplot.Pmf(numbers_pmf)
thinkplot.Cdf(cdf)
```
It's really hard to tell from the Pmf what's going on here as the graph is just a blue box. From the Cdf we see what is almost a straight, diagonial line, which suggests that each value has the same probability as being picked and that the distribution is truly uniform. I changed the amount of random numbers from 1000 to 10000 and the line is even straighter.
