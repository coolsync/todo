# movie_name = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
movie_name = ['j加勒比海盗','h骇客帝国','d第一滴血','z指环王','h霍比特人','s速度与激情']


print('------删除之前------')
for tmp_name in movie_name:
    print(tmp_name)

# del movie_name[2]
# movie_name.pop()
movie_name.remove('z指环王')
# movie_name.reverse()
movie_name.sort(reverse=True)

print('------删除之后------')
for tmp_name in movie_name:
    print(tmp_name)