import requests, json, os

def app_label() :
    print('+-------------------------------+')
    print('|     Kurs Bank di Indonesia    |')
    print('|          > Hams73r <          |')
    print('|           v 1.0.0.0           |')
    print('+-------------------------------+')

def app_clear() :
    if os.name == 'nt' : os.system('cls') # Untuk Windows
    else : os.system('clear') # Untuk Linux/OS X

bank_name = ['BCA','BRI','BJB','BNI','BRI','BTN','BUKOPIN','CIMB','COMMONWEALTH','DANAMON','HSBC','JTRUST','MANDIRI','MAYAPADA','MAYBANK','MEGA','MUAMALAT','OCBC','PANIN','PERMATA','SINARMAS','UOB','WOORISAUDARA']
bank_code = ['bca','bri','bjb','bni','bri','btn','bukopin','cimb','commonwealth','danamon','hsbc','jtrust','mandiri','mayapada','maybank','mega','muamalat','ocbc','panin','permata','sinarmas','uob','woorisaudara']
bank_url = 'http://kurs.web.id/api/v1/'

in_menu = 1
while in_menu == 1 :
    app_clear()
    app_label()
    print('|          Pilih Bank           |')
    print('+-------------------------------+')
    for i in range(len(bank_name)) :
        print('[ %d ] %s' % (i+1, bank_name[i]))

    print('\n[ 0 ] Keluar')
    print('+-------------------------------+')

    pilih_bank = str(input('[ > ] '))
    if pilih_bank.isnumeric() : pilih_bank = int(pilih_bank) - 1
    else : pilih_bank = -1
    
    app_clear()
    app_label()
    if pilih_bank >= 0 :
        val_bank = (json.loads((requests.get(bank_url + bank_code[pilih_bank])).text))
        if val_bank['status'] == 'success' :
            print('Bank           : ' + val_bank['bank'])
            print('Mata Uang      : ' + val_bank['matauang'])
            print('Harga Jual     : ' + val_bank['jual'])
            print('Harga Beli     : ' + val_bank['beli'])
            print('\n[ 0 ] Keluar')
            print('+-------------------------------+')
            input('[ > ] ')

    else :
        print('[] Terimakasih dan Sampai Jumpa []')
        in_menu = 0