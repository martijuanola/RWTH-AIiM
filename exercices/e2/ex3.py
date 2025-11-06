import pandas as pd
import re
import numpy as np

def get_song_data(filePath, targetWords):

    df = pd.read_csv(filePath, delimiter=';', header=None, names=["id", "lyrics"], encoding="latin1")

    # NA as text
    songs = df["lyrics"].astype(str).tolist()

    # N from the equation
    number_songs = len(songs)
    
    # tokenize all songs
    all_songs_words = [re.findall(r'\b\w+\b', song.lower()) for song in songs]
    
    # calculate n(i)
    all_songs_sets = [set(words) for words in all_songs_words] 
    
    word_data = {}
    for word in targetWords:
        # calculate freq(i, j) for all j
        # list of occurences where index j is the occurence of word i in song j
        freq_ij_List = [words.count(word) for words in all_songs_words]
         
        # calculate normalisation factor,occurence of i in all songs
        freq_i_AllSongs = sum(freq_ij_List)
        
        # calculate n(i)
        n_i = sum(1 for song_set in all_songs_sets if word in song_set)

        # safe all data for the word i
        word_data[word] = {
            "freq_i_AllSongs": freq_i_AllSongs, 
            "n_i": n_i,                         
            "freq_ij_List": freq_ij_List        
        }
        
    return word_data, number_songs

if __name__ == "__main__":

    filePath = "data/lyrics50.csv"
    targetWords = ["always", "but", "christmas", "city", "feel", "love", "think", "you", "world", "yeah"]

    #get data from lyrics50 file
    word_data, number_songs = get_song_data(filePath, targetWords)

    # calculate IDF
    idf_values = {}
    for word in targetWords:
        n_i = word_data[word]["n_i"]
        
        if n_i > 0:
            idf_values[word] = np.log(number_songs / n_i)
        else:
            idf_values[word] = 0.0

    #calculate TF-IDF
    #create panda series to save solution values
    final_tf_idf = pd.Series(0.0, index=targetWords)
    
    # iterate over number of songs
    for j in range(number_songs):
        
        #iterate over every targetword i
        for word in targetWords:
            data = word_data[word]
            
            #calculate TF
            
            freq_ij = data["freq_ij_List"][j]
            
            freq_i_AllSongs = data["freq_i_AllSongs"]
            
            tf = 0.0
            if freq_i_AllSongs:
                tf = freq_ij / freq_i_AllSongs
            
            idf = idf_values[word]
            
            # calculate TF-IDF
            tf_idf_res = tf * idf
            # add current tf idf result to final solution
            final_tf_idf[word] += tf_idf_res

    print("TF-IDF Results (Sum over all Songs)")
    tf_idf_sorted = final_tf_idf.sort_values(ascending=False)
    print(tf_idf_sorted)
<<<<<<< HEAD
  
=======
  
>>>>>>> bbcefeddbca928f7f32708fd5fcbc340715e20e8
