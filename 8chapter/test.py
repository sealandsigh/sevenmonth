def damage(skill1,skill2=1):
    skill1 = skill1 + 10
    skill2 = skill2 + 6
    return skill1,skill2

skill_1,skill_2 = damage(3,skill2=3)
print(skill_1,skill_2)
print('签卡')
