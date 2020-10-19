import pygame
import math
from queue import PriorityQueue

WIDTH=800
WIN=pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot: 
    def __init__(self,row,col,width,total_row):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.neighbours=[]
        self.width=width
        self.total_row=total_row

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color==RED

    def is_open(self):
        return self.color==GREEN
    
    def is_barrier(self):
        return self.color==BLACK
    
    def is_start(self):
        return self.color==ORANGE
    
    def is_end(self):
        return self.color==TURQUOISE

    def reset(self):
        self.color=WHITE

    
    def make_closed(self):
        self.color=RED

    def make_open(self):
        self.color=GREEN
    
    def make_barrier(self):
        self.color=BLACK
    
    def make_start(self):
        
        self.color=ORANGE
    
    def make_end(self):
        self.color=TURQUOISE

    def make_path(self):
        self.color=PURPLE
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
        

    def update_neighbours(self,grid):
        self.neighbours=[] 
        if self.row<self.total_row-1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbours.append(grid[self.row+1][self.col])
        
        if self.row>0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbours.append(grid[self.row-1][self.col])
        
        if self.col<self.total_row-1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbours.append(grid[self.row][self.col+1])
        
        if self.col>0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbours.append(grid[self.row][self.col-1])
    
    def __lt__(self,other):
        return False


def heuristic(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)


def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def make_grid(rows,width):
    grid=[]
    size=width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,size,rows)
            grid[i].append(spot)

    return grid

def draw_grid(win,rows,width):
    size = width//rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*size),(width,i*size))
        for j in range(rows):
            pygame.draw.line(win,GREY,(j*size,0),(j*size,width))


def draw(win,grid,rows,width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)  

    draw_grid(win,rows,width)
    pygame.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width//rows
    y,x = pos
    
    row = y//gap
    col = x//gap

    return row,col

def algorithm(draw,grid,start,end):
    print('chiryo algorthm')
    count = 0
    node_param = PriorityQueue()
    node_param.put((0,count,start))
    came_from ={}
    g = {spot:float('inf') for row in grid for spot in row}
    g[start] = 0
    f = {spot:float('inf') for row in grid for spot in row}
    f[start] = heuristic(start.get_pos(),end.get_pos())

    node_param_hash = {start}

    while not node_param.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = node_param.get()[2]
        node_param_hash.remove(current)

        if current ==end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbour in current.neighbours:
            temp_g = g[current]+1
            if temp_g<g[neighbour]:
                came_from[neighbour] = current
                g[neighbour]=temp_g
                f[neighbour] = temp_g + heuristic(neighbour.get_pos(),end.get_pos())
                if neighbour not in node_param_hash:
                    count+=1
                    node_param.put((f[neighbour],count,neighbour))
                    node_param_hash.add(neighbour)
                    neighbour.make_open()
        
        draw()

        if current!=start:
            current.make_closed()
    
    return False


def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS,width)

    start  = None
    end = None

    run = True
    started = False

    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                # print('left mouse')
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                spot = grid[row][col]
                if not start and spot!=end:
                    
                    start = spot
                    start.make_start()
                elif not end and spot!=start:
                    end = spot
                    end.make_end()
                elif spot!=end and spot!=start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                # print('right mouse')
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                spot = grid[row][col]
                spot.reset()
                if spot==start:
                    start=None
                elif spot==end:
                    end=None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # print('space key ayo')
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    algorithm(lambda : draw(win,grid,ROWS,width),grid,start,end)
            
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS,width)

    
    
    
    pygame.quit()

   

main(WIN,WIDTH) 