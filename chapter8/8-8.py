def make_album(singer_name,album_name):
    full =f"{singer_name,album_name}" 
    return full
while True:
    print("please tell me your favorite singer's information next to:")
    print("(enter 'q' at any time to quit)")
    singer = input("singer name:")
    if singer == "q":
        print("thank you!")
        break
    album = input("album name:")
    if album == "q":
        print("thank you!")
        break
    Full_album = make_album(singer,album)
    print(f" {Full_album}")
    print("thank you!")