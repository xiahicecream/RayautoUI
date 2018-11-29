import os
path = 'project-path'
for prefix, dirs, files in os.walk('D:\web_automatic'):
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            os.remove(filename)