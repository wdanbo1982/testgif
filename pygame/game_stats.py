#����������Ϸ����Ϣ��
class GameStates():
    
    #��ʼ������
    def __init__(self,settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False #������Ϸ������־
        self.high_score = 0
        self.level = 1
        
    
    #���ó�ʼ������
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        
    
