def calculate_love_score(name1 , name2):
    # Occurance of TRUE
    count_1=0
    for char in name1.upper():
        if (char == 'T') or( char ==  'R') or (char ==  'U') or (char == 'E'):
            count_1 += 1
    for char in name2.upper():
        if (char == 'T') or( char ==  'R') or (char ==  'U') or (char == 'E'):
            count_1 += 1
    # print(count_1)

    # Occurance of LOVE
    count_2=0
    for char in name1.upper():
        if (char == 'L') or( char ==  'O') or (char ==  'V') or (char == 'E'):
            count_2 += 1
    for char in name2.upper():
        if (char == 'L') or( char ==  'O') or (char ==  'V') or (char == 'E'):
            count_2 += 1
    # print(count_2)
    love_score=str(count_1) + str(count_2)

    print(f"The love score should be {love_score}")


calculate_love_score("Kanye West", "Kim Kardashian")



