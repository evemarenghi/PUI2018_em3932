For assignment 1, I worked on time series analysis. I uploaded the MTA card type/station/weekly data and plotted a time series to identify the most prominent event. I plotted individual time series for each card type to identify the card type with the largest increase and the card type with the largest decrease in the number of swipes. I then built a classifier to assign a card type to a time series based on time series features. 

For assignment 2, I improved my plot based on the feedback I received from Christine in HW8. Christine made the following suggestions: 
- Accidents per person in each borough would be an interesting element to present rather than absolute counts.
- I might make the circles you use for data points a bit bigger; there is one instance in May where the Queens and Manhattan points are almost on top of each other, and it might be easier to see that they are both there if they are a larger.
- The colors for the Bronx and Brooklyn data points may look the same to those who are red-green color blind.

Based on Christine's recommendations, I: 
- changed the plot to accidents per 1000 people instead of absolute counts of accidents
- did not change circle size because when I tested this, it made the plot more difficult to interpret
- changed the color of the Brooklyn points to be more color blind compliant 

![main plot](hw11_plot.png)

**Caption**: The plot above shows average number of motor vehicle accidents per 1000 people by month and borough in NYC for 2014 - 2017. I took the average number of accidents for each month from 2014 to 2017 and the average population for each borough from 2014 to 2017. Manhattan has the highest number of accidents per 1000 people (residents) for every month throughout the year. Staten Island has the lowest number of accidents per 1000 people (residents) for every month except January and February when the Bronx is the lowest. May has the highest number of accidents per 1000 people for every borough, indicating that May is the most dangerous month. February has the lowest number of accidents per 1000 people for the Bronx, Queens, Brooklyn, and Manhattan indicating that February is the safest month for those boroughs. Staten Island has the lowest number of accidents per 1000 people in August. 


For part 1 of this homework, I worked with Ursula Kaczmarek, Nathan Caplan, Sam Burns, Christine Biddlecombe, and Ilyas helped me as well. I worked on part 2 of this homework by myself. 