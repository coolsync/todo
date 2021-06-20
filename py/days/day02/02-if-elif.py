
# if elif struct
""" 
需求：
1. 成绩⼤于等于90 ，输出优秀
2. 成绩⼤于等于80，⼩于90，输出良好
3. 成绩⼤于等于60，⼩于80，输出及格
4. ⼩于60，输出不及格
"""

score = 69

if score >= 90:
    print('优秀')
elif score >= 80 and score < 90:
    print('良好')
elif score >= 60 and score < 80:
    print('及格')
else:
    print('不及格')