# Monte-Carlo-Simulation

In this practice, I’ve made used of Monte Carlo Simulation in order to reach the endorsement of some companies in Turkey.

To realizing the usefulness of the Monte Carlo Simulations, I’ve handled the data of company of Arçelik. The data includes the endorsement of Arçelik Company from 1993 to 2022. 

I’ve split the data to two part. First part of the data contains quartiles of years (1993-2019) based on their endorsement values. The second part of the data contains quartiles of years (2019-2022) based on their endorsement values like the first part.

We can assume that the second part of our data is our test dataset. As a data scientist candidate, we would be able to think that this is train and test split. However the difference is we are not going to build a model to predict something by using the part of data. I’m just trying to make you understand what we are going to do.

There is an argument, which must be known is the economics values can not be able to handled like this. Therefore, you should not take this comparison as an argument.

Summary;
We used the data from 1993 to 2019 in order to build Monte Carlo Simulations. The metric that we use to test our practice is values from 2019 to 2022.  
I’ve simulated 10000 scenario to predict 12 quartiles.
The value, which must be reached is 39191.88 to say that Monte Carlo Simulations are useful for predicting of endorsement values of companies.
Let’s skip to the code section.
