import os
print ("Welcome to Terminus plugin setup")
print ("Please Install Homebrew")
os.system("open https://brew.sh/")
print ("I have installed Home Brew:")
print ("1.I Agree to install the following plugins:")
print ("a.Colorama For Python")
print ("b.Pynput For Python")
print ("Agree to Installments [y/Y]")
binstall=input()
if  binstall =="y" or "Y":
    os.system("pip3 install colorama")
    os.system("pip3 install pynput")
    os.system("brew update")
    os.system("brew cask install hyper")