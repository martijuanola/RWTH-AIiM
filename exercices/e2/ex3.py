import pandas as pd
import re


def count_words(filepath, target_words):
    #load file
    with open(filepath, 'r', encoding='latin1') as f:
        #remove header
        f.readline()

        full_text = f.read()
    #convert all word to lower case
    all_text_lower = full_text.lower()
    #tokenize words
    words = re.findall(r'\b\w+\b', all_text_lower)
    #count all words
    all_words_nr = len(words)
    #turn list into pandas column
    word_series = pd.Series(words)
    #filter out the words we want to count
    target_word_series = word_series[word_series.isin(target_words)]
    #count the words
    word_counts = target_word_series.value_counts()
    #make sure that all target words are returned, especially the ones that have 0 occurences
    final_counts = word_counts.reindex(target_words, fill_value=0)

    return final_counts,all_words_nr

if __name__ == "__main__":

    FILE_PATH = 'data/lyrics50.csv'
    TARGET_WORDS = ['always', 'but', 'christmas', 'city', 'feel', 'love', 'think', 'you', 'world', 'yeah']

    #get pandas series where every words has its occurence nr next to it
    counts,all_words_nr = count_words(FILE_PATH, TARGET_WORDS)

    #calculate tf for every entry in counts series
    tf = counts/all_words_nr

    #calculate idf, but we have only one document, where every word is contained so log(1/1) = 0
    idf = 0

    #calculate tf -df
    tf_idf = tf * idf

    #print solutions
    print("target words:")
    print(TARGET_WORDS)
    print("")
    print("from:")
    print(FILE_PATH)
    print("")
    print("Term Frequencies (TF) for every target word")
    print(tf)
    print("")
    print("Inverse Document Frequency (IDF), Note: for every target word holds log(1/1) = 0 here")
    print(idf)
    print("")
    print("!!!!SOLUTION OF TF*IDF!!!!")
    print(tf_idf)







