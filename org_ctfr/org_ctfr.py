#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
    CTFR - 04.03.18.02.10.00 - Sheila A. Berta (UnaPibaGeek)
------------------------------------------------------------------------------
"""

## # LIBRARIES # ##
import re
import requests

## # CONTEXT VARIABLES # ##
version = 1.2

## # MAIN FUNCTIONS # ##

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--input', type=str, help="Input file")
    group.add_argument('-d', '--domain', type=str, help="Target domain.")
    parser.add_argument('-o', '--output', type=str, help="Output file.")
    return parser.parse_args()

def banner():
    global version
    b = '''
          ____ _____ _____ ____  
         / ___|_   _|  ___|  _ \ 
        | |     | | | |_  | |_) |
        | |___  | | |  _| |  _ < 
         \____| |_| |_|   |_| \_\\
    
     Version {v} - Hey don't miss AXFR!
    Made by Sheila A. Berta (UnaPibaGeek)
    '''.format(v=version)
    print(b)
    
def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
    with open(output_file,"a") as f:
        f.write(subdomain + '\n')
        f.close()

def main():
    args = parse_args()
    targets = []
    
    subdomains = []
    if args.domain != None:
        target = clear_url(args.domain)
    output = args.output

    input_file = args.input

    if input_file != None:
        with open(input_file) as my_file:
            for line in my_file:
                targets.append(line)
        targets = [x.strip() for x in targets]
    else:
        targets.append(target)

        for target in targets:
            print("Target: " + target)
        req = requests.get("https://crt.sh/?O={d}&output=json".format(d=target))

        if req.status_code != 200:
            print("[X] Information not available!") 
            exit(1)

        for (key,value) in enumerate(req.json()):
            subdomains.append(value['common_name'])

    
    #print("\n[!] ---- TARGET: {d} ---- [!] \n".format(d=target))

    subdomains = sorted(set(subdomains))

    for subdomain in subdomains:
        print("{s}".format(s=subdomain))
        if output is not None:
            save_subdomains(subdomain,output)

    print("\n\n[!]  Done. Have a nice day! ;).")


main()
    
