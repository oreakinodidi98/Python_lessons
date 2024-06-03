class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"{self.album_name} by {self.album_artist} ({self.number_of_songs})"
    
# create list called albums1 with 5 albums
albums1 = [Album("Album1", 10, "Artist1"), Album("Album2", 12, "Artist2"), Album("Album3", 15, "Artist3"), Album("Album4", 8, "Artist4"), Album("Album5", 20, "Artist5")]
# print the list
print(f"\nAlbum 1:")
for album in albums1:
    print(album)

#sort list according to number of songs
albums1.sort(key=lambda x: x.number_of_songs)
print(f"\nSorted list by number of songs:")
for album in albums1:
    print(album)

# swap the first element with the second element
albums1[1], albums1[2] = albums1[2], albums1[1]
print(f"\nSwapped list")
for album in albums1:
    print(album)

# create list called albums2 with 5 albums
albums2 = [Album("Album6", 10, "Artist6"), Album("Album7", 12, "Artist7"), Album("Album8", 15, "Artist8"), Album("Album9", 8, "Artist9"), Album("Album10", 20, "Artist10")]
# print the list
print(f"\nAlbum 2:")
for album in albums2:
    print(album)

# copy all elements from albums1 to albums2
albums2 = albums1.copy()
print(f"\nCopied list")
for album in albums2:
    print(album)

# add a new album to albums2
albums2.append(Album("Darkside of the mooon", 9, "Pink Floyd"))
albums2.append(Album("Ooops!... I did it again", 16, "Britney Spears"))

print(f"\nList with Added new albums")
for album in albums2:
    print(album)

#sort list alphabetically according to album name
albums2.sort(key=lambda x: x.album_name)
print(f"\nAlbum Name, Alphaabetically Sorted list:")
for album in albums2:
    print(album)

# search for an album in the album2 and print the album index
album_name = "Darkside of the mooon"
for index, album in enumerate(albums2):
    if album.album_name == album_name:
        print(f"\n{album_name} found at index {index}")
        break
else:
    print(f"\n{album_name} not found")
