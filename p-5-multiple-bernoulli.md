# Repeated Bernoulli Experiments

## Objectives for this lesson

***

- Learn about the binomial distribution
- Understand how the Bernoulli experiments can be scaled
- Calculate the probability of an event

## The Binomial Distribution

***

What you've been seeing here is the groundwork of what is called the **binomial distribution**. The binomial distribution is essentially a probability distribution that represents the likelihood of obtaining a predetermined number of successes (say, *r*) in a predetermined number of trials (say, *n*). Like in the Bernoulli experiment, you also need to know ahead of time what the probability of success is (say,  <img src="https://render.githubusercontent.com/render/math?math=p"> ).

> *Example*: What is the probability of obtaining "heads" 4 times, when flipping 5 coins? 

In this example,  <img src="https://render.githubusercontent.com/render/math?math=r=4"> ,  <img src="https://render.githubusercontent.com/render/math?math=n=5"> and (because we're talking about a coin flip)  <img src="https://render.githubusercontent.com/render/math?math=p=0.5"> .

The answer to this question (and Binomial distribution as a whole) can be derived mathematically, but in this lesson we'll be **using Python** to get to the answer by repeating the experiment a very high number of times (say, 1000 or even 10000). If it doesn't immediately click, don't worry, you'll see what we mean in a bit!

Let's use `np.random.binomial` and run the experiment "flipping 5 coins" 20 times. 

If you use the function correctly, the output will for each of the 20 experiments, simulate how many times "heads" was obtained.

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli5?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>Let's take a moment to understand what the output of this function is.  When we run this function the result is a list of numbers.  Each of these numbers represents the result of an experiment of flipping 5 coins.  It tells us the total number of successes, or in our case, the number of heads from the 5 flips.

Out of these 20 experiments, there were _four_ instances of "obtaining heads 4 times". So here, you obtained the desired outcome in 4 experiments out of the 20 experiments, so 20% of the time.

## Calculating the probability

***

Now, to get an accurate approximation of exactly what the probability is of getting 4 times heads, we need to repeat this experiment far more than 20 times. Below, we'll run the experiment 1000 times, 10,000 times, and 100,000 times. We'll store the list of outcomes in variables that we will call: `n_1000`, `n_10000` and `n_100000`.

Next, to get an understanding of what the proportion of "4"'s is ("how many of my trials resulted in obtaining heads 4 times"), we can use the following code:

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli7?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

When looking at the results, it looks like the probability of getting 4 heads when flipping a coin 5 times is somewhere between  15% and  16%. For those of you who like to dive into the mathematics, this probability can actually be calculated mathematically as well! The "binomial probability" can be calculated as follows (don't worry if what follows doesn't immediately click - you'll get really familiar with all this in Flatiron School's Data Science Program):

 <img src="https://render.githubusercontent.com/render/math?math=P(X=r) = \displaystyle {n\choose r}p^r (1-p)^{n-r}"> 

where

 <img src="https://render.githubusercontent.com/render/math?math=\displaystyle {n\choose r} = \dfrac{n!}{k!(n-k)!}"> 


 <img src="https://render.githubusercontent.com/render/math?math=n!"> is "n factorial". You can calculate  <img src="https://render.githubusercontent.com/render/math?math=n!"> as <img src="https://render.githubusercontent.com/render/math?math=n*(n-1) * (n-2) * 1">. In this case, our <img src="https://render.githubusercontent.com/render/math?math=n = 5"> and  <img src="https://render.githubusercontent.com/render/math?math=5"> factorial is,  <img src="https://render.githubusercontent.com/render/math?math=5!= 5*4*3*2*1 = 120">. Applying this formula to our problem:


 <img src="https://render.githubusercontent.com/render/math?math=P(X=4)=\dfrac{5!}{4!(1)!} 0.5^4 (0.5)^{1} =0.15625 "> or 15.625% , which is indeed between 15% and 16% as indicated by repeating our experiments thousands of times!

## Recap

***

In this lesson we took a look at the binomial distribution and calculated the probability of an event.  These numbers are great and give us some good data to work with.  In the next lesson we will take a look at how we can visualize these numbers to gain some insight.