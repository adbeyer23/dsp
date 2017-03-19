[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```{python}
import nsfg
import numpy as np
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
first = live[live.birthord == 1]
other = live[live.birthord != 1]
first_mean = first.totalwgt_lb.mean()
other_mean = other.totalwgt_lb.mean()
first_std = first.totalwgt_lb.std()
other_std = other.totalwgt_lb.std()
first_num = len(first.totalwgt_lb)
other_num = len(other.totalwgt_lb)

pooled_std = np.sqrt(((first_std**2 * first_num) + (other_std**2 * other_num)) / (first_num + other_num))
effect_size = (first_mean - other_mean) / pooled_std

'''
Answer: -.089. This effect size is bigger than that of pregnancy length between first born and other born babies, but both effect sizes are very small, and probably not very relevant. 
