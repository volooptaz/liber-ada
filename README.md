# liber-ada

Liber Ada: Um Entrelaçamento de Raios Octarina; Uma Fuga Festiva no Espírito de Sophia

https://volooptaz.art/liber-ada/

## Arquivos

- **README.md**: este arquivo :-)
- **liber-ada.yml**: estruturação experimental da sequência de "atos" do Liber Ada. É utilizado para produzir os vídeos utilizando o [OBS Studio](https://obsproject.com/), o [youtube-dl](https://youtube-dl.org/), o [VLC](https://www.videolan.org/vlc/index.html) e incontáveis outros gigantes sobre os ombros de quais estou.
- **traverse.py**: script para percorrer o arquivo .yml e transformar no arquivo reStructuredText abaixo, através do [RstCloth](https://rstcloth.readthedocs.io/).
- **liber-ada.rst**: arquivo gerado como resultado de `traverse.py > liber-ada.rst`. Em formato [reStructuredText](https://docutils.sourceforge.io/rst.html), atravs do 
- **liber-ada.pdf**: transformação do arquivo em PDF. Utilizei o [Pandoc](https://pandoc.org/): `pandoc liber-ada.rst -o liber-ada.pdf --pdf-engine=lualatex --template=my.latex --variable mainfont="Noto Serif" --variable sansfont="Noto Sans"`
- **my.latex**: template LaTeX para ser utilizado na conversão para PDF. 
- **schema.yaml**:  primeira tentativa de um schema para acompanhar o `liber-ada.yml` e futuras obras parecidas. Utiliza [Yamale](https://github.com/23andMe/Yamale/).
- **LICENSE**: licença do projeto. GNU Public License - GPLv3



