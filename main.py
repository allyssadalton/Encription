password="1A2B3C4D"
global message
message=input("Enter your message: ").lower()

def code():
  global message
  message=message.replace(" ", '"')
  message=message.replace("a","@")
  message=message.replace("b","%")
  message=message.replace("c","¥")
  message=message.replace("d","&")
  message=message.replace("e",">")
  message=message.replace("f","<")
  message=message.replace("g","#")
  message=message.replace("h","/")
  message=message.replace("i","*")
  message=message.replace("j","…")
  message=message.replace("k",":")
  message=message.replace("l","=")
  message=message.replace("m","+")
  message=message.replace("n","-")
  message=message.replace("o","£")
  message=message.replace("p","~")
  message=message.replace("q","§")
  message=message.replace("r","^")
  message=message.replace("s","$")
  message=message.replace("t","€")
  message=message.replace("u","|")
  message=message.replace("v",".")
  message=message.replace("w","_")
  message=message.replace("x","[")
  message=message.replace("y","]")
  message=message.replace("z","}") 
  message=message.replace("0","a")
  message=message.replace("1","z")
  message=message.replace("2","y")
  message=message.replace("3","w")
  message=message.replace("4","c")
  message=message.replace("5","x")
  message=message.replace("6","f")
  message=message.replace("7","g")
  message=message.replace("8","m")
  message=message.replace("9","n")
  print(message)
  print(" ")

def decode():
  global message
  message=message.replace("a","0")
  message=message.replace("z","1")
  message=message.replace("y","2")
  message=message.replace("w","3")
  message=message.replace("c","4")
  message=message.replace("x","5")
  message=message.replace("f","6")
  message=message.replace("g","7")
  message=message.replace("m","8")
  message=message.replace("n","9")
  message=message.replace('"',' ')
  message=message.replace("@","a")
  message=message.replace("%","b")
  message=message.replace("¥","c")
  message=message.replace("&","d")
  message=message.replace(">","e")
  message=message.replace("<","f")
  message=message.replace("#","g")
  message=message.replace("/","h")
  message=message.replace("*","i")
  message=message.replace("…","j")
  message=message.replace(":","k")
  message=message.replace("=","l")
  message=message.replace("+","m")
  message=message.replace("-","n")
  message=message.replace("£","o")
  message=message.replace("~","p")
  message=message.replace("§","q")
  message=message.replace("^","r")
  message=message.replace("$","s")
  message=message.replace("€","t")
  message=message.replace("|","u")
  message=message.replace(".","v")
  message=message.replace("_","w")
  message=message.replace("[","x")
  message=message.replace("]","y")
  message=message.replace("}","z")  
  print(message)
  print(" ")

#asks if you want fo decode the message
x=input("Would you like to decode the message? ").lower()

#asks for password until you get it correct
while True:
  passguess=input("Enter the password: ")
  if passguess==password:
    #looks for yes in input
    if x.find("y")==0:
      print("The decoded message:")
      decode()
      #prints if y isn't in input
    else:
      print("The encripted message:")
      code()
    break
  else:
    print("The is the wrong password.")
    
