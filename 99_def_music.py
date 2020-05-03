#definition for music_func goes here
def music_func(a="Beatles", b="Classic Rock", c="Freddie"):
    if a is None or b is None or c is None:
        print("The best kind of music is Classic Rock")
        print("The best music group is The Beatles")
        print("The best lead vocalist is Freddie Mercury")
    else:
        print("The best kind of music is",a)
        print("The best music group is",b)
        print("The best lead vocalist is",c)
    return
def main():
    music, group, singer = input().split(',')
    music_func(music, group, singer)
    music_func() #This is suppose to print the first if-statements 
main()