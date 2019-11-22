import csv
import re

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def get_csv(name, out):
    with open(name, 'r') as in_file:
        stripped = [line.strip() for line in in_file]
        with open(out, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(['Name', 'Gender', 'Microphone', 'Accent', 'Year'])
            for n, line in enumerate(stripped):
                if line.find('Year') == -1:
                    line = ", ".join(line.split())
                    line += year
                    comma_count = line.count(',')
                    # Good lines will have either 4 or 5 commas
                    if comma_count in [4,5]:
                        if comma_count == 5:
                            comma = find_nth(line, ',', 4)
                            line = line[:comma] + line[comma+1:]
                            writer.writerow(line.split(', '))
                elif n is not 1:
                    year = ', ' + line[line.find('2'):]




def main():
    get_csv('info.txt', 'log.csv')


if __name__ == "__main__":
    main()
