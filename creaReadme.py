#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printHead():
	print(bcolors.WARNING + bcolors.BOLD +'''
	
         _           _____ ___________                  _                
        (_)         /  __ \_   _|  ___|                | |               
   _ __  _  ___ ___ | /  \/ | | | |_ _ __ ___  __ _  __| |_ __ ___   ___ 
  | '_ \| |/ __/ _ \| |     | | |  _| '__/ _ \/ _` |/ _` | '_ ` _ \ / _ \\
  | |_) | | (_| (_) | \__/\ | | | | | | |  __/ (_| | (_| | | | | | |  __/
  | .__/|_|\___\___/ \____/ \_/ \_| |_|  \___|\__,_|\__,_|_| |_| |_|\___|
  | |                                                                    
  |_|                                                                @manulqwerty


''' + bcolors.ENDC )

def templ(challenge='',points='',category='',question='',hint=''):
    content = '# ' + challenge
    content += '\n**Points: ' + points + '**'
    content += '\n\n## ' + category
    content += '\n\n## Question\n'
    content += '>'+question
    content += '\n\n### Hint'
    content += '\n>' + hint
    content += '\n\n## Solution\n\n'
    content += '\n\n### Flag\n'
    return content

	
def main():
	
	printHead()
	parser = argparse.ArgumentParser(description='https://ironhackers.es - picoCTF WriteUp Template')
	args = parser.parse_args()
	
	challenge = input(bcolors.OKBLUE + "Challenge Name: " + bcolors.ENDC )
	points = input(bcolors.OKBLUE + "Points: " + bcolors.ENDC )
	category = input(bcolors.OKBLUE + "Category: " + bcolors.ENDC )
	question = input(bcolors.OKBLUE + "Question: " + bcolors.ENDC )
	hint = input(bcolors.OKBLUE + "Hint: " + bcolors.ENDC )
	
	f = open('README.md',"w")
	f.write(templ(challenge,points,category,question,hint))
	f.close()
	
	print(bcolors.OKGREEN + "\n[+] Template exported to: " + os.getcwd() + "/" + 'readme.md\n' + bcolors.ENDC )

	
if __name__ == '__main__':
    main()
