 # Building the experiment

 ## Objectives for this lesson

 ***

 - Learn about 
 
 ## Designing the experiment

 *** 

 In the previous lesson we learned how to simulate the toss of a coin using NumPy's random.binomial function.  Flipping a coin once is not much of an experiment, so n this lesson we will look at using that function to perform multiple coin tosses and look at the results.
 
 We saw in our first experiment that the outcome of the coin flip is **random**, but if you run it enough times you'll notice that about half of the times, you'll get 1 about half of the time and 0 about half of the time.  Let's take a look at what it looks like when we run the experiment 10 times.
 >Remember to click on the <a style="color: green">Green</a> arrow to initialize the code console.

 <iframe height="600px" width="100%" src="https://repl.it/@DSExperience/Bernoulli2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

 The code in the console above is also known as a "for loop" - this for loop repeats an operation ((in our case, the random experiment of flipping a coin) 10 times. In other words, you're **running 10 experiments**. Remember that you get a similar type outcome if you change the third argument in the `np.random.binomial()` function to 10, as this is the argument that represents "number of experiments".

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

The code above is also known as a "for loop" - this for loop repeats an operation ((in our case, the random experiment of flipping a coin) 10 times. In other words, you're **running 10 experiments**. Remember that you get a similar type outcome if you change the third argument in the `np.random.binomial()` function to 10, as this is the argument that represents "number of experiments".

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Next, let's look at what happens if we change the first parameter from 1 to 20.

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli4?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="no" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>