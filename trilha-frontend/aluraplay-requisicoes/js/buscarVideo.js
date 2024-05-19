import { conectaApi } from "./conectaApi.js";

async function buscarVideo(evento) {
  evento.preventDefault();
  const dadosDePesquisa = document.querySelector("[data-pesquisa]").value;
  const busca = await conectaApi.buscaVideo(dadosDePesquisa);
  console.log("🚀 ~ buscarVideo ~ busca:", busca);
}

const botaoPesquisa = document.querySelector("[data-botao-pesquisa]");

botaoPesquisa.addEventListener("click", (evento) => buscarVideo(evento));
