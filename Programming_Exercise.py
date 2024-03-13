#Programming Exercise
#Name Getnet Tadele
#Id   043/RMSC_B7/2023

class MinitermGenerator:
    def __init__(self, list_of_relations):
        self.list_of_relations = list_of_relations

    def generate_miniterms(self):
        fr_1 = []  # List to store fragments for predicate "Mark > 85" and "Age < 21"
        fr_2 = []  # List to store fragments for predicate "Mark <= 85" and "Age >= 21"


        for relations in self.list_of_relations:
            if self.satisfies_predicate(relations, "Mark > 85", "Age < 21"):
                fr_1.append(relations)
            if self.satisfies_predicate(relations, "Mark <= 85", "Age >= 21"):
                fr_2.append(relations)

        return [fr_1, fr_2]

    def satisfies_predicate(self, relations, predicate1, predicate2):
        if (predicate1 == "Mark > 85" and predicate2 == "Age < 21") or \
           (predicate1 == "Age < 21" and predicate2 == "Mark > 85"):
            return relations.get('Mark', 0) > 85 and relations.get('Age', 0) < 21
        elif (predicate1 == "Mark <= 85" and predicate2 == "Age >= 21") or \
             (predicate1 == "Age >= 21" and predicate2 == "Mark <= 85"):
            return relations.get('Mark', 0) <= 85 and relations.get('Age', 0) >= 21
        return False

# Assuming list of relations as a Python list of dictionaries:
list_of_relations = [{'Name': 'kasim', 'ID': 'abc', 'Age': 19, 'Mark': 90},
                     {'Name': 'Aster', 'ID': 'yts', 'Age': 21, 'Mark': 80},
                     {'Name': 'Tola', 'ID': 'hty', 'Age': 20, 'Mark': 95},
                     {'Name': 'Abebe', 'ID': 'cvd', 'Age': 22, 'Mark': 76}]

miniterm_generator = MinitermGenerator(list_of_relations)

#  CON-MIN algorithm
result = miniterm_generator.generate_miniterms()

# Print each fragment separately
for fragment in result:
    print(fragment)

