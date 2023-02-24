import matplotlib.pyplot as plt
def plots(all_nmax, all_proportions, log_scale=True):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    if log_scale:
        plt.xscale("log")
        plt.yscale("log")

