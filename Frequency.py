txt = {'Hello' : 2, 'guys' : 2, ':)' : 1}
print('Da text iz ' + str(txt))

k = 2
res = 0

for tim in txt:
    if txt[tim] == k:
        res = res + 1

print('Da frequency of k iz ' + str(res) + '.')
