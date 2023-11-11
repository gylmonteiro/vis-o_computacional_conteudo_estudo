import os

def rename_images_in_directory(directory, prefix="image"):
    """
    Renomeia as imagens em um diretório de forma sequencial com um prefixo específico.

    Args:
    - directory (str): Caminho do diretório onde as imagens estão localizadas.
    - prefix (str): Prefixo a ser usado ao renomear as imagens.
    """
    
    # Lista de extensões de imagens válidas
    valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"]
    
    # Listar todos os arquivos do diretório
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Filtrar apenas imagens com extensões válidas
    images = [f for f in files if os.path.splitext(f)[1].lower() in valid_extensions]

    # Renomear cada imagem
    for idx, image in enumerate(images, start=1):
        original_path = os.path.join(directory, image)
        new_name = f"{prefix}_{idx}{os.path.splitext(image)[1]}"
        new_path = os.path.join(directory, new_name)
        
        os.rename(original_path, new_path)
        print(f"{image} -> {new_name}")

if __name__ == "__main__":
    dir_path = input("Digite o caminho do diretório contendo as imagens: ")
    prefix = input("Digite o prefixo desejado para as imagens (por padrão, será 'image'): ") or "image"
    
    rename_images_in_directory(dir_path, prefix)
