import mysql.connector
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer


connection = mysql.connector.connect(host='localhost', database='moviesdb', user='root', password='12345')
cursor = connection.cursor(buffered=True)

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("search.html")

@app.route('/search', methods=["POST"])
def search():
    connection = mysql.connector.connect(host='localhost', database='moviesdb', user='root', password='12345')
    cursor = connection.cursor(buffered=True)
    keyword = request.form['search']
    intornot = (str(keyword).isdigit())
    result = []
    results = []
    if not intornot:
        cursor.execute("select * from movie where title LIKE '%{}%' ".format(keyword))
        a = cursor.fetchall()
        if len(a) != 0:
            result.append((len(a), a))
        cursor.execute("select * FROM movie WHERE actorname LIKE '%{}%' ".format(keyword))
        b = cursor.fetchall()
        if len(b) != 0:
            result.append((len(b), b))
        cursor.execute("select * FROM movie WHERE actor2name LIKE '%{}%'  ".format(keyword))
        c = cursor.fetchall()
        if len(c) != 0:
            result.append((len(c), c))
        cursor.execute("select * FROM movie WHERE director_name LIKE '%{}%' ".format(keyword))
        d = cursor.fetchall()
        if len(d) != 0:
            result.append((len(d), d))
        cursor.execute("select * FROM movie WHERE genres LIKE '%{}%' ".format(keyword))
        f = cursor.fetchall()
        if len(f) != 0:
            result.append((len(f), f))
        cursor.execute("select * FROM movie WHERE keyword LIKE '%{}%' ".format(keyword))
        g = cursor.fetchall()
        if len(g) != 0:
            result.append((len(g), g))
        cursor.execute("select * FROM movie WHERE language LIKE '%{}%'".format(keyword))
        h = cursor.fetchall()
        if len(h) != 0:
            result.append((len(h),h,))
        total_count = sum(count for count, _ in result)
        for count, rows in result:
           print(f"Count: {count}")
           for row in rows:
                results.append(row)
        return render_template('index.html', result = results)
    else:
        cursor.execute("select * FROM movie WHERE year LIKE '%{}%' ".format(keyword))
        query = cursor.fetchall()
        return render_template('index.html', result=query)

@app.route('/recommendation', methods=['POST'])
def recommend():
    results = []
    result = []
    import mysql.connector
    keyword = request.form['keyword']

    # establish connection to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
     password="12345",
    database="moviesdb"
    )

    # retrieve the movie data from the database
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT title, genres, actorname,actor2name,director_name FROM movie")

    movies = mycursor.fetchall()
    from sklearn.feature_extraction.text import TfidfVectorizer

    # create a TfidfVectorizer object
    tfidf = TfidfVectorizer()

    # create a list of movie titles
    titles = [movie[0] for movie in movies]

    # create a list of movie genres, actors, and directors
    genres = [movie[1] for movie in movies]
    actors = [movie[2] for movie in movies]
    directors = [movie[3] for movie in movies]

    # concatenate the genres, actors, and directors into a single string for each movie
    movie_features = []
    for i in range(len(movies)):
        genre = genres[i] if genres[i] is not None else ""
        actor1 = actors[i] if actors[i] is not None else ""
        actor2 = directors[i] if directors[i] is not None else ""
        movie_features.append(genre + ' ' + actor1 + ' ' + actor2)

    # create the TF-IDF matrix for the movie features
    tfidf_matrix = tfidf.fit_transform(movie_features)
    from sklearn.metrics.pairwise import cosine_similarity

    # define a function to get the most similar movies
    def get_similar_movies(keyword, tfidf_matrix, titles, top_n=250):
    # transform the search keyword using the TF-IDF vectorizer
        keyword_tfidf = tfidf.transform([keyword])
    
    # calculate the cosine similarity between the search keyword and each movie in the database
        cosine_similarities = cosine_similarity(keyword_tfidf, tfidf_matrix).flatten()
    
    # get the indices of the top N most similar movies
        similar_movie_indices = cosine_similarities.argsort()[::-1][:top_n]
    
    # return the titles of the most similar movies
        return [titles[i] for i in similar_movie_indices]
    # search for movies similar to "The Dark Knight"
    similar_movies = get_similar_movies(keyword, tfidf_matrix, titles)
    # print the similar movies
    

    
    for i in similar_movies:
       query = ("select * FROM movie WHERE title LIKE '%s' ".format (str(i)))
       mycursor.execute(query)
       m = mycursor.fetchall()
       result.append((len(m),m))
       count, rows = (len(m)), m
       for count,rows in result:
            (f"Count: {count}")
            for row in rows:
                results.append(row)    
       
    mycursor.close()
    mydb.close()
    return render_template('recommendationresult.html', result = results)

        
cursor.close()
connection.close()

if __name__ == '__main__':
    app.run(debug=True)


