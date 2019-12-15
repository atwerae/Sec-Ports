import random
import sys
from os import system

#List of lists of ports and protocols for SEC+ exam
numbers= {'TCP 22':('ssh','scp','sftp'),'TCP AND UDP 53':('DNS'),
'TCP 20 and 21':('FTP'),'UDP 69':('TFTP'),'443':('FTPS,HTTPS,SSL VPN443'),'TCP 25':('SMTP'),
'TCP 110':('POP3'), 'TCP 143':('Imap'),'TCP 23':('TelNet'),'TCP 49':('TACACS+'),'UDP 49':('TACACS'),
'UDP 1701':('L2TP'),'TCP and UDP 1723':('PPTP'),'TCP and UDP 3389':('RDP'),
'UDP 67,68':('DHCP'),'TCP 80':('HTTP'),'TCP AND UDP 88':('Kerberos'), 'TCP 119':('NNTP'),'UDP 161':('SNMP'),
'UDP 514':('Syslog'),'TCP 443':('HTTPS/SSL VPN/FTPS'),'UDP 67 and 68':('DHCP'),'UDP 500':('ISAKMP VPN'),'TCP AND UDP 162':('SNMP Trap')
        }

#List of ports for random choice
random_gen= ('TCP 20 and 21','TCP 22','UDP 69','TCP 443','TCP 25','TCP 110','TCP 143','TCP 23','TCP 49','UDP 49','UDP 500'
,'UDP 1701','TCP and UDP 1723','TCP and UDP 3389','TCP AND UDP 53','UDP 67 and 68','TCP 80','TCP AND UDP 88','TCP 119','UDP 161',
'TCP AND UDP 162','UDP 514'
            )
#creates the random port for question            
#rand_choice= random.choice(random_gen)


def Sec_port_game():
    correct = 0
    incorrect = 0
    system('cls')
    print("""This will ask you for port number and weather or not is uses TCP or UDP for communication. Answer must be formatted like 'TCP 443'
if the uses both the answer must be formatted 'TCP and UDP' followed by the port number. If it uses more than one port it must be formatted like 
67 and 68. The lowest number will always come first.""")


    while (1==1):
        #Keeps track of total answred
        total = incorrect + correct
        #prints the amount of answers that you have correct, incorrect and total
        print(f"correct {correct} incorrect {incorrect}: {total} total answered out of 20 questions.")
        #creates the random port for question            
        rand_choice= random.choice(random_gen)
        #Total of 20 random ports will ne assesed. Gives the total correct, incorrect and % coorect.
        if(total == 20):
            print(f"Total correct is {correct} total incorrectis {incorrect}")
            print("Precent correct is")
            print(correct/20 * 100)
            #Asks the player if they would like to play again
            play_again=input('''Would you like to play again? "yes" or "no" any other response to exit the program
:''')
            #if player wants to play agin sets the correct and incorrect to 0 to start exit if and start over.
            if(play_again.upper() == 'YES') or (play_again.upper() == 'Y'):
                correct =0
                incorrect = 0
            #If the player does not wish to play again thanks them for playing and break out of the while loop wo exit the game.
            else:
                print("""Thank you for playing""")
                break
        #Takes the answer for the random port
        answer = input(f"""Port number for {numbers[rand_choice]}?
:""")

        #Checks the answer to see if it's correct
        if (answer.upper() == rand_choice.upper()):
            print('CORRECT!')
            correct += 1
            
        else:
            print(f"""Nice try but the correct port is {rand_choice}""")
            incorrect += 1

#starts the game that does not require any vargs
Sec_port_game()