from header_import import *


class Windy_World(object):
    def __init__(self, action_type, wind_type):
        self.action_type = action_type
        self.wind_action = wind_type
        
        if self.action_type == "regular":
            self.action_space = [0, 1, 2, 3]
        elif self.action_type == "king":
            self.action_space = [0, 1, 2, 3, 4, 5, 6, 7]
        elif self.action_type == "king_zero":
            self.action_space = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            
        self.start = (0, 3)
        self.goal = (7, 3)
        
    def action_type_space(self):
        return self.action_space
        
    def reset(self):
        self.x_position, self.y_position = self.start
        return self.start
    
    def step(self, action):
        self.x_position, self.y_position = self.transition(self.x_position, self.y_position, action)
        if self.x_position == self.goal[0] and self.y_position == self.goal[1]:
            return True, -1, (self.x_position, self.y_position)
        return False, -1, (self.x_position, self.y_position)
        
    def transition(self, x, y, action):
        
        if x in [3, 4, 5, 8]:
            y += 1
        if x in [6, 7]:
            y += 2
            
        
        if self.action_type == "regular":
            if action == 0:
                x -= 1
            elif action == 1:
                y -= 1
            elif action == 2:
                x += 1
            elif action == 3:
                y += 1

        elif self.action_type == "king":
            if action == 0:
                x -= 1
            elif action == 1:
                y -= 1
            elif action == 2:
                x += 1
            elif action == 3:
                y += 1
            elif action == 4:
                x -= 1
                y -= 1
            elif action == 5:
                x -= 1
                y += 1
            elif action == 6:
                x += 1
                y -= 1
            elif action == 7:
                x += 1
                y += 1
                
        elif self.action_type == "king_zero":
            if action == 0:
                x -= 1
            elif action == 1:
                y -= 1
            elif action == 2:
                x += 1
            elif action == 3:
                y += 1
            elif action == 4:
                x -= 1
                y -= 1
            elif action == 5:
                x -= 1
                y += 1
            elif action == 6:
                x += 1
                y -= 1
            elif action == 7:
                x += 1
                y += 1
            elif action == 0:
                x += 0
                y += 0
                
                
        if self.wind_action != "regular":
            prob = random.random()
            
            if prob < 0.33:
                y -= 1
            elif prob < 0.66:
                y = y
            elif prob < 1:
                y += 1
                
        x = np.clip(x, 0, 9)
        y = np.clip(y, 0, 6)
        
        return x, y





class Grid_World(object):
    def __init__(self, action_type, wind_type):
        self.action_type = action_type
        self.wind_action = wind_type
        
        if self.action_type == "regular":
            self.action_space = [0, 1, 2, 3]

        elif self.action_type == "big world":
            self.action_space = [0, 1, 2, 3]
            
        self.start = (0, 0)
        self.goal = (2, 2)
        
    def action_type_space(self):
        return self.action_space
        
    def reset(self):
        self.x_position, self.y_position = self.start
        return self.start
    
    def step(self, action):
        self.x_position, self.y_position = self.transition(self.x_position, self.y_position, action)
        
        if self.x_position == self.goal[0] and self.y_position == self.goal[1]:
            return True, 5, (self.x_position, self.y_position)
        
        if random.random() < 0.5:
            if self.x_position in range(-1,3) and self.y_position == -1:
                return False, -12, (self.x_position, self.y_position)
            elif self.x_position in range(-1,3) and self.y_position == 3:
                return False, -12, (self.x_position, self.y_position)
            elif self.x_position == -1 and self.y_position in range(-1,3):
                return False, -12, (self.x_position, self.y_position)
            elif self.x_position == 3 and self.y_position in range(-1,3):
                return False, -12, (self.x_position, self.y_position)
            else:
                return False, -12, (self.x_position, self.y_position)
        else:
            if self.x_position in range(-1,3) and self.y_position == -1:
                return False, 10, (self.x_position, self.y_position)
            elif self.x_position in range(-1,3) and self.y_position == 3:
                return False, 10, (self.x_position, self.y_position)
            elif self.x_position == -1 and self.y_position in range(-1,3):
                return False, 10, (self.x_position, self.y_position)
            elif self.x_position == 3 and self.y_position in range(-1,3):
                return False, 10, (self.x_position, self.y_position)
            else:
                return False, 10, (self.x_position, self.y_position)
        
        
    def transition(self, x, y, action):
        
        if action == 0:
            x -= 1
        elif action == 1:
            y -= 1
        elif action == 2:
            x += 1
        elif action == 3:
            y += 1
                
        x = np.clip(x, 0, 2)
        y = np.clip(y, 0, 2)
        
        return x, y
