from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # C'est la clé pour que GitHub puisse accéder à ton localhost

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    sujet = data.get('topic')
    
    # Ici, c'est normalement là que l'IA travaille.
    # Pour le test, on renvoie une réponse fixe :
    reponse = {
        "titre": f"COMMENT DEVENIR RICHE AVEC {sujet.upper()}",
        "description": "Cette vidéo va changer votre vie...",
        "tags": f"{sujet}, IA, Argent, 2026"
    }
    return jsonify(reponse)

if __name__ == '__main__':
    # Le serveur se lance sur le port 5000
    app.run(host='0.0.0.0', port=5000)
