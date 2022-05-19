import os
user = input("What color would you like? ")
if user == "list":
	print("""yellow/blue -- Yellow text on blue background | gray/green -- gray text on green background """)


elif user == "yellow/blue":
	os.system("python3 script2.py")


elif user == "gray/green":
	os.system("python3 script3.py")

elif user == "overwrite":
	os.system("python3 script.py")

else:
	print("What?")
