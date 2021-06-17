sps = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
chis = [sps[num] for num in range(1, len(sps)) if sps[num] > sps[num - 1]]
print(chis)