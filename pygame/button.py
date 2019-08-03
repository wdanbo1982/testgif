import pygame.font

#������ť��
class Button():
    
    def __init__(self,settings,screen,msg):
        #��ʼ����ť������
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #���ð�ť�ĳߴ硢��ť��ɫ��������ɫ�������С
        self.width,self.height = 200,50
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.Font("freesansbold.ttf",48)
        
        #������ť��rect���󣬲�ʹ�����
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #��ť�ı�ǩֻ�贴��һ��
        self.prep_msg(msg)
    
    #��msg��ȾΪͼ�񣬲�ʹ���ڰ�ť�Ͼ��� 
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,
                                            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    #����һ������ɫ���İ�ť���ٻ����ı�
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
