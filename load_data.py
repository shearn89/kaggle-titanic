import re
import csv

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# int, bool, int, string, male/female, int, bool, bool, int, float, string, char 
# int, 0/1, 1/2/3, string, male/female, int, 0/1, 0/1, int, float, string, char

reg_number = re.compile("(\d+)")

def load_file(filename):
    output = []
    with open(filename, 'r') as f:
        flines = csv.reader(f, delimiter=',', quotechar='"')
        for row in flines:
            output.append(row)
    return output

def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

def mk_embarked(s):
    s = s.strip()
    if s == 'Q':
        return 0
    elif s == 'S':
        return 1
    elif s == 'C':
        return 2
    else:
        return -1

def mk_sex(s):
    s = s.strip()
    if s == "male":
        return 0
    elif s == "female":
        return 1
    else:
        return -1

def mk_ticket(s):
    s = s.strip()
    try:
        ticket_number = reg_number.findall(s)[0]
    except IndexError:
        ticket_number = -1
    return ticket_number

def process_lines(lines):
    passengers = []
    for info in lines[1:]:
        passenger = {
            "id": int(info[0]),
            "survived": int(info[1]),
            "class": int(info[2]),
            "name": info[3],
            "sex": mk_sex(info[4]),
            "age": mk_float(info[5]),
            "sibsp": int(info[6]),
            "parch": int(info[7]),
            "ticket": mk_ticket(info[8]),
            "fare": float(info[9]),
            "cabin": info[10],
            "embarked": mk_embarked(info[11])
        }
        passengers.append(passenger)
    return passengers

def main():
    lines = load_file('train.csv')
    passengers = process_lines(lines)

if __name__ == "__main__":
    main()
