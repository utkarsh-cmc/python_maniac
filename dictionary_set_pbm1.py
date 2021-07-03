myDict = {
    "pankha":"fan",
    "relgadi":"train",
    "bansuri":"flute"
}
print("Welcome to hindi to english dictionary\n Your options are \n",myDict.keys())
a=input("Enter the Hindi word\n")
print("The meaning of\t" +a+ "\tis "+myDict.get(a))