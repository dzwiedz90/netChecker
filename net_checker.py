import os

import time

 

from pythonping import ping

 

 

 

def net_checker(hostAddress):

                response = ping(hostAddress, size=1, count=1)

                response = str(response)

                if response[0:5] == 'Reply' and response[-2:] == 'ms':

                               print(hostAddress,"- online.")

                else:

                               print(hostAddress,"- ofline.   !!! !!!")

 

                              

while True:

                os.system('cls')

                print('-------------------------')

                print('| Net Checker by Ókasz  |')

                print('-------------------------\n')

                print('serwer  - ', end = '')

                net_checker('192.168.1.1')

                time.sleep(0.2)

                print('serwer1     - ', end = '')

                net_checker('192.168.1.1')

                time.sleep(0.2)

                print('serwer3     - ', end = '')

                net_checker('192.168.1.1')

                time.sleep(0.2)

                print('switch     - ', end = '')

                net_checker('192.168.1.1')

                time.sleep(0.2)

                time.sleep(60)
