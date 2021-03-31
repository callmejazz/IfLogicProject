animeRecommendation = [{
    "Title": "Naruto Shippuden",
    "Genre": "Action",
    "Status": "Completed"},
    {
    "Title": "Hunter X Hunter",
    "Genre": "Action",
    "Status": "Ongoing"},
    {
    "Title": "The Devil is a Part-Timer",
    "Genre": "Comedy",
    "Status": "Ongoing"},
    {
    "Title": "Ginatma",
    "Genre": "Comedy",
    "Status": "Ongoing"},
    {
    "Title": "Sword Art Online",
    "Genre": "Fantasy",
    "Status": "Ongoing"},
    {
    "Title": "Seven Deadly Sins",
    "Genre": "Fantasy",
    "Status": "Completed"},
    {
    "Title": "Your Lie in April",
    "Genre": "Slice of Life",
    "Status": "Completed"},
    {
    "Title": "Fruit Basket",
    "Genre": "Slice of Life",
    "Status": "Completed"},
    {
    "Title": "Attack on Titan",
    "Genre": "Supernatural",
    "Status": "Ongoing"},
    {
    "Title": "Jujustu Kaisen",
    "Genre": "Supernatural",
    "Status": "Ongoing"}]

def validate_Genre(genre):
    #try:
        #selection = animeRecommendation(genre)
    print("Genre: " + genre)

    if genre == "action":
        print("These are you selections for some action packed Anime: ")

    elif genre == "comedy":
        print(
            "You'll be laughing for hours with this selection: ")
    elif genre == "slice of life":
        print("So you feel like crying today?: ")
    elif genre == "fantasy":
        print("Get ready for a wild adventure with these selections!: ")

    elif genre == "supernatural":
        print(
            "You'll be on the edge of you seat with this list: ")
    else:
        print("So you chose violence today, huh. Choose a valid genre")
        return
    for anime in animeRecommendation:
        if anime.get("Genre").lower() == genre:
            print(anime.get("Title") + " " + anime.get("Status"))


    #except ValueError:
        #print("I never heard of that genre before")


while True:
    #print(animeRecommendation)
    print("Welcome to the Anime selection list!")
    genre = input("Please choose a genre, your choices are: Action, Comedy, Fantasy, Slice of life and Supernatural or Done to quit")
    genre = genre.lower()
    if genre == "done":
        break
    validate_Genre(genre)




