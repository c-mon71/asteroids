import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle_diff = random.uniform(20, 50)
            velocity_01 = self.velocity.rotate(angle_diff)
            velocity_02 = self.velocity.rotate(-angle_diff)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_01 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_02 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_01.velocity = velocity_01 * 1.2 
            asteroid_02.velocity = velocity_02 * 1.2 

        
