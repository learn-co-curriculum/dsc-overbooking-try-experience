for character in ('$$', '$'):
    file_name = 'p-7-widget.md'
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    sep = character
    sep_clean = sep + " "
    data = data.replace(sep_clean, sep)

    if r"\begin{align}" in data:
        data.replace(r'\begin{align}', '&')

    if r"\end{align}" in data:
        data.replace(r'\end{align}', '&')
    data_split = data.split(sep)
    special_characters = ["\backslash", "\subset", "\subseteq", "\cap", "\cup"]
    for i in range(len(data_split)):
        if i %2 !=0:
            for item in special_characters:
                data_split[i] = data_split[i].replace(item,(' '+item))
            if "prod" in data_split[i]:
                data_split[i] = data_split[i].replace('prod', 'displaystyle\prod')
            
            if "sum" in data_split[i]:
                data_split[i] = data_split[i].replace('prod', 'displaystyle\sum')
            
            if "+" in data_split[i]:
                data_split[i] = data_split[i].replace('+', '%2b')
                
            data_split[i] = ' <img src="https://render.githubusercontent.com/render/math?math='+data_split[i]+'"> '


    # %%
    final = ''.join(data_split)


    # %%
    f = open(file_name, 'w')
    f.write(final)
    f.close()