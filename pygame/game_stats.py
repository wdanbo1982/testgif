#创建跟踪游戏的信息类
class GameStates():
    
    #初始化变量
    def __init__(self,settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False #设置游戏结束标志
        self.high_score = 0
        self.level = 1
        
    
    #重置初始化变量
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        
    
