import pandas as pd
import numpy as np
import csv

df1=pd.read_csv('tmdb_5000_credits.csv')
df2=pd.read_csv('tmdb_5000_movies.csv')

df1.columns=['id','title','cast','crew']
df2=df2.merge(df1,on='id')

df2.to_csv('movies.csv')
df2=df2.reset_index()
indices=pd.Series(df2.index,index=df2['title'])
with open('movies.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)
