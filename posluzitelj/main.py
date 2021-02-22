from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import uuid
from uuid import uuid4

app = Flask(__name__)
CORS(app)

def create_connection():
    try:
        db = sqlite3.connect('baza.db')
        return db
    except:
        return None


def close_connection(db):
    db.close()


@app.route('/')
def start():
    return 'Server is up and runing!'


@app.route('/register', methods=['POST'])
def register():
    post_data = request.get_json()
    ime = post_data.get('ime')
    prezime = post_data.get('prezime')
    oib = post_data.get('oib')
    broj_mobitela = post_data.get('broj_mobitela')
    q = registerkorisnik(ime, prezime, oib, broj_mobitela)
    if q == 0:
        return jsonify({
            'status': 'unseccessful'
        })
    else:
        return jsonify({
            'status': 'success'
        })
        
@app.route('/izbori', methods=['PUT'])
def jedanGlas():
    put_data = request.get_json()
    id = put_data.get('id')
   
    q = UpdateRezultat(id)
    if q == 0:
        return jsonify({
            'status': 'unseccessful'
        })
    else:
        return jsonify({
            'status': 'success'
        })

@app.route('/rezultati', methods=['GET'])
def rezultati():
    
    q = NumberofVote()
    if q == 0:
        return jsonify({
            'status': 'unseccessful'
        })
    else:
        return jsonify({
            'status': 'success',
            'data': q
        })
    

    
def registerkorisnik(ime, prezime, oib, broj_mobitela):
    kor_id = uuid4().hex
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Korisnik (id, ime, prezime, oib, broj_mobitela) VALUES (?, ?, ?, ?, ?)",
                   (kor_id, ime, prezime, oib, broj_mobitela))
    conn.commit()
    close_connection(conn)
    return kor_id


def UpdateRezultat(id_kandidata):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Kandidati set gl_brojglasova= gl_brojglasova+1 where ID=?", (id_kandidata,))
    conn.commit()
    close_connection(conn)
    return id_kandidata

def NumberofVote():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Kandidati")
    _brojglasova = cursor.fetchall()
    brojglasova = list(_brojglasova)
    conn.close()
    return brojglasova


if __name__ == '__main__':
    app.run(debug=True)
