from pyscript import display, document

def areyouin(e):
    document.getElementById("in").innerHTML = "" #resets the output when we enter a new one
    fname = document.getElementById("name").value #gets value of first name
    lname = document.getElementById("lname").value #gets value of last name
    mathpeoplename = ["Cheree Mendoza", "Anya Basuil", "Edrian Correa", "Emmanuel Correa", "Francesca Daquigan", "Francis Fernandez", "Gabrielle De Jesus", "Georgina Gamponia", "Hannah Galapon", "Jarvis Joven", "Jibril Abdul", "Julienne Musni", "Khadija Lucman", "Kian Ang", "Krishna Pascua", "Lorissa Paragas", "Lucas Ladion", "Maria Bamba ", "Orange Mendoza", "Rafael Castro", "Rayne Maniago", "Rohan Tabasan", "Tyler Sales", "Yanis Concepcion", "Zander Mirza"] #list of math club members

    fullnamenow = str(fname + " " + lname) #add the value of the two input boxes together and turn them to string
    checkplspls = fullnamenow in mathpeoplename #checks if the name the user entered is inside the list
    lolnotin = "Sorry" + " " + fullnamenow + "," + " " + "you have failed and you will not be joining Math Club for SY 26-27."
    hoorayin = "Congratulations" + " " + fullnamenow + "!" + " " + "you have passed and you will be joining Math Club for SY 26-27." #creates the result message

    display({
        False: lolnotin,
        True: hoorayin} #because it returns a boolean if i only do checkplspls,, we make both of the possible results of a boolean equal to the result messages we created earlier
          [checkplspls], target="in")
    
    