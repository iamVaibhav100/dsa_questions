from itertools import combinations

def acmTeam(topic):
    arr = []
    teams = list(combinations(range(1,n+1),2))
    for i in range(len(teams)):
        sum = int(topic[teams[i][0]-1])+int(topic[teams[i][1]-1])
        know_sub = str(sum)
        unknown = len(know_sub.split('0'))-1
        knows = m - unknown
        arr.append(knows)
    return [max(arr), arr.count(max(arr))]

    # Write your code here

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print(result)
