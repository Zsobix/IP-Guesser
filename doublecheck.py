with open('ips.txt', 'r') as dcheck:
    list = dcheck.read().split('\n')
    dcheck.close()
for i in range(len(list)):
    ip = list[i]
    list[i] = ''
    if ip in list:
        continue
    else:
        list[i] = ip
print('Done! Writing to file...')
with open('ips.txt', 'w') as final:
    final.write(f"{list[0]}\n")
    final.close()
with open('ips.txt', 'a') as final2:
    for count in range(len(list)):
        if count == 0:
            continue
        else:
            final2.write(f'{list[count]}\n')