from astropy.io import fits
import os

# Definindo o caminho da pasta 'fits' dentro da pasta 'saturn'
fits_path = os.path.join('.', 'saturn/fits')

# Nome do arquivo FITS que você deseja acessar
file_name = 'bias_01.fits'

# Construindo o caminho completo para o arquivo FITS
file_path = os.path.join(fits_path, file_name)

# Verificando se o arquivo existe antes de tentar abri-lo
if os.path.exists(file_path):
    # Abrir o arquivo FITS
    with fits.open(file_path) as hdu_list:
        # Exibir informações sobre os HDUs (Header Data Units)
        print("Informações sobre os HDUs:")
        hdu_list.info()

        # Acessar o cabeçalho da primeira HDU
        header = hdu_list[0].header
        print("\nCabeçalho da Primeira HDU:")
        for key in header.keys():
            print(f"{key}: {header[key]}")

        # Acessar os dados da imagem da primeira HDU
        image_data = hdu_list[0].data
        print("\nDados da Imagem:")
        print(type(image_data))  # Exibir o tipo de image_data
        if image_data is not None:
            print(image_data.shape)  # Exibir a forma dos dados da imagem
        else:
            print("Os dados da imagem não estão presentes ou são None.")
else:
    print(f"O arquivo '{file_name}' não foi encontrado em '{fits_path}'.")