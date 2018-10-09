## Question A: 
Verify that the null and alternative hypotheses are formulated correctly

## Response A: 
The null hypothesis is stated correctly in words. Since the idea is that long trips are more likely on weekends than on weekdays, the null hypothesis is that the proportion of long trips on weekends is the same or smaller than the proportion of long trips on weekdays. 

The null hypothesis is set up partially correctly in mathematical format since the proportion of weekday long trips should be greater than or equal to the proportion of weekend long trips. However, since we're testing the proportion of long trips for each sample (weekday trips vs. weekend trips), the fractions should be weekday long trips / **total weekday trips** and weekend long trips / **total weekend trips**. 

The correct mathematical formats for null and alternative hypotheses should be as follows: 


# $H_0$ : $\frac{weekend_{\mathrm{long}}}{weekend_{\mathrm{total}}} <= \frac{weekday_{\mathrm{long}}}{weekday_{\mathrm{total}}}$
# $H_1$ : $\frac{weekend_{\mathrm{long}}}{weekend_{\mathrm{total}}} > \frac{weekday_{\mathrm{long}}}{weekday_{\mathrm{total}}}$

A significance level was included (alpha = 0.05) which is also part of correctly stating the null hypothesis. 

## Question B: 
Verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

## Response B: 
The data supports the project. The data has the appropriate features needed to answer the question - date and trip duration. The data was partially pre-processed to extract the needed values. 'Starttime' was converted to 'date', and 'duration' was left as is. One additional step would be to prepare the data for statistical testing. To prepare the data for the z-test, which is the statistical test I chose, the data should be split into 'weekend long trips' and 'weekday long trips', since weekend riders and weekday riders are the samples being compared. 


## Question C:
Choose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

## Response C: 
I would use the z-test to test H0. I would use the z-test because we have two samples and categorical data. The two samples are 'weekend riders' and 'weekday riders'. The categorical variable is long ride vs. not long ride. We are trying to determine if there is a difference between proportions in 2 samples - the proportion of long rides between the weekend sample and the weekday sample. The z-test can be used to test the null hypothesis in this case. 

One variation or additional step that I would recommend would be to do some analysis on trip duration before deciding that 10 minutes defines a 'long trip'. From the bar chart showing distribution of trip duration, we can see that on nearly every day of the week, the proportion of 'long trips' is significantly higher than the proportion of 'short trips'. I would recommend looking at the distribution of trip duration on weekdays during commuting hours to get an idea of how long commuting trips typically take. Then, a more informed threshold can be set for 'long trip'.

I would also recommend using both a cold month and a warm month to control for seasonality, since people might not want to commute to work on a bike in the cold. 

## Assignment 2: Literature choices of statistical tests

For part 2 of the homework, I chose 3 statistical tests from the table provided. I searched the online journal Plos One to find papers that utilized each of the 3 tests I selected. For each paper, I scanned and identified features used in the statistical test (such as independent variable, independent variable type, dependent variable, dependent variable type). I also included a screenshot of the main plot for each statistical test. This exercise helped me to get a better understanding of how statistical tests are used in research and how statistical tests are presented in scientific journals. 

## Assignment 3: Reproduce the analysis of the Hard to Employ program in NY

For part 3 of the homework, I reproduced the analysis of the hard to employ program in NY. I read about the program to get an idea of how the study worked. I then 

## Assignment 4: Literature choices of statistical tests