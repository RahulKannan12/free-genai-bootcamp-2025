from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data
DUMMY_VOCAB = [
    {'Kanji': '猫', 'reading': 'ねこ', 'english': 'cat'},
    {'Kanji': '犬', 'reading': 'いぬ', 'english': 'dog'},
    {'Kanji': '本', 'reading': 'ほん', 'english': 'book'},
    {'Kanji': '学校', 'reading': 'がっこう', 'english': 'school'},
    {'Kanji': '先生', 'reading': 'せんせい', 'english': 'teacher'}
]

@app.route('/api/groups/<id>/raw', methods=['GET'])
def get_vocabulary(id):
    return jsonify(DUMMY_VOCAB)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
