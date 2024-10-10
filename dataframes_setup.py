#Cargar datos de usuarios, voy a usar "df" para indicar que es un dataframe.
df_users=pd.read_csv('users.csv')
df_movies=pd.read_csv('movies.csv')
#Primero,Creo un diccionario con borrowing records 
borrowing_records= [
    {"user_id":1,"movie_ids":[101,102],"borrow_date":"2024-09-01"},
    {"user_id":2,"movie_ids":[103],"borrow_date":"2024-09-05"}
]
#Ahora que ya esta creado el diccionario, vamos a crear el dataframe de borrowing
df_borrowing_records=pd.DataFrame(borrowing_records)
#Ahora imprimo para probar que se creo correctamente
print(df_borrowing_records)
print(df_users)
print(df_movies)