import pygame
from Image import load_image


class Caillou:
    def __init__(self, pos, size):
        self.name = "Caillou"
        self.pos = list(pos)
        self.velocity = [0,0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.size = size
        self.frame_movement = 0   
        self.anim_count = 0

        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = False
        self.set_action('caillou-idle')

    def render(self, surf, offset=(0, 0)):

        pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        surf.blit(load_image('player/shesh.png'), (self.pos[0], self.pos[1]))

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets['./sprites/' + self.action + '/' + self.anim_count].copy()

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.detectObjectsColliding(tilemap)
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def detectObjectsColliding(self, tilemap):
        self.detectObjectsCollidingY(tilemap)
        self.detectObjectsCollidingX(tilemap)
    
    def detectObjectsCollidingX(self, tilemap):
        self.pos[0] += self.frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if self.frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
                
    def detectObjectsCollidingY(self, tilemap):
        self.pos[1] += self.frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
<<<<<<< HEAD:Character/Caillou.py
                self.pos[1] = entity_rect.y
=======
                self.pos[1] = entity_rect.y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

        if self.collisions['down']:
            self.air_time = 0
            
        if movement[0] != 0:
            self.set_action('caillou-run')
        else:
            self.set_action('caillou-idle')

        self.anim_count += 1
            
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
>>>>>>> 91bd95727f647c9dc0c151783131536eac177b86:Caillou.py
