import sys
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--url', type = str, help = 'URL to be processed')
parser.add_argument('--url-list', type = str, help = 'Text file containing a list of URLs to be processed')
args = parser.parse_args()


def format_url(domain):
    if not re.match('(?:http|https)://', domain):
        return 'http://{}'.format(domain)


if args.url:
    formatted_url = format_url(args.url)
    print(formatted_url)
elif args.url_list:
    with open(args.url_list, 'r') as f:
        for line in f:
            line = line.strip()
            formatted_url = format_url(line)
            print(formatted_url)
elif not sys.stdin.isatty():
    # stdin is not a terminal, meaning it has been redirected or piped
    for line in sys.stdin:
        line = line.strip()
        formatted_url = format_url(line)
        print(formatted_url)
        
        
