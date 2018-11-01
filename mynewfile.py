
mark = int(input("Enter final mark for CSF:"))
if mark>= 40:
    elem1= int(input("Enter mark for Element1:"))
    if elem1>=20:
        print("you have passed")
    else:
        print("you needed a minimum of 20 for this element to pass the modul")
elif mark>=20:
    print("you have faild but are eligible for a re-sit")
else:
    print("sorry! you will have to retake your modul")
