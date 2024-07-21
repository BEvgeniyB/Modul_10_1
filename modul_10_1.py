from time import sleep
from datetime import datetime
from threading import Thread

def write_file(file_name):
    with open(file_name, mode='w', encoding='utf8'):
        pass
    def wite_words(word_count, file_name):

        with open(file_name, mode='a', encoding='utf8') as fyle_my:

            for i in range(1,word_count+1):
                fyle_my.write(f'Это просто слово № {i} \n')
                sleep(0.1)

        print(f"Завершилась запись в файл {file_name}")
    return wite_words

fyle_1 = write_file('example1.txt')
fyle_2 = write_file('example2.txt')
fyle_3 = write_file('example3.txt')
fyle_4 = write_file('example4.txt')
start_ = datetime.now()
fyle_1(10, 'example1.txt')
fyle_2(30, 'example2.txt')
fyle_3(200, 'example3.txt')
fyle_4(100, 'example4.txt')
finisch_ = datetime.now()
print(finisch_-start_)

fyle_5 = write_file('example5.txt')
fyle_6 = write_file('example6.txt')
fyle_7 = write_file('example7.txt')
fyle_8 = write_file('example8.txt')

thr_5 = Thread(target=fyle_5,args=[10, 'example5.txt'])
thr_6 = Thread(target=fyle_6,args=[30, 'example6.txt'])
thr_7 = Thread(target=fyle_7,args=[200, 'example7.txt'])
thr_8 = Thread(target=fyle_8,args=[100, 'example8.txt'])
start_ = datetime.now()
thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()
thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()

finisch_ = datetime.now()
print(finisch_-start_)