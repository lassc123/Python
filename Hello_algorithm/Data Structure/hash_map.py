# 初始化哈希表
hmap:dict ={}

# 添加操作
# 在哈希表中添加键值对（key,value）
hmap[12836] = '小哈'
hmap[15937] = '小啰'
hmap[16750] = '小算'
hmap[13276] = '小法'
hmap[10583] = '小鸭'

# 查询操作
# 向哈希表中输入键key,得到值value
name:str =hmap[15937]

# 删除操作
# 在哈希表中删除键值对（key,value）
hmap.pop(10583)


# 遍历哈希表
# 遍历键值对key->value
for key,value in hmap.items():
    print(key,"->",value)
# 单独遍历键key
for key in hmap.keys():
    print(key)
# 单独遍历值value
for value in hmap.values():
    print(value)