import pandas as pd
import os  # Importamos el módulo os para verificar la existencia de archivos

# --------------------------EN ESTE BLOQUE ORDENAMOS LOS DATA FRAMES------------------
# Load user data
df_users = pd.read_csv('users.csv')
df_movies = pd.read_csv('movies.csv')

# Verificar si 'borrowing_records.csv' existe
if os.path.exists('borrowing_records.csv'):
    df_borrowing = pd.read_csv('borrowing_records.csv')
else:
    # Si no existe, creamos un DataFrame vacío con las columnas necesarias
    df_borrowing = pd.DataFrame(columns=['user id', 'movie ids', 'borrow_date'])
    df_borrowing.to_csv('borrowing_records.csv', index=False)

# Add the description column to the movies dataframe if it doesn't exist
if 'description' not in df_movies.columns:
    df_movies['description'] = None

# Now create a dictionary with the movie descriptions.
movie_descriptions = {
    101: "A thief who enters people's dreams to steal secrets must pull off his toughest mission yet: planting an idea in someone's subconscious.",
    102: "A computer hacker discovers reality is a simulated world, and joins a rebellion to free humanity from its machine overlords.",
    103: "A group of astronauts embarks on a journey through a wormhole to find a new home for humanity as Earth faces extinction.",
    104: "A poor family schemes to infiltrate a wealthy household, leading to unexpected and dark consequences.",
    105: "The aging patriarch of a powerful crime family hands control to his reluctant son, sparking a violent struggle for power.",
    106: "The lives of two hitmen, a boxer, a gangster, and his wife intertwine through a series of violent and darkly humorous events.",
    107: "Batman faces his greatest challenge yet as he battles the Joker, a criminal mastermind who seeks to create chaos in Gotham City.",
    108: "An insomniac office worker forms an underground fight club with a charismatic soap salesman, leading to an anarchic movement that challenges consumerism.",
    109: "Forrest Gump, a slow-witted but kind-hearted man, unwittingly influences several historical events while navigating life and love in America.",
    110: "Oskar Schindler, a German businessman, saves the lives of over a thousand Jewish refugees during the Holocaust by employing them in his factories"
}

# Fill the 'description' column with the movie descriptions information.
df_movies['description'] = df_movies['Movie ID'].map(movie_descriptions)
# Save the updated dataframe to the .csv.
df_movies.to_csv('movies.csv', index=False)

# -------------------------FUNCIONES QUE VAMOS A UTILIZAR MAS ABAJO------------
# Función menú de bienvenida.
def welcome_user(df_users):
    print("Welcome to the movie management system")
    print("Please, pick one option from the following menu:")
    print("1. Enter your user ID")
    print("2. See all users")

# Función para el menú principal del usuario
def user_menu(user_name):
    print(f"\n{user_name}, please pick one option from the following menu (1, 2, 3, or 4):")
    print("1. Rent a movie")
    print("2. Return a movie")
    print("3. Administrator")
    print("4. Exit")

# Función menú del administrador
def admin_menu():
    print("\nWelcome to the Administrator menu. Please pick one option from the following menu (1, 2, 3, or 4):")
    print("1. Add or remove movies")
    print("2. Check available copies for movies")
    print("3. Add or delete users")
    print("4. Exit")

# Función para agregar o eliminar películas
def add_or_remove_movies():
    global df_movies  # Uso el dataframe ya cargado
    action_movies = input('Do you want to add or delete a movie? (add/delete): ')

    if action_movies == "add":
        # Pedimos los datos de la película
        Movie_ID = int(input("Enter the movie ID (It is always a number above 100): "))
        Title = input("Enter the title of the movie: ")
        Director = input("Enter the name of the director: ")
        Year = input("Enter the year the movie was released: ")
        New_movie_available_copies = int(input("Enter the number of available copies: "))
        description = input("Enter the description of the movie: ")
        # Verifica si la película ya existe por el ID
        if Movie_ID in df_movies['Movie ID'].values:
            print(f"The movie with ID {Movie_ID} already exists. It cannot be added.")
        else:
            new_movie = pd.DataFrame({
                'Movie ID': [Movie_ID],
                'Title': [Title],
                'Director': [Director],
                'Year': [Year],
                'Available Copies': [New_movie_available_copies],
                'description': [description]
            })
            df_movies = pd.concat([df_movies, new_movie], ignore_index=True)
            print(f"The new movie '{Title}' has been added.")
    elif action_movies == "delete":
        # Pedimos el ID a eliminar.
        movie_id_delete = int(input("Enter the ID of the movie to delete: "))
        if movie_id_delete in df_movies['Movie ID'].values:
            df_movies = df_movies[df_movies['Movie ID'] != movie_id_delete]
            print(f"The movie with ID: {movie_id_delete} has been deleted.")
        else:
            print(f"No movie found with ID {movie_id_delete}.")
    else:
        print("Invalid action, please select 'add' or 'delete'.")

    # Guardamos el data frame actualizado
    df_movies.to_csv('movies.csv', index=False)

# Función para ver número de copias disponibles
def view_available_copies():
    movie_id_copies = int(input("Enter the movie ID to see the number of available copies: "))
    # Buscamos la película por su ID
    movie_row = df_movies[df_movies['Movie ID'] == movie_id_copies]
    if not movie_row.empty:
        available_copies = movie_row['Available Copies'].values[0]  # Obtenemos el número de copias disponibles
        print(f"The movie with ID {movie_id_copies} has {available_copies} available copies.")
    else:
        print(f"No movie was found with ID {movie_id_copies}.")

# Función para agregar o eliminar usuarios
def add_or_create_new_users():
    global df_users
    action_user = input('Do you want to add or delete a user? (add/delete): ')

    if action_user == "add":
        add_new_user = int(input("Enter the ID of the new user: "))
        add_new_name = input("Enter the name of the new user: ")

        # Verifica si el ID ya existe
        if add_new_user in df_users['User ID'].values:
            print(f"The user with ID {add_new_user} already exists. Cannot add.")
        else:
            new_user_df = pd.DataFrame({
                'User ID': [add_new_user],
                'User Name': [add_new_name],
            })
            df_users = pd.concat([df_users, new_user_df], ignore_index=True)
            print(f"The new user '{add_new_name}' has been added.")

    elif action_user == "delete":
        # Pedimos el ID a eliminar.
        user_id_delete = int(input("Enter the ID of the user to delete: "))
        if user_id_delete in df_users['User ID'].values:
            df_users = df_users[df_users['User ID'] != user_id_delete]
            print(f"The user with ID: {user_id_delete} has been deleted.")
        else:
            print(f"No user found with ID {user_id_delete}.")
    else:
        print("Invalid action, please select 'add' or 'delete'.")

    # Save the updated dataframe to the CSV
    df_users.to_csv('users.csv', index=False)

# Funciones para la sección de alquiler de películas
def mostrar_menu():
    # Display the main menu and get the user's choice
    print("\nPlease choose your option:")
    print("(1) See available movies")
    print("(2) See movie descriptions")
    print("(3) Full movie list")
    print("(4) Pick a movie to rent")
    print("(5) Return to main menu")
    choice = int(input("Enter your choice: "))
    return choice

def mostrar_peliculas_disponibles():
    # Display list of currently available movies
    available_movies = df_movies[df_movies['Available Copies'] > 0]
    if not available_movies.empty:
        print("\nShowing available movies:\n")
        for index, row in available_movies.iterrows():
            print(f"{row['Movie ID']}. {row['Title']}")
    else:
        print("\nNo movies are currently available.")

def mostrar_descripcion_peliculas(df_movies):
    # Mostrar las descripciones de todas las películas desde el DataFrame
    print("\nMovie Descriptions:\n")
    for index, row in df_movies.iterrows():
        print(f"{row['Movie ID']}. {row['Title']} - {row['description']}")

def mostrar_lista_completa(df_movies):
    # Display the full list of movies
    print("\nShowing full movie list:\n")
    for index, row in df_movies.iterrows():
        print(f"{row['Movie ID']}. {row['Title']}")

def rent_movie(user_id, movie_id):
    global df_movies, df_borrowing
    # Check if the movie exists
    movie_row = df_movies[df_movies['Movie ID'] == movie_id]
    if movie_row.empty:
        print(f"No movie was found with ID {movie_id}.")
        return
    # Check if there are available copies
    available_copies = movie_row['Available Copies'].values[0]
    if available_copies <= 0:
        print(f"No available copies for movie ID {movie_id}.")
        return
    # Update available copies
    df_movies.loc[df_movies['Movie ID'] == movie_id, 'Available Copies'] = available_copies - 1
    # Update borrowing records
    borrow_date = pd.Timestamp.now().strftime('%Y-%m-%d')
    df_borrowing = pd.read_csv('borrowing_records.csv')
    if user_id in df_borrowing['user id'].values:
        # Append movie ID to existing record
        current_movie_ids = df_borrowing.loc[df_borrowing['user id'] == user_id, 'movie ids'].values[0]
        if current_movie_ids == '':
            updated_movie_ids = str(movie_id)
        else:
            updated_movie_ids = f"{current_movie_ids},{movie_id}"
        df_borrowing.loc[df_borrowing['user id'] == user_id, 'movie ids'] = updated_movie_ids
    else:
        # Create new borrowing record
        new_borrowing = pd.DataFrame({
            'user id': [user_id],
            'movie ids': [str(movie_id)],
            'borrow_date': [borrow_date]
        })
        df_borrowing = pd.concat([df_borrowing, new_borrowing], ignore_index=True)
    # Save updates to CSV
    df_movies.to_csv('movies.csv', index=False)
    df_borrowing.to_csv('borrowing_records.csv', index=False)
    print(f"Movie with ID {movie_id} has been rented to user {user_id}.")

# Función para devolver una película
def return_movie(user_id):
    global df_movies, df_borrowing
    movie_id_to_return = int(input("Enter the movie ID to return: "))
    df_borrowing = pd.read_csv('borrowing_records.csv')
    df_borrowing['movie ids'] = df_borrowing['movie ids'].astype(str)
    user_borrowing = df_borrowing[df_borrowing['user id'] == user_id]

    if not user_borrowing.empty:
        borrowed_movie_ids = user_borrowing['movie ids'].iloc[0].split(',')
        if str(movie_id_to_return) in borrowed_movie_ids:
            # Remove the movie ID from 'movie ids'
            borrowed_movie_ids.remove(str(movie_id_to_return))
            # Update the borrowing record
            new_movie_ids = ','.join(borrowed_movie_ids)
            df_borrowing.loc[df_borrowing['user id'] == user_id, 'movie ids'] = new_movie_ids
            # If no movies left, remove the record
            if new_movie_ids == '':
                df_borrowing = df_borrowing[df_borrowing['user id'] != user_id]
            # Increase the available copies in df_movies
            df_movies.loc[df_movies['Movie ID'] == movie_id_to_return, 'Available Copies'] += 1
            # Save changes
            df_movies.to_csv('movies.csv', index=False)
            df_borrowing.to_csv('borrowing_records.csv', index=False)
            print(f"Movie with ID {movie_id_to_return} has been returned by user {user_id}.")
        else:
            print(f"User {user_id} does not have movie with ID {movie_id_to_return} borrowed.")
    else:
        print(f"User {user_id} does not have any movies borrowed.")

# Menú para devolución de películas
def movie_return_menu(user_id):
    while True:
        print("\n=== Movie Return Menu ===")
        print("1. Return a movie by movie ID")
        print("2. View your borrowing records")
        print("3. Exit")

        option = int(input("Choose an option (1, 2, or 3): "))
        if option == 1:
            return_movie(user_id)
        elif option == 2:
            view_records(user_id)
        elif option == 3:
            break
        else:
            print("Invalid option, please select again.")

def view_records(user_id):
    df_borrowing = pd.read_csv('borrowing_records.csv')
    user_records = df_borrowing[df_borrowing['user id'] == user_id]
    if user_records.empty:
        print("\nYou have no borrowing records.")
    else:
        print("\nYour Current Borrowing Records:")
        for index, row in user_records.iterrows():
            print(f"Borrowed Movies IDs: {row['movie ids']}, Borrow Date: {row['borrow_date']}")

# Programa principal
if __name__ == "__main__":
    while True:
        # Empezamos el programa
        welcome_user(df_users)

        user_welcome_menu = input("Please enter your choice: ")
        if user_welcome_menu == '1':
            user_id = int(input("Please enter your User ID: "))

            # Busca el nombre del usuario en el DataFrame
            user_row = df_users[df_users['User ID'] == user_id]

            if not user_row.empty:
                user_name = user_row['User Name'].values[0]  # Extrae el nombre del usuario
                print(f"\nWelcome {user_name}! Now you are in the main menu.")

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
                                mostrar_lista_completa(df_movies)
                            elif choice == 4:
                                movie_id = int(input("Enter the Movie ID of the movie you want to rent: "))
                                rent_movie(user_id, movie_id)
                            elif choice == 5:
                                break  # Regresar al menú de usuario
                            else:
                                print("Invalid option, please select again.")

                    elif user_choice == "2":
                        # Return a movie
                        movie_return_menu(user_id)

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

                # Actualizar archivos CSV al salir del menú de usuario
                df_users.to_csv('users.csv', index=False)
                df_movies.to_csv('movies.csv', index=False)
                df_borrowing.to_csv('borrowing_records.csv', index=False)

            else:
                print("Invalid User ID. Please try again.")

        elif user_welcome_menu == '2':
            print("\nHere are all users:")
            print(df_users[['User ID', 'User Name']])  # Muestra todos los usuarios

        else:
            print("Invalid option. Please try again.")
