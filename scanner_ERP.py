#!/usr/bin/python3

#Menu driven network scanning tool:
import nmap
import sys

def main_menu():
	
	print("1.Scan single host") #nmap ip ex: nmap 192.168.1.1
	print("2.scan range") # nmap 192.168.1.1-254
	print("3.Scan network")# nmap 192.168.1.0/24
	print("4.Agressive scan") # -T4 time   #-A
	print("5.Scan ARP packet") # nmap ip/mask -PR 
	# ex: nmap 192.168.1.0/24 -PR
	print("6.Scan All port only")# -Pn
	print("7.Scan in verbose mod")# nmap -v
	print("8.Exit")
while True:
	main_menu()
	ch =  int(input("Enter choice: "))
	
	nm = nmap.PortScanner() #Create object of nmap port scannet class
	
	#ip = input("Enter the IP : ")
	
	
	if ch == 1:
		#Scan single host
		ip = input("Enter the IP : ")
		print("Wait.......................")
	
	
		try:
			scan = nm.scan(hosts=ip,ports="1-100",arguments="-sS -O -v -Pn")
			
			for host in scan["scan"][ip]['tcp'].items():
				print("Tcp Port :",host[0])
				print("State :",host[1]['state'])
				print("Reason :",host[1]['reason'])
				print("Name :",host[1]['name'])
		except:
			print("Use root priviliege")
	elif ch == 2:
		#scan range
		ip = input("Enter the IP : ")
		print("Wait.......................")
		
		try:
			scan = nm.scan(hosts=ip,arguments="-sS -O -Pn")
			#print(scan)
			for host in scan["scan"]:
				print("Ip range :",host)
		except:
			print("Use root priviliege")
		#print(scan)
		
	elif ch == 3:
		#Scan network
		ip = input("Enter the IP : ")
		print("Wait.......................")
	
		try:
			scan = nm.scan(hosts=ip,arguments="-sS -O -Pn")
			for  i in scan["scan"][ip]["osmatch"]:
				print("Name :",i['name'])
				for j in i['osclass']:
					print(f"Os-type :",{j['type']})
					print(f"Vendor :",{j['vendor']})
		except:
			print("Use root priviliege")
		#print(scan)
		
	elif ch == 4:
		#Agressive scan
		ip = input("Enter the IP : ")
			
		print("Wait.......................")
		try:
			scan = nm.scan(hosts=ip,arguments = "-sS -O -Pn -T4")
			for i in scan["scan"][ip]['osmatch']:
				print(f"Name : {i['name']}")
				print(f"Accuracy : {i['accuracy']}")
				for j in i['osclass']:
					print(f"Os-type :,{j['type']}")
					print(f"Vendor :,{j['vendor']}")
		
		except:
			print("Use root priviliege")
		print(scan)
		
	
	elif ch == 5:
		ip = input("Enter the IP : ")
			
		print("Wait.......................")
		try:
			scan = nm.scan(hosts=ip,arguments = "-sS -O -PR")
			for i in scan["scan"][ip]['osmatch']:
				print(f"Name : {i['name']}")
				print(f"Accuracy : {i['accuracy']}")
		except:
			print("Use root privilige")

		#print(scan)
		
	elif ch == 6:
		ip = input("Enter the IP : ")
			
		print("Wait.......................")
		try:
			scan = nm.scan(hosts=ip,ports="1-4",arguments="-sS -O -Pn")
			
			for host in scan["scan"][ip]['tcp'].items():
				print("Tcp Port :",host[0])
				print("State :",host[1]['state'])
				print("Reason :",host[1]['reason'])
				print("Name :",host[1]['name'])
			
		except:
			print("Use root privilige")
		#print(scan)
	elif ch == 7:
	
		ip = input("Enter the IP : ")
			
		print("Wait.......................")
		try:
			scan = nm.scan(hosts = ip,arguments = "-sS -O -Pn -v")
			for i in scan["scan"][ip]["osmatch"]:
				print(f"Name : {i['name']}")
				print(f"Accuracy : {i['accuracy']}")
				for j in i["osclass"]:
					print(f"Os-type : {j['type']}")		
		except:
			print("Use root priviliege")
		
		
	elif ch == 8:
		break;
	else:
		print("Wrong Choice")
	

