from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama # Utilise l'IA locale gratuite

app = Flask(__name__)
CORS(app) # Autorise ton site web à parler à ce script

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    topic = data.get('topic')
    
    # Prompt ultra-puissant pour forcer l'IA à être virale
    prompt = f"""
    Tu es un expert en croissance YouTube (style MrBeast). 
    Sujet : {topic}
    Donne-moi :
    1. Trois titres 'Clickbait' mais honnêtes.
    2. Une idée de miniature choc.
    3. Un script court (intro de 30 sec) qui retient l'attention.
    Réponds en Français.
    """

    try:
        # Appel du modèle local (Llama3 ou Mistral)
        response = ollama.chat(model='llama3', messages=[
            {'role': 'user', 'content': prompt},
        ])
        
        return jsonify({
            "status": "success",
            "content": response['message']['content']
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    print("🚀 Serveur RED-AI lancé sur http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
