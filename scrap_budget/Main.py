import tkinter as tk, blockData
from tkinter import filedialog
root = tk.Tk()

totalLabel = tk.Label(root, 
    text="No blueprint",  
    height=3,width=30,font=("Arial", 16, "bold"), )
    
miniInfo = tk.Label(root, 
    text="-",    
    font=("Arial", 10, "bold"), )

infoLabel = tk.Label(root, 
    text="No blueprint",                                  
    font=("Arial", 16, "bold"),)

def setup():
    global data
    data = {
        "totalText": "No blueprint",
        "infoText": "No blueprint",
        "miniText": "-",
        "data": [blockData.blocks,blockData.inetractive],
        "update": []
    }

    checkBtn = tk.Button(root, 
    text="Open Blueprint",                                   
    font=("Arial", 16, "bold"),
    command=checkFile)


    data["update"] = [totalLabel,infoLabel,miniInfo]
    checkBtn.pack()
    miniInfo.pack()
    totalLabel.pack()
    infoLabel.pack()

def updateAll():
    totalLabel["text"] = data["totalText"]
    miniInfo["text"] = data["miniText"]
    infoLabel["text"] = data["infoText"]

def checkFile():
    fileName = tk.filedialog.askopenfilename()
    text = open(fileName,"r").read()
    data["miniText"] = fileName
    items = {}
    total = 0

    data["infoText"] = "Items:\n"

    for category in data["data"]:
        for e in category:
            this = category[e]
            count = text.count(e)
            print(e,"found: ",count, "price:",count*this[1])
            if count > 0:
                price = count*this[1]
                total += price
                items.update({this[0]: [count,price]})
                data["infoText"] += f"{this[0]}[{count}db] : {price}$\n"
    
    data["totalText"] = "Total cost: "+f"{total}$"
    updateAll()





if __name__ == "__main__":
    setup()

root.mainloop()