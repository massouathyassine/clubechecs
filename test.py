list_score = [(1,1),(2,3),(3,7),(4,8),(5,8),(6,13),(7,14),(8,15)]
list_rank = [(1,12),(2,17),(3,8),(4,18),(5,17),(6,88),(7,15),(8,24)]

list1 = sorted(
                list_score, key=lambda colonnes: colonnes[1], reverse=True
            )
print('list par score: ' , list1)
print('list avec classement : ' , list_rank)

list_players_ranked = []
while len(list1) > 1:
    if list1[0][1] == list1[1][1]:
        list_players_for_rank = []
        while True:
            try:
                if (
                        list1[0][1] ==
                        list1[1][1]
                ):
                    list_players_for_rank.append(
                        list1[0][0]
                    )
                    list1.pop(0)
                else:
                    list_players_for_rank.append(
                        list1[0][0]
                    )
                    list1.pop(0)
                    break
            except IndexError:
                list_players_for_rank.append(
                    list1[0][0]
                )
                list1.pop(0)
                break
        print('list score egal',list_players_for_rank)
        temp_list_players = []
        for i in range(len(list_players_for_rank)):
            p_data = (
                list_rank[list_players_for_rank[i]-1][0],
                list_rank[list_players_for_rank[i]-1][1]
            )
            temp_list_players.append(p_data)
            temp_list_players_ranked = sorted(
                temp_list_players, key=lambda colonnes: colonnes[1],
                reverse=False
            )
        print('temp player avec rank',temp_list_players)
        print('temp player ranked',temp_list_players_ranked)
        for i in range(len(temp_list_players_ranked)):
            list_players_ranked.append(
                temp_list_players_ranked[0][0]
            )
            temp_list_players_ranked.pop(0)
        print(temp_list_players_ranked)
    else:
        list_players_ranked.append(list1[0][0])
        list1.pop(0)
    print('list 1 : ',list1)


try:
    list_players_ranked.append(list1[0][0])
    list1.pop(0)
except IndexError:
    pass

print('liste final :',list_players_ranked)