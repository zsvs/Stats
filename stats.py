import csv
from datetime import datetime, timedelta
import argparse
import os

parser = argparse.ArgumentParser(description="Calculate winner. All path for window must be like \"C:\\Foo\\Bar\\text.txt\"")
parser.add_argument("--start-file", "-s", required=True,
                    help="Path to CSV file with start time values", type=str)
parser.add_argument("--end-file", "-e", required=True,
                    help="Path to CSV file with end time values", type=str)
parser.add_argument("--time", "-t", help="Timestamp parameter. Must be in format \"%Y-%m-%d %H:%M:%S %Z\". Example 2022-09-23 14:02:41 UTC", required=True, type=str)
args = parser.parse_args()

                #args.start_file       args.end_file
def PrepareFile(source_file_path: str, result_file_path: str):
    ######################################
    ###### Create new csv with headers
    ######################################
    stats_headers = "ID,Name,Username,MSG,Last message,XP,REP"

    #"E:\\Downloads\\stats_complete.csv"
    with open(args.source_file_path, "w", encoding='utf-8') as complete_file:
        complete_file.write(stats_headers)


    ######################################
    ###### Read csv with stats
    ######################################

    #"E:\\Downloads\\Cryptonic Чат - users (exported from combot.org).csv"
    with open(args.result_file_path, "r", encoding="utf-8", newline='') as stats_file:
        stats = csv.reader(stats_file, delimiter=',')
        with open(args.source_file_path, "a", encoding="utf-8") as complete_file:
            for row in stats:
                complete_file.write("\n" + ", ".join(row))

    list_users = []
    with open(args.source_file_path, "r", encoding="utf-8") as complete_file:
        stats = csv.DictReader(complete_file, delimiter=",", fieldnames = stats_headers.split(","))
        for item in stats:
            list_users.append(item)
    return list_users


list_corrupted_users = []
min_val = {"Name": None, "Value": 0, "ID": None}
max_val = {"Name": None, "Value": 0, "ID": None}
for j in range(1, len(list_users)):
    try:
        if (int(list_users[j]["MSG"].strip()) < min_val["Value"]):
            min_val["Value"] = int(list_users[j]["MSG"].strip())
            min_val["Name"] = list_users[j]["Name"].strip()
            min_val["ID"] = list_users[j]["ID"].strip()

        if (int(list_users[j]["MSG"].strip()) > max_val["Value"]):
            max_val["Value"] = int(list_users[j]["MSG"].strip())
            max_val["Name"] = list_users[j]["Name"].strip()
            max_val["ID"] = list_users[j]["ID"].strip()
    except:
        list_corrupted_users.append(list_users[j]["Name"].strip())

print("Users with corrupted fields: ", list_corrupted_users)
print("Max: ", max_val["Value"], "\nMin: ", min_val["Value"], "\nWinner: ", max_val["Name"], "\nWinner ID: ", max_val["ID"])

time = list_users[1].get("Last message").strip()
format_string = "%Y-%m-%d %H:%M:%S %Z"
time_start = datetime.strptime(time, format_string)
time_end = time_start + timedelta(days=7)
print("Last message: ", args.time, "\nStart time: ", time_start, "\nEnd time: ", time_end)
os.system("pause")