def calculate_love_score(name1, name2):
    
    name = name1 + name2
    name_lower = name.lower()
    
    t = name_lower.count("t")

    r = name_lower.count("r")

    u = name_lower.count("u") 

    e = name_lower.count("e") 

    true_lower = t + r + u + e

    l = name_lower.count("l") 

    o = name_lower.count("o") 

    v = name_lower.count("v") 

    e = name_lower.count("e") 
    
    love = l + o + v + e
    
    score = int(str(true_lower) + str(love))
    
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")
    
    