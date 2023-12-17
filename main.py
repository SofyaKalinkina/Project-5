import gdown
import pandas as pd

# Загрузка файла .xlsx из Google Drive
url = 'https://docs.google.com/spreadsheets/d/1kS6TIiR8bNG-4jtAa_1VCH3Xtsvxyr9P/edit?usp=sharing&ouid=113706080460613369715&rtpof=true&sd=true'
output = 'phone_numbers.xlsx'
gdown.download(url, output, quiet=False)

# Чтение данных из файла .xlsx
df = pd.read_excel('phone_numbers.xlsx')

# Функция для очистки номеров телефонов
def clean_phone(phone):
    return ''.join(filter(str.isdigit, str(phone)))

# Очистка номеров телефонов от ненужных символов
df['phone_number'] = df['phone_number'].apply(clean_phone)

# Сохранение очищенных данных в новый файл .xlsx
cleaned_file = 'cleaned_phones.xlsx'
df.to_excel(cleaned_file, index=False)

import pandas as pd

# Загрузка файла Excel в DataFrame
df = pd.read_excel('cleaned_phones.xlsx')

# Вывод всех строк DataFrame
print(df)
