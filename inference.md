Statistical inference
=====================

Probability and statistics can be considered one as the inverse problem
of the other. In the previous chapters we studied what is the theory of
probability. Given a probability density function (p.d.f) describing the
problem at hand, we can *calculate* in a straightforward way the
probability of any outcome. Statistics deals with the inverse problem.
Given a set of data which samples an unknown parent distribution it
allows to *infer*[^1] some characteristics of the parent distribution.\
The statistical inference gets different names depending on the specific
problem to which is applied:

-   *parameter estimation*: you have a set of data which you think is
    distributed according to a parent distribution and you want to
    estimate its parameters (e.g. the parent distribution is a Gaussian
    and you want its mean and width). This procedure is also called
    *fitting*.

-   *hypothesis testing*: you have a set of data and you want to know
    whether they are distributed according to some parent distribution
    (e.g. you want to accept or reject the hypothesis that your data are
    distributed according to a Gaussian distribution)

The two problems are clearly intertwined: it doesn't make sense to
perform a parameter estimation without an hypothesis on the p.d.f. to be
tested and often in order to accept or reject that data are distributed
according to a p.d.f. we need to estimate its parameters.\
\
In order to proceed further in the treatment of statistical inference we
define what we mean by statistics. *A statistic is any function of the
data sample*. Being a function of random variables the statistics is
itself a random variable and its p.d.f. is usually called the *sampling
distribution* of sampling p.d.f., to distinguish it from the *parent
distribution*. A statistic does not depend on any of the characteristics
of the unknown parent distribution. Examples of statistics are the mean
of a sample or even just the data themselves.\
The two approaches to the probability theory, frequentist and bayesian,
give rise to two approaches to statistical inference, bayesian
statistics and frequentist statistics. In the next chapters, we will
discuss the implications of the two approaches will be.

[^1]: Infer = deduce or conclude from evidence and reasoning rather than
    from explicit statements
