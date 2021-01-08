#  https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        string = input().strip().split(" ")
        if string[0] == "insert":
            result.insert(int(string[1]), int(string[2]))
        elif string[0] == "append":
            result.append(int(string[1]))
        elif string[0] == "remove":
            result.remove(int(string[1]))
        elif string[0] == "sort":
            result.sort()
        elif string[0] == "pop":
            result.pop()
        elif string[0] == "reverse":
            result.reverse()
        elif string[0] == "print":
            print(result)
