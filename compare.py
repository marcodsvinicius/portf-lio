import difflib

file1_path = "index.html"
file2_path = "index.jhtml"

with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

diff = difflib.unified_diff(
    f1_lines, f2_lines,
    fromfile='index.html',
    tofile='index.jhtml',
    lineterm=''
)

diff_list = list(diff)
if not diff_list:
    print("Files are identical!")
else:
    print(f"Found {len(diff_list)} diff lines:")
    for line in diff_list:
        print(line)
