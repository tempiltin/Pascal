import os
import random
import datetime

def generate_pascal_file(file_name):
    code_templates = [
        "program HelloWorld; begin writeln('Hello, World!'); end.",
        "program SumTwoNumbers; var a, b: integer; begin a := 5; b := 10; writeln(a + b); end.",
        "program PrintNumbers; var i: integer; begin for i := 1 to 10 do writeln(i); end."
    ]
    
    code = random.choice(code_templates)
    with open(file_name, "w") as f:
        f.write(code)

def get_commit_dates():
    letters = {
        "T": [(1, 3), (1, 4), (1, 5), (1, 6), (2, 5), (3, 5), (4, 5)],
        "E": [(1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5)],
        "M": [(1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 4), (3, 4), (4, 4), (1, 5), (4, 5)],
        "P": [(1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 4), (3, 4), (1, 5)],
        "I": [(1, 3), (2, 3), (3, 3), (4, 3)],
        "L": [(1, 3), (2, 3), (3, 3), (4, 3), (4, 4)],
        "T": [(1, 3), (1, 4), (1, 5), (1, 6), (2, 5), (3, 5), (4, 5)],
        "I": [(1, 3), (2, 3), (3, 3), (4, 3)],
        "N": [(1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 5), (3, 6), (4, 6)]
    }
    
    base_date = datetime.date(2015, 1, 1)
    commit_dates = []
    
    for i, letter in enumerate("TEMPILTIN"):
        for week, day in letters[letter]:
            commit_dates.append(base_date + datetime.timedelta(weeks=week, days=day + i * 7))
    
    return commit_dates

def commit_and_push(date):
    os.system("git add .")
    commit_date = date.strftime("%Y-%m-%dT00:00:00")
    os.system(f'git commit --date="{commit_date}" -m "Commit on {commit_date}"')
    os.system("git push")

def main():
    commit_dates = get_commit_dates()
    for date in commit_dates:
        file_name = f"random_code_{date}.pas"
        generate_pascal_file(file_name)
        commit_and_push(date)
        print(f"Committed and pushed for {date}")

if __name__ == "__main__":
    main()
