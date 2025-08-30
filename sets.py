# A set is a collection of unique data. That is, elements of a set cannot be duplicated.
# Sets are unordered, meaning that the elements do not have a defined order, and you cannot access them using an index.
# Sets are mutable, meaning that you can add or remove elements from a set after it has been created.
# Sets are defined using curly braces {} or the set() function.
# Example of creating a set
student_id = {111, 112, 113, 114}
print("Student ID:", student_id)
# creating an empty set
empty_set = set()
print("Empty set:", empty_set)
# adding elements to a set
student_id.add(115)
print("Updated Student ID:", student_id)
# removing elements from a set
student_id.remove(112)
print("After removing 112:", student_id)
# updating python sets
companies = {"Google", "Apple", "Microsoft"}
print("Companies:", companies)
tech_companies = {"Amazon", "Facebook"}
companies.update(tech_companies)
print("After update:", companies)
# iterating through a set
for company in companies:
    print(company)
# set operators
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# union of 2 sets including all elements from both sets without duplicates
print("Union of A and B:", A | B)
# intersection of 2 sets including only elements that are in both sets
print("Intersection of A and B:", A & B)
# difference of 2 sets including elements that are in A but not in B
print("Difference of A and B:", A - B)
# symmetric difference of 2 sets including elements that are in either set but not in both
print("Symmetric difference of A and B:", A ^ B)
# membership test
print("Is 2 in A?", 2 in A)
print("Is 5 in B?", 5 in B)
