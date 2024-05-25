async function listaVideos() {
  const conexao = await fetch("http://localhost:3000/videos");
  console.log("🚀 ~ listaVideos ~ conexao:", conexao);
  const conexaoConvertida = await conexao.json();
  console.log("🚀 ~ listaVideos ~ conexaoConvertida:", conexaoConvertida);

  return conexaoConvertida;
}

// Requisições do tipo POST são usadas para enviar dados para a API.

// Diferente de requisições do tipo GET, você precisará passar um objeto das opções de configuração como um segundo argumento em requisições POST.

async function criaVideo(titulo, descricao, url, imagem) {
  const conexao = await fetch("http://localhost:3000/videos", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      titulo: titulo,
      descricao: `${descricao} mil visualizações`,
      url: url,
      imagem: imagem,
    }),
  });

  if (!conexao.ok) {
    throw new Error("Não foi possível enviar o vídeo!");
  }

  const conexaoConvertida = await conexao.json();
  return conexaoConvertida;
}

async function buscaVideo(termoDeBusca) {
  const conexao = await fetch(`http://localhost:3000/videos?q=${termoDeBusca}`);
  const conexaoConvertida = await conexao.json();

  return conexaoConvertida;
}

export const conectaApi = { listaVideos, criaVideo, buscaVideo };
