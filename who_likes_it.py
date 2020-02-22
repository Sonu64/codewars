def likes(names):
    new_string = ""
    if len(names)==0:
        return "no one likes this"
    else:
        if len(names)==1:
            return names[0] + " likes this"
        elif len(names)==2:
            return names[0] + " and " + names[1] + " like this"
        elif len(names) == 3:
            return names[0] + ", " + names[1] + " and " + names[2] + " like this"
        else:
            user_one = names[0]
            user_two = names[1]
            rem = len(names) - 2
            return user_one + ", " + user_two + " and " + str(rem) + " others like this"
    return new_string
     



