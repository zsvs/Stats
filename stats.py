import csv
import argparse
import os



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
    with open(result_file_path, "w", encoding='utf-8') as complete_file: #former source_file_path
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

def calc_delta(new_val: int, old_val: int):
    """
    Takes two integer values and return their delta
    """
    return new_val - old_val

def sort_func(dct):
    return dct["MSG"]

def create_result(newer_list: list, older_list: list, **kwargs):
    """
    Takes two positional arguments, <newer_list> and <older_list> and one boolean key-word argument for verbosity
    Performs comparison between them, and if elements are the same add them to the new dict
    Return the result as a sorted by MSG field list of the dictionary.
    Keys in dict: ID, Name, Username, MSG(delta of messages), From_datetime, To_datetime
    """
    result_list = []
    admins_list = ["qwerty_nana", "lebovsk"]
    for item in newer_list:
        for old_item in  older_list:
            if(item["ID"] != old_item["ID"]) or (item["Username"] in admins_list):
                continue
            else:
                try:
                    if(calc_delta(int(item["MSG"].strip()), int(old_item["MSG"].strip())) != 0):
                        if(kwargs.get("verbose")):
                            print("New:|","ID:", item["ID"],"Name:",item["Name"], item["Username"], "Time:",item["Last message"],"Old:|", "ID:",old_item["ID"], "Name:",old_item["Name"], old_item["Username"], " Time: ",old_item["Last message"], " MSG delta: ", calc_delta(int(item["MSG"].strip()), int(old_item["MSG"].strip())))
                        result_list.append({"ID": item["ID"], "Name": item["Name"], "Username": item["Username"], "MSG": calc_delta(int(item["MSG"].strip()), int(old_item["MSG"].strip())), "From_datetime": old_item["Last message"],"To_datetime": item["Last message"]})
                        result_list.sort(key=sort_func) # sorting by "MSG" field
                except ValueError:
                    if(item["ID"] == "ID"):
                        pass
                    else:
                        print(item["ID"]," - have corrupted fields")
    return result_list

def find_min_max_count_of_msg(list_users_dicts: list):
    print("Total counts of different entries:", len(list_users_dicts))
    min_val = {"Name": None, "Value": 0, "ID": None}
    max_val = {"Name": None, "Value": 0, "ID": None}
    for j in range(1, len(list_users_dicts)):
        if (int(list_users_dicts[j]["MSG"]) < min_val["Value"]):
            min_val["Value"] = int(list_users_dicts[j]["MSG"])
            min_val["Name"] = list_users_dicts[j]["Name"].strip()
            min_val["ID"] = list_users_dicts[j]["ID"].strip()
            min_val["Start_datetime"] = list_users_dicts[j]["From_datetime"].strip()
            min_val["Final_datetime"] = list_users_dicts[j]["To_datetime"].strip()

        if (int(list_users_dicts[j]["MSG"]) > max_val["Value"]):
            max_val["Value"] = int(list_users_dicts[j]["MSG"])
            max_val["Name"] = list_users_dicts[j]["Name"].strip()
            max_val["ID"] = list_users_dicts[j]["ID"].strip()
            max_val["Start_datetime"] = list_users_dicts[j]["From_datetime"].strip()
            max_val["Final_datetime"] = list_users_dicts[j]["To_datetime"].strip()

    print("Max: ", max_val["Value"], "\nMin: ", min_val["Value"], "\nWinner: ", max_val["Name"], "\nWinner ID: ", max_val["ID"], "\nStart datetime: ", max_val["Start_datetime"], "\nFinal datetime:", max_val["Final_datetime"])
    return {max_val["ID"]: [max_val["Name"], max_val["Value"]]}

def write_csv(filepath: str, list_dict: list):
    with open(filepath, 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ["ID", "Name", "Username", "MSG", "From_datetime", "To_datetime"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in list_dict:
            writer.writerow({"ID": item["ID"], "Name": item["Name"], "Username": item["Username"], "MSG": item["MSG"], "From_datetime": item["From_datetime"], "To_datetime": item["To_datetime"]})

def main():
    src_file = "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\Cryptonic Чат - users (exported from combot.org).csv"
    res_file = "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\stats_complete.csv"
    new_src_file = "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\Cryptonic Чат - users (exported from combot.org)(1).csv"
    new_res_file = "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\stats_complete_new.csv"
    out_file = "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\result.csv"

    # parser = argparse.ArgumentParser(description="Calculate winner. All path for window must be like \"C:\\Foo\\Bar\\text.txt\"")
    # parser.add_argument("--source-file", "-s", required=True, help="Path to CSV file with start time values", type=str)
    # parser.add_argument("--result-file", "-r", required=True, help="Path to CSV file with end time values", type=str)
    # parser.add_argument("--new-source-file", "-sn", required=True, help="Path to new CSV file with start time values", type=str)
    # parser.add_argument("--new-result-file", "-rn", required=True, help="Path to new CSV file with end time values", type=str)
    # parser.add_argument("--out-file", "-o", required=True, help="Save result to csv file. You need to provide path to file", type=str)
    # parser.add_argument("--verbose", "-v", required=False, help="Enable verbose. Print all difference in entries", type=bool)
    # args = parser.parse_args()

    # list_users_dict = PrepareFile(args.source_file, args.result_file) #PrepareFile(src_file, res_file) #
    # list_users_dict_new = PrepareFile(args.new_source_file, args.new_result_file) #PrepareFile(new_src_file, new_res_file) #
    # result = create_result(list_users_dict_new, list_users_dict, args.verbose) #verbose = False) #
    # find_min_max_count_of_msg(result)
    # write_csv(args.out_file, result) #(out_file, result)#
    list_users_dict = PrepareFile(src_file, res_file)
    list_users_dict_new = PrepareFile(new_src_file, new_res_file) #
    result = create_result(list_users_dict_new, list_users_dict, verbose = False)
    find_min_max_count_of_msg(result)
    write_csv(out_file, result)
    os.system("pause")
    return 0

main()

# Example Usage:
# C:\Users\stepa\Documents\Repositories\Python\Stats\stats.py `
# -s "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\Cryptonic Чат - users (exported from combot.org).csv" `
# -r "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\stats_complete.csv" `
# -sn "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\Cryptonic Чат - users (exported from combot.org)(1).csv" `
# -rn "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\stats_complete_new.csv" `
# -o "C:\\Users\\stepa\\Documents\\Repositories\\Python\\Stats\\csv\\result.csv" `
# -v True
