import argparse
from prayers_times import PrayersTimesPage

def main() -> None:
    parser = argparse.ArgumentParser(description='This is the main.py script for test')
    parser.add_argument('--url',action='store',dest='url',default=None,help='<Required> url link',required=True)
    results = parser.parse_args()
    url = results.url
    PrayersTimesPage(url)._write_to_json()
    #print(calendar)

if __name__ == "__main__":
    main()
