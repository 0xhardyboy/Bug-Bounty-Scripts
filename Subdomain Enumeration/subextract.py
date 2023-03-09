import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, nargs="+", help="input file names")
parser.add_argument("--output", required=True, help="output file name")
args = parser.parse_args()

unique_domains = set()

with open(args.output, "w") as output_file:
    for input_file_name in args.input:
        with open(input_file_name, "r") as input_file:
            for line in input_file:
                domain = line.strip()
                parsed_domain = urlparse(domain)

                if parsed_domain.scheme:
                    domain_without_scheme = parsed_domain.netloc or parsed_domain.path
                    subdomains = domain_without_scheme.split(".")[:-2]
                else:
                    subdomains = domain.split(".")[:-2]

                new_domain = ".".join(subdomains)

                if new_domain not in unique_domains:
                    output_file.write(new_domain + "\n")
                    unique_domains.add(new_domain)

