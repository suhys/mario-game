from game_data import level_map
class Settings():
    
    def __init__(self):
        # level setting
        self.tile_size = 64
        self.world_shift = -1
        
        #screen setting        
        self.screen_width = 1200
        self.screen_height = len(level_map) * self.tile_size
        self.bg_color = 0,0,0

        
        #overworld setting
        self.start_level = 0
        self.max_level = 1
        
        
        # camera
        CAMERA_BORDERS = {
            'left': 100,
            'right': 200,
            'top': 100,
            'bottom': 150
        }