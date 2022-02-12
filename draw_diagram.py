import matplotlib.pyplot as plt

def draw(data, output_png, diagram_type, xlabel, ylabel, titel, xsize, ysize):
    names = list(data.keys())
    values = list(data.values())

    # scatter, bar, ...
    if diagram_type == "scatter":
        fig, axs = plt.subplots()
        axs.scatter(names, values)
    if diagram_type == "bar":
        fig, axs = plt.subplots()
        axs.bar(names, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titel)

    # save as png
    fig = plt.gcf()
    fig.set_size_inches(xsize, ysize)
    fig.savefig(output_png, dpi=100)
