# Open Videos

### Programa para automatizar a abertura das páginas de animes semanais

#### Problema

<p align="justify">
	Eu acompanho vários lancamentos de animes durante a semana, mas não uso um site que gerencie isso.
	Então, eu vi aquele mesmo processo de ficar pesquisando qual anime vou assistir, pesquisar no site, 
	e depois procurar o último episódio visto.
</p>
<p align="justify">
	Se uma pessoa assistir poucos animes semanalmente é bem tranquilo, mas como assisto muitos, o processo
	se torna algo repetitivo e cansativo. Por conta disso, me motivei a criar um código que permitisse 
	automatizar boa parte do processo.
</p>

#### Funcionamento

<p align="justify">
	Se você quiser utilizar, não é preciso saber nada do que foi codificado, somente saber manipular o 
	arquivo de texto "open_videos.txt". Além disso, é preciso saber um pouco como funciona as URL's que 
	aparecem na barra do navegador. Com isso, só é preciso memorizar as palavras reservadas e como 
	colocar as URL's corretamente no documento.
</p>
<p align="justify">
	O arquivo de texto foi feito pra interpretar comandos-chave pra identificar a lista de animes e a
	lista de servidores disponíveis. Portanto, é preciso formatar o arquivo de texto corretamente. Beleza,
	mas como que isso funciona? Simples! Existem duas palavras-chave (ou palavras reservadas). Elas são 
	respectivamente, "--animes--" e "--servidores". O programa identifica "--animes--" e pega tudo abaixo
	dele e insere na lista de animes disponíveis até que se identifique a palavra-chave "--servidores--".
</p>
<p align="justify">
	Quando identificado a string "--servidores--", a função é encerrada. Para inicializar a lista de servidores, 
	é preciso ter um processo bem semelhante a função de inicializar a lista de animes, porém não é necessário 
	verificar palavras reservadas abaixo, pois até o momento não exitem outras. (Se em versões futuras forem 
	necessárias mais palavras-chave, essa função será igual a anterior).
</p>

#### Na Prática

<p align="justify">
	Supondo que você queira acompanhar Bleach, então pelo menos uma única vez é preciso acessar o site/servidor
	que você vai assistir para copiar a URL manualmente. Pegando a URL, podemos ver, por exemplo, um endereço 
	parecido com esse: "https://openvideos.com/animes/bleach". O que precisa ser feito agora é segmentar esse 
	endereço.
</p>
<p align="justify">
	Se você quiser acompanhar outros animes no mesmo site/servidor, será preciso colocar no arquivo 
	"open_videos.txt", abaixo de "--servidores--", somente a parte responsável pelo servidor. Por exemplo: "https://openvideos.com/animes/". Se quiser colocar o anime de Bleach na sua lista de animes assistidos, 
	então é preciso colocar esse trecho da URL: "bleach/" abaixo de "--animes--".
</p>
<p align="justify">
	Se você for mais observador, pode ter percebido que o trecho de "bleach/" está diferente da URL original: "https://openvideos.com/animes/bleach". Isso se deve ao fato de que não há padrões nos nomes de 
	URL's entre sites/servidores. Em alguns testes manuais, achei um padrão para alguns sites, onde utilizar 
	o "/" no fim pode resolver alguns desses problemas de compatibilidade. Se não resolver, ele é 
	simplesmente ignorado.
</p>
<p align="justify">
	É bastante comum termos erros para abrir os animes com esses trechos de URL, justamente por conta dessa
	"não-padronização", mas principalmente por causa de estarmos acessando um back-end que não foi projetado 
	para servir o cliente dessa forma, através desses tipos de requisições, ao contrário do que ocorre numa API. 
</p>

#### Outras utilidades

<p align="justify">
	Além de abrir sites de animes, é possivel usar o programa para abrir qualquer site, pois é utilizado URL's.
	Isso pode incluir aplicações desktop, como Netflix. Se você utilizar a versão web, é possivel ver a URL e 
	simular requisições baseado no padrão visto. Logicamente, é preciso ter a versão paga da Netflix para que 
	funcione. Esse programa não tem o intuito de piratear nada, ele apenas gerencia e automatiza aberturas de 
	várias abas de sites em navegadores.
</p>