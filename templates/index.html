
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu Banco</title>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        button { padding: 10px; font-size: 16px; cursor: pointer; }
        #lista-usuarios { list-style-type: none; padding: 0; }
        #lista-usuarios li { border: 1px solid #ccc; margin: 10px 0; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>

    <h1>Bem-vindo ao Banco Virtual</h1>
    <p>Clique no botão abaixo para ver a lista de clientes cadastrados.</p>

    <button id="buscar-clientes">Buscar Clientes</button>

    <hr>

    <h2>Clientes:</h2>
    <ul id="lista-usuarios">
        </ul>

    <script>
    const botao = document.getElementById('buscar-clientes');
    const lista = document.getElementById('lista-usuarios');

    botao.addEventListener('click', async () => {
        const response = await fetch('/api/usuarios');
        const usuarios = await response.json();
        lista.innerHTML = '';

        usuarios.forEach(usuario => {
            const item = document.createElement('li');
            
            // Vamos construir o HTML do item dinamicamente
            let htmlContent = '';

            // Usamos Object.entries para pegar cada [chave, valor] do documento
            for (const [chave, valor] of Object.entries(usuario)) {
                
                // 1. Ignoramos o campo '_id' para não mostrar na tela
                if (chave === '_id') {
                    continue; // Pula para a próxima chave
                }

                // Formata o nome da chave para ficar mais bonito (ex: "redes_sociais" -> "Redes sociais")
                const chaveFormatada = chave.charAt(0).toUpperCase() + chave.slice(1).replace('_', ' ');

                // 2. Verificamos o TIPO do valor para exibi-lo da melhor forma
                if (Array.isArray(valor)) {
                    // Se for uma lista (como habilidades), juntamos com vírgula
                    htmlContent += `<strong>${chaveFormatada}:</strong> ${valor.join(', ')} <br>`;
                } 
                else if (typeof valor === 'object' && valor !== null) {
                    // Se for um objeto aninhado (como redes_sociais), criamos uma sub-lista
                    htmlContent += `<strong>${chaveFormatada}:</strong>`;
                    let subLista = '<ul>';
                    for (const [subChave, subValor] of Object.entries(valor)) {
                        subLista += `<li>${subChave}: ${subValor}</li>`;
                    }
                    subLista += '</ul>';
                    htmlContent += subLista;
                } 
                else {
                    // Para todos os outros tipos (texto, número, etc.)
                    htmlContent += `<strong>${chaveFormatada}:</strong> ${valor} <br>`;
                }
            }

            item.innerHTML = htmlContent;
            lista.appendChild(item);
        });
    });
</script>

</body>
</html>
