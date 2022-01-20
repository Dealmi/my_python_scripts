#Selecting a number of lunar coins
coinsNum=str (input("Enter the number of lunar coins you want to have (1-999999) or just press Enter for max number") or "9999999")
#name of a RoR2 xml file with user data
fileName="aba67c4c-371f-4da6-a76f-0874b3c6e4a2.xml"
#setting a number of lunar coins into xml file
import xml.etree.ElementTree as ET
tree = ET.parse(fileName)
root = tree.getroot()

for coins in root.iter('coins'):
    coins.text = coinsNum
tree.write(fileName)
  



