from astropy.io import fits
import os

# Caminho para o diretório contendo o arquivo FITS
fits_dir = os.path.join('.', 'saturn/fits')

# Nome do arquivo FITS
fits_file = 'flat_01_v.fits'
fits_path = os.path.join(fits_dir, fits_file)

# Abrir o arquivo FITS para atualizar
with fits.open(fits_path, mode='update') as hdu_list:
    # Exibir informações sobre os HDUs (Header Data Units)
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
    print(image_data.shape)  # Exibir a forma dos dados da imagem

    # Modificar o cabeçalho
    header['IMAGETYP'] = 'flat'
    # Você pode descomentar e atualizar as seguintes linhas conforme necessário:
    # header['OBJECT'] = "EUSGURI"
    # header['RA'] = ...
    # header['DEC'] = ...
    # header['OBJCTRA'] = ...
    # header['OBJCTDEC'] = ...
    # header['RADECSRC'] = "site com informacao do objeto ra e dec"
    #header['EXPTIME'] = 15
    #header['FILTER'] = 'v'
    # header['NAXIS1'] = 775

# O arquivo FITS foi atualizado no mesmo local
print(f"\nArquivo FITS atualizado: {fits_path}")
