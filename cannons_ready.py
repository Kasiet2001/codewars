def cannons_ready(gunners):
    ready = 0
    for i in gunners:
        if gunners[i] != 'nay':
            ready += 1
    return ('Fire!' if ready == len(gunners) else 'Shiver me timbers!')
print(cannons_ready({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}))