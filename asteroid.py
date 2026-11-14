import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        smaller1_velocity = self.velocity.rotate(rand_angle)
        smaller2_velocity = self.velocity.rotate(-rand_angle)
        smaller1 = Asteroid(self.position.x, self.position.y, new_rad)
        smaller2 = Asteroid(self.position.x, self.position.y, new_rad)
        smaller1.velocity = smaller1_velocity * 1.2
        smaller2.velocity = smaller2_velocity * 1.2

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
