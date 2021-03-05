# Calculating Profit on any given night

## Objectives for this lesson

***

From what you've seen before, it looks like overbooking your hotel seems like a potential solution to use the full capacity of your hotel in an optimal way. But how many rooms should you overbook? The answer depends on the cost structure of overbooking.

For our hotel, we have the following information:

- Our customers pay a price of $220 USD per night for our hotel.
- If on any night we have fewer rooms available than hotel guests, we have to place customers at a competitor hotel, which costs us $400 USD. 


This means that we end up losing $180 USD per room that is overbooked, when more guests show up than number of rooms available.


The total profit on any given night is equal to:

 <img src="https://render.githubusercontent.com/render/math?math=\text{Profit} = 220 \times \text{(number of booked rooms)} - 400 \times \text{(number of rooms booked - 100 [if more than 100 rooms were booked] )} "> 


Let's say that in total 104 guests booked a room on a given night, and only 99 show up. Our expected profit that night is then equal to:

 <img src="https://render.githubusercontent.com/render/math?math=\text{Profit} = 220 \times 104 = 22,880 "> USD

Note how the hotel benefits from overbooking because the customers fully prepay! 


On the other hand, if we overbooked and 104 guests and all of them show up on one given night, the expected is then equal to:


 <img src="https://render.githubusercontent.com/render/math?math=\text{Profit} = 220 \times 104 - 400 \times 4  = 21,280 "> USD

## Expected Profit when overbooking at 104 rooms

Previously, you saw how overbooking at 104 rooms can give very different profits depending on how many guests actually end up staying in the hotel. Overbooking is a great tool to make more money, but can end up being costly if more hotel guests end up staying than rooms are available.

In this section, we'll look into what our hotel's expected profit is when overbooking 104 rooms.

We can achieve getting the expected profit by taking the following 3 steps:
- Run a Bernoulli experiment like you did before, this time with <img src="https://render.githubusercontent.com/render/math?math=n=104"> instead of <img src="https://render.githubusercontent.com/render/math?math=n=100">. Let's run the experiment 10,000 times.
- For each of the potential outcomes, we'll calculate the profit.
- Next, we'll calculate the _expected profit_. You'll learn how to do that in a bit!

### 1) The Bernoulli Experiment when booking 104 rooms

Let's run a Bernoulli experiment of what happens if we allow 104 rooms to be booked, knowing that on average, there is a 92% "success rate", in other words, 8% of hotel customers don't end up staying at the hotel. We'll run the experiment 10,000 times. 

Let's create a plot to analyze what we're seeing. Use the dropdown in the widget below to see how the number of bookings can affect the outcome.

<iframe height="900px" width="100%" src="https://learn-co-curriculum.github.io/dsc-overbooking-try-experience-widgets/widget_3.html"></iframe>

As you can see here, the majority of the nights, around 94 to 98 rooms end up being occupied. Next, let's create a similar plot but looking at the profit on the y-axis. We'll have to use some of the financial information to get there, but we'll explain the code step by step

### 2) The Profit Distribution when booking 104 rooms

Next, let's use our array that stores 10,000 random experiments of 104 room bookings and eventual turnout, and let's use that array to calculate the profit that the hotel would make in each of the 10,000 cases. To get there, we need to calculate:
- The revenue
- The cost
- Profit = Revenue - Cost

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli9?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Let's plot the resulting "profit distribution"

<iframe height="900px" width="100%" src="https://learn-co-curriculum.github.io/dsc-overbooking-try-experience-widgets/widget_3.html"></iframe>

### 3) The Expected Profit

Now what is our actual "expected profit"? The answer is not complicated: you can simply take the average of all the entire profit distribution, so you'll sum up all 10,000 elements in your array, and divide them by 10,000!

<iframe height="400px" width="100%" src="https://repl.it/@DSExperience/Bernoulli10?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

The expected profit when booking 104 rooms on any given night is around $21,035 USD!

## Recap

***

We now know what the expected profit is when booking 104 rooms. Now, we'll want to do this very same analysis again for 103 rooms. And for 102 rooms and for 105 rooms! Lets take a look at how we decide this in the next lesson.