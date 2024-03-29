from models import *

##creates the tables for the Artists
def create_artist_tables():
    db.create_tables([Artist])

##this function create the artist with name and email arguements
def create_artist(name, email):
    try:
        ##creates the artists and saves
        artist = Artist(name=name, email=email)
        artist.save()
        print("\nArtist Created\n")
        return True
    except Exception as e:
        print('Database Error Couldnt Create Artist')

##this function returns all the artists in a list
def search_artist():
    try:
        artists = Artist.select()
        return artists
    except Exception as e:
        print('Database Error Couldnt Fetch Artist')