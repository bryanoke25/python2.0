movies = {"Ellio" : "Adventure", "JurassicPark" : "Adventure", "Fantastic 4: new steps" : "Adventure", "Friday 13th" : "Horror", "A christmas carol" : "Fairy-tale", "Little mermaid" : "fairytale"}
print(movies)

print(movies["Ellio"])
print(movies["Friday 13th"])

choice = str(input("Choose a movie : "))
print(movies[choice])

movies["Despicable me 4"]="Mystery"
print(movies)

movie = str(input("Enter a movie choice : "))
genre = str(input("Enter a following genre : "))
movies[movie]=genre
print(movies)

del movies["JurassicPark"]
print(movies)

movies.pop("Ellio")
print(movies)

del_choice = str(input("what would you like to delete?"))
del movies[del_choice]
print(movies)