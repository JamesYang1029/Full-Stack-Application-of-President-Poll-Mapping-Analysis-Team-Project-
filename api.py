import pymongo
from flask import Flask, jsonify

#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["language_word_count"]

app = Flask(__name__)

@app.route("/api/v1/<language>")
def get_api_lang(language):
	data = list(db[language].find({}, {'_id': False}))
	return jsonify(data)

if __name__ == "__main__":
    app.run()