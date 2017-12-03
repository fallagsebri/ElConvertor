import os
os.system('cls' if os.name == 'nt' else 'clear')
def menu():
 print '''
 El Convertor 
 Created BY Saber Sebri
 '''
def binary(zeb):
   if zeb > 1:
       binary (zeb//2)
   print zeb % 2
menu()
print "[1] Convert string to get Ascii Code"
print "[2] Convert String To Binary"
print "[3] Convert integer To Binary"
print "[4] Convert Binary To Dec"
ch1=raw_input("\n[>] ")
if ch1 == '2':
 zebi =raw_input("give me a string\n[>]")
 print ' '.join(format(ord(x), 'b') for x in zebi)
if ch1 == '1':
 rania =raw_input("give me a string\n[>]")
 for char in rania:
  print(ord(char))
if ch1 == '3':
  sorm = int(input("the integer to convert it to bin :"))
  binary(sorm)
if ch1 == '4':
 binary = raw_input("the integer to convert it to dec :")
 decimal = 0
 for digit in binary:
    decimal = decimal*2 + int(digit)
 print 'result is ',decimal,"and this is the ascii code of ",chr(decimal)
print "[1] repeat"
print "[2] exit"
ch2=raw_input("\n[>] ")
if ch1 == '1':
 os.system('elconvertor.py' if os.name == 'nt' else 'python elconvertor.py')

