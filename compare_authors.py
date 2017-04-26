import os


fse_authors = set()
with open(os.path.join('authors', 'fse.txt'), 'r', encoding='utf-8') as fse:
    for line in fse:
        fse_authors.add(line.rstrip())

software_authors = set()
with open(os.path.join('authors', 'software.txt'), 'r', encoding='utf-8') as software:
    for line in software:
        software_authors.add(line.rstrip())

print('|fse| =', len(fse_authors))
print('|software| =', len(software_authors))
print('|fse but not software| =', len(fse_authors - software_authors))
print('|software but not fse| =', len(software_authors - fse_authors))
print('|both fse and software| =', len(fse_authors & software_authors))
print('|fse or software but not both| =', len(fse_authors ^ software_authors))

