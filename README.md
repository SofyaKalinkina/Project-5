# Очистка номеров телефонов в файле .xlsx

## Описание
Этот скрипт предназначен для очистки номеров телефонов, хранящихся в файле .xlsx, от ненужных символов. Он удаляет все символы, кроме цифр, из номеров телефонов, таких как: скобки, тире, пробелы, и преобразует их к стандартному формату без лишних символов. Результат очистки сохраняется в новый файл с расширением .xlsx.

## Установка и начало работы
1. Для начала работы у вас должны быть установлены следующие пакеты в сервисе replit:
- `gdown`: для загрузки файла из Google Drive
- `pandas`: для обработки данных в формате .xlsx
- `openpyxl3.0.10`: для чтения и записи данных о номерах телефонов в файле .xlsx.

Инструкция по установке:
- Создайте файл requirements.txt: Создайте файл и перечислите в нем все пакеты, которые вы хотите установить, по одному на каждой строке. 

- Запустите установку пакетов: После создания файла requirements.txt Replit автоматически определит его и запустит установку всех перечисленных пакетов при запуске вашего кода. 

- Перезапустите среду выполнения: Если вы добавили новые пакеты в requirements.txt после начала работы, перезапустите среду выполнения Replit, чтобы убедиться, что новые пакеты будут установлены перед запуском вашего кода.

2. Скопируйте код для выполнения процесса очистки номеров телефонов из файла и сохранения результата:

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

3. Запустите код и получите результат, при необходимости замените ссылку на ваш файл .xlsx

4. Ссылка на файл, используемый в проекте, доступна [здесь](https://docs.google.com/spreadsheets/d/1kS6TIiR8bNG-4jtAa_1VCH3Xtsvxyr9P/edit?usp=sharing&ouid=113706080460613369715&rtpof=true&sd=true)


