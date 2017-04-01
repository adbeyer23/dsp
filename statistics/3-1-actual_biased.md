
```{r test-python, engine='python'}

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
