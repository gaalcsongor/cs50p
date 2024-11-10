import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.fullmatch(r"(([1-9])|(1[012])):?(\d\d)? ([AP])M to (([1-9])|(1[012])):?(\d\d)? ([AP])M", s):
        first_hour = int(match.group(1))
        second_hour = int(match.group(6))
        
        if match.group(4) != None:
            if int(match.group(4)) >= 60:
                raise ValueError
            first_min = int(match.group(4))
        else:
            first_min = 0
            
        if match.group(9) != None:
            if int(match.group(9)) >= 60:
                raise ValueError
            second_min = int(match.group(9))
        else:
            second_min = 0
        
        # first_hour + first_min
        if match.group(5) == "A":
            if first_hour == 12:
                converted_first = f"00:{first_min:02}"
            elif first_hour >= 1 and first_hour < 12:
                converted_first = f"{first_hour:02}:{first_min:02}"
            else:
                raise ValueError
        elif match.group(5) == "P":
            if first_hour == 12:
                converted_first = f"{first_hour:02}:{first_min:02}"
            elif first_hour >= 1 and first_hour < 12:
                first_hour += 12
                converted_first = f"{first_hour:02}:{first_min:02}"
            else:
                raise ValueError
        # second_hour + second_min
        if match.group(10) == "A":
            if second_hour == 12:
                converted_second = f"00:{second_min:02}"
            elif second_hour >= 1 and second_hour < 12:
                converted_second = f"{second_hour:02}:{second_min:02}"
            else:
                raise ValueError
        elif match.group(10) == "P":
            if second_hour == 12:
                converted_second = f"{second_hour:02}:{second_min:02}"
            elif second_hour >= 1 and second_hour < 12:
                second_hour += 12
                converted_second = f"{second_hour:02}:{second_min:02}"
            else:
                raise ValueError
        return f"{converted_first} to {converted_second}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()