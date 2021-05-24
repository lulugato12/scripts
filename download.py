import gdown

# genes cerebro
url = 'https://drive.google.com/uc?id=1RT99lD9FQ7fl5tKm32eKdy9N1gGnolJ_'
output = 'breast_data.gz'
gdown.download(url, output, quiet=False)

# ids
url = 'https://drive.google.com/uc?id=1PD4uqSYW5bXoR9tHJjkSv30RgrMlb_9E'
output = 'mart_export.txt'
gdown.download(url, output, quiet=False)

# motif data
url = 'https://drive.google.com/uc?id=1DXtTuTIIL5uT_FZkJtLrzC-uiTyvSwEA'
output = 'ToyMotifData.txt'
gdown.download(url, output, quiet=False)
