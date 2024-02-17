import pygame

class _AnimationBase:
    def __init__(self) -> None:
        super().__init__()
        self._is_animating = False
        self._animation_list = []
        self._cur_animation = 0
        self._cur_frame = 0
        
    def play(self, name: str) -> None:
        """Play animation

        Args:
            name (string): name of the animation
        """
        self._is_animating = True
        if self._animation_list[self._cur_animation]["name"] == name:
            return
            
        self._cur_animation = None
        for anim in self._animation_list:
            if anim["name"] == name:
                self._cur_animation = self._animation_list.index(anim)
        if self._cur_animation is None:
            raise Exception("This animation does not exits")
        
        self._cur_frame = 0
    
    def stop(self) -> None:
        """Stop animation
        """
        self._is_animating = False

    def add_animation(self, name: str, keyframes: list, speed: int) -> None:
        """Create animation

        Args:
            name (string): animation name
            sprites (list): list of sprites
            speed (number): animation speed from 1
        """
        for anim in self._animation_list:
            if anim["name"] == name:
                raise Exception("This animation was create")

        anim = {'name': name, 'keyframes': keyframes, 'speed': speed}
        self._animation_list.append(anim)
        
class Property(_AnimationBase):
    def __init__(self, surface: pygame.Surface) -> None:
        super().__init__()
        self._start_time = pygame.time.get_ticks()
        self._original_size = surface.get_size()
        self._previos_size = surface.get_size()
        self._previos_rotate = 0
        
    def update(self, surface: pygame.Surface) -> pygame.Surface:
        """Update animation

        Args:
            surface (pygame.Surface): animation object

        Returns:
            pygame.Surface: animated object
        """
        image = surface
        if self._is_animating:         
            if self._cur_frame >= len(self._animation_list[self._cur_animation]["keyframes"]):
                self._cur_frame = 0
            
            count_keyframes = len(self._animation_list[self._cur_animation]["keyframes"])
            cur_keyframe = self._animation_list[self._cur_animation]["keyframes"][self._cur_frame]
            
            time = self._animation_list[self._cur_animation]["speed"]
            duration = self._animation_list[self._cur_animation]["keyframes"][self._cur_frame]["duration"]
            elapsed_time = pygame.time.get_ticks() - self._start_time
            progress = int(elapsed_time / ((((duration / 100) * time) / count_keyframes) * 1000) * 100)
            print(progress)
            end_time = self._start_time + (((duration / 100) * time) / count_keyframes) * 1000
            for property, value in cur_keyframe.items():
                if pygame.time.get_ticks() > end_time:
                    if property == "scale":
                        image = pygame.transform.scale(image, (self._original_size[0] * value[0], self._original_size[1] * value[1]))
                    elif property == "rotate":
                        image = pygame.transform.rotate(image, value)
                        self._previos_rotate = value
                    self._start_time = pygame.time.get_ticks()
                    self._previos_size = image.get_size()
                    self._cur_frame += 1
                    break
                
                if property == "scale":
                    step_width = (self._original_size[0] * value[0] - self._previos_size[0]) / 100
                    step_height = (self._original_size[1] * value[1] - self._previos_size[1]) / 100
                    new_width =  self._previos_size[0] + step_width * progress
                    new_height = self._previos_size[1] + step_height * progress
                    
                    image = pygame.transform.scale(image, (new_width, new_height))
                if property == "rotate":
                    step_rotate = value / 100
                    new_angle = self._previos_rotate + step_rotate * progress
                    
                    image = pygame.transform.rotate(image, new_angle)

        return image

class Sprites(_AnimationBase):
    def __init__(self) -> None:
        super().__init__()
        
    def update(self) -> pygame.Surface:
        """Update current animation sprite

        Returns:
            pygame.Surface: current animation sprite
        """
        if self._is_animating:
            self._cur_frame += 0.1 * self._animation_list[self._cur_animation]["speed"]
            
            if self._cur_frame >= len(self._animation_list[self._cur_animation]["keyframes"]):
                self._cur_frame = 0

        return self._animation_list[self._cur_animation]["keyframes"][int(self._cur_frame)]
    
    

    