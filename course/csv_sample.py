import glob
import csv
from collections import defaultdict


def csvreader():
    csv_data = list()
    sublist = list()

    files = glob.glob("./csvfiles/*")
    for filename in files:
        with open(filename) as f:
            csv_open = csv.reader(f,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            header = next(csv_open)
            for row in csv_open:
                sublist.append(row[3])
                sublist.append(filename.replace("./csvfiles\\grades-",""))
                row[3] = sublist
                csv_data.append(row)
                sublist = []
        f.close()
    
    csv_dict = defaultdict(list)
    for i in range(len(csv_data)):
        csv_dict[csv_data[i][0]].append(csv_data[i][3])
    return csv_dict



def analyzer(request):
    csv_dict = csvreader()
    username = request.user.username
    nigate_list = list()

    for k,v in csv_dict.items():
        if k == username:
            for count in range(len(v)):
            #print(count)
                if float(v[count][0]) < 80.0:
                    nigate_list.append(v[count][1])
    return nigate_list