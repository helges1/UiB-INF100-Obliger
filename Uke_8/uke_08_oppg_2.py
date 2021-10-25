import math

def pearson_corr(x, y):

  mean_x = sum(x)/len(x)
  mean_y = sum(y)/len(y)

  dx = [i - mean_x for i in x]
  dy = [i - mean_y for i in y]

  dxdy = [a * b for a, b in zip(dx, dy)]
  sum_dxdy = sum(dxdy)

  x_square = [i**2 for i in dx]
  y_square = [i**2 for i in dy]

  sum_x_square = sum(x_square)
  sum_y_square = sum(y_square)

  sqr_dx2dy2 = math.sqrt(sum_x_square * sum_y_square)

  r = sum_dxdy / sqr_dx2dy2

  return r

x1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2_ls = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

print(pearson_corr(x1_ls, y1_ls))
print(pearson_corr(x1_ls, y2_ls))


