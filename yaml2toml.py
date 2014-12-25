#!/usr/bin/env python2

from jinja2 import Template
from yaml import load
import argparse
import sys


def parse_arguments():
    description = 'YAML to TOML converter'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--template', '-t',
        metavar='FILE',
        dest='template_fh',
        type=argparse.FileType('r'),
        default='./yaml2toml_macro.j2',
        help='jinja2 template (default: ./yaml2toml_macro.j2)')
    parser.add_argument(
        '--yaml', '-y',
        metavar='FILE',
        dest='yaml_fh',
        type=argparse.FileType('r'),
        default='-',
        help='YAML file to convert (default: -)')

    return (parser.parse_args(), parser)


def main():
    # Parse command line arguments
    (args, parser) = parse_arguments()

    # Read the content of the template file
    template_text = args.template_fh.read()
    args.template_fh.close()

    # Read the YAML file
    yaml_data = load(args.yaml_fh)
    args.yaml_fh.close()

    # Create jinja template object
    t = Template(template_text)
    # Convert the YAML data to TOML
    toml_output = t.module.yaml2toml(yaml_data).encode('utf8')

    # Print the result
    sys.stdout.write(toml_output)


if __name__ == '__main__':
    main()
