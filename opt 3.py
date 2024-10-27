def mostrar_menu():
    # Display the main menu and get the user's choice
    return int(input(
        "Please choose your option\n"
        "(1) Pick a movie\n"
        "(2) See description\n"
        "(3) Full movie list\n"
        "(4) Return to menu\n"
    ))

def mostrar_peliculas_disponibles():
    # Display list of currently available movies
    print("\nShowing available movies:\n")
    print("101. Inception\n102. The Matrix\n103. Interstellar\n104. Parasite\n105. The Godfather\n"
          "106. Pulp Fiction\n107. The Dark Knight\n108. Fight Club\n109. Forrest Gump\n"
          "110. Schindler's List\n")

def mostrar_descripcion_peliculas():
    # Dictionary containing movie descriptions
    descripciones = {
        101: "Inception: A thief who steals corporate secrets through dream-sharing technology is given the task of planting an idea into the mind of a CEO.",
        102: "The Matrix: A computer hacker learns about the true nature of his reality and his role in the war against its controllers.",
        103: "Interstellar: A team of explorers travel through a wormhole in search of a new home for humanity.",
        104: "Parasite: Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        105: "The Godfather: An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",
        106: "Pulp Fiction: The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        107: "The Dark Knight: When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        108: "Fight Club: An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
        109: "Forrest Gump: The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal, and other historical events unfold through the perspective of an Alabama man.",
        110: "Schindler's List: In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution."
    }

    # Show descriptions of all movies
    print("\nMovie Descriptions:\n")
    for num, descripcion in descripciones.items():
        print(f"{num}. {descripcion}")

def mostrar_lista_completa():
    # Display the full list of movies
    print("\nShowing full movie list:\n")
    print("101. Inception")
    print("102. The Matrix")
    print("103. Interstellar")
    print("104. Parasite")
    print("105. The Godfather")
    print("106. Pulp Fiction")
    print("107. The Dark Knight")
    print("108. Fight Club")
    print("109. Forrest Gump")
    print("110. Schindler's List\n")

def seleccionar_pelicula(pelicula_numero):
    # Dictionary of available movies
    peliculas_disponibles = {
        101: "Inception",
        102: "The Matrix",
        103: "Interstellar",
        104: "Parasite",
        105: "The Godfather",
        106: "Pulp Fiction",
        107: "The Dark Knight",
        108: "Fight Club",
        109: "Forrest Gump",
        110: "Schindler's List"
    }
    
    if pelicula_numero in peliculas_disponibles:
        print(f"You have selected: {peliculas_disponibles[pelicula_numero]}")
    else:
        print("Invalid movie number. Please try again.")

# Main program loop
while True:
    try:
        Rent = mostrar_menu()
        
        if Rent == 1:
            mostrar_peliculas_disponibles()
            # Ask user to select a movie
            pelicula_numero = int(input("Enter the movie number to select: "))
            seleccionar_pelicula(pelicula_numero)
        elif Rent == 2:
            mostrar_descripcion_peliculas()  # Show all movie descriptions
        elif Rent == 3:
            mostrar_lista_completa()
        elif Rent == 4:
            print("Returning to menu...\n")
            break
        else:
            print("Please choose a valid option (1-4).\n")
            
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.\n")
