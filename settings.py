class settings:

    def __init__(self):
        
        # game settings
        self.bg_color = (0,0,0)
        self.game_active = False
        self.background_move_x = 1
        self.background_move_y = 1
        self.hardcore_mode = False

        # character settings
        self.character_speed = 6
        self.movement_type_arrows = False
        self.character_lives = 3

        # challenger settings
        self.spawn_counter = 30
        self.challenger_speed = 3
        self.challenger_rate = 1

        #forcefield settings
        self.forcefield_active = False
        self.forcefield_charge = 500 
        self.forcefield_charge_limit = 500
        self.forcefield_min = False
        self.display_forcefield = False
        self.forcefield_size = 2
        self.forcefield_smaller = False
        self.forcefield_bigger = False
        self.forcefield_normal= False

        # main menu
        self.main_menu = True
        self.starting_pos_character = -200
        self.starting_pos_challenger = -400
        self.main_menu_y = 680
        self.menu_attack = False

        # scoring
        self.score = 0

        # options menu
        self.options_menu = False
        self.hardcore_mode = True

        # pause menu
        self.pause_menu = False

        # Game over
        self.game_over = False

        # Power Ups
        self.powerup_forcefield_size = False
        self.powerup_assignment_forcfield_size = False
        self.percentage_powerup = 10
        self.powerup_assingment_speed_character = False
        self.powerup_speed_character = False    # actual indicator for powerup


    
   