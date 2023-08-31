import xml.etree.ElementTree as ET

#The XML file has to be in current directory or user has to provide full path of this file
try:
    with open("export_full.xml", "r", encoding='utf-8') as file:
        xml_data = file.read()

except FileNotFoundError:
    file_path = input("XML file was not found, please provide the full path of this file\n")
    with open(file_path, "r", encoding='utf-8') as file:
        xml_data = file.read()


#Option number 1, how much of products are in store
def first_func(products):
    print(f"1. Počet produktů: {len(products)}")

#Option number 2, print names of those products
def second_func(products):
    print("2. Názvy produktů:")
    for product in products:
        print(product.get("name"))


#Option number 3, print spare parts for each products, if spare parts exists.
def third_func(products):
    print("3. Náhradní díly k jednotlivým produktům:")
    for product in products:

        #Loop throught all products, and look for category with ID of 1(ID 1 means spare parts(náhradní díly). 
        spare_parts = product.findall("./parts/part[@categoryId='1']/item")

        #If the spare parts for current products exists, will print them, else will continue to next product
        if spare_parts:
            
            print(f"\n{product.get('name')}\n")

            for part in spare_parts:
                print(f"\t{part.get('name')}")
            
            print()


function_dictionary = {
    1 : first_func,
    2 : second_func,
    3: third_func
} 

#Validate user input
try:

    choice = int(input("Enter your choice.\n\t1 for printing the number of products\n\t2 for printing product names\n\t3 for printing spare parts for products\n"))
    if choice not in function_dictionary:
        raise ValueError("Invalid input. Please enter 1, 2, or 3.")
    
    #Default parser is XML parser, so no need to specify it.
    root = ET.fromstring(xml_data)
    products = root.findall("./items/item[@name]")

    #Will map right function to user input, and then execute this function
    func_to_exec = function_dictionary.get(choice)
    func_to_exec(products)

except Exception as e:
    print(e)






