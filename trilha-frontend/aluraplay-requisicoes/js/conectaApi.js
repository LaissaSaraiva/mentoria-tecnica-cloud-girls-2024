async function listaVideos() {
  const conexao = await fetch("http://localhost:3000/videos");
  console.log("🚀 ~ listaVideos ~ conexao:", conexao);
  const conexaoConvertida = await conexao.json();
  console.log("🚀 ~ listaVideos ~ conexaoConvertida:", conexaoConvertida);

  return conexaoConvertida;
}

export const conectaApi = { listaVideos };
