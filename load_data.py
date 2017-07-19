import csv

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# int, bool, int, string, male/female, int, bool, bool, int, float, string, char 
# int, 0/1, 1/2/3, string, male/female, int, 0/1, 0/1, int, float, string, char

def load_file(filename):
    output = []
    with open(filename, 'r') as f:
        flines = csv.reader(f, delimiter=',', quotechar='"')
        for row in flines:
            output.append(row)
    print output[0]
    return output

def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

def process_lines(lines):
    passengers = []
    for info in lines[1:]:
        print info
        passenger = {   "id": info[0],
            "survived": bool(info[1]),
            "class": int(info[2]),
            "name": info[3],
            "sex": info[4],
            "age": mk_float(info[5]),
            "sibsp": bool(info[6]),
            "parch": bool(info[7]),
            "ticket": info[8],
            "fare": float(info[9]),
            "cabin": info[10],
            "embarked": info[11] }
        passengers.append(passenger)
    return passengers

def main():
    lines = load_file('train.csv')
    passengers = process_lines(lines)

if __name__ == "__main__":
    main()
