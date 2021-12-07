##Step1

increased = []
raw =[]

with(open('depth_dataset.txt', 'r')) as f:
    for line in f:
        raw.append(int(line.strip()))

prev=0
for i,item in enumerate(raw):
    if item>prev:
        increased.append(item)
    prev = item

print(len(increased))

##step2