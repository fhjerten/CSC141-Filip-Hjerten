def make_album(artist, title):

# I make a dictionary representing an album
    album = {'artist': artist.title(), 'title': title.title()}
    return album

while True:
    print("\nEnter album information:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name.lower() == 'q':
        break

    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break

    album_info = make_album(artist_name, album_title)
    print(album_info)
