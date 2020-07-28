#// Zip Cracker Cracking Tutorial

import zipfile


count = 1
passlist = input("Please type the file name of your password list: ")
zippy = input("Please enter the file name for your password protected Zip file: ")
with open(passlist, 'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(zippy, 'r')as zf:
                zf.extractall(pwd=password)
                
                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~%s\n ~%s\n ~%s\n**********************'''
                    % (pssword.decode('utf8'), data, data_size))
                break


        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass


    
