licenses = []

while True:
    command = input().split()

    if command[0] == "exit":
        break

    if command[0] == "add":
        licenses.append({
            "license_plate": command[1].replace("\"", ""),
            "make": command[2].replace("\"", ""),
            "year": int(command[3])
        })

    if command[0] == "view":
        for i in licenses:
            if command[1].replace("\"", "") == i["license_plate"]:
                print(f"{i["make"]} ({i["year"]})")
