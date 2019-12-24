#Music Database

import time

def main():
    artistfile= open("artists.txt", "r+")
    songfile= open("songnames.txt", "r+")
    artistData= artistfile.read().split(",")
    songNameData= songfile.read().split(",")
    
    while True:
        artistfile= open("artists.txt", "r+")
        songfile= open("songnames.txt", "r+")
        artistData= artistfile.read().split(",")
        songNameData= songfile.read().split(",")
        print ("What would you like to do: \n Type (1) to view all songs \n Type (2) to add an new song \n Type (3) to delete an song \n Type (4) to quit")
        choice= eval(input())
        print ("------------------------------------------------------------")

        if choice == 1:
            for line in zip(artistData, songNameData):
                print ("{}, {:20}".format(*line))
                print ()
            
        elif choice == 2:
            songfile= open("songnames.txt", "a+")
            newSong= input("Please type the name of the song to add: ")
            print ()
            songfile.write(" , "+newSong)
            songfile.read().split(",")
            songfile.close()
            
            artistfile= open("artists.txt", "a+")    
            newArtist= input("Please type the name of the artist to add: ")
            print ()
            artistfile.write(" , "+newArtist)
            artistfile.read().split(",")
            artistfile.close()
            
            

        elif choice == 3:
            songfile= open("songnames.txt", "r+")
            data= songfile.read()
            delSong= input("Please type the name of the song to remove: ")
            print ()
            newdata= data.replace(delSong, "")
            songfile= open("songnames.txt", "w")
            songfile.write(newdata)
            songfile.close()

            artistfile= open("artists.txt", "r+")
            data= artistfile.read()
            delartist= input("Please type the name of the artist to remove: ")
            print ()
            newdata= data.replace(delartist, "")
            artistfile= open("artists.txt", "w")
            artistfile.write(newdata)
            artistfile.close()

        elif choice == 4:
            time.sleep (2)
            quit()

        else:
            print ("Why do you not listen!, I put you on time sleep \n for 10,000,000 seconds next time")

            
    
print ("Hello welcome to your music database!")
print ("------------------------------------------------------------")
time.sleep (1)    
main()
