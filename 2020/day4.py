with open("./day4input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

passports = []
passport = {}
for i in range(len(lines)):
    if lines[i] == "":
        passports.append(passport)
        passport = {}
    else:
        split = lines[i].split(" ")
        for item in split:
            key = item.split(":")[0]
            value = item.split(":")[1]
            passport[key] = value
passports.append(passport)

validity_requirements = {
    "byr": {
        "len": 4,
        "min": 1920,
        "max": 2002
    },
    "iyr": {
        "len": 4,
        "min": 2010,
        "max": 2020
    },
    "eyr": {
        "len": 4,
        "min": 2020,
        "max": 2030
    },
    "hgt": {
        "contains": ["cm", "in"],
        "min_in": 59,
        "min_cm": 150,
        "max_in": 76,
        "max_cm": 193
    },
    "hcl": {
        "len": 7,
        "start": "#",
        "allowedchars": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    },
    "ecl": {
        "allowed": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    },
    "pid": {
        "len": 9,
        "allowedchars": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    }
}
    
valid_passports = 0

for passport in passports:
    valid = True
    for k, v in validity_requirements.items():
        if k not in passport.keys():
            valid = False
            break
        else:
            if "len" in v.keys():
                if len(passport[k]) != v["len"]:
                    valid = False
                    break
            if "min" in v.keys():
                if int(passport[k]) < v["min"]:
                    valid = False
                    break
            if "max" in v.keys():
                if int(passport[k]) > v["max"]:
                    valid = False
                    break
            if "contains" in v.keys():
                con_count = 0
                for con in v["contains"]:
                    if con in passport[k]:
                        try:
                            if int(passport[k].split(con)[0]) < v["min_{}".format(con)]:
                                valid = False
                                break
                            if int(passport[k].split(con)[0]) > v["max_{}".format(con)]:
                                valid = False
                                break
                        except:
                            valid = False
                            break
                    else:
                        con_count += 1
                if con_count == 2:
                    valid = False
                    break
            if "allowedchars" in v.keys():
                if "start" in v.keys():
                    if passport[k][0] != v["start"]:
                        valid = False
                        break
                    string_to_check = passport[k][1:]
                else:
                    string_to_check = passport[k]
                for ch in string_to_check:
                    if ch not in v["allowedchars"]:
                        valid = False
                        break
                if not valid:
                    break
            if "allowed" in v.keys():
                if passport[k] not in v["allowed"]:
                    valid = False
                    break
    if valid: 
        valid_passports += 1

print(valid_passports)