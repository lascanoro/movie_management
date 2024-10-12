import pandas as pd
#Cargar datos de usuarios, voy a usar "df" para indicar que es un dataframe.
df_users=pd.read_csv('users.csv')
df_movies=pd.read_csv('movies.csv')
#Creo las columnas para el data frame de borrowing
borrowing_records= ['user id','movie ids','borrow_date']

#Ahora que ya estan especificadas las columnas que queiro, vamos a crear el dataframe de borrowing
df_borrowing_records=pd.DataFrame(columns=borrowing_records)
#Creo el csv de borrowing records
df_borrowing_records.to_csv('borrowing_records.csv',index=False)
#Agrego columna descripcion a data frame movies
df_movies['description']=None
#Ahora creo un diccionario con la descripcion de la pelicula.
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
#llenar la columna 'description' con la informacion de movie descriptions
df_movies['description']=df_movies['Movie ID'].map(movie_descriptions)
#Guardo el data frame actualizado en el .csv 
df_movies.to_csv('movies.csv',index=False)
