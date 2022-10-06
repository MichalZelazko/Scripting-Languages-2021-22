colors_en = ('red','green','blue')
colors_fr = ('rouge','vert','bleu')
for i,en in enumerate(colors_en):
    print(en,colors_fr[i])

for en,fr in zip(colors_en, colors_fr):
    print(en,fr)
