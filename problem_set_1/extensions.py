'''
file = input("File name: ").strip()

mime_types = ('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')

if file.endwith(mime_types) == '.gif':
    print("image/gif")
else:
    print("application/octet-stream")
'''

file = input("File name: ").strip().lower()

mime_types = ('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')

# Check if the file ends with any of the provided mime_types
for mime_type in mime_types:
    if file.endswith(mime_type):
        if mime_type == '.gif':
            print("image/gif")
        elif mime_type == '.jpg' or mime_type == '.jpeg':
            print("image/jpeg")
        elif mime_type == '.png':
            print("image/png")
        elif mime_type == '.pdf':
            print("application/pdf")
        elif mime_type == '.txt':
            print("text/plain")
        elif mime_type == '.zip':
            print("application/zip")
        break
else:
    print("application/octet-stream")
