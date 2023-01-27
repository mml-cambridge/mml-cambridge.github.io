import bibtexparser


template = '''---
author: "{}"
title: "{}"
date: {}-{:02d}-01
tags: ["publication"]
---

'''

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


with open('pubs.bib') as file:

    parser = bibtexparser.bparser.BibTexParser()
    parser.customization = bibtexparser.customization.convert_to_unicode
    bibliography = bibtexparser.load(file, parser=parser)

    for k, v in bibliography.entries_dict.items():

        v.setdefault('month', "jan")

        with open(f'content/posts/{k}.md', 'w') as out:
            print(template.format(v["author"], v["title"], v["year"], month_string_to_number(v["month"])), file=out)

            if 'doi' in v:
                print(f"DOI: [{v['doi']}](https://doi.org/{v['doi']})", file=out)

            if 'abstract' in v:
                print(f"##Abstract\n{v['abstract']}", file=out)
       

    # with open(f"content/publication/{}")


   

# print(bib_database.entries)

# @article{Zhu2019,
#   doi       = {10.3390/s19051191},
#   url       = {https://doi.org/10.3390/s19051191},
#   year      = {2019},
#   month     = mar,
#   publisher = {{MDPI} {AG}},
#   volume    = {19},
#   number    = {5},
#   pages     = {1191},
#   author    = {Hao Zhu and Bin Guo and Ke Zou and Yongfu Li and Ka-Veng Yuen and Lyudmila Mihaylova and Henry Leung},
#   title     = {A Review of Point Set Registration: From Pairwise Registration to Groupwise Registration},
#   journal   = {Sensors}
# }