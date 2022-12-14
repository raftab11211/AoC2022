import os
import json
file = open(os.path.join(os.getcwd(), "AoC2022/Day7/example_input.txt"))
data = file.read().strip()
lines = [x.strip() for x in data.split('\n')]

file_system = { "/": { 
    "directory":"a","directories": [
            {"directory":"b","files":[{"name":"file1", "size":100}, {"name":"file2","size":200}], 
                "directories":[{"directory":"c"}]}, 
            {"directory":"d", "file":[{"name":"file3","size":300}, {"name":"file4", "size":400}]}
        ]
    }
}

jsonString = json.dumps(file_system, indent=4)
print(jsonString)