import pygame

pygame.init()

w_width, w_height = 1000,700
window = pygame.display.set_mode((w_width, w_height))
clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.color, self.text = color, text
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, (0, 0, 0))
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def hover_effect(self):
        pygame.draw.rect(window, (255,0,0), (self.x-3, self.y-3, self.width+3, self.height+3), 3)
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover_effect()
    def execute(self, func):
        func()

def show_esc_label():
    font = pygame.font.SysFont('comicsans', 15)
    esc_label = font.render("press [ESC] to return to main menu", 1, (0,0,0))
    window.blit(esc_label, (0,0))


def options():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                main_menu()
        clock.tick(30)
        window.fill((0,255,0))
        show_esc_label()
        pygame.display.update()
    pygame.quit()    

def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                main_menu()
        clock.tick(30)
        window.fill((255,0,0))
        pygame.display.update()
    pygame.quit()

def main_menu():
    p_coords = (w_width/2-50, w_height/2-50)
    play_button = Button(*p_coords,100,50,(255,255,255),"play")
    options_button = Button(p_coords[0], p_coords[1]+100,100,50,(255,255,255), "options")
    quit_button = Button(p_coords[0], p_coords[1]+200,100,50,(255,255,255), "exit")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    play_button.execute(play)
                elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    exit()
                elif options_button.rect.collidepoint(pygame.mouse.get_pos()):
                    options_button.execute(options)

        
        clock.tick(30)
        window.fill((0,0,0))

        play_button.draw()
        options_button.draw()
        quit_button.draw()

        play_button.update()
        options_button.update()
        quit_button.update()

        pygame.display.update()

    pygame.quit()


main_menu()