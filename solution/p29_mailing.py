# Sends marking email to every student according to the marking file "marking.xlsx"

# Access Exel documents
from openpyxl import Workbook, load_workbook

# To sleep a few second between emails
import time

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Import for Prompting the user for a password without echoing.
import getpass

# smtp host name
smtp_host_name = 'mail.bfh.ch'
# port number
port_number = 587

# set up the SMTP server
smtp_server = smtplib.SMTP(host=smtp_host_name, port=port_number)
# security
smtp_server.starttls()
# smtp_server.login(sender_username, password)

# marking file
marking_filename = "marking-sample.xlsx"
# marking sheet
sheetname = "Marking"

# loading all the marking information
work_book = load_workbook(marking_filename, data_only=True)
work_sheet = work_book[sheetname]

# The 3 first lines
header1 = work_sheet[1]
header2 = work_sheet[2]
header3 = work_sheet[3]

# total number of students# Module's name, term, year
module_name = header1[0].value

print("Marking for: " + module_name + "\n")  # type: ignore

number_of_students = int(input("Enter the number of students: "))

# Requires interactive username and password
sender_username = input("Enter your username: ")

sender_password = getpass.getpass("Enter your password: ")
print()

# vertical index of first student
offset_header = 4
# between marks and scale
delta_marks = 7
# vertical offset of the scale, horizontal is 10
offset_scale = offset_header + delta_marks + number_of_students

scale_A = work_sheet[offset_scale + 0][0].value
scale_A_from = work_sheet[offset_scale + 0][1].value
scale_A_to = work_sheet[offset_scale + 0][2].value
scale_B = work_sheet[offset_scale + 1][0].value
scale_B_from = work_sheet[offset_scale + 1][1].value
scale_B_to = work_sheet[offset_scale + 1][2].value
scale_C = work_sheet[offset_scale + 2][0].value
scale_C_from = work_sheet[offset_scale + 2][1].value
scale_C_to = work_sheet[offset_scale + 2][2].value
scale_D = work_sheet[offset_scale + 3][0].value
scale_D_from = work_sheet[offset_scale + 3][1].value
scale_D_to = work_sheet[offset_scale + 3][2].value
scale_E = work_sheet[offset_scale + 4][0].value
scale_E_from = work_sheet[offset_scale + 4][1].value
scale_E_to = work_sheet[offset_scale + 4][2].value
scale_FX = work_sheet[offset_scale + 5][0].value
scale_FX_from = work_sheet[offset_scale + 5][1].value
scale_FX_to = work_sheet[offset_scale + 5][2].value
scale_F = work_sheet[offset_scale + 6][0].value
scale_F_from = work_sheet[offset_scale + 6][1].value
scale_F_to = work_sheet[offset_scale + 6][2].value

max_project_percent = header3[5].value
max_test_point = header3[6].value
max_test_percent = header3[7].value

smtp_server.login(sender_username, sender_password)

# For each student composes the mail and sends it
i = 0
while i < number_of_students:

    # current line for the i th student
    row = work_sheet[i+offset_header]
    # various information to include in the mail
    student_number = row[0].value
    last_name = row[1].value
    first_name = row[2].value
    project_percent = row[5].value
    test_point = row[6].value
    test_percent = row[7].value
    total_percent = row[8].value
    mark = row[9].value
    # email of the i th student
    email_address = row[10].value

    message = \
        "Dear Ms./Mr. {first_name} {last_name}\n\n".format(first_name=first_name, last_name=last_name) + \
        "Here follow the details for the marking of module {module_name}.\n\n".format(module_name=module_name) + \
        "You find below the percentage-points of your project, test , total, and final mark:\n\n" + \
        "   Project: {project_percent} % (max {max_project_percent})\n".format(project_percent=project_percent, max_project_percent=max_project_percent) + \
        "   Test   : {test_point} points (max {max_test_point})\n".format(test_point=test_point, max_test_point=max_test_point) + \
        "   Test   : {test_percent} % (max {max_test_percent})\n".format(test_percent=test_percent, max_test_percent=max_test_percent) + \
        "   Total  : {total_percent} %\n".format(total_percent=total_percent) + \
        "   ------------\n" + \
        "   Mark   : {mark}\n\n".format(mark=mark) + \
        "The scale is as follows: \n\n" + \
        "      FROM   TO \n\n" + \
        "   {scale_A} : {scale_A_from} - {scale_A_to} \n".format(scale_A=scale_A, scale_A_from=scale_A_from, scale_A_to=scale_A_to) + \
        "   {scale_B} : {scale_B_from}  - {scale_B_to} \n".format(scale_B=scale_B, scale_B_from=scale_B_from, scale_B_to=scale_B_to) + \
        "   {scale_C} : {scale_C_from}  - {scale_C_to} \n".format(scale_C=scale_C, scale_C_from=scale_C_from, scale_C_to=scale_C_to) + \
        "   {scale_D} : {scale_D_from}  - {scale_D_to} \n".format(scale_D=scale_D, scale_D_from=scale_D_from, scale_D_to=scale_D_to) + \
        "   {scale_E} : {scale_E_from}  - {scale_E_to} \n".format(scale_E=scale_E, scale_E_from=scale_E_from, scale_E_to=scale_E_to) + \
        "   {scale_FX}: {scale_FX_from}  - {scale_FX_to} \n".format(scale_FX=scale_FX, scale_FX_from=scale_FX_from, scale_FX_to=scale_FX_to) + \
        "   {scale_F} : {scale_F_from}  - {scale_F_to} \n".format(scale_F=scale_F, scale_F_from=scale_F_from, scale_F_to=scale_F_to) + \
        "\n" + \
        "Cheers\n\n" + \
        "Olivier Biberstein\n\n"

    msg = EmailMessage()

    msg["Subject"] = "Marking: " + module_name
    msg["From"] = "olivier.biberstein@bfh.ch"
    msg["Cc"] = "olivier.biberstein@bfh.ch"
#    msg["To"] = "olivier.biberstein@gmail.com"
    msg["To"] = email_address

    msg.set_content(message)
    # login to the SMTP server

    # sends the message
#    smtp_server.send_message(msg)

    print("\n#####", student_number, email_address,
          first_name, last_name, "#####\n")

    print(message)

    # delay for the mail server 2 seconds
    time.sleep(3)

    i += 1

smtp_server.quit
print("Done")
