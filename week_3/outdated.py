month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    user_date = input("Date: ").strip()

    if len(user_date) <= 10:
        short_list = user_date.split(sep="/")
        # print(short_list)
        if int(short_list[0]) > 12 or int(short_list[1]) > 31:
            continue
        print(f"{short_list[2]}-{int(short_list[0]):02}-{int(short_list[1]):02}")
        break
    else:
        long_list = user_date.split(sep=" ")
        # print(long_list)
        if long_list[0] in month_list:
            long_list[0] = int(month_list.index(long_list[0])) + 1
            long_list[1] = long_list[1].removesuffix(",")
            if long_list[0] > 12 or int(long_list[1]) > 31:
                continue
            print(f"{long_list[2]}-{int(long_list[0]):02}-{int(long_list[1]):02}")
            break
        
        