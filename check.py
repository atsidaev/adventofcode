import json
import os, sys
import subprocess

ANSWERS_FILENAME = "answers.json"
SOLUTION1_FILENAME = "1.py"
SOLUTION2_FILENAME = "2.py"
SOLUTIONS_BOTH_FILENAME = "both.py"

log = []

def test(script, num, year, both = False):
    output = subprocess.run([ "python", script ], capture_output=True)
    decoded = [ l.strip() for l in output.stdout.decode(sys.stdout.encoding).split('\n') ]
    decoded = list(filter(lambda x: x != '', decoded))

    try:
        if not both:
            val = decoded[-1]
            if isinstance(answers[day][num], int):
                val = int(val)

            if val != answers[day][num]:
                log.append(f"{year}: Task {num+1}: Should be {answers[day][num]} but got {decoded[-1]}")
                return False
            else:
                return True
        else:
            vals = [ decoded[-2], decoded[-1] ]
            res = [ None, None ]

            for num in [0,1]:
                val = vals[num]
                if isinstance(answers[day][num], int):
                    val = int(val)
                
                if val != answers[day][num]:
                    log.append(f"{year}: Task {num+1}: Should be {answers[day][num]} but got {vals[num]}")
                    res[num] = False
                else:
                    res[num] = True

            return res[0], res[1]
    except:
        log.append(f"{year}: Task {num+1}: FAIL. Stdout: {decoded}")
        if both:
            return False, False
        return False

results = dict()

for year in os.listdir("."):
    filename = os.path.join(year, ANSWERS_FILENAME)
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            answers = json.load(f)
    else:
        continue

    results[year] = list([ None ] * 50)

    for day in range(len(answers)):
        day_code = str(day + 1)
        if len(day_code) == 1: day_code = "0" + day_code
        day_dir = os.path.join(str(year), day_code)
        if os.path.isdir(day_dir):
            prefix = f"{year}: Running solution for day {day + 1}: "
            
            cur_dir = os.path.abspath(os.getcwd())
            os.chdir(day_dir)
            if os.path.isfile(SOLUTIONS_BOTH_FILENAME):
                print(prefix, "Both tasks", end='\r')
                res1, res2 = test(SOLUTIONS_BOTH_FILENAME, "both", year, True)
            else:
                print(prefix, "Task 1    ", end='\r')
                res1 = test(SOLUTION1_FILENAME, 0, year)
                print(prefix, "Task 2    ", end='\r')
                res2 = test(SOLUTION2_FILENAME, 1, year)

            pos = day * 2
            results[year][pos] = res1
            results[year][pos + 1] = res2

            os.chdir(cur_dir)
        else:
            # print(f"{year}: No solution for day {day + 1}")
            pass

        print()
        for year in results:
            print(year, ": ", end='')
            for solution in results[year]:
                if solution is None:
                    print("_", end='')
                elif not solution:
                    print('\033[91mF\033[0m', end='')
                elif solution:
                    print('\033[93m*\033[0m', end='')
            print()

        for year in results:
            print('\033[A', end='')
        print('\033[A', end='')

# Skip filled lines
print()
for year in results:
    print()

for l in log:
    print(l)