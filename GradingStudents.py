def gradingStudents(grades):
    n = len(grades)
    for i in range(0, n):
        z = grades[i] 
        if z >= 38:
            x = z % 5
            if z % 5 > 2:
                z+=(5-x)
                grades[i] = z
            else:
                continue    
    return grades 
