## Using Python to define Optimal numbers of rooms booked

## Objectives for this lesson

- Look at the final results of the experiment

***

Below you can see a simulation using a for loop to iterate through a number of rooms booked and conducting the bernouli experiment using each of the numbers in the range from _97_ to _120_.  The results are then plotted on a graph for you to visualize the profit associated with each number of rooms booked.  Below is the code in Python to accomplish this along with descriptions of what is happening in the code.

## Declaring variables

***

To begin this final experiment, we first need to define some of the variables we will be using.  Below is the code followed by the description.

``` python
revenue = 220 * booking_104
cost = (booking_104 - 100) * 400
cost_final = np.where(cost<0, 0, cost) 
profit = revenue - cost_final
```
First we determine the income we would recieve from each of experiments we performed.  In this line of code, the result of each of the experiments is multiplied by the cost of each room, $220. We then store this in a variable called _revenue_.  
`revenue = 220 * booking_104`

Next, we calculate the cost of placing a customer with another hotel if we don't have a room avaliable.  In this case, for every room we book, over our occupancy, it costs us $400.  we store this value in a variable called _cost_.  
`cost = (booking_104 - 100) * 400`

Then we need to correct for negative cost.  Here we use the `.where()` function from the `numpy` library. In our case we want the cost if it is positive, but if it is less than 0 we will use 0 so we don't have a negative cost.  We store this information in a variable called *cost_final*.   
`cost_final = np.where(cost<0, 0, cost)`

Finally we are able to calculate our profit using these calculations by subtracting *cost_final* from _revenue_.  We store this using the variable _profit_.  
`profit = revenue - cost_final`

## Simulating multuple experiments

*** 

In the loop below we use the above variables along with the code from the experiments we did before to perform the experiment for each number of rooms booked between _97_ and _120_ and store the profit form each in a list.  The code for this is below.

``` python
n_experiments = 10000 # The number of experiments performed 
rooms_in_loop = range(97,121) # creates a range of numbers from 97 to 120 to iterate through.
all_profits = [] # an empty list to store our results

for r in rooms_in_loop: # selects each number in our range and assigns the value to r
    bookings = np.random.binomial(r, 0.92, n_experiments) # simulates 10000 experiments
    revenue = 220 * bookings
    cost =  (bookings - 100) * 400
    cost_final = np.where(cost<0, 0, cost) 
    profit = revenue - cost_final
    expected_profit = np.sum(profit)/ n_experiments 
    all_profits.append(expected_profit)
```
## Graphing the experiment results

***

Now that we have simulated 10,000 experiments for each number of overbookings, we can graph the resulting profits to see which will yield us the best profit. To do this we use a library in Python called _matplotlib.pyplot_ which has been assigned to the common alias _plt_ so we don't have to type it all out everytime we want to use it.  With the command below, we are able to generate a simple line plot so we can visualize the number of overbooked rooms and the profit associated with each. This gives us a quick way to see where the best number of rooms to overbook is.  Don't worry about the details of how to use _matplotlib- for now, you can learn more about this useful tool in the Flatiron School Data Science Bootcamp. The code to create the plot is below.  
`plt.plot(rooms_in_loop, all_profits);`

<img src="https://learn-co-curriculum.github.io/dsc-overbooking-try-experience/profit_graph.png" width="50%">


## Conclusion

Is overbooking your hotel a wise decision or not? Hotels often face the problem of customers not showing up. In this course you learned how Python can be used to help make better business decisions.  In Flatiron School's Data Science Boot Camp, you can learn techniques such as these and how you can apply them to a business scenario.