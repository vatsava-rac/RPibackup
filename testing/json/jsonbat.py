import json

stack = {
    "stack1" : [
        {
            "dock1" : "RACEA01A001",
            "dock2" : "RACEA01A002",
            "dock3" : "RACEA01A003",
            "dock4" : "RACEA01A004"
            },
        ],
    "stack2" : [
        {
            "dock1" : "RACEA02A001",
            "dock2" : "RACEA01A002",
            "dock3" : "RACEA02A003",
            "dock4" : "RACEA02A004"
            }
        ]
    
    
    }

print(stack)

a = json.dumps(stack,indent = 2)
print(a)

with open("stacks.json", "w") as jos:
    jos.write(a)