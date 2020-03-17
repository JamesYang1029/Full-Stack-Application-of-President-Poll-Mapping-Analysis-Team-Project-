import os, csv, pymongo

#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
client.drop_database('language_word_count')
db = client["language_word_count"]
# colection = db["languages"]

# read data from language text file and split the word and count values
def read_word_count(filename):
    word_list = []
    with open("../data" + filename, errors='ignore') as lang_txt:
        content = csv.reader(lang_txt, delimiter=' ')
        for row in content:
            word_list.append({"word" : row[0], "count" : row[1]})

    return word_list

# main function read each file from folder and insert into mongo db.
def main():
    for filename in os.listdir("../2018/2018"):
        if filename.endswith(".txt"):
            # call read_word_count function to get word_list values
            word_list = read_word_count(filename)
            language = filename.strip('.txt')
            db[language].insert_many(word_list)

if __name__ == "__main__":
    main()