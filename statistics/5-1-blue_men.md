[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```{python} 
import scipy
lower_cutoff = 177.8 
higher_cutoff = 185.4
mu = 178
std = 7.7
blue_man = scipy.stats.norm(mu, std)
low = blue_man.cdf(177.8)
high = blue_man.cdf(185.4)
percentage_of_men = high-low

Answer = .342
