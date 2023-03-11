from tabulate import tabulate
#to write data to "doctors_aid_output.txt"
doctor_information_screen = open("doctors_aid_outputs.txt","w")
#lists to keep data
name_list = []
patient_information_list = []
#This function creates a new patient 
def create_patient(name,information):
    if name not in name_list:
        print("Patient {} is recorded.".format(name))
        doctor_information_screen.write("Patient {} is recorded.\n".format(name))
        name_list.append(name)
        patient_information_list.append(information)
    else:
        print("Patient {} cannot be recorded due to duplication.".format(name))
        doctor_information_screen.write("Patient {} cannot be recorded due to duplication.\n".format(name))
#This function removes an existing patient 
def remove_patient(name):
    if name in name_list:
        print("Patient {} is removed.".format(name))
        doctor_information_screen.write("Patient {} is removed.\n".format(name))
        name_list.remove(name)
        for j in patient_information_list:
            if name == j[0].split(" ")[1]:
                patient_information_list.remove(j)
    else:
        print("Patient {} cannot be removed due to absence.".format(name))
        doctor_information_screen.write("Patient {} cannot be removed due to absence.\n".format(name))
#This function calculates the risk of dying from cancer
def probability_patient(name):
    number_of_name_calculator = 0
    for j in patient_information_list:
        if name == j[0].split(" ")[1]:
            probability_calculator = round(100*(float(j[3].split("/")[0]) / ((float(j[3].split("/")[1]) - float(j[3].split("/")[0]))*(1 - float(j[1])) + float(j[3].split("/")[0]))),2)
            illness_of_patient = j[2]
            number_of_name_calculator += 1
    if number_of_name_calculator == 1:
        print("Patient {} has a probability of {}% of having{}.".format(name,probability_calculator,illness_of_patient.lower()))
        doctor_information_screen.write("Patient {} has a probability of {}% of having{}.\n".format(name,probability_calculator,illness_of_patient.lower()))
    else:
        print("Probability for {} cannot be calculated due to absence.".format(name)) 
        doctor_information_screen.write("Probability for {} cannot be calculated due to absence.\n".format(name))
#This function compares the risk of dying from cancer with the risk of dying from treatment
def recommendation_patient(name):
    number_of_name_calculator = 0
    for j in patient_information_list:
        if name == j[0].split(" ")[1]:
            probability_calculator = round(100*(float(j[3].split("/")[0]) / ((float(j[3].split("/")[1]) - float(j[3].split("/")[0]))*(1 - float(j[1])) + float(j[3].split("/")[0]))),2)
            treatment_risk = 100*(float(j[5]))
            number_of_name_calculator +=1
    if number_of_name_calculator == 1:
        if probability_calculator > treatment_risk:
            print("System suggests {} to have the treatment.".format(name))
            doctor_information_screen.write("System suggests {} to have the treatment.\n".format(name))
        else:
            print("System suggests {} NOT to have the treatment.".format(name))
            doctor_information_screen.write("System suggests {} NOT to have the treatment.\n".format(name))
    else:
        print("Recommendation for {} cannot be calculated due to absence.".format(name))
        doctor_information_screen.write("Recommendation for {} cannot be calculated due to absence.\n".format(name))
#This function displays the list of registered patients
def list_patient():
    table_data = []
    table_row_information1 = ["Patient","Diagnosis","Disease","Disease","Treatment","Treatment"]
    table_row_information2 = ["Name","Accuracy","Name","Incidence","Name","Risk"]
    table_row_line = ["--------------------","----------------------","----------------------","-----------------","---------------------","-----------"]
    table_data.append(table_row_information1)
    table_data.append(table_row_information2)
    for i in patient_information_list:
        table_row = [i[0].split(" ")[1], f"{100*float(i[1]):.2f}%", i[2], i[3], i[4] , f"{int(100*float(i[5]))}%"]
        table_data.append(table_row_line)
        table_data.append(table_row)
    print(tabulate(table_data,tablefmt="psql"))
    doctor_information_screen.write(tabulate(table_data,tablefmt="psql")+"\n")
#to read data from "doctors_aid_inputs.txt"
file = open("doctors_aid_inputs.txt","r")
data = file.readlines()
data = [a.split(",") for a in data]
for i in data:
    if i[0].split(" ")[0] == "create":
        create_patient(i[0].split(" ")[1],i)
    elif i[0].split(" ")[0] == "remove":
        remove_patient(i[0].split(" ")[1].rstrip("\n"))
    elif i[0].split(" ")[0] == "probability":
        probability_patient(i[0].split(" ")[1].rstrip("\n"))
    elif i[0].split(" ")[0] == "recommendation":
        recommendation_patient(i[0].split(" ")[1].rstrip("\n"))
    elif i[0].split(" ")[0].rstrip("\n") == "list":
        list_patient()