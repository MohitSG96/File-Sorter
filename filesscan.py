from pathlib import Path
from tabulate import tabulate

userPath = r'C:/Users/Mohit/OneDrive/Desktop/'
moviePath = r'E:/Movies'

path = Path(userPath)
count = 0
# result = []
# for p in path.rglob("*.pdf"):
#     result.append(p.suffix)
#     print(p.name, "\t\t\t", "{0:.2f}".format((p.stat().st_size)/1024), "KB")

# # print(result[0])
# # print(tabulate(result, headers=['Suffix', 'Size']))
# # result = dict.fromkeys(result)


def get_suffix_with_total():
    result = []
    seen = {}
    dupes = []
    for x in path.rglob('*.*'):
        if x.suffix not in seen:
            seen[x.suffix] = 1
        else:
            if seen[x.suffix] == 1:
                dupes.append(x.suffix)
            seen[x.suffix] += 1

    for i, x in enumerate(dupes):
        result.append([dupes[i], seen[dupes[i]]])

    return sorted(result, key=lambda k: float(k[1]))


def get_files_stat():
    files = []
    for p in path.rglob("*.*"):
        files.append([p.name, "{0:.2f}".format(
            ((p.stat().st_size)/1024))+"KB"])

    return files


print(tabulate(get_suffix_with_total(), headers=['Suffix', 'total']))
print(tabulate(get_files_stat(), headers=['Name', 'Size']))
