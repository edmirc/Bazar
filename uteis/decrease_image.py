from PIL import Image
from os import listdir, path
def decrease_image():
    caminho = 'C:\\Projetos\\Bazar\\media\\products'
    for pasta in listdir(caminho):
        caminho_arquivo = path.join(caminho, pasta)
        redimensionar_e_salvar(caminho_arquivo)
    print('Imagens redimensionadas e salvas com sucesso!')

def redimensionar_e_salvar(caminho):
    with Image.open(caminho) as img:
        # Calcula as novas dimensões mantendo a proporção
        largura, altura = img.size
        if largura >= 800 or altura >= 1000:
            proporcao = min(800/largura, 1000/altura)
            nova_largura = int(largura * proporcao)
            nova_altura = int(altura * proporcao)
            # Redimensiona com LANCZOS para melhor qualidade
            img_redimensionada = img.resize((nova_largura, nova_altura), Image.LANCZOS)
        
            # Salva com qualidade ajustável
            if caminho.lower().endswith('.jpg') or caminho.lower().endswith('.jpeg'):
                img_redimensionada.save(caminho, quality=85, optimize=True)
            else:
                img_redimensionada.save(caminho)
# Exemplo de uso:
if __name__ == "__main__":
     decrease_image()