import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.utils.data import download_file

# Download da imagem FITS
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)

# Abrir o arquivo FITS e carregar os dados da imagem
image_data = fits.getdata(image_file)

# Verificar o tipo e a forma dos dados da imagem
print(type(image_data))  # Exibir o tipo de image_data
print(image_data.shape)  # Exibir a forma dos dados da imagem

# Plotar a imagem e o histograma
plt.figure(figsize=(12, 6))  # Tamanho da figura

# Plotar a imagem
plt.subplot(1, 2, 1)  # Dividir a figura em 1 linha e 2 colunas, e usar o primeiro subplot
plt.imshow(image_data, cmap='gray', origin='lower')  # Adiciona origin='lower' para o alinhamento correto
plt.colorbar()
plt.title('Imagem FITS')

# Plotar o histograma dos dados da imagem
plt.subplot(1, 2, 2)  # Usar o segundo subplot
plt.hist(image_data.flatten(), bins='auto', color='gray')
plt.title('Histograma dos Dados da Imagem')
plt.xlabel('Valor do Pixel')
plt.ylabel('Frequência')

# Ajustar layout para que não haja sobreposição
plt.tight_layout()
plt.show()

# Exibir estatísticas básicas da imagem
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

# Basic image math: image stacking
base_url = 'http://data.astropy.org/tutorials/FITS-images/M13_blue_{0:04d}.fits'
image_list = [download_file(base_url.format(n), cache=True) for n in range(1, 6)]

# Carregar os dados das imagens
image_concat = [fits.getdata(image) for image in image_list]

# Somar as imagens
final_image = np.sum(image_concat, axis=0)

# Plotar o histograma da imagem final
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
min_value = np.min(image_data)
max_value = np.max(image_data)
plt.hist(final_image.flatten(), bins='auto', color='gray')
plt.title('Histograma da Imagem Final')
plt.xlabel('Valor do Pixel')
plt.ylabel('Frequência')

# Plotar a imagem final
plt.subplot(1, 2, 2)
plt.imshow(final_image, cmap='gray', vmin=2E3, vmax=3E3)
plt.colorbar()
plt.title('Imagem Final Combinada')

# Ajustar layout para que não haja sobreposição
plt.tight_layout()
plt.show()

#Writing image data to a FITS file

outfile = 'stacked_M13_blue.fits'

hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, overwrite=True)