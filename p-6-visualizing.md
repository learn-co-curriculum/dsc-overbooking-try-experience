# Visualizing flipping a coin

## Objectives for this lesson

- Visualize the probability of customers not showing for a booked room
- Calculate the best number of rooms to overbook for the best profitability.
***

To get a full picture on how likely it is to throw a heads a certain number of times, you can visualize this in a plot. In the plot below, you can see for each possible outcome (ranging from "throwing heads 0 times" to "throwing heads 5 times" how likely it is: for 4 heads, you see it's about 16% chance. For 3 heads, it's about 31%. In the widget below, you can chose the number of experiments being performed and see the effect it has on the graph.

<iframe height="500px" width="100%" src="https://learn-co-curriculum.github.io/dsc-overbooking-try-experience-widgets/widget_1.html"></iframe>

## Bernoulli experiments to model room bookings

If you have 100 hotel rooms, in an ideal world, you have all of your 100 rooms booked every night.
However, a room booking still holds uncertainty in itself. When someone booked a room at the hotel, the hotel guest showing up is still not 100% certain. In that sense, the "guest showing up" is a probability event at itself, except (hopefully!) with a much higher chance than 50% in the event of a coin toss. in our hotel, on average, 8% of the customers who book a room don't end up staying on a given night.

Let's check in Python what we can expect in terms of room bookings. We'll use NumPy again, and run the "experiment" so we can create a plot like the one before. Use the dropdown box to adjust the number of experiments to see how the result is affected.

<iframe height="900px" width="100%" src="https://learn-co-curriculum.github.io/dsc-overbooking-try-experience-widgets/widget_2.html"></iframe>

If you select `100,000` you can see in this plot, the probability that exactly all guests that booked rooms, is virtually 0. Out of the 100,000 experiments we ran, only 20 times all 100 rooms are booked (you can't even see that with the naked eye!). This is one night out of every ~14 years!

## Recap

***

In this lesson we were able to visualize the probability using a bar chart, and we also were able to see the how the accuracy is much better with more experiments. In the next lesson we will look at how we can use this information to calculate our best profitability.

