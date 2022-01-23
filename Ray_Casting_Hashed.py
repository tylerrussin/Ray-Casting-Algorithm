from classes.Simulation_Class import Simulation
from sprites import Wall_Sprite
from maps.Map_One import map_one
from maps.Map_Two import map_two
from maps.Map_Three import map_three
from maps.Map_Four import map_four
from maps.Map_Five import map_five
from maps.Map_Six import map_six
from maps.Map_Seven import map_seven
from maps.Map_Eight import map_eight
from maps.Map_Nine import map_nine


if __name__ == '__main__':

    # Initiate simpulation loop

    # Classic
    game = Simulation(screen_width = 500, 
                    screen_height = 200,
                    console_font_size= 2, 
                    simulation_type = 'hashed', 
                    step_size = 0.01, 
                    matrix_wall = Wall_Sprite.matrix, 
                    color_to_glyph_wall = Wall_Sprite.color_to_glyph)

    # Defining user controlls
    print('')
    print('Controls:')
    print('')
    print('Forward:     W')
    print('Backward:    S')
    print('Move Left:   A')
    print('Move Right:  D')
    print('')
    print('Turn Left:   Q')
    print('Turn Right:  E')
    print('')
    print('Ouit:        P')
    print('')
    print('')
    input('Press the Enter to continue...')

    # Initiate with map_six
    game.update_map(map_nine, 'map_nine')
    game.on_user_create()

    while True:
        game.on_user_update()

    # That's It!! - Tyler