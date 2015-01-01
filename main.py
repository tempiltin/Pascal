import os
import random
import datetime

# Pascal papkasini yaratish
if not os.path.exists("pascal"):
    os.makedirs("pascal")

# Pascal kod shablonlari
CODE_TEMPLATES = [
  
    "program HelloWorld; begin writeln('Hello, World!'); end.",
    "program SumTwoNumbers; var a, b: integer; begin a := 5; b := 10; writeln(a + b); end.",
    "program PrintNumbers; var i: integer; begin for i := 1 to 10 do writeln(i); end.",
    "program Factorial; var n, f, i: integer; begin n := 5; f := 1; for i := 1 to n do f := f * i; writeln(f); end.",
    "program ReverseString; var s: string; begin s := 'Pascal'; writeln(copy(s, length(s), 1)); end."
]

# 1 yil davomida 70% kunni tanlab olish
def get_commit_dates(year, activity_percent=70):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    all_days = [(start_date + datetime.timedelta(days=i)) for i in range((end_date - start_date).days + 1)]
    
    # Tasodifiy kunlarni tanlash (70% faollik)
    active_days = random.sample(all_days, int(len(all_days) * (activity_percent / 100)))
    return sorted(active_days)

# Pascal fayl yaratish
def generate_pascal_file(file_name):
    code = random.choice(CODE_TEMPLATES)
    with open(file_name, "w") as f:
        f.write(code)

# Git commit va push qilish
def commit_and_push(date):
    os.system("git add .")
    commit_date = date.strftime("%Y-%m-%dT12:00:00")
    os.system(f'git commit --date="{commit_date}" -m "Commit on {commit_date}"')
    os.system("git push")

# Asosiy funksiya
def main():
    year = 2015  # O'zingiz xohlagan yilni tanlang
    commit_dates = get_commit_dates(year)

    for date in commit_dates:
        file_name = f"pascal/code_{date}.pas"
        generate_pascal_file(file_name)
        commit_and_push(date)
        print(f"✅ {date} uchun commit qilindi.")

if __name__ == "__main__":
    main()
