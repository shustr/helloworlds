print("\n Select option by number or press q to quit...")
ans=True
while ans:
    print ("""
    1. Selection one
    2. Selection two
    3. Selection three
    """)
    ans=raw_input("Choose option: ")

    if ans == "1":
        print("\n you've selected ONE")
    elif ans == "2":
        print("\n you've selected TWO")
    elif ans == "3":
        print("\n you've selected THREE")
    elif ans == "q":
        print("\n quit")
        ans = None
    else:
        print("\n try again")
