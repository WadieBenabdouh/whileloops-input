def make_album(artist, album):
    metadata = {artist : album}
    return metadata


user_chosen_artist = input("type the name of the artist ")
while user_chosen_artist == "":
    print("Please fill the artist name!!")
    user_chosen_artist = input("type the name of the artist ")
    
    
    
user_chosen_album = input("Type the name of the album ")
while user_chosen_album == "":
    print("Please type the album name!!")
    user_chosen_album = input("Type the name of the album ")
    
    
meta_enigma = make_album(user_chosen_artist, user_chosen_album)
print(meta_enigma)

    
