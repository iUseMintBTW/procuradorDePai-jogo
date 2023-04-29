import time
import sys, subprocess
import requests

subprocess.run('clear', shell=True)

print("\n\t =======================================")
print("\t|                                       |")
print("\t| Seja bem viade ao encontrador de pai! |")
print("\t|                                       |")
print("\t =======================================")

pai = input("\n\n\nMe diga o nome do teu pai: ")
time.sleep(1)
print("\n.")
time.sleep(1)
print(".")
time.sleep(2)
print('.')
time.sleep(3)

subprocess.run('clear', shell=True)
print("\n\n\n\n\t[                      ]")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[=                     ]")
time.sleep(3)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[==                    ]")
time.sleep(1)
subprocess.run('clear', shell=True)




print("\n\n\n\n\t[===                   ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(5)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[====                  ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(8)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[====                  ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[=====                 ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[======                ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[=======               ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[========              ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[=========             ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(13)
subprocess.run('clear', shell=True)



print("\n\n\n\n\t[==========            ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[===========           ]")
print("\t\tIsso pode levar algum tempo. Aguente firme! XD")
time.sleep(1)
subprocess.run('clear', shell=True)
print("\n\n\n\n\t[============          ]")
print("\t\tQuase lá...")
time.sleep(21)
subprocess.run('clear', shell=True)


print("\n\n\n\n\t[======================]")
print("\t\tProcuração concluida! ^^\n\n")
time.sleep(3)




try:
  pai =  requests.get("encontrameupai.com")
  pai.raise_for_status()
  subprocess.run('clear', shell=True)
  print("\n\n\n\n\t[======================]")
  print("Seu pai:", pai.text)
  exit()
except requests.exceptions.RequestException:
	subprocess.run('clear', shell=True)
	print("\n\n\n\n\t[======================]\n\n")
	print("\tDesculpe, ", pai.text, " não foi encontrado ;-;")
	exit(1)


