import csv
from datetime import datetime, timedelta
import argparse
import os

parser = argparse.ArgumentParser(description="Calculate winner. All path for window must be like \"C:\\Foo\\Bar\\text.txt\"")
parser.add_argument("--source-file", "-s", required=True, help="Path to CSV file with start time values", type=str)
parser.add_argument("--result-file", "-e", required=True, help="Path to CSV file with end time values", type=str)
parser.add_argument("--new-source-file", "-sn", required=True, help="Path to new CSV file with start time values", type=str)
parser.add_argument("--new-result-file", "-en", required=True, help="Path to new CSV file with end time values", type=str)
#parser.add_argument("--time", "-t", help="Timestamp parameter. Must be in format \"%Y-%m-%d %H:%M:%S %Z\". Example 2022-09-23 14:02:41 UTC", required=True, type=str)
args = parser.parse_args()

               #args.source-file       args.result-file
def PrepareFile(source_file_path: str, result_file_path: str):
    """
    Function create a complete CSV file with correct headers by getting <result_file path>
    and adding headers and info from <source_file_path>
    """
    ######################################
    ###### Create new csv with headers
    ######################################
    stats_headers = "ID,Name,Username,MSG,Last message,XP,REP"

#! ALL source_file_path rename to result_file_path

    #"E:\\Downloads\\stats_complete.csv"
    with open(result_file_path.replace("\\"), "w", encoding='utf-8') as complete_file: #former source_file_path
        complete_file.write(stats_headers)


    ######################################
    ###### Read csv with stats
    ######################################
#C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\
    #"E:\\Downloads\\Cryptonic Чат - users (exported from combot.org).csv"
    with open(source_file_path, "r", encoding="utf-8", newline='') as stats_file:
        stats = csv.reader(stats_file, delimiter=',')
        with open(result_file_path, "a", encoding="utf-8") as complete_file: #former source_file_path
            for row in stats:
                complete_file.write("\n" + ", ".join(row))

    list_users = []
    with open(result_file_path, "r", encoding="utf-8") as complete_file: #former source_file_path
        stats = csv.DictReader(complete_file, delimiter=",", fieldnames = stats_headers.split(","))
        for item in stats:
            list_users.append(item)
    return list_users

def calc_delta(old_val: int, new_val: int):
    return new_val - old_val

def create_result(newer_list: list, older_list: list):
    result = {}
    for item in newer_list:
        for old_item in  older_list:
            if item["ID"] != old_item["ID"]:
                continue
            else:
                result[item["ID"]] = [item["Name"], item["UserName"], calc_delta(int(item["MSG"]) - int(old_item["MSG"]))]
    return result

def find_min_max_count_of_msg(list_users_dicts: list):
    list_corrupted_users = []
    for j in range(1, len(list_users_dicts)):
        try:
            if (int(list_users_dicts[j]["MSG"].strip()) < min_val["Value"]):
                min_val["Value"] = int(list_users_dicts[j]["MSG"].strip())
                min_val["Name"] = list_users_dicts[j]["Name"].strip()
                min_val["ID"] = list_users_dicts[j]["ID"].strip()

            if (int(list_users_dicts[j]["MSG"].strip()) > max_val["Value"]):
                max_val["Value"] = int(list_users_dicts[j]["MSG"].strip())
                max_val["Name"] = list_users_dicts[j]["Name"].strip()
                max_val["ID"] = list_users_dicts[j]["ID"].strip()
        except:
            list_corrupted_users.append(list_users_dicts[j]["Name"].strip())

    print("Users with corrupted fields: ", list_corrupted_users)
    print("Max: ", max_val["Value"], "\nMin: ", min_val["Value"], "\nWinner: ", max_val["Name"], "\nWinner ID: ", max_val["ID"])
    return {max_val["ID"]: [max_val["Name"], max_val["Value"]]}



min_val = {"Name": None, "Value": 0, "ID": None}
max_val = {"Name": None, "Value": 0, "ID": None}
list_users_dict = PrepareFile(args.source_file, args.result_file)
list_users_dict_new = PrepareFile(args.new_source_file, args.new_result_file)
result = create_result(list_users_dict_new, list_users_dict)
find_min_max_count_of_msg(result)


# time = list_users_dict[1].get("Last message").strip()
# format_string = "%Y-%m-%d %H:%M:%S %Z"
# time_start = datetime.strptime(time, format_string)
# time_end = time_start + timedelta(days=7)
# print("Last message: ", time, "\nStart time: ", time_start, "\nEnd time: ", time_end)
os.system("pause")


# c:\Users\stepa\Documents\Repositories\Python\Stats\stats.py ^
# -s "C:\Users\stepa\Documents\Repositories\Python\Stats\csv\Cryptonic Чат - users (exported from combot.org).csv" ^
# -e "C:\Users\\tepa\Documents\Repositories\Python\Stats\csv\stats_complete.csv" ^
# -sn "C:\Users\stepa\Documents\Repositories\Python\Stats\csv\Cryptonic Чат - users (exported from combot.org)(1).csv" ^
# -en "C:\Users\stepa\Documents\Repositories\Python\Stats\csv\stats_complete_new.csv" ^