n = int(input())
n_dist = list(map(int, input().split()))
m = int(input())
m_dist = list(map(int, input().split()))
dist_to_vills = sorted(zip(range(n), n_dist), key=lambda x: x[1])
dist_to_vaults = sorted(zip(range(m), m_dist), key=lambda x: x[1])
res = [-1 for _ in range(n)]
last_vault_idx = 0
for i in range(n):
    dist_to_village = dist_to_vills[i][1]
    village_idx = dist_to_vills[i][0]
    min_dist = abs(dist_to_village - dist_to_vaults[last_vault_idx][1])
    for j in range(last_vault_idx, m):
        d = abs(dist_to_vaults[j][1] - dist_to_village)
        if d <= min_dist:
            min_dist = d
            last_vault_idx = j
            res[village_idx] = dist_to_vaults[j][0] + 1
        else:
            break
print(*res)
