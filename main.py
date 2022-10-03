import argparse
from prayers_times import PrayersTimesPage

def main() -> None:
    parser = argparse.ArgumentParser(description='This is the main.py script for test')
    parser.add_argument('--url',action='store',dest='url',default=None,help='<Required> url link',required=True)
    results = parser.parse_args()
    url = results.url
    time_prayers_of_the_day = PrayersTimesPage(url)._get_times_prayers_of_the_day()
    print(time_prayers_of_the_day)

if __name__ == "__main__":
    main()
