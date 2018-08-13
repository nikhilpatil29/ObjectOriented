import json
from Doctor import *
from Patient import *
from Appointment import *
from datetime import *
def add_doctor():
    doctor_obj = Doctor()
    data = {}
    data["doctor"] = {}
    data = json.load(open('Doctor.json', 'r'))
    try:
        first_name = raw_input("Enter first name: ")
        doctor_obj.set_first_name(first_name)

        last_name = raw_input("Enter last name: ")
        doctor_obj.set_last_name(last_name)

        id = raw_input("Enter Doctor Id : ")
        doctor_obj.set_id(id)

        specialization = raw_input("Enter doctor Specialization : ")
        doctor_obj.set_specification(specialization)

        availability = raw_input("Enter Doctor Availability : ")
        doctor_obj.set_availability(availability)

        data["doctor"][first_name] = ({
            'first_name': doctor_obj.get_first_name(),
            'last_name': doctor_obj.get_last_name(),
            'id': doctor_obj.get_id(),
            'specialization': doctor_obj.get_specification(),
            'availability': doctor_obj.get_availability(),

        })
        with open('Doctor.json', 'w') as data1:
            json.dump(data, data1,sort_keys=True)

        print ("Person Detail Added Successfully!")

    except (NameError, SyntaxError,TypeError):
        print "Please enter a proper formated data only !"


def add_patient():
    patient_obj = Patient()
    data = {}
    data["patient"] = {}
    data = json.load(open('Patient.json', 'r'))
    try:
        first_name = raw_input("Enter first name: ")
        patient_obj.set_first_name(first_name)

        last_name = raw_input("Enter last name: ")
        patient_obj.set_last_name(last_name)

        id = raw_input("Enter Patient Id : ")
        patient_obj.set_patient_id(id)

        patientNumber = raw_input("Enter Patient Mobile Number : ")
        patient_obj.set_patient_number(patientNumber)

        age = raw_input("Enter Patient age : ")
        patient_obj.set_age(age)

        data["patient"][first_name] =({
            'first_name': patient_obj.get_first_name(),
            'last_name': patient_obj.get_last_name(),
            'id': patient_obj.get_patient_id(),
            'patientNumber': patient_obj.get_patient_number(),
            'age': patient_obj.get_age(),

        })
        with open('Patient.json', 'w') as data1:
            json.dump(data, data1,sort_keys=True)

        print ("Person Detail Added Successfully!")

    except (NameError, SyntaxError, TypeError):
        print "Please enter a proper formated data only !"


def display_doctor():
    print "\n--------------Listing Contacts...-------------\n"

    doctorjson = json.load(open('Doctor.json', 'r'))
    name_keys = list(doctorjson["doctor"].keys())
    print '\tFIRSTNAME\t','\tLASTNAME\t' 'ID\t', 'SPECIFICATION\t', 'AVAILABILITY\t'
    for data in name_keys:
        print "\t", doctorjson["doctor"][data]['first_name'], "\t",\
            doctorjson["doctor"][data]["last_name"], "\t", \
            doctorjson["doctor"][data]["id"], "\t", \
            doctorjson["doctor"][data]["specialization"], "\t",\
            doctorjson["doctor"][data]["availability"], "\t"


def display_patient():
    print "\n--------------Listing Contacts...-------------\n"

    patientjson = json.load(open('Patient.json', 'r'))
    name_keys = list(patientjson["patient"].keys())
    print '\tFIRSTNAME\tLASTNAME\t\tID\tNUMBER\t\tAGE'
    for data in name_keys:
        print "\t", patientjson["patient"][data]['first_name'], "\t", \
            patientjson["patient"][data]["last_name"], "\t", \
            patientjson["patient"][data]["id"], "\t", \
            patientjson["patient"][data]["patientNumber"], "\t", \
            patientjson["patient"][data]["age"], "\t"
    print "\n"


def search_doctor():
    print "Enter the Doctor Name or Id or Specialization : "
    checkname = raw_input()

    try:
        doctorlist = json.load(open('Doctor.json', 'r'))
        name_keys = list(doctorlist["doctor"].keys())

        for data in name_keys:
            if doctorlist["doctor"][data]["first_name"] == checkname or doctorlist["doctor"][data]["id"] == checkname or doctorlist["doctor"][data]["specialization"] == checkname :
                # print "Data Found\n"
                print '\tFIRSTNAME\t', '\tLASTNAME\t' 'ID\t', 'SPECIFICATION\t', 'AVAILABILITY\t'
                print "\t", doctorlist["doctor"][data]['first_name'], "\t", doctorlist["doctor"][data][
                    "last_name"], "\t", doctorlist["doctor"][data]["id"], "\t", doctorlist["doctor"][data][
                    "specialization"], "\t", doctorlist["doctor"][data]["availability"], "\t\n"
    except SyntaxError:
        print "error in name"
    # for data in name_keys:
    #     if doctorlist['doctor'][data]["first_name"] == search:
    #         print "Data Found"
    #         print '\tFIRSTNAME\t', '\tLASTNAME\t' 'ID\t', 'SPECIFICATION\t', 'AVAILABILITY\t'
    #         print "\t", doctorlist["doctor"][data]['first_name'], "\t", \
    #             doctorlist["doctor"][data]["last_name"], "\t", \
    #             doctorlist["doctor"][data]["id"], "\t", \
    #             doctorlist["doctor"][data]["specialization"], "\t", \
    #             doctorlist["doctor"][data]["availability"], "\t"

def take_appointment():
    doctorinfo = raw_input("Enter a doctor detail to be search\n")
    doctor_availibility = search_doctor_name(doctorinfo)
    count = 0
    # print doctor_availibility
    if doctor_availibility != None:
        # print doctor_availibility
        appointment_list = json.load(open('Appoinment.json', 'r'))
        appointment = appointment_list["appointment"]
        # name_keys = list(appointment_list["appoinment"].keys())
        for data in appointment:
            # print data["doctor"]
            # for name in name_keys:
            #     print appointment_list["appoinment"]["doctor"][name]
            if doctor_availibility["first_name"] == data["doctor"]["first_name"] and doctor_availibility["id"] == \
                    data["doctor"]["id"]:
                # print "match found"
                count += 1
        print "Dr. ", doctor_availibility["first_name"], " had ", count, " appoinments"
        if count < 5:
            patient_name = raw_input("Enter any patient details to search : ")
            patient_availabile = search_patient_name(patient_name)
            print patient_availabile
            if patient_availabile != None:
                # doctorlist = json.load(open('Doctor.json', 'r'))
                # name_keys = list(doctorlist["doctor"].keys())
                print "match found"
                print addAppointmentDetails(doctor_availibility, patient_availabile)
            #         # displayAppointmentDetails()
            else:
                print "Patients not Found...."
        #
        else:
            print "Doctor will not available today...."

def search_patient():
    print "Enter the Patient Name or Id or Number : "
    checkpatient = raw_input()

    try:
        doctorlist = json.load(open('Patient.json', 'r'))
        name_keys = list(doctorlist["patient"].keys())

        for data in name_keys:
            if doctorlist["patient"][data]["first_name"] == checkpatient or doctorlist["patient"][data][
                "id"] == checkpatient or doctorlist["patient"][data]["patientNumber"] == checkpatient:
                # print "Data Found\n"
                print '\tFIRSTNAME\t', '\tLASTNAME\t' 'ID\t', 'AGE\t', 'PATIENTNUMBER\t'
                print "\t", doctorlist["patient"][data]['first_name'], "\t", doctorlist["patient"][data][
                    "last_name"], "\t", doctorlist["patient"][data]["id"], "\t", doctorlist["patient"][data][
                    "age"], "\t", doctorlist["patient"][data]["patientNumber"], "\t\n"
    except SyntaxError:
        print "error in name"

def search_doctor_name(doctorinfo):
    count = 0
    try:
        doctorlist = json.load(open('Doctor.json', 'r'))
        name_keys = list(doctorlist["doctor"].keys())

        for data in name_keys:
            if doctorlist["doctor"][data]["first_name"] == doctorinfo or doctorlist["doctor"][data][
                "id"] == doctorinfo or doctorlist["doctor"][data]["specialization"] == doctorinfo:
                count += 1
                doctorfname = doctorlist["doctor"][data]["first_name"]
                doctorlname = doctorlist["doctor"][data]["last_name"]
                doctorid = doctorlist["doctor"][data]["id"]
                doctorspecialization = doctorlist["doctor"][data]["specialization"]
                doctoravailibility = doctorlist["doctor"][data]["availability"]
        new_obj = {"first_name": doctorfname, "last_name ": doctorlname, "id": doctorid,
            "specification": doctorspecialization, "availability": doctoravailibility}
        if count == 0:
            return None
        else:
            return new_obj
    except SyntaxError:
        print "error in name"


def search_patient_name(patient_name):
    try:
        patientlist = json.load(open('Patient.json', 'r'))
        name_keys = list(patientlist["patient"].keys())
        count = 0
        for data in name_keys:
            if patientlist["patient"][data]["first_name"] == patient_name or patientlist["patient"][data][
                "id"] == patient_name or patientlist["patient"][data]["patientNumber"] == patient_name:
                count += 1
                patientfname = patientlist["patient"][data]["first_name"]
                patientname = patientlist["patient"][data]["last_name"]
                patientid = patientlist["patient"][data]["id"]
                patientage = patientlist["patient"][data]["age"]
                patientnumber = patientlist["patient"][data]["patientNumber"]
        new_obj1 = {
            "first_name": patientfname,
            "last_name ": patientname,
            "id": patientid,
            "patientNumber": patientage,
            "age": patientnumber
        }
        if count == 0:
            return None
        else:
            return new_obj1
    except SyntaxError:
        print "error in name"

def addAppointmentDetails(doctordetail, patientdetail):

    data = json.load(open('Appoinment.json', 'r'))
    # data = {"appointment":[]}
    # data["appoinment"] = {}

    doctor_obj = Doctor()
    patient_obj = Patient()

    appointment_json = Appointment()
    appointment_json.set_doctor(doctordetail)
    appointment_json.set_patient(patientdetail)
    now = datetime.now()
    appointment_json.set_date(str(now)[:10])
    try:
        data["appointment"].append(
            {'doctor': appointment_json.get_doctor(), 'patient': appointment_json.get_patient(),
                'date': appointment_json.get_date()})

        with open('Appoinment.json', 'w') as data1:
            json.dump(data, data1, sort_keys=True)

        print ("Person Detail Added Successfully!")

    except (NameError, SyntaxError, TypeError):
        print "Please enter a proper formated data only !"

class clinic:
    # doctorjson = {}
    # doctorjson['doctor'] = {}
    # doctor = json.load(open('Doctor.json', 'r'))


    while True:
        print "-----------------Clinic Management System Operation--------------------"
        print "--------------------------Would you like to:----------------------------"
        print "\t\t\t1.) Add a Doctor Detail "
        print "\t\t\t2.) Add a Patient Detail "
        print "\t\t\t3.) Display Doctor "
        print "\t\t\t4.) Display Patient "
        print "\t\t\t5.) Search Doctor by Name or Id or Specification "
        print "\t\t\t6.) Search Patient by Name or Id or MobileNumber "
        print "\t\t\t7.) Take Doctor Appointment"
        print "\t\t\t8.) Exit "
        choice = input("Enter the number\n")

        if choice == 1:
            add_doctor()

        elif choice == 2:
            add_patient()

        elif choice == 3:
            display_doctor()

        elif choice == 4:
            display_patient()

        elif choice == 5:
            search_doctor()

        elif choice == 6:
            search_patient()

        elif choice == 7:
            take_appointment()

        elif choice == 8:
            print "Thank you for showing your interest..."
            exit()
        else:
            print"You have entered a wrong choice! Please enter a choice again..."