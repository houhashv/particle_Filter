class Ploter:

    def __init__(self, figure=None, plt=None):

        self.figure = figure
        self.plt = None

    def config_plot(self, plt, lim):

        plt.xlim((0, lim))
        plt.ylim((0, lim))
        plt.xticks([x for x in range(0, lim, 10)])
        plt.yticks([x for x in range(0, lim, 10)])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("robot world")
        return plt