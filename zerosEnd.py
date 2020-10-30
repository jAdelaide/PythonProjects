array = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
moved = []
zeroes = 0

for item in array:
            # Counts 0 and 0.0 as zero but not False
    if item == 0 and type(item) == int or type(item) == float:
        zeroes +=1
    else:
        moved.append(item)

while zeroes > 0:
    moved.append(0)
    zeroes -=1
        
print(moved)
