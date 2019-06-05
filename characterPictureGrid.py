grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

####solution for just this grid####
#for i in range(6):
 #   print()
  #  for j in range(8):
   #     print(grid[j][i], end='')


#redone solution that works for all sizes
cols = len(grid[0])
rows = len(grid)

for c in range(cols):
    for r in range(rows):
        print(grid[r][c], end='')
    print()
