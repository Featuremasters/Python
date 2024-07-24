import colorgram
need=[]
colors=colorgram.extract('selectcolor.jpg', 30)
for i in colors:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    ncolor=(r,g,b)
    need.append(ncolor)
print(need)