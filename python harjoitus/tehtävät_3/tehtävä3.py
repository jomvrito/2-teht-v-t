pituus = int (input("anna kuhan pituus senttimetreinä:"))
if pituus < 37:
    puuttuu = 37 - pituus
    print("laske kuha takasin järveen.")
    print("pyyntimitasta puuttuu", puuttuu,"cm")
else:
    print ("kuha on riittävän pitkä")


