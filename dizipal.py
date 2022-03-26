import requests
from bs4 import BeautifulSoup
 


first = input("Nerden: ")
second = input("Nereye: ")
for i in range(int(first),int(second)):
    try:
        r = requests.get(f'https://dizipal{i}.com')
        source = BeautifulSoup(r.content,"html.parser")
        if r.status_code == 200:
            
            if source.title.text == "DiziPAL – yabancı dizi, film ve anime izle":
                print(f' aktif: https://dizipal{i}.com')
            else:  
                print("No data")   
    except:
        pass


