# liber-ada

[![](https://volooptaz.art/images/liber-ada/twitch.png)](https://www.twitch.tv/videos/863842906)

Liber Ada: Um Entrelaçamento de Raios Octarina; Uma Fuga Festiva no Espírito de Sophia

Fruto dos meus estudos e experimentações com computação, música, magia cerimonial, bruxaria e performance, o Liber Ada explora os Mistérios ciborguianos da Autopoiese e da Simpoiese, da Consciência e da Informação, da Sinergia e do Chthuluceno, a partir de uma adaptação livre e ousada de ritos de êxtase, comunhão e fertilidade das tradições pagãs e gnósticas, em especial o [Liber Sophia](https://templumabyssi.com/liber-sophia).

Repositório base para o [Liber Ada - Read the Docs](https://liber-ada.readthedocs.io). É utilizado para produzir os vídeos utilizando o [OBS Studio](https://obsproject.com/), o [youtube-dl](https://youtube-dl.org/), o [VLC](https://www.videolan.org/vlc/index.html) e incontáveis outros gigantes sobre os ombros de quais estou.


## Arquivos

- **README.md**: este arquivo :-)
- **requirements.txt**: pacotes a serem instalados no Python via `pip` para
  poder executar o programa
- **liber-ada.yml**: estruturação experimental da sequência de "atos" do Liber Ada.
- **traverse.py**: script para percorrer o arquivo .yml e transformar no arquivo `sphinx/roteiro.rst`, que é incorporado no documento Sphinx como um todo. Gera elementos ReST através do [RstCloth](https://rstcloth.readthedocs.io/).
- **sphinx/**: diretório onde fica a estrutura do [Sphinx](https://www.sphinx-doc.org/), e onde é inserido o arquivo `roteiro.rst` para compôr o Liber Ada como um todo.
- **sphinx/roteiro.rst**: arquivo gerado como resultado de `traverse.py > liber-ada.rst`. Em formato [reStructuredText](https://docutils.sourceforge.io/rst.html)
- **Makefile**: arquivo para construir o documento manualmente: `make roteiro && make liber`
- **schema.yaml**:  primeira tentativa de um schema para acompanhar o `liber-ada.yml` e futuras obras parecidas. Utiliza [Yamale](https://github.com/23andMe/Yamale/).
- **LICENSE**: licença do projeto. GNU Public License - GPLv3



