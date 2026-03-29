async function processAI() {
    const topic = document.getElementById('topic').value;
    const btn = document.querySelector('.btn-prime');
    const resultBox = document.getElementById('script-box');

    if(!topic) return alert("Choisis un sujet !");

    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> CALCUL IA...';
    
    try {
        const response = await fetch('http://127.0.0.1:5000/generate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ topic: topic })
        });

        const data = await response.json();
        
        if(data.status === "success") {
            // Transforme le texte de l'IA en HTML lisible
            resultBox.innerHTML = data.content.replace(/\n/g, "<br>");
            btn.innerText = 'GÉNÉRER À NOUVEAU';
        } else {
            alert("Erreur: Lance Ollama sur ton PC !");
        }
    } catch (error) {
        console.error(error);
        alert("Le serveur Python n'est pas lancé.");
    }
}
