mkdir AoC2022/Day$1
touch AoC2022/Day$1/example_input.txt
touch AoC2022/Day$1/input.txt
touch AoC2022/Day$1/day$1.py
echo "import os" >> AoC2022/Day$1/Day$1.py
echo "file = open(os.path.join(os.getcwd(), \"AoC2022/Day$1/example_input.txt\"))" >> AoC2022/Day$1/Day$1.py
echo "data = file.read().strip()" >> AoC2022/Day$1/Day$1.py
echo "lines = [x.strip() for x in data.split('\\\n')]" >> AoC2022/Day$1/Day$1.py
