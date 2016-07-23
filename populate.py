# -*- coding: utf-8 -*-
import os, csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proupologismos.settings')

import django

django.setup()

from visualisations.models import Office, SubOffice


def add_office(id, name, year, total):
    office = Office.objects.get_or_create(id=id, year=year, total=total)[0]
    office.officeId = id
    office.name = name
    office.year = year
    office.total = total
    office.save()
    return office


def add_subOffice_initial(office, subOfficeId, name, year, total):
    subOffice = SubOffice.objects.get_or_create(office=office, subOfficeId=subOfficeId, year=year, total=total)[0]
    subOffice.name = name
    subOffice.year = year
    subOffice.total = total
    subOffice.save()


def populate():
    # Only Offices and SubOffices
    firstline = True
    with open('proupologismos-revised-csv.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if firstline:
                firstline = False
                continue
            elif len(row[0]) == 2:
                add_office(row[0], row[1], 2014, float(row[2]))
            elif len(row[0]) == 4:
                # SubOffices in here
                officeId = row[0][:2]
                subOfficeId = row[0]
                name = row[1]
                year = 2015
                total = float(row[2])
                office = Office.objects.get(officeId=officeId)
                add_subOffice_initial(office, subOfficeId, name, year, total)
                # if len(row[0]) > 4 and not row[0] == "Column":
                #     # Pagio, taktites, anaptuksiakes in here


def add_more_data():
    firstline = True
    with open('proupologismos-revised-csv.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if firstline:
                firstline = False
                continue
            elif len(row[0]) > 4 and not row[0] == 'Column':
                # SubOffices in here
                subOfficeId = row[0][:4]
                suboffice = SubOffice.objects.get(subOfficeId=subOfficeId)
                if row[0][-1] == '1':
                    # pagio
                    pagio = float(row[2])
                    suboffice.pagio = pagio
                    suboffice.save()
                elif row[0][-1] == '2':
                    taktikes = float(row[2])
                    suboffice.taktikes = taktikes
                    suboffice.save()
                elif row[0][-1] == '3':
                    anaptuksiakes = float(row[2])
                    suboffice.anaptuksiakes = anaptuksiakes
                    suboffice.save()                    # anaptuksiakes
                    # if len(row[0]) > 4 and not row[0] == "Column":
                    #     # Pagio, taktites, anaptuksiakes in here


#DIFFERENT YEARS

if __name__ == '__main__':
    print "Starting Budget population script..."
    populate()
    add_more_data()
