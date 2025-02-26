
def create_record (name, telephone, address):
    """"Create Records"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record("Mike", "+447856669444","Farnham, Ham Street")
user2 = create_record("Andrew", "+47854565465454", "Sevenoaks, Park Road")

print(user1)
print(user2)

def give_award(medal, *persons):
    """"Give medals to persons"""
    for person in persons:
        print("Mr " + person.title() + " is awarded with the medal " + medal)

give_award("Golden Medal","Andrew", "Simon")
give_award("Silver ", "Alexander", "Dominic", "Luke")



