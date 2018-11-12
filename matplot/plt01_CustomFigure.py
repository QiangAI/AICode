import matplotlib.pyplot as plt
from matplotlib.figure import Figure
#定制Figure
class MyFigure(Figure):
    def __init__(self, *args, figtitle='Figure', **kwargs):
        super().__init__(*args, **kwargs)
        self.text(0.5, 0.95, figtitle, ha='center')

fig = plt.figure(FigureClass=MyFigure, figtitle='my title')
ax = fig.subplots()
ax.plot([1, 2, 3])

plt.show()