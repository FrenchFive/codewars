def get_count(sentence):
    listsen = list(sentence)
    vowels = ['a','e','i','o','u']
    total = 0
    for i in range(len(vowels)):
        total+= listsen.count(vowels[i])
    return(total)

test = "hello world" #should output 3
print(get_count(test))