from collections import Counter
def climbingLeaderboard(ranked, player):
    currentrank = len(set(ranked))
    score_index = 0
    highscore_index = len(ranked) - 1
    while score_index != len(player):
        while player[score_index] > ranked[highscore_index] and highscore_index > -1:
            highscore_index -= 1
            if ranked[highscore_index] != ranked[highscore_index + 1]:
                currentrank -= 1
        if player[score_index] == ranked[highscore_index]:
            yield currentrank
        else:
            yield currentrank + 1
        score_index += 1

    # ranked = set(ranked)
    # ranked = sorted(ranked, reverse=True)
    # dict = {key: value for key, value in enumerate(ranked,start=1)}
    # for i in range(player):
    #     if player[i] in dict:
    #         return dict[i]

    # Write your code here

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(*result)
