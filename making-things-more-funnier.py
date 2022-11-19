import os
def arrowPointVisualization(list:[str]) -> list:
	for item in list:
		print(" ->", item)


print("Hello there!")
print("My name is Mancier and this is my second code in python")
print("Lets do some math basics to test this thing")
print("5 + 3 = ", (5+3))
print("5 x 3 = ", 5*3)
print("5 / 3 = ", 5/3)
print("5 // 3 = ", 5//3)
print("=====================================================")
print("Lets do something more interesting")
print("Santa Claus list")
gifts=["skate", "bicicle", "video game", "RTX 4090 GDDR6 12GB MSI Limited"]
arrowPointVisualization(gifts)
print("everything is expensive, lets reduce this list")
gifts.pop(2)
arrowPointVisualization(gifts)
print("lets add something sweet in this list")
gifts.append("chocolate")
arrowPointVisualization(gifts)
print("I dont wanna a skate anymore")
gifts.remove("skate")
arrowPointVisualization(gifts)
print("This is my final list, lets fix this")
finalListOfGifts = (gifts)
arrowPointVisualization(finalListOfGifts)
print("=====================================================")
print("My familly wants gifts to")
famillyGifts = {
	"mom": [
		"Traxart Revolt Roller",
		"Day-off in spa",
		"Dress"
	],
	"dad": [
		"BMW E30",
		"Turbo Charger",
		"Rotiform Whells"
	],
	"sister": [
		"Nike Air Jordan",
		"Make-up kit",
		"Asus Notebook space edition"
	]
}
print("Lets see my mom gift list")
arrowPointVisualization(famillyGifts["mom"])
print("Lets see my dad gift list")
arrowPointVisualization(famillyGifts["dad"])
print("Lets see my sister gift list")
arrowPointVisualization(famillyGifts["sister"])
