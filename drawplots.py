import matplotlib.pyplot as plt
import pandas as pd
import os

class Plots:
    def draw_plots(self, file):
        paths = []
        df = pd.read_json(file)
        plt.plot(df['gt_corners'], df['rb_corners'])
        plt.xlabel('gt_corners')
        plt.ylabel('rb_corners')
        path = 'plots'
        paths.append(os.path.join(path, 'test.png'))
        plt.savefig(os.path.join(path, 'test.png'), bbox_inches='tight')
        return paths
    
p = Plots()
print(p.draw_plots('deviation.json'))

