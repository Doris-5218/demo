def make_album(singer_name,album_name,song_count = None):
    full = {"singer":singer_name,"album":album_name}
    if song_count:
        full["song"] = song_count
    return full
x = make_album("蔡依琳","72變","10") 
print(x)