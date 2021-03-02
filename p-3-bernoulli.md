# The Bernoulli Experiment

## Objectives for this lesson
***
- Learn about the Bernoulli experiment

A Bernoulli experiment is an experiment for which the probability a certain event occurs is  <img src="https://render.githubusercontent.com/render/math?math=p"> and the probability the event does not occur is <img src="https://render.githubusercontent.com/render/math?math=(1-p)">; or in other words, the event is has two possible outcomes: one event occurring with probability <img src="https://render.githubusercontent.com/render/math?math=p"> and the other one with probability <img src="https://render.githubusercontent.com/render/math?math=(1-p)">.

> **EXAMPLE 1**: A classical example of the Bernoulli experiment is flipping a coin. When flipping a coin, <img src="https://render.githubusercontent.com/render/math?math=p"> is equal to 0.5, and the probability of heads is 0.5, as well as the probability of tails, which is the other possible event, is <img src="https://render.githubusercontent.com/render/math?math=(1-0.5 = 0.5)">.


> **EXAMPLE 2**: The probability of scoring a point when being granted a penalty kick in soccer is 0.8. In this case the Bernoulli experiment is whether someone scores or not: <img src="https://render.githubusercontent.com/render/math?math=p"> is equal to 0.8, and the probability of not scoring is <img src="https://render.githubusercontent.com/render/math?math=(1-p = 1-0.8 =0.2)">.

We can use Python to design a Bernoulli experiment. Let's look at the code we use to generate the Bernoulli experiment that equals tossing a coin:

```python
import numpy as np
print(np.random.binomial(1, 0.5, 1))
```
The first line of code imports the Python `NumPy` library. A library is essentially an open-source reusable chunk of code that you may want to include in your programs / projects. All you need to know is that NumPy is a library widely used in Python, and will help you solve some of the problems you'll see in this course.

The second line of code uses the `random.binomial` function in the NumPy library to run a Bernoulli experiment. The function `random.binomial` takes in three so-called "arguments" here:
  - The first argument represents the number of trials - or how many coin flips we're doing in each experiment
  - The second argument represents <img src="https://render.githubusercontent.com/render/math?math=p"> or the probability of "success". 
  - The third argument represents how many experiments you're running (if the difference between argument 1 and 3 is not entirely clear at this time, don't worry - it will become clear later!)
        
Now, run the codeblock below by clicking the right green arrow. You'll see that you either see "1" (= success, say head) as an output, or "0" (no success, say tail). Let's say that we consider head as success, that means running this experiment (or running this code cell) is exactly the same as tossing a coin. Run the code a few times and see how you'll sometimes get a 1 and sometimes a 0!        

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>