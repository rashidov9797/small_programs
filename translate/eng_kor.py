#영어 분서를 한글로 자동번역하는 프로그램이다


# pip install googletrans==4.0.0-rc1
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"translate\\eng_file.txt"
# 파일일 읽어 올 경로를 지정

write_read_file =  r"translate\\kor_file.txt"
# 파일 번역해서 새 파일로 저장 



with open(read_file_path, 'r') as f:
    readLines = f.readlines()
# 파일에서  줄별로 읽어 list형으로 변경 

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_read_file, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')
# list형으로 저장된 readLines에서 한 줄씩 한글로 변환하여 풀력 

    