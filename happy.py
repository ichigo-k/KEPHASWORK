my_details={"name":"micheal","age":12,"gender":"male"}
print(my_details["name"])

#creating a python dictionary
user_info={"name":"KEPHAS",
           "age":12,
           "hobbies":{
                    "outdoor":["Dancing","running"] , 
                    "indoor":["eating","singing"],
                    }
 }
#retrieving data
hobbies=user_info["hobbies"]
print(f"my hobbies are {hobbies}")

outdoor=hobbies["outdoor"]
print(f"my outdoor hobbies{outdoor}")

second_hobby=outdoor[1]
print(second_hobby)

student_grade={}

#adding data
student_grade["Kephas"]="A+"
student_grade["Arnold"]="C"
student_grade["Sheryl"]="A"
student_grade["Mike"]="A"
print (student_grade)

#Removing from a list
student_grade.pop("Arnold")
print(student_grade)

#Editing an element
student_grade["Mike"]="B"
print(student_grade)

#how to edit a key
student_grade["Mike"] = student_grade["Micheal"]
print(student_grade)


age=input("What is your age?")
name=input("what is your name?\n")
           
print(f"your name is {name} and age is {age}") 
