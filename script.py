import django
django.setup()

import csv
from api.models import myModel,AcMaster, DemographyDetail
from rest_framework import status
from rest_framework.response import Response
import uuid

from django.core.files.storage import default_storage
from django.db.transaction import atomic

@atomic
def import_acmaster_process(file_name):
    file = default_storage.open(file_name)
    decoded_file = file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded_file)

    index = 1
    entries= dict()

    # for row in reader:


    for row in reader:
        entry = AcMaster(
            state = row["state"],
            ac_no = row["ac_no"],
            ac_name = row["ac_name"],
            pc_no = row["pc_no"],
            pc_name = row["pc_name"],
            zone = row["zone"],
            district_no = row["district_no"],
            district_name = row["district_name"],
            mp = row["mp"],
            mla = row["mla"],
            current_seat_category = row["current_seat_category"]
        )
        entries[index] = entry
        index+=1

    try:
        AcMaster.objects.bulk_create(entries.values())
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

    return Response("Your file has been successfully uploaded", status=status.HTTP_200_OK)


@atomic
def import_demographydetail_process(file_name):

    file = default_storage.open(file_name)
    decoded_file = file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded_file)

    index = 1
    entries= dict()

    for row in reader:

        print(row["ac"])
        master = AcMaster.objects.get(id=row["ac"])
        print(master)
        entry = DemographyDetail(
            ac = master,
            category = row["category"],
            type = row["type"],
            population = row["population"]
        )
        print("Hiiiiiiiiiii")
        entries[index] = entry
        index+=1

    print(entries)
    try:
        DemographyDetail.objects.bulk_create(entries.values())
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

    return Response("Your file has been successfully uploaded", status=status.HTTP_200_OK)

# import_acmaster_process('Gujarat_ac_master.csv')
import_demographydetail_process('Gujarat_Demography.csv')