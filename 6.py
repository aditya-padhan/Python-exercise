my_list = ['a','s','d','f','g','h','j','k','l','e','y','v','n']
my_dict = {"a":1,"b":2,"d":3,"g":6,"s":9,"h":6,"x":7}
my_key = ['d','r','h','e','f','s','j','k','x','g']

for i in my_key:
    if i in my_list and i in my_dict:
        print(i,' : ',my_dict.get(i))
