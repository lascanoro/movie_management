import pandas as pd

#--------------------------EN ESTE BLOQUE ORDENAMOS LOS DATA FRAMES------------------
#Load user data, I will use "df" to indicate it's a dataframe.
df_users=pd.read_csv('users.csv')
df_movies=pd.read_csv('movies.csv')
#Create the columns for the borrowing dataframe.
borrowing_records= ['user id','movie ids','borrow_date']

# Now that the columns I want are specified, let's create the borrowing dataframe.
df_borrowing=pd.read_csv("borrowing_records.csv")
#Create the borrowing records CSV

# Add the description column to the movies dataframe.
df_movies['description']=None
# Now create a dictionary with the movie descriptions.
movie_descriptions= {
    101:f"A thief who enters people's dreams to steal secrets must pull off his toughest mission yet: planting an idea in someone's subconscious.",
    102:f"A computer hacker discovers reality is a simulated world, and joins a rebellion to free humanity from its machine overlords.",
    103:f"A group of astronauts embarks on a journey through a wormhole to find a new home for humanity as Earth faces extinction.",
    104:f"A poor family schemes to infiltrate a wealthy household, leading to unexpected and dark consequences.",
    105:f"The aging patriarch of a powerful crime family hands control to his reluctant son, sparking a violent struggle for power.",
    106:f"The lives of two hitmen, a boxer, a gangster, and his wife intertwine through a series of violent and darkly humorous events.",
    107:f"Batman faces his greatest challenge yet as he battles the Joker, a criminal mastermind who seeks to create chaos in Gotham City.",
    108:f"An insomniac office worker forms an underground fight club with a charismatic soap salesman, leading to an anarchic movement that challenges consumerism.",
    109:f"Forrest Gump, a slow-witted but kind-hearted man, unwittingly influences several historical events while navigating life and love in America.",
    110:f"Oskar Schindler, a German businessman, saves the lives of over a thousand Jewish refugees during the Holocaust by employing them in his factories"
}
#Fill the 'description' column with the movie descriptions information.
df_movies['description']=df_movies['Movie ID'].map(movie_descriptions)
#Save the updated dataframe to the .csv.
df_movies.to_csv('movies.csv',index=False)

#-------------------------FUNCIONES QUE VAMOS A UTILIZAR MAS ABAJO------------
#funcion menu welcome.
def welcome_user(df_users):
    print("Welcome to the movie managament")
    print("Please,pick one option from the following menu:")
    print("1.Enter your user ID")
    print("2.See all users")


#Funcion para el menu main
def user_menu(user_name):
      print(f"{user_name}, Please,pick one option from the following menu(1,2,3 or 4):")
      print("1. Rent")
      print("2. Return")
      print("3. Administrator")
      print("4.Exit")
#funcion menu admisnitrador
def admin_menu():
              print("Welcome to the Administrator menu.Please pick one option from the following menu(1,2,3 or 4):")
              print('1.Add or remove movies')
              print('2.Copies availables for movies')
              print('3.Add or delete  users')
              print('4.Exit')
#funciones que se utilizan adentro del menu administrador---- 
#----agregar o eliminar peliculas---
def add_or_remove_movies():
    global df_movies #uso el dataframe ya cargado 
    action_movies=input('Do you want add o delete a movie ?(add/delete):')

    if action_movies == "add":
        #Pedimos los datos de la pelicula
        Movie_ID= int(input("Enter the movie ID (It is always a number above 100):"))
        Title= input("Enter the titles of the movie:")
        Director= input("Enter the name of the director:")
        Year= input("Enter the year the movie was released:")
        New_movie_available_copies=int(input("Enter the number of available copies:"))
        description=input("Enter the description of the movie:")
        #Verifica si la pelicula ya existe por el ID
        if Movie_ID in df_movies['Movie ID'].values:
            print(f"The movie with ID {Movie_ID} already exists. It cannot be added.")
        else:
            new_movie=pd.DataFrame({
                'Movie ID':[Movie_ID],
                'Title':[Title],
                'Director':[Director],
                'Year':[Year],
                'Available Copies':[New_movie_available_copies],
                'description': [description]
                    
            })
            df_movies=pd.concat([df_movies,new_movie], ignore_index=True)
            print(f"The new movie' {Title} ' has been added.")
    elif action_movies== "delete":
        #Pedimos el ID a eliminar.
        movie_id_delete=int(input("Enter the ID of the movie to delete:"))
        if movie_id_delete in df_movies:
            df_movies=df_movies[df_movies['Movie ID']!=movie_id_delete]
            print(f"The movie with ID: {movie_id_delete} has been deleted.")
    else:
        print("Invalid action, please select 'add' or 'delete'.")
    
    #Guardamos el data frame actualizado
    df_movies.to_csv('movies.csv',index=False)

#----Funcion para ver numero de copias----
def view_available_copies():
    movie_id_copies=int(input("Enter the movie ID to see the number of available copies:"))
    #buscamos la pelicula por su id
    movie_row=df_movies[df_movies['Movie ID']==movie_id_copies]
    if not movie_row.empty:
        available_copies = movie_row['Available Copies'].values[0]  # Obtenemos el número de copias disponibles
        print(f"The movie with ID {movie_id_copies} has {available_copies} available copies.")
    else:
        print(f"No movie was found with ID {movie_id_copies}.")

#----funcion para agregar o eliminar usuarios------
def add_or_create_new_users():
    global df_users
    action_user=input('Do you want to add or delete a user? (Add/Delete):')

    if action_user == "add":
        #Pedimos los datos de la pelicula
        add_new_user= int(input("Enter the ID of the new user :"))
        add_new_name=(input("Enter the name of the new user:"))
        
        #Verifica si ID ya existe
        if add_new_user in df_users['User ID'].values:
            print(f"The user with ID {add_new_user} already exists. Cannot add.")
        else:
            new_user_df=pd.DataFrame({
                'User ID':[add_new_user],
                'User Name':[add_new_name],
                    
            })
            df_users=pd.concat([df_users,new_user_df], ignore_index=True)
            print(f"The new user '{add_new_name}' has been added.")

    elif action_user== "delete":
        #Pedimos el ID a eliminar.
        user_id_delete=int(input("Enter the ID of the user to delete:"))
        if user_id_delete in df_users['User ID'].values:
            df_users=df_users[df_users['User ID']!=user_id_delete]
            print(f"The user with ID: {user_id_delete} has been deleted.")
    else:
        print("Invalid action, please select 'add' or 'delete'.")
     
    # Save the updated dataframe to the CSV
    df_users.to_csv('users.csv', index=False)

### Rama DANI RENT--------------------------------------------
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

def mostrar_descripcion_peliculas(df_movies):
    # Mostrar las descripciones de todas las películas desde el DataFrame
    print("\nMovie Descriptions:\n")
    for index, row in df_movies.iterrows():  # Itera sobre las filas del DataFrame
        print(f"{row['Movie ID']}. {row['description']}")

def mostrar_lista_completa(df_movies):
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
#--------------MARCELA RENT--------------------------------
def return_movie():
    movie_ids_to_filter = [int(input("\nPlease enter the movie ID: "))]
    # Verificar si el usuario ha tomado prestada la película
    df_borrowing = pd.read_csv('borrowing_records.csv')
    print(df_borrowing.head())
   # user_borrowing = df_borrowing[(df_borrowing['user id'] == user_id) & (df_borrowing['movie ids'].str.contains(str(movie_id)))]
    user_borrowing = df_borrowing[(df_borrowing['movie ids'].isin(movie_ids_to_filter)) & (df_borrowing['user id'] == user_id)]
    print (user_borrowing.head())
    if not user_borrowing.empty:
        # Remover el ID de la película de la columna 'movie ids'
        df_borrowing['movie ids'] = df_borrowing['movie ids'].apply(lambda ids: ','.join([id for id in ids.split(',') if id != str("Movie ID")]))
        
        # Eliminar filas donde todas las películas han sido devueltas (columna 'movie ids' vacía)
        df_borrowing = df_borrowing[df_borrowing['movie ids'] != '']
        
        print(f"Movie with id {"Movie ID"} has been returned by user {user_id}.")
    else:
        print(f"User {user_id} does not have movie with id {"Movie ID"} borrowed.")
    
    return df_borrowing

# Menú para devolución de películas
def movie_return_menu():
    while True:
        print("\n=== Movie Return Menu ===")
        print("1. Return a movie by movie ID")
        print("2. View current borrowing records")
        print("3. Exit")
        
        option = int(input("Choose an option (1, 2, or 3): "))
        print('here', option)
        if option == 1:
            return_movie()
            print('return movie ', option)
        elif option == 2:
            view_records()
        elif option == 3: 
            break
        else:
            print("Invalid option, please select again.")
        
             
def view_records (df_borrowing_records):
    print (df_borrowing_records)
         

    
        
    




    
if __name__=="__main__":
    #--------------------ACA PROGRAMAMOS---------------------------------------
    while True:
        # Empezamos el programa
        welcome_user(df_users)

        user_welcome_menu = input("Please enter your choose:")
        if user_welcome_menu == '1':
            user_id = input("Please enter your User ID: ")

            # Busca el nombre del usuario en el DataFrame
            user_row = df_users[df_users['User ID'] == int(user_id)]  # Compara el User ID ingresado

            if not user_row.empty:
                user_name = user_row['User Name'].values[0]  # Extrae el nombre del usuario
                print(f"Welcome {user_name}! Now you are in the main menu")

                while True:
                    user_menu(user_name)
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        # Rent a movie
                        while True:
                            choice = mostrar_menu()
                            if choice == 1:
                                mostrar_peliculas_disponibles()
                            elif choice == 2:
                                mostrar_descripcion_peliculas(df_movies)
                            elif choice == 3:
                                mostrar_lista_completa()
                            elif choice == 4:
                                break  # Regresar al menú de usuario
                            else:
                                print("Invalid option, please select again.")

                    elif user_choice == "2":#MARCELAAAAAAA---------------------------
                        movie_return_menu()
                            
                            

                    elif user_choice == "3":
                        # Enter the administrator menu
                        while True:
                            admin_menu()
                            admin_choice = input("Select an option: ")

                            if admin_choice == "1":
                                add_or_remove_movies()
                            elif admin_choice == "2":
                                view_available_copies()
                            elif admin_choice == "3":
                                add_or_create_new_users()
                            elif admin_choice == "4":
                                break  # Regresar al menú de usuario
                            else:
                                print("Invalid option, please select again.")

                    elif user_choice == "4":
                        print("Exiting the system.")
                        break  # Exit from user menu
                    else:
                        print("Invalid option, please select again.")


        elif user_welcome_menu == '2':
            print("Here are all users:")
            print(df_users)  # Muestra todos los usuarios

        else:
            print("Invalid user ID. Please try again.")