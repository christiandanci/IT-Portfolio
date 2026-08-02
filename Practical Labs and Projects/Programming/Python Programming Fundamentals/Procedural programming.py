def print_id(student_id):
    print("Your ID is:", student_id)

def print_age(age):
    print("Your age is:", age)

def print_name(name):
    print("Your name is:", name)

def update_name(name):
    return name

def main():
    # Student 1 details
    student1_id = 12345
    student1_name = "Cristian"
    student1_age = 44
    
    print_id(student1_id)
    print_name(student1_name)
    print_age(student1_age)
    
    # Student 2 details
    student2_id = 54321
    student2_name = "James"
    student2_age = 35
    
    print_id(student2_id)
    print_name(student2_name)
    print_age(student2_age)
    
    # Updating name of student 2
    student2_name = update_name("John")
    print_name(student2_name)

if __name__ == "__main__":
    main()
