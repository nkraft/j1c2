import os


def get_authors_filename(venue):
    return os.path.join('authors', venue + '.txt')


def get_authors(filename):
    authors = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            authors.add(line.rstrip())
    return authors


fse_authors = get_authors(get_authors_filename('fse'))
icse_authors = get_authors(get_authors_filename('icse'))
software_authors = get_authors(get_authors_filename('software'))

print('|fse| =', len(fse_authors))
print('|icse| =', len(icse_authors))
print('|software| =', len(software_authors))
print()
print('|fse but not software| =', len(fse_authors - software_authors))
print('|software but not fse| =', len(software_authors - fse_authors))
print('|both fse and software| =', len(fse_authors & software_authors))
print('|fse or software but not both| =', len(fse_authors ^ software_authors))
print()
print('|icse but not software| =', len(icse_authors - software_authors))
print('|software but not icse| =', len(software_authors - icse_authors))
print('|both icse and software| =', len(icse_authors & software_authors))
print('|icse or software but not both| =', len(icse_authors ^ software_authors))

