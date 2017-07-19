

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# int, bool, int, string, male/female, int, bool, bool, int, float, string, char 

def load_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def process_lines(lines):
    for line in lines:
        print line.strip()

def main():
    lines = load_file('train.csv')
    process_lines(lines)

if __name__ == "__main__":
    main()
