import pandas as pd

# Definir la ruta completa a la carpeta de los archivos
base_path = "C:/Users/patri/Desktop/Phython/piton clonasion/movie_management/movie_management/"

# Cargar los registros de préstamos desde el archivo CSV
borrowing_records = pd.read_csv(base_path + 'borrowing_records.csv')

# Cargar datos de películas desde el archivo CSV
df_movies = pd.read_csv(base_path + 'movies.csv')

# Mostrar los registros de préstamo cargados
print("Initial Borrowing Records:")
print(borrowing_records.head())

# Función para devolver una película
def return_movie(df_borrowing, df_movies, user_id, movie_id):
    # Verificar si el usuario ha tomado prestada la película
    user_borrowing = df_borrowing[(df_borrowing['user id'] == user_id) & (df_borrowing['movie ids'].str.contains(str(movie_id)))]
    
    if not user_borrowing.empty:
        # Remover el ID de la película de la columna 'movie ids'
        df_borrowing['movie ids'] = df_borrowing['movie ids'].apply(lambda ids: ','.join([id for id in ids.split(',') if id != str(movie_id)]))
        
        # Eliminar filas donde todas las películas han sido devueltas (columna 'movie ids' vacía)
        df_borrowing = df_borrowing[df_borrowing['movie ids'] != '']
        
        print(f"Movie with id {movie_id} has been returned by user {user_id}.")
    else:
        print(f"User {user_id} does not have movie with id {movie_id} borrowed.")
    
    return df_borrowing

# Menú para devolución de películas
def movie_return_menu(df_borrowing, df_movies):
    while True:
        print("\n=== Movie Return Menu ===")
        print("1. Return a movie by movie ID")
        print("2. View current borrowing records")
        print("3. Exit")
        
        option = input("Choose an option (1, 2, or 3): ")
        
        if option == '1':
            user_id = int(input("Enter the user ID: "))
            movie_id = int(input("Enter the movie ID: "))
            
            # Llamar a la función return_movie para procesar la devolución
            df_borrowing = return_movie(df_borrowing, df_movies, user_id, movie_id)
        
        elif option == '2':
            print("\n=== Current Borrowing Records ===")
            print(df_borrowing)
        
        elif option == '3':
            print("Exiting the return system.")
            break
        
        else:
            print("Invalid option. Please try again.")
    
    return df_borrowing

# Simular algunos registros de préstamo
data_borrowing = {'user id': [1, 2],
                  'movie ids': ['101,102', '103'],
                  'borrow_date': ['2024-10-01', '2024-10-03']}

# Crear el DataFrame de registros de préstamo
borrowing_records = pd.DataFrame(data_borrowing)

# Ejecutar el menú de devolución de películas
updated_borrowing_records = movie_return_menu(borrowing_records, df_movies)

# Guardar los registros de préstamo actualizados en el archivo CSV
updated_borrowing_records.to_csv(base_path + 'borrowing_records.csv', index=False)

# Mostrar los registros de préstamo actualizados después de procesar las devoluciones
print("\n=== Updated Borrowing Records ===")
print(updated_borrowing_records)
