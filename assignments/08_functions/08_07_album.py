def make_album(artist, title, songs=None):

# I make a dictionary representing an album
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album

album_1 = make_album('the weeknd', 'after hours')
album_2 = make_album('taylor swift', 'evermore')
album_3 = make_album('drake', 'scorpion', songs=25)

print(album_1)
print(album_2)
print(album_3)
