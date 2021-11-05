from imdb import IMDb
from biblioSqlite3 import DataBase


# create an instance of the IMDb class
ia = IMDb()


listeMovie = ['Just Wright','Wilby Wonderful','Travelling Players','Judith of Bethulia','Cop Land',
              'Exterminating Angels','Death In Love','Rosencrantz and Guildenstern Are Dead','Beastie Boys: Sabotage','By the Pricking of My Thumbs',
              'Cape No. 7','Tribute','Counterfeit Traitor','In Your Hands','Run',
              'Charlie Chan Carries On','Branded','Time of Eve','Centre Stage: Turn It Up','Road to Zanzibar',
              'Capture of Bigfoot','In the Heart of the Sea','Living Wake','Le Mans','Sicilian',
              'Strangler','And So It Goes','Salt of the Earth','Taking Lives','Shiver',
              'Local Color','Stand Up Guys','Life Is Sweet','Porn Theater','Millennium Mambo',
              'Violets Are Blue...','Helter Skelter','Jean Gentil','1776','Mating Game',
              'Frozen North','Indiscreet','Escape from Suburbia: Beyond the American Dream','Red Cliff Part II',"It's a Wonderful Afterlife",
              'Dennis the Menace','Care Bears Movie II: A New Generation','Black Hawk Down','Secret Glory','Wondrous Oblivion',
              'And Now a Word from Our Sponsor','Superman vs. The Elite','Deux mondes','Green Chair','Liberty',
              'Like Water','Plácido','Big Fish','Terrorist','El Greco',
              'Ring of Bright Water','Art & Copy','War of the Roses','Wrong Guy','Kentucky Fried Movie',
              'I Love You, Man','Friday','Lady Takes a Chance, A','Amelia','Takeshis',
              'House of the Dead','Out of the Blue','Samson and Delilah','Edge of Fear','Shanghai',
              'Dead or Alive: Final','Shutter Island',"Madonna's Pig",'Forrest Gump','My Man and I',
              'Alaska: Silence & Solitude','Rammbock','Accident on Hill Road','Frozen Fever','A Pigeon Sat on a Branch Reflecting on Existence',
              'Pictures of the Old World','Manzanar Fishing Club','My Favorite Wife',"To Grandmother's House We Go","Southern District",
              "Because of Winn-Dixie","Good Job:  Stories of the FDNY, A","He's Just Not That Into You",'Knowing','Night and Fog',
              'Bang Bang','Hoop Dreams','Nemesis 3: Time Lapse','Littlerock','Elektra Luxx']



def captureAndSave (myDB, listeMovie) :
    
    for i in range(8,len(listeMovie),1):
        # get a movie
        movie = ia.search_movie(listeMovie[i])
        
        movieID =  movie[0].movieID

        movieV2 = ia.get_movie(movieID)

        if 'rating' in movieV2:
            rate =  movieV2['rating']
        else :
            rate = ' 0 '


        if 'year' in movieV2:
            year =  movieV2['year']
        else :
            year = ' 0 '


        if 'genres' in movieV2 :
            genre = movieV2['genres'][0]
        else:
            genre = ' - '

        myDB.addData("movies","id , name , releaseYear , genre , rating", ( str(movieID) , movie[0]['title'] , int(year) , genre , int(rate) ) )### I add some data



##########################################################
#                       My code
##########################################################

myDB = DataBase("movies.db") ### I create my object

"""

### step 1 => adding data
captureAndSave(myDB, listeMovie)


### step 2 => print data
myDB.printTableData("*","movies")


### step 3 => update Data
myDB.updateData("movies","genre = 'Dramatique' ","genre = 'Drama'  ")


### step 4 => delete Data
myDB.deleteData("movies", "Genre = 'Dramatique' ")


"""


myDB.printTableData("*","movies")


del myDB ### I destroy my object
