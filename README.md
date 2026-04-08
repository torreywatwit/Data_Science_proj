# Data Science Final Project - Food Cost Analysis
### Brendan McCormack, Will Torrey, Michael Lesse

## Introduction:

The goal of this final project is to perform data analysis on a few different datasets to answer proposed research questions. Our focus for this project is the cost of food and how it has changed over the years and what has been changing alongside it. If we can get a detailed and varied analysis on how many different economic factors have been changing alongside the cost of food prices, we can see if anything is outpacing another and showing signs of economic stress. 

The intention and overall goal for the direction of this project is to try and provide better insight for the college students and those soon to be entering the full economic world in factors that they may previously been anaware of or net needing to worry about. If the trends have changed and stayed changed over recent events than there is cause for concern that it is not just short term market reactions but an overall change in the trends of costs.

For the project we selected 5 core questions we wanted to explore and find an answer for:
1. How has the price of groceries increased in comparison to inflation over the years?
2. How has the price of groceries increased in comparison to wages over the years?
3. How has the price of unhealthy foods increased over the years in comparison to the increase in the price of healthy foods over the years?
4. How has the number of children in a household affected the cost of living grocery-wise, over the years?
5. How has the cost of paying for groceries for a family of 4 changed over the years (3.13 as the national average of people in a household)?

## Selection of Data & Reasons of Selection:

The datasets and values to try and reach a better understanding of food costs and changes are primarily sourced from the US Federal Government, something that is very helpful considering the study we are trying to achive is one isolated to the US. These datasets, gained through public logs from the Department of Agriculture are able to be seen as reliable as can be and hold large swaths of data that allow for many means of analysis. 

The majority of the data can be cortioned off into 4 sections, the analytical data of cost of food, the data of wage changes and growth, the same analyis with inflation, and the correlation of household population with the changing times and generations. While the first section is self explainatory as the more cost data there are in food production and purchases over the years allows more a more accurate analysis of what readings are achived there will be, for the remaining 3, the data is to act as important factors that can easily be compared and be able to be done so with little leaps in logic or further steps to the core data of cost analysis. 

An example of a core Department of Agriculture dataset that was used in the project is as follows:

<img width="908" height="423" alt="image" src="https://github.com/user-attachments/assets/20e4deb8-8135-4340-ace7-458e176b25f2" />

The dataset itself holds many different subsections of data that sum together to reach the 'total' for a specific section and allows for not only a larger 'final' value to use in comparison graphs, but also see better what values have been trending higher that are contributing the most. For this project in particular the most important and used subsection of code is 'total_food_at_home_expenditures_(millions_of_nominal_u.s._dollars)' as it focuses entierly on the purchasing of food without taking into acount eating out or events but on groceries and preparing one's own meals.

## Meathods:
Tools:
- NumPy, Seaborne, Pandas, and Scikit-learn for data analysis and inference
- GitHub for code housing and submission
- Jupyter Notebook & Google Colab for sharing code and testing of code before merging
Meathods:
- Linear Regression under 3 of 5 questions to help analysis and understanding
- Data cleaning / munging through:
    - Shortening / Streching code to have comparable lengths
    - Merging of data points to allow for consistent increments (converting from monlthy data points to yearly data points)
    - Convergion of 3 data sets of smaller increments into 1 single dataset containing all the information for better access 
    - Conversion of data values to better units of measurements and significant figures to allow for better reading from code processes.

## Results:

The core results and conclusions reached through the analysis and reading of the data and formatting it into plots and graphs to make the information more digestable has provided a definative answer to the questions we set out to accomplish. These answers hwoever, are not the uplifting or positive results we were hoping to see as prospective college students soon to fully enter the working world.

The results and answers for the questions as a whole can be grouped into 3 sections, results for Questions 1/2, results for Question 3, and results for Questions 4/5. 

Question 1 and 2 focus on simmilar and synchronus concepts, with the raise of both inflation and wage growth with the overall cost and payment people are making for groceries over the course of ~20 years. These comparisons lead to the following plotted results:

<img width="781" height="497" alt="image" src="https://github.com/user-attachments/assets/9cc87f81-658e-4b48-97ce-43495854a451" />

<img width="790" height="477" alt="image" src="https://github.com/user-attachments/assets/0e941351-e0b9-4454-bf39-ab8689c55e7b" />

As able to be seen both the growth of wages and the growth of inflation are being outpaced by the changes in the trend for the price that people are paying for groceries. This shows that there is a fundimental gap that is being created and is causing further issues as every year passes, making the process harder for the younger generation.

Question 3 focuses on its own particuilar type of data analysis comparing the cost of unhealthy food staples to more healthy food staples. This was done through the comparison of changing soda prices to changing milk prices and how favord they are in particular areas of America compared to its alternatve.

<img width="663" height="462" alt="image" src="https://github.com/user-attachments/assets/1ec53a0a-c1c7-4422-be5d-16b25efcafbf" />

As seen in the attached graph, about 2/3 of the states preffer and have a higher purchasing ratio of soda in comparison to the remaining 1/3 having the same for milk. This does further push the idea and inclination that there is a greater attachment to the unhealthier and cheaper option of soda in many states than the healthier expensive option. While a bit uplifiting that in the minority is the state I live in (Massachusettes), it is also still a worry that it appears that the natural economic trend is closer to the unhealthy path than the heathly one.

Questions 4 and 5 focus on the simmilar core concept of how large of a household and how many children in the family have a effect on the overall cost that comes into groceries and the overall extra everday weight that comes in with that responsibility. The core reson for choosing such questions is to see how much of a change over the years the economy has been incentivising the newer generation to not have larger families or avoid certain household structures.

<img width="930" height="477" alt="image" src="https://github.com/user-attachments/assets/467a9081-bdc7-49c7-8e83-be46e4a8237b" />

<img width="586" height="440" alt="image" src="https://github.com/user-attachments/assets/b9d2184a-bd65-45f9-97bc-bb4ab069e43e" />

As seen above in the two provided graphs we have created as part of the data analysis, not only is the inplicit cost of a hosehold with a child compared to one without much higher on average, but the overall costs that come alongside with a family of four (a classic 'nuclear family') has a ever increasing trend of growth in money needed to be put in to get the same results every year. This does nothing but further push forward a means of encouragement for newer generations to be more stungy with not only their money as cost are rising, but also hold back on starting families in times of economic stress.

## Discussion:

From the five questions that we originally sent out to find the answer for, we have been able to not only find a definative and detailed answer to all 5, but gathered an overall conclusion of the nature of the economy that the code and data itself provides to us. Overall, the state of the groceries and foodstuffs costs has a dire look twards the future. The trends of each of the 5 questions all push forward the idea that things are becoming less sustainable overall when it comes to groceries and grocery prices while the wages and inflation are falling behind leading risk of every year becoming less and less sustainable. 

For the look towards the future that this data analysis provides to us as stated for the reflection on Question 4 and 5 is one of holding back and doing as little as you can when it comes to growing. It is unfortunate of a thing to acknolege but there is a lot of risk of starting a family given that in the current world enviorment even the food and grocery prices are something working against you and your possible future children, all due to people of the past focusing on the short term rather than the long term. 

Not all is doom and gloom however as the very process of studying and analysing the data gives us a head start on understanding and preparing for how the cards are stacked against us in the economic sense in certian feilds. This preparation will allow us to take less things for granted as previous generations have and begin saving and learning tricks to pay less sooner rather than later in order to keep pace.

## Summary:


