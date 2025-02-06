# def mutation(s,position,char):
#     pass
# s = input()
# position,char = input().split() #['5','k']
# mutation(s,int(position),char)

#hacker rank
def mutate_string(string, position, character):
    li = list(s)
    li[position] = character
    res = ''.join(li)
    return res

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)