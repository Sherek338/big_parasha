def get_close(grid, pos, row_count, col_count) -> list:
    posx, posy = pos
    close_cells = []
    
    dots = [{"x": posx - 1, "y": posy},
            {"x": posx + 1, "y": posy},
            {"x": posx - 1, "y": posy - 1},
            {"x": posx, "y": posy - 1},
            {"x": posx + 1, "y": posy - 1},
            {"x": posx - 1, "y": posy + 1},
            {"x": posx, "y": posy + 1},
            {"x": posx + 1, "y": posy + 1},]
    
    for dot in dots:
        if dot["x"] >= 0 and dot["x"] < col_count and dot["y"] >= 0 and dot["y"] < row_count:
            close_cells.append(grid[dot["y"]][dot["x"]])
            
    return close_cells

def get_col():
    pass
