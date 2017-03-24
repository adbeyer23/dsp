[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```
%matplotlib inline
import thinkstats2
import thinkplot
import nsfg
resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='unbiased')
biased_pmf = BiasPmf(pmf, "biased")
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Config(xlabel="Number of kids", ylabel='PMF')
pmf.Mean()
biased_pmf.Mean()
```

Unbiased mean: 1.02
Biased mean: 2.4
