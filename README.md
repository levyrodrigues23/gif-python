# Criador de GIF com Python e ImageIO

Este projeto é um script simples em Python para criar um GIF animado a partir de imagens PNG usando a biblioteca [imageio](https://imageio.readthedocs.io/).

## Como funciona

O script lê uma lista de arquivos de imagem (`.png`) e os combina em um único arquivo GIF animado.

## Pré-requisitos

- Python 3.7 ou superior
- Biblioteca `imageio`

Instale a biblioteca com:
```
pip install imageio
```

## Estrutura do Projeto

```
gif python/
├── image.io/
│   ├── create_gif.py
│   ├── nyan-cat1.png
│   ├── nyan-cat2.png
│   ├── nyan-cat3.png
```

## Como usar

1. Coloque suas imagens PNG na mesma pasta do script `create_gif.py`.
2. Edite a lista `filenames` no script para corresponder aos nomes dos seus arquivos.
3. Execute o script:

```
python create_gif.py
```

O GIF será salvo como `nyan-cat.gif` na mesma pasta.

## Exemplo de código

```python
import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
imagens = []

for filename in filenames:
    imagens.append(iio.imread(filename))

iio.imwrite('nyan-cat.gif', imagens, duration=500, loop=0)
```

## Dicas de solução de problemas

- Certifique-se de que os nomes dos arquivos nas listas estão corretos e que os arquivos existem na pasta.
- Para verificar se os arquivos existem, adicione este trecho ao seu script:
    ```python
    import os
    for filename in filenames:
        if not os.path.isfile(filename):
            print(f"Arquivo não encontrado: {filename}")
        else:
            print(f"Arquivo encontrado: {filename}")
    ```
- Se receber erro `FileNotFoundError`, confira o nome e o caminho dos arquivos.

## Licença

Este projeto está sob a licença MIT.
