
import random, re
a=[str((x,y)) for x in range(1,9) for y in range(1,13)]
coordinates = a.copy()

def get_coordinate(n):
    if n>len(coordinates):
        print('数字超过了上限!')
        return
    random.shuffle(coordinates)
    b=[]
    for x in range(n):
        b.append(coordinates.pop())
    print(b)

def add_coordinate(coor):
    if coor: coordinates.extend(coor)

def refresh():
    coordinates=a.copy()

def enter_command():
    cmd=input('请输入指令(1是get, 2是add, 3是refresh, 4是随机商品, 5是check, 6是quit): ')
    return cmd

def main():
    global coordinates
    pat=re.compile(r'\(\d+,\s*\d+\)')
    while True:
        try:
            cmd=enter_command()
            if cmd=='1':
                n=int(input('请输入提取坐标的个数: '))
                get_coordinate(n)
                print('')
            elif cmd=='2':
                n = input('请输入要加入的坐标(例:(1, 2), 最好加空格): ')
                b=pat.findall(n)
                add_coordinate(b)
                print('')
            elif cmd=='3':
                coordinates = a.copy()
                print('')
            elif cmd=='4':
                s=int(input('请输入商品个数: '))
                k=[]
                while len(k)<s:
                    t=random.randint(1,15)
                    while t in k:
                        t = random.randint(1, 15)
                    k.append(t)
                print(k, end='\n')
            elif cmd=='5':
                print(len(coordinates))
            elif cmd=='6':
                print('已退出', end='\n')
                break
        except TypeError:
            print('请输入正确的内容!', end='\n')
        except IndexError:
            print('请输入正确范围内的数字!', end='\n')


if __name__ == '__main__': main()