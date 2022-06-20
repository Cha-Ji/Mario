IMG_PATH = 'img/'

def createMissile(pygame):
    missile = [pygame.image.load(IMG_PATH + 'missile.png') for i in range(40)]
    for i in range(len(missile)):
        missile[i] = pygame.transform.scale(missile[i], (20, 20))
    return missile
