# -*- coding: utf-8 -*-
import os, csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget_project.settings')

import django

django.setup()

from visualisations.models import Office, SubOffice


def add_office(id, name, year, total, approved, revised):
    office = Office.objects.get_or_create(officeId=id, year=year, total=total, approved=approved, revised=revised)[0]
    office.officeId = id
    office.name = name
    office.year = year
    office.total = total
    office.approved = approved
    office.revised = revised
    office.save()
    return office


def add_subOffice_initial(office, subOfficeId, name, year, total, approved, revised):
    subOffice = SubOffice.objects.get_or_create(office=office, subOfficeId=subOfficeId, year=year, total=total, approved=approved, revised=revised)[0]
    subOffice.name = name
    subOffice.year = year
    subOffice.total = total
    subOffice.approved = approved
    subOffice.revised = revised
    subOffice.save()


def populate():
    # Only Offices and SubOffices
    firstline = True
    firstrow = []
    with open('budget_project-revised-csv.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if firstline:
                firstline = False
                firstrow = row
                continue
            elif len(row[0]) == 2:
                #Add different years
                i = 2
                while i < len(row):
                    year = int(firstrow[i][:4])
                    if firstrow[i][-1]=='a':
                        add_office(row[0], row[1], year, float(row[i]), True, False)
                    elif firstrow[i][-1]=='r':
                        add_office(row[0], row[1], year, float(row[i]), False, True)
                    else:
                        add_office(row[0], row[1], year, float(row[i]), False, False)

                    i += 1
            elif len(row[0]) == 4:  # SubOffices in here
                officeId = row[0][:2]
                subOfficeId = row[0]
                name = row[1]
                i = 2
                total = float(row[2])
                while i < len(row):
                    year = int(firstrow[i][:4])
                    if firstrow[i][-1]=='a':
                        office = Office.objects.get(officeId=officeId, year=year,approved=True,revised=False)
                        add_subOffice_initial(office, subOfficeId, name, year, total, True, False)
                    elif firstrow[i][-1]=='r':
                        office = Office.objects.get(officeId=officeId, year=year,approved=False,revised=True)
                        add_subOffice_initial(office, subOfficeId, name, year, total, False, True)
                    else:
                        office = Office.objects.get(officeId=officeId, year=year,approved=False,revised=False)
                        add_subOffice_initial(office, subOfficeId, name, year, total, False, False)
                    i += 1




def add_more_data():
    firstline = True
    firstrow = []
    with open('budget_project-revised-csv.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if firstline:
                firstline = False
                firstrow = row
                continue
            elif len(row[0]) > 4 and not row[0] == 'Column':
                # SubOffices in here
                subOfficeId = row[0][:4]
                i=2
                while i < len(row):
                    year = int(firstrow[i][:4])
                    if firstrow[i][-1]=='a':
                        suboffice = SubOffice.objects.get(subOfficeId=subOfficeId, year=year,approved=True,revised=False)
                    elif firstrow[i][-1]=='r':
                        suboffice = SubOffice.objects.get(subOfficeId=subOfficeId, year=year,approved=False,revised=True)
                    else:
                        suboffice = SubOffice.objects.get(subOfficeId=subOfficeId, year=year,approved=False,revised=False)
                    if row[0][-1] == '1':
                        # pagio
                        pagio = float(row[i])
                        suboffice.pagio = pagio
                        suboffice.save()
                    elif row[0][-1] == '2':
                        taktikes = float(row[i])
                        suboffice.taktikes = taktikes
                        suboffice.save()
                    elif row[0][-1] == '3':
                        anaptuksiakes = float(row[i])
                        suboffice.anaptuksiakes = anaptuksiakes
                        suboffice.save()  # anaptuksiakes
                    i+=1


# DIFFERENT YEARS

if __name__ == '__main__':
    print "Starting Budget population script..."
    populate()
    print "Finished initial population amending data..."
    add_more_data()
