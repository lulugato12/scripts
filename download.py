import gdown

# genes cerebro
url = 'https://drive.google.com/uc?id=1jj1L8NaaCQzm7s6sc8gXh2oP8vbpnK13'
output = 'cerebro_data.gz'
gdown.download(url, output, quiet=False)

# ids
url = 'https://drive.google.com/uc?id=16rQs0vCapz3S9tjBgmJjWRBIBTEfiNRi'
output = 'mart_export.txt'
gdown.download(url, output, quiet=False)

# protein coding
url = 'https://drive.google.com/uc?id=1XBkZ98oQKmZ7YRKExvm48Z4IU3YtROK1'
output = 'protein_coding.txt'
gdown.download(url, output, quiet=False)

# motif data
url = 'https://drive.google.com/1DXtTuTIIL5uT_FZkJtLrzC-uiTyvSwEA'
output = 'ToyMotifData.txt'
gdown.download(url, output, quiet=False)
