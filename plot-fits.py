import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os

# Caminho para o diretório onde está o arquivo FITS
fits_path = os.path.join('/fits')

# Nome do arquivo FITS que você deseja acessar
image_file = 'bias_02.fits'

# Construindo o caminho completo para o arquivo FITS
file_path = os.path.join(fits_path, image_file)

# Abrir o arquivo FITS e carregar os dados da imagem
image_data = fits.getdata(file_path)

# Verificar o tipo e a forma dos dados da imagem
print(type(image_data))  # Exibir o tipo de image_data
print(image_data.shape)  # Exibir a forma dos dados da imagem

# Plotar a imagem e o histograma
plt.figure(figsize=(12, 6))  # Tamanho da figura

# Plotar a imagem
plt.subplot(1, 2, 1)  # Dividir a figura em 1 linha e 2 colunas, e usar o primeiro subplot
plt.imshow(image_data, cmap='inferno', origin='lower')  # Adiciona origin='lower' para o alinhamento correto
plt.colorbar()
plt.title('Imagem FITS')

# Plotar o histograma dos dados da imagem
plt.subplot(1, 2, 2)  # Usar o segundo subplot
plt.hist(image_data.flatten(), bins=20, color='red')
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