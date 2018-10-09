a. verify that their Null and alternative hypotheses are formulated correctly

b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

Write your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown named CitibikeReview_<netID>.md. Suggest variations on the question, if you think it may be made more interesting.
    
    
Question A: verify that the null and alternative hypotheses are formulated correctly

Response A: The null hypothesis is stated correctly in words. Since the idea is that long trips are more likely on weekends than on weekdays, the null hypothesis is that the proportion of long trips on weekdays is the same or greater than the proportion of long trips on weekends. 

The null hypothesis is set up partially correctly in mathematical format since the proportion of weekday long trips should be greater than or equal to the proportion of weekend long trips. However, since we're testing the proportion of long trips, the fractions should be weekday long trips / **total long trips** and weekend long trips / **total long trips**. 

The correct mathematical formats for null and alternative hypotheses should be as follows: 

h0: long weekend / long total <= long weekday / long total 
h1: long weekend / long total > long weekday / long total 

h0: long weekend / long total - long weekday / long total <= 0 
h1: long weekend / long total - long weekday / long total > 0 


# $H0$ : $\frac{Weekend_{\mathrm{long}}}{Weekend{\mathrm{total}}} <= \frac{Weekday{\mathrm{long}}}{Weekday{\mathrm{total}}}$
# $H1$ : $\frac{Weekend{\mathrm{long}}}{Weekend{\mathrm{total}}}> \frac{Weekday{\mathrm{long}}}{Weekday{\mathrm{total}}}$

or identically:

# $H0$ : $\frac{Long_{\mathrm{weekend}}}{Long{\mathrm{total}}} - \frac{Long_{\mathrm{weekday}}}{Long{\mathrm{total}}} <= 0 $
# $H1$ : $\frac{Long_{\mathrm{weekend}}}{Long{\mathrm{total}}} - \frac{Long_{\mathrm{weekday}}}{Long{\mathrm{total}}}> 0 $

A significance level was included (alpha = 0.05) which is also part of correctly stating the null hypothesis. 

Question B: verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

Response B: The data supports the project. The data has the appropriate features needed to answer the question - date and trip duration. The data was partially pre-processed to extract the needed values. 'Starttime' was converted to 'date', and 'duration' was left as is. One additional step would be to prepare the data for statistical testing. To prepare the data for the z-test, the data should be split into 'weekend long trips' and 'weekday long trips'. 

The chart for distribution of CitiBike trips shows the distribution for both long trips and short trips. Since the null hypothesis states, 'The proportion of long trip biking on weekdays is the same or higher than the proportion of long trip biking on weekends', only the distribution of long trips needs to be shown in this chart. The distribution of short trips is extraneous information. 

If the null hypothesis were instead, 'The proportion of long trips on weekends is the same or higher than the proportion of short trips on weekends', then the distribution of both long trips and short trips would need to be shown in the chart. 

c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

I would use the z-test to test H0. I would use the z-test because we have two samples and categorical data. The two samples are 'weekend riders' and 'weekday riders'. The categorical variable is long ride vs. not long ride. We are trying to determine if there is a difference between proportions in 2 samples - the proportion of long rides between the weekend sample and the weekday sample. The z-test can be used to test the null hypothesis in this case. 

One variation or additional step that I would recommend would be to do some analysis on trip duration before deciding that 10 minutes defines a 'long trip'. From the bar chart showing distribution of trip duration, we can see that on every day of the week, the proportion of 'long trips' is significantly higher than the proportion of 'short trips'. I would recommend looking at the distribution of trip duration on weekdays during commuting hours to get an idea of how long commuting trips typically take. Then, a more informed threshold can be set for 'long trip'.