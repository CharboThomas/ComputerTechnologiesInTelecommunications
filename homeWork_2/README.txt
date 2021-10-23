	
		    Computer Technologies In Telecommunications
				   Homework n° 2 : 



	Creator : Thomas Charbonnet

---------------------------------------------------------------------------------

	Goal : 
		Discover Pandas library

---------------------------------------------------------------------------------

	Solution :
	
		Question 1 : Use the .csv file and assign it to a dataframe
		called cars

		I use the command : 
			cars = read_csv("myTarget.cvs")
			
			
			
			
		Question 2 : Print the number of rows in the dataset;
		
		I take the first data generate by the command : 
			cars.shape
			
			
			
			
		Question 3 : Print the name of all the columns
		
		I use this command : 
			cars.columns




		Question 4 : Print only the records with cars of red color;
		
		In order to filter my data, i will use the command :
					cars.loc[ condition ]
		
		I want to take the red car so I use this condition : 
			car["color"] == "Red"
			
			
			
			
		Question 5 : Select all the records where the year IS NOT "1992"
		
		I am using the same command in question 4. I only change 
		my condition. This condition is : 
			car["car_year"] != 1992
		



		Question 6 : Select model, year and price columns for the
		cars from the last 10 row

		I use this command : 
		cars[["car_model","car_year","price","color"]].tail(10)




		Question 7.a : Select and print 5 lines from the beginning
		of a price maximal column and calculate sum of the values,
		minimal value, value, median
		
		In order to take the 5 first data, i use this command : 
			cars.head(5)
		
		For sum => I use this command : cars.sum()
		For max => I use this command : cars.max()
		For min => I use this command : cars.min()
		For median => I use this command : cars.median()
		
		
		
		
		Question 7.b : Select and print 5 lines from the end of a
		price column and calculate sum of the values, minimal value,
		maximal value, median
		
		I am also using the same command in the question 7.a .
		
		I only change the command .head(5) by the command tail(5).

		
		
---------------------------------------------------------------------------------

	Tools : 
		Python 3.9
		Jupyter (IDE)
		Pandas Library

---------------------------------------------------------------------------------

	Slides : 
	
		https://slides.com/thomascharbonnet/deck-6dbe45

---------------------------------------------------------------------------------

