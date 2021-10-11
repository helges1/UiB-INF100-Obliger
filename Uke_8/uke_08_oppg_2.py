import math

def pearson_corr(x,y):

    #1
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)

    #2
    dx = sum(x) - mean_x
    dy = sum(y) - mean_y

    #3
    sum_dxdy = dx * dy

    #4
    dx2 = (sum(x) - mean_x)**2
    dy2 = (sum(y) - mean_y)**2

    #5
    sqr_dx2dy2 = math.sqrt(((dx2 - mean_x) * (dy2 - mean_y)))

    #6
    altSammen = sum_dxdy / sqr_dx2dy2

    return altSammen




x1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2_ls = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

print(pearson_corr(x1_ls, y1_ls))
print(pearson_corr(x1_ls, y2_ls))
