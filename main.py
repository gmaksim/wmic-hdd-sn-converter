import re

whats_decode = input('enter wmic hdd sn: ')
dec_res = bytearray.fromhex(whats_decode).decode()
print('decode', dec_res)

wd_hdd = dec_res.startswith('WD')
if wd_hdd is True:
    dec_res = dec_res.replace(' ', '')
    dec_res = dec_res.replace('-', '')
    dec_cut = dec_res[2:]  # cut WD (correct data)
    dec_len = len(dec_cut)  # 12

    count = 0
    ltr1 = 0
    ltr2 = 2
    dec_changed = []

    for count in range(dec_len):
        if ltr1 >= dec_len:
            break
        two_ltr = dec_cut[ltr1:ltr2:1]
        a = two_ltr[0]
        b = two_ltr[1]
        mix_res = a, b = b, a
        dec_changed.append(mix_res)
        ltr1 += 2
        ltr2 += 2

    # later need make normal cutter
    dec_changed = str(dec_changed).strip('[]')
    dec_changed = re.sub(r'\(', '', dec_changed)
    dec_changed = re.sub(r'\)', '', dec_changed)
    dec_changed = re.sub(r'\'', '', dec_changed)
    dec_changed = re.sub(r'\,', '', dec_changed)
    dec_changed = re.sub(r' ', '', dec_changed)
    dec_final = 'WD' + dec_changed
    print('final', dec_final)
else:
    dec_len = len(dec_res)  # 12

    count = 0
    ltr1 = 0
    ltr2 = 2
    dec_changed = []

    for count in range(dec_len):
        if ltr1 >= dec_len:
            break
        two_ltr = dec_res[ltr1:ltr2:1]
        a = two_ltr[0]
        b = two_ltr[1]
        mix_res = a, b = b, a
        dec_changed.append(mix_res)
        ltr1 += 2
        ltr2 += 2

    # later need make normal cutter
    dec_changed = str(dec_changed).strip('[]')
    dec_changed = re.sub(r'\(', '', dec_changed)
    dec_changed = re.sub(r'\)', '', dec_changed)
    dec_changed = re.sub(r'\'', '', dec_changed)
    dec_changed = re.sub(r'\,', '', dec_changed)
    dec_changed = re.sub(r' ', '', dec_changed)
    print('final', dec_changed)