	
		Computer Technologies In Telecommunications
				Homework n° 1 : 



	Creator : Thomas Charbonnet

---------------------------------------------------------------------------------

	Goal : 
		Capture Data generates by the command Ping.
		
		Target -> www.google.com
		
		Linux Command -> ping -c 4 www.google.com

---------------------------------------------------------------------------------

	Solution : I creat an object called PING.

	   Now You can see a UML diagrama of my object : 

			|---------------------|
			|        PING         |
			|---------------------|
			|+ cmd : str          |
			|+ target : str       |
			|+ param : int        |
			|+ jsonData : json    |
			|+ out : str          |
			|+ err : str          |
			|+ data : list        |
			|+ position : int     |
			|---------------------|
			|+ traitement         |
			|+ traitementModeleA  |
			|+ traitementModeleB  |
			|+ traitementModeleC  |
			|+ traitementModeleD  |
			|+ ecriture           |
			|+ __del__	      |
			|---------------------|


	   In order to take data, I creat these 3 steeps:
	   
	   	First : take data - You can find this part of the code 
	   		on the --init-- method of my object
	   	
	   	Second : clean data - You can find this part of the code
	   		 on the method called "traitement". The init method 
	   		 used this methid after the steep 1. 
	   		 The "traitement" method used 4 smalls methods 
	   		 (traitementModeleA,traitementModeleB,traitementModeleC,
	   		 traitementModeleD) in order to clean 4 type of data.
	   	
	   	Third : save data - You can find this part of the code
	   		 on the method called "ecriture". The init method 
	   		 used this method after the steep 2. 
	   	
---------------------------------------------------------------------------------

	Tools : 
		Python 3.9
		Spyder (IDE)
		JSON Library
		OS Library
		Subprocess Library

---------------------------------------------------------------------------------

	Slides : 
	
		https://slides.com/thomascharbonnet/title-texttitle-text

---------------------------------------------------------------------------------

