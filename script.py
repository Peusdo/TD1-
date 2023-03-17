import random
def create_identities(nbidentite= 0):
    if nbidentite > 10 :
        print("impossible")
        return None
    else : 
        first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Julia']
        last_names = ['Smith', 'Jones', 'Brown', 'Johnson', 'Garcia', 'Davis', 'Wilson', 'Anderson', 'Thomas', 'Jackson']
        phone_numbers = ['555-1234', '555-5678', '555-9012', '555-3456', '555-7890', '555-2345', '555-6789', '555-0123', '555-4567', '555-8901']
        addresses = ['123 Main St.', '456 Maple Ave.', '789 Oak Ln.', '234 Elm St.', '567 Pine Rd.', '890 Cedar St.', '1234 Birch Ave.', '5678 Walnut St.', '9012 Spruce Ln.', '3456 Cherry Dr.']
        identite = []
        for i in range (nbidentite):
            identity1 = {}
            first_name1 = random.choice(first_names)
            first_names.remove(first_name1)
            last_name1 = random.choice(last_names)
            last_names.remove(last_name1)
            phone_number1 = random.choice(phone_numbers)
            phone_numbers.remove(phone_number1)
            address1 = random.choice(addresses)
            addresses.remove(address1)
            identity1['first_name'] = first_name1
            identity1['last_name'] = last_name1
            identity1['phone_number'] = phone_number1
            identity1['address'] = address1
            identite.append(identity1)
        return identite


def second_degree_polynomial(a = None, b = None, c = None):
    if (a == None) or (b == None) or (c == None) :
        return None
    delta=b**2-4*a*c
    print("Résolution de l'équation ",a,"x² + ",b,"x + ",c)
    if delta>0:
        x1=(-b-delta**0.5)/(2*a)
        x2=(-b+delta**0.5)/(2*a)
        print("Delta est positif donc il y a 2 solutions")
        print("x1 =",x1)
        print("x2 =",x2)
        return x1 , x2
    else:
        if delta==0:
            x0=-b/(2*a)
            print("Delta est nul donc il y a 1 solution unique")
            print("x0 =",x0)
            return x0
        else:
            print("Pas de solution dans l'espace des réel")
            return "null"

