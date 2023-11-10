# pygame template
import math
import random
import pygame

def linear_interpolation(x, x0, x1, y0, y1):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


pygame.init()
pygame.font.init()


WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

num_students = 33
MAP_SIZE = math.ceil(math.sqrt(num_students))
MAP_SIZE += 1 - MAP_SIZE % 2
MID = MAP_SIZE//2
PLOT_WIDTH = 640
PLOT_HEIGHT = 480
MIN_SCALE = HEIGHT/(MAP_SIZE*PLOT_HEIGHT)
MAX_SCALE = 1
screen = pygame.Surface((PLOT_WIDTH * MAP_SIZE, PLOT_HEIGHT * MAP_SIZE))
camera_x = screen.get_width()//2
camera_y = screen.get_height()//2
zoom_level_gallo = 1 # 1-10
grid_font = pygame.font.SysFont('Arial', 20)


# ---------------------------
# Initialize global variables for animation
# These must have your name in there

font_gallo = pygame.font.SysFont('Arial', 120)
welcome_font_gallo = pygame.font.SysFont('Arial', 40)
bg_color_gallo = "#E15E03"
# fg_color_gallo = "#FF9142"
fg_color_gallo = "#FEC661"
text_gallo = font_gallo.render("The Gallo-verse", True, fg_color_gallo)
welcome_text_gallo = welcome_font_gallo.render("Welcome to", True, fg_color_gallo)
frames_gallo = 0
bg_start = pygame.Color("#E05F02")
bg_end = pygame.Color("#6B2D01")
bg_gallo_large = pygame.Surface((1000, 1000))
bg_gallo_large.fill((0, 0, 0))
for x in range(1000):
    pygame.draw.line(bg_gallo_large, bg_end.lerp(bg_start, x/1000), (x, 0), (x, 1000))
bg_gallo_large = pygame.transform.rotate(bg_gallo_large, -45)
bg_gallo = pygame.Surface((640, 480))
bg_gallo.blit(bg_gallo_large, (-500, -500))
welcome_text_buffer = {}
# ---------------------------

ghost_x_maggie = 0
ghost_y_maggie = 200

switch_maggie = "right"

# ----------------------

wind_x_angie = 0
wind_y_angie = 0

# ----------------------
duncan_glow_x, duncan_glow_y, duncan_glow_radius = 315, 220, 70
duncan_vignette_x, duncan_vignette_y, duncan_vignette_radius = 320, 240, 250

duncan_rect_x, duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey = 285, 190, 60, 70
duncan_circle_x, duncan_circle_y, duncan_circle_radius = 315, 187, 30

duncan_inside_x, duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey = 288, 193, 55, 65
duncan_inner_circle_x, duncan_inner_circle_y, duncan_inner_circle_radius = 315, 190, 27.5

duncan_eye_leftx, duncan_eye_lefty, duncan_eye_left_radius = 307, 190, 6
duncan_eye_rightx, duncan_eye_righty, duncan_eye_right_radius = 322, 190, 5

duncan_hover_speed = 1
duncan_glow_speed, duncan_glow_color, duncan_glow_growth = 2, 245, 1
duncan_background_color, duncan_background_change_speed = 50, 2
#---------------------

circle_x_ilia = 320
circle_y_ilia = 240
flash_color = (0, 0, 255)
last_flash_time = 0
flash_interval = 500
growrate = 5
sizeilia = 150

# ------------------
olivia_timer = 0
olivia_circle_counter = 0

olivia_circles_list = []

olivia_text = "Aw sweet! Man-made horrors beyond my comprehension!"

olivia_font = pygame.font.SysFont("Arial",20)

for i in range(20,640,40):
    for j in range(20,480,40):
        if (i + j) % 80 == 0:
            olivia_circles_list.append({"x":i,"y":j})

#HUZZAH I DONT NEED TO WORRY ABOUT VARIABLE NAMES THANK GOD FOR LOCAL VARIABLES
def olivia_draw_circles():
    for circle in olivia_circles_list:
        num = (circle["x"] + circle["y"])/20 + olivia_timer
        r = 255 * abs(math.cos(math.pi*(num/60-1/3)))
        g = 255 * abs(math.cos(math.pi*(num/60-2/3)))
        b = 255 * abs(math.cos(math.pi*(num/60-3/3)))
        
        circle_x = x+circle["x"]
        circle_y = y+circle["y"]+math.sin(math.pi*num/20)*8
        circle_colour = (r,g,b)
        circle_size = 20
        # mouse hover doesn't work in galloverse :(
        '''mouse_x, mouse_y = pygame.mouse.get_pos()       
        x_distance = abs(circle_x - mouse_x)
        y_distance = abs(circle_y - mouse_y)
        
        if x_distance <= 100 and y_distance <= 100:
            circle_size += (200 - x_distance - y_distance)/10'''
        
        pygame.draw.circle(screen,circle_colour,(circle_x,circle_y),circle_size)

def olivia_generate_text():
    letters = "aaaaaaaabbcccddddeeeeeeeeeeeefffgghhhhhhiiiiiiiijkllllmmmnnnnnnnnooooooooppqrrrrrrsssssssstttttttttuuuvwwxyyz"
    symbols = "!?,.:;"
    string = " "
    for i in range(15):
        num = random.randrange(0,25)
        if num == 24 and string[i-1] not in symbols and string[i-1] != " ":
            string += symbols[random.randrange(0,len(symbols))] + " "
        elif num > 15 and string[i-1] != " ":
            string += " "
        else:
            string += letters[random.randrange(0,len(letters))]
    string += symbols[random.randrange(0,3)]
    string = string [1:]
    return(string)
# ------------------

cord_yang1 = 320
cord_yang3 = 440
cord_yang2 = 440
cord_yang4 = 200
cord_yang5 = 200
count_yang = 0
upyang = 0
upyang2 = 0
upyang3 = 0
upyang4 = 0
upyang5 = 0

#-----------------

#position (0, 1440)
#OUTSIDE LOOP:
DARK_GREEN = (24, 87, 13)
EVERGREEN = (35, 130, 4)
bark_x_ocampo = 20
bark_y_ocampo = 1670

leaves_x_ocampo = 75
leaves_y_ocampo = 1575

x = 0 
y = 0 

#Car outer
polygon_ocampo = [
(x, y+300),
(x+10, y+100),
(x+60, y+275),
(x+65, y+80),
(x+150, y+80),
(x+140, y+140),
(x+175, y+155),
(x+200, y+300)
]

#Window
polygon_ocampo2 = [
(x+50, y+270),
(x+50, y+240),
(x+140, y+240),
(x+190, y+290)
]

#Wheels
polygon_ocampo3 = [
(x+30, y+340),
(x+67, y+310),
(x+100, y+340),
(x+67, y+370)
]

polygon_ocampo4 = [
(x+210, y+340),
(x+247, y+310),
(x+280, y+340),
(x+247, y+370)
]
# Lucas -----------------

asteroid_x_p = 0
asteroid_y_p = 0

asteroid_2_x_p = 0 
asteroid_2_y_p = 0

smallhole_1_x_p = 20
smallhole_1_y_p = 10

smallhole_2_x_p = -20
smallhole_2_y_p = -10

smallhole_3_x_p = 20
smallhole_3_y_p = -20

smallhole_4_x_p = -5
smallhole_4_y_p = 30

ufo_body_x_p  = 0
ufo_body_y_p = 0 

line1_x_p = 0 

#-------------------

running = True
while running:
    # GALLO VERSE SPECIFIC ----------------------------------------------------------------
    scale = linear_interpolation(zoom_level_gallo, 10, 1, MIN_SCALE, MAX_SCALE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            direction = event.y
            zoom_level_gallo -= direction
            zoom_level_gallo = max(min(zoom_level_gallo, 10), 1)
        elif event.type == pygame.MOUSEMOTION:
            click, _, _ = event.buttons
            if click:
                dx, dy = event.rel
                camera_x += -dx/scale
                camera_y += -dy/scale

    # DRAWING
    screen.fill((255, 255, 255))
    window.fill((100, 100, 100))

    # Draw Plot points
    for x in range(0, MAP_SIZE * PLOT_WIDTH, PLOT_WIDTH):
        for y in range(0, MAP_SIZE * PLOT_HEIGHT, PLOT_HEIGHT):
            pygame.draw.circle(screen, (30, 30, 200), (x, y), 5)
            coord_text = grid_font.render(f"({x}, {y})", False, (0, 0, 0))
            screen.blit(coord_text, (x, y))
    
    # -----------MAGGIE
    x = 1920
    y = 960
    width = 640
    height = 480


    width = 640
    height = 480

    points_maggie = [
        (x+345,y+100),
        (x+285,y+150),
        (x+385,y+150)
    ]

    points_maggie1 = [
        (x+275,y+170),
        (x+225,y+220),
        (x+315,y+220)
    ]

    points_maggie2 = [
        (x+405,y+170),
        (x+355,y+220),
        (x+445,y+220)
    ]

    points_maggie3 = [
        (x+385,y+223),
        (x+385,y+203),
        (x+443,y+190)
    ]


    pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))

    if ghost_x_maggie > 642:
        switch_maggie = "left"
    elif ghost_x_maggie < 0:
        switch_maggie = "right"


    if switch_maggie == "right":
        ghost_x_maggie += 3
    else:
        ghost_x_maggie -= 3

    # BACKGROUND
    pygame.draw.rect(screen, ("#05133d"), (x, y, width, height))

    #ground
    pygame.draw.rect(screen, ("#013220"), (x, y + 280, width, 200))


    #moon
    pygame.draw.circle(screen, ("gray"), (x + 260, y + 140), 70)

    #smallghost
    pygame.draw.circle(screen, ("white"), (x + 380, y + 183), 20)
    pygame.draw.circle(screen, ("black"), (x + 380, y + 189), 4) #mouth
    pygame.draw.circle(screen, ("black"), (x + 376, y + 180), 2) #eye
    pygame.draw.circle(screen, ("black"), (x + 386, y + 180), 2) #eye
    pygame.draw.polygon(screen, ("white"), points_maggie3)

    # HOUSE    
    pygame.draw.rect(screen, (0, 0, 0), (x + 300, y+150, 70, 150))
    pygame.draw.polygon(screen, (0,0,0), points_maggie)


    pygame.draw.rect(screen, (0, 0, 0), (x + 250, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie1)

    pygame.draw.rect(screen, (0, 0, 0), (x + 373, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie2)

    #TOP
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+87, 20, 5))
    pygame.draw.rect(screen, (0,0,0), (x + 343, y+83, 5, 30))


    #FENCE
    for i in range(40):
        pygame.draw.rect(screen, (0, 0, 0), (x + 150 + 10*i, y+270, 5, 25))
    pygame.draw.rect(screen, (0, 0, 0), (x + 150, y+278,400, 3))

    #WINDOW
    pygame.draw.rect(screen, ("#e0b42c"), (x + 390, y+250, 15, 40)) #right
    pygame.draw.rect(screen, ("#e0b42c"), (x + 260, y+250, 15, 40)) #left
    pygame.draw.rect(screen, ("#e0b42c"), (x + 325, y+170, 25, 40)) #middle

    pygame.draw.circle(screen, ("#e0b42c"), (x + 338, y + 170), 12)


    pygame.draw.rect(screen, (0,0,0), (x + 325, y+190, 28, 3))     #middle lines
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+172, 3, 41))
    pygame.draw.rect(screen, (0,0,0), (x + 325, y+174, 28, 3)) 

    #door
    pygame.draw.rect(screen, ("#3f2a14"), (x + 319, y+257, 30, 40))


    #pumpkin
    pygame.draw.circle(screen, ("orange"), (x + 130, y + 290), 14)
    pygame.draw.rect(screen, ("brown"), (x + 127, y+268, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 80, y + 310), 14)
    pygame.draw.rect(screen, ("brown"), (x + 77, y+288, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 40, y + 302), 14)
    pygame.draw.rect(screen, ("brown"), (x + 37, y+280, 3, 10))

    #grave
    pygame.draw.rect(screen, ("gray"), (x + 525, y+290, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 538, y + 290), 12)

    pygame.draw.rect(screen, ("gray"), (x + 575, y+280, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 588, y + 280), 12)

    #path
    pygame.draw.rect(screen, ("#515151"), (x + 319, y+300, 50, 50))


    # GHOST
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie + 30), 10)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 30, ghost_y_maggie, 60, 30))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 20, y + ghost_y_maggie + 30), 10)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie +20, y + ghost_y_maggie + 30), 10)

    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 100), 15)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 115), 5)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 73, ghost_y_maggie + 100, 27, 15))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 72, y + ghost_y_maggie + 115), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 50, y + ghost_y_maggie + 115), 5)


    # DUNCAN -------------------------------

    x = 3200
    y = 960
    width = 640
    height = 480
    
    duncan_rect_y += duncan_hover_speed
    duncan_circle_y += duncan_hover_speed
    
    duncan_inside_y += duncan_hover_speed
    duncan_inner_circle_y += duncan_hover_speed
    
    duncan_eye_lefty += duncan_hover_speed * 0.54
    duncan_eye_righty += duncan_hover_speed * 0.65
    
    duncan_glow_y += duncan_hover_speed
    duncan_glow_color += duncan_glow_speed
    duncan_glow_radius += duncan_glow_growth
    
    duncan_background_color += duncan_background_change_speed
    
    if duncan_circle_y < 197: duncan_hover_speed *= -1
    if duncan_rect_y > 180: duncan_hover_speed *= -1
    if duncan_glow_color >= 255: duncan_glow_speed *= -1
    if duncan_glow_color <= 235: duncan_glow_speed *= -1
    if duncan_glow_radius > 100 or duncan_glow_radius < 60: duncan_glow_growth *= -1
    if duncan_background_color > 50 or duncan_background_color < 2: duncan_background_change_speed *= -1

    pygame.draw.rect(screen, (duncan_background_color, duncan_background_color, duncan_background_color), (x, y, width, height))

    pygame.draw.circle(screen, (235, 235, 235), (x + duncan_vignette_x, y + duncan_vignette_y), duncan_vignette_radius)
    pygame.draw.circle(screen, (duncan_glow_color, duncan_glow_color, duncan_glow_color), (x + duncan_glow_x, y + duncan_glow_y), duncan_glow_radius)
    
    pygame.draw.rect(screen, "Black", (x + duncan_rect_x, y + duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey))
    pygame.draw.circle(screen, "Black", (x + duncan_circle_x, y + duncan_circle_y), duncan_circle_radius)
    
    pygame.draw.rect(screen, "White", (x + duncan_inside_x, y + duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey))
    pygame.draw.circle(screen, "White", (x + duncan_inner_circle_x, y + duncan_inner_circle_y), duncan_inner_circle_radius)
    
    pygame.draw.circle(screen, "Black", (x + duncan_eye_leftx, y + duncan_eye_lefty), duncan_eye_left_radius)
    pygame.draw.circle(screen, "Black", (x + duncan_eye_rightx, y + duncan_eye_righty), duncan_eye_right_radius)

    # ILIA ------------------
    current_time = pygame.time.get_ticks()
    
    # Change the color of the circle only if the flash_interval has passed
    if current_time - last_flash_time >= flash_interval:
        flash_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        last_flash_time = current_time

    sizeilia += growrate
    if sizeilia < 10 or sizeilia > 150:
        growrate = growrate *- 1
    x = 2560
    y = 1440
    width_ilia = 640
    height_ilia = 480

    pygame.draw.rect(screen, (45, 96, 255), (x, y, width_ilia, height_ilia))

    pygame.draw.circle(screen, flash_color, (x + circle_x_ilia, y + circle_y_ilia), sizeilia)
    #  OLIVIA ------------------
    x = 3840
    y = 1440
    if olivia_timer % 60 == 0:
        olivia_text = olivia_font.render(olivia_generate_text(),True,"black")
    olivia_timer += 1
    pygame.draw.rect(screen,(80,30,70),(x,y,640,480))
    olivia_draw_circles()
    
    olivia_cat_x = 5*(abs(100-olivia_timer/2%200))+x-75
    olivia_cat_y = -50*(abs(math.sin(olivia_timer/10)))+y
    #text
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+50,y+150,180,120))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+125,y+263),(olivia_cat_x+155,y+263),(olivia_cat_x+140,olivia_cat_y*0.5+y*0.5+330)))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+54,y+154,172,112))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+130,y+260),(olivia_cat_x+150,y+260),(olivia_cat_x+140,olivia_cat_y*0.5+y*0.5+320)))
    screen.blit(olivia_text,(olivia_cat_x+70,y+195))
    
    #body
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+96,olivia_cat_y+351,88,78))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+104,olivia_cat_y+340),(olivia_cat_x+101,olivia_cat_y+377),(olivia_cat_x+131,olivia_cat_y+360)))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+175,olivia_cat_y+340),(olivia_cat_x+178,olivia_cat_y+377),(olivia_cat_x+148,olivia_cat_y+360)))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+100,olivia_cat_y+355,80,70))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+106,olivia_cat_y+345),(olivia_cat_x+106,olivia_cat_y+370),(olivia_cat_x+126,olivia_cat_y+360)))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+173,olivia_cat_y+345),(olivia_cat_x+173,olivia_cat_y+370),(olivia_cat_x+153,olivia_cat_y+360)))
    #mouth
    if 100-olivia_timer/2%200 > 0:
        olivia_cat_x -= 5
    else:
        olivia_cat_x += 5
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+127,olivia_cat_y+378,26,39))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+130,olivia_cat_y+381,20,33))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+122,olivia_cat_y+378,20,20))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+138,olivia_cat_y+378,20,20))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+119,olivia_cat_y+376,23,19))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+138,olivia_cat_y+376,23,19))
    pygame.draw.rect(screen,"white",(olivia_cat_x+120,olivia_cat_y+370,40,20))
    #eyes
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+123,olivia_cat_y+380,6,8))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+151,olivia_cat_y+380,6,8))

    # Lucas -----------------------------------------------------------

    asteroid_x_p += 1
    asteroid_y_p += 1
    smallhole_1_x_p += 1
    smallhole_1_y_p += 1
    smallhole_2_x_p += 1
    smallhole_2_y_p += 1
    smallhole_3_x_p += 1
    smallhole_3_y_p += 1
    smallhole_4_x_p += 1
    smallhole_4_y_p += 1
    asteroid_2_x_p += 1.5
    asteroid_2_y_p += 1.5
    ufo_body_x_p += 1
    line1_x_p += 1
    
    x = 1280
    y = 960
    width = 640
    height = 480
    circle_list_p = []
    for i in range(40):
        circle_p = {
            'x_p': random.randint(x, x + 640),
            'y_p': random.randint(y, y + 480),
            'radius_p': random.randint(1,4)
        }
        circle_list_p.append(circle_p)
    ufo_body_y_p = int((HEIGHT - 200) / 2 + math.sin(ufo_body_x_p / 100) * 100)
    line1_y_p = int((HEIGHT - 200) / 2 + math.sin(line1_x_p / 100) * 100)
    flame_variation_1_p = random.randint(-5, 5)  
    if asteroid_y_p - 50 >= HEIGHT or asteroid_x_p - 50 >= WIDTH:
      asteroid_x_p = x
      asteroid_y_p = y
      smallhole_1_x_p = x + 20
      smallhole_1_y_p = y + 20
      smallhole_2_x_p = x - 20
      smallhole_2_y_p = y - 10
      smallhole_3_x_p = x + 20
      smallhole_3_y_p = y - 20
      smallhole_4_x_p = x - 5
      smallhole_4_y_p = y + 30
    if asteroid_2_y_p >= HEIGHT or asteroid_2_x_p >= WIDTH:
      asteroid_2_x_p = x
      asteroid_2_y_p = y 
    if ufo_body_y_p >= HEIGHT or ufo_body_x_p >= WIDTH:
      ufo_body_x_p = x 
      ufo_body_y_p = y
      line1_x_p = x
      line1_y_p = y
    pygame.draw.rect(screen, (20, 20, 20), (x, y, width, height))
# STARS
    for circle_p in circle_list_p:  
      pygame.draw.circle(screen, (255, 255, 255), (x + circle_p['x_p'], y + circle_p['y_p']), circle_p['radius_p'])
# PLANET
    pygame.draw.circle(screen, (20, 20, 160), (x + 30, y + 200), 10)
    pygame.draw.polygon(screen, (20, 160, 20), [(x + 31, y + 202), (x + 34, y + 200), (x + 36, y + 202), (x + 30, y + 210), (x + 28, y + 202)])
    pygame.draw.polygon(screen, (20, 160, 20), [(x + 25, y + 195), (x + 28, y + 194), (x + 30, y + 197), (x + 24, y + 199), (x + 22, y + 202)])
# PLANET 2
    pygame.draw.circle(screen, (201, 28, 40), (x + 300, y + 100), 10)
    pygame.draw.polygon(screen, (227, 151, 70), [(x + 301, y + 102), (x + 306, y + 102), (x + 300, y + 110)])
    pygame.draw.polygon(screen, (227, 151, 70), [(x + 295, y + 95), (x + 300, y + 97), (x + 294, y + 99), (x + 292, y + 102)])
# UFO
    pygame.draw.ellipse(screen, (173, 169, 163), (x + ufo_body_x_p, y + ufo_body_y_p + 100, 50, 20), 0)
    pygame.draw.arc(screen, (67, 153, 91), (x + ufo_body_x_p + 8, y + ufo_body_y_p + 90, 33, 40), 0, 3.14, 300)
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p +10, y + line1_y_p + 125), (x + line1_x_p, y + line1_y_p + 140), 3) 
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p + 25, y + line1_y_p + 127), (x + 25 + line1_x_p, y + line1_y_p + 142), 3) 
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p + 40, y + line1_y_p + 125), (x + 50 + line1_x_p, y + line1_y_p + 140), 3) 
# ASTEROID 1 (BIG ONE)
    pygame.draw.polygon(screen, (84, 200, 204), [(x + asteroid_x_p, y + asteroid_y_p - 50), (x + asteroid_x_p - 50, y + asteroid_y_p), (x + asteroid_x_p - 100 + flame_variation_1_p, y + asteroid_y_p - 100)])
    pygame.draw.polygon(screen, (93, 144, 158), [(x + asteroid_x_p, y + asteroid_y_p - 50), (x + asteroid_x_p - 50, y + asteroid_y_p), (x + asteroid_x_p - 75 + flame_variation_1_p, y + asteroid_y_p - 75)])
    pygame.draw.circle(screen, (140, 129, 116), (x + asteroid_x_p, y + asteroid_y_p), 50)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_1_x_p, y + smallhole_1_y_p), 10)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_2_x_p, y + smallhole_2_y_p), 20)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_3_x_p, y + smallhole_3_y_p), 7)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_4_x_p, y + smallhole_4_y_p), 9)    

    # Youlchan --------------------------------------------------------

    x = 0
    y = 480 * 5
    width = 640
    height = 480
    # animation
    count_yang += 1
    if count_yang == 1:
      n_yang = random.randrange(16)
      n_yang2 = random.randrange(16)
      n_yang3 = random.randrange(16)
      n_yang4 = random.randrange(16)
      n_yang5 = random.randrange(16)
      yang1 = random.randrange(6)
      yang2 = random.randrange(6)
      yang3 = random.randrange(6)
      yang4 = random.randrange(6)
      yang5 = random.randrange(6)
    if count_yang == 20:
      cord_yang3 += n_yang
      cord_yang1 -= n_yang2
      cord_yang2 -= n_yang3
      upyang4 -= yang4
      upyang5 += yang5
    if count_yang == 30:
      upyang += yang1
      upyang2 -= yang2
      upyang3 += yang3
      cord_yang4 += n_yang4
      cord_yang5 += n_yang5
    if count_yang == 40:
      cord_yang3 -= n_yang*2
      cord_yang1 += n_yang2*2
      cord_yang2 += n_yang3*2
      upyang -= yang1*2
      upyang2 += yang2*2
      upyang5 -= yang5*2
    if count_yang == 50:
      cord_yang4 += n_yang4
      cord_yang5 += n_yang5
      upyang3 -= yang3*2
      upyang4 += yang4*2
    if count_yang == 60:
      cord_yang1 = 320
      cord_yang4 = 200
      cord_yang5 = 200
      upyang4 = 0
      upyang5 = 0
    if count_yang == 70:
      cord_yang3 = 440
      cord_yang2 = 440
      upyang = 0
      upyang2 = 0
      upyang3 = 0
      count_yang = 0
    # bg
    pygame.draw.rect(screen, (150,20,20), (x, y, width, height))

  
    
    # Sclera 
    pygame.draw.ellipse(screen, (255,255,255),(x + 320 - 60 ,y + 240 - 30, 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 440 - 30,y + 380 , 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 440 - 30,y + 100 - 60, 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 200 - 90,y + 380 , 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 200 - 90,y + 100- 60, 120, 60))
    #Iris
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang1 ,y + 240 + upyang), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang2+30, y+410 + upyang2),30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang3 + 30,y + 70 + upyang3), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang4 -30,y + 410 + upyang4), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang5 -30,y + 70 + upyang5), 30)
    #Pupil
    pygame.draw.circle(screen, (25,50,50),(x + cord_yang1 ,y + 240 + upyang), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang2 + 30 ,y + 410 + upyang2), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang3 + 30,y + 70 + upyang3), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang4 -30,y + 410 + upyang4), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang5 -30,y + 70 + upyang5), 15)

    # JOSH OCAMPO ---------------------------------------------------------------------------------------
    x = 0
    y = 1440
    width = 640
    height = 480
    
    bark_x_ocampo -= 5
    leaves_x_ocampo -= 5

    # Must draw with reference to that coordinate
    #car
    pygame.draw.polygon(screen, (245, 32, 17), ((x, y+340), (x+10, y+280), (x+60, y+280), (x+65, y+250), (x+150, y+250), (x+200, y+290), (x+290, y+300), (x+300, y+340)))
    pygame.draw.polygon(screen, (15, 245, 252), ((x+67, y+280), (x+72, y+255), (x+143, y+255), (x+190, y+290)))
    pygame.draw.rect(screen, (245, 32, 17), (x+110, y+250, 7, 40))
    pygame.draw.polygon(screen, (46, 44, 44), ((x+30, y+340), (x+67, y+310), (x+100, y+340),(x+67, y+370)))
    pygame.draw.polygon(screen, (46, 44, 44), ((x+210, y+340), (x+247, y+310), (x+280, y+340),(x+247, y+370)))

    #tree
    pygame.draw.rect(screen, (105, 71, 13), (bark_x_ocampo + 90, bark_y_ocampo - 100, 35, 250))
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo, leaves_y_ocampo), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 25, leaves_y_ocampo - 30), 37)
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo + 65, leaves_y_ocampo - 20), 50)
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo + 65, leaves_y_ocampo + 20), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 35, leaves_y_ocampo + 40), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 95, leaves_y_ocampo + 30), 40)
    if leaves_x_ocampo == -100: 
        bark_x_ocampo = 640 
        leaves_x_ocampo = 695
        
    # -----------ANGIE YAN
    angie_width = 1280
    angie_height = 1440
    
    wind_x_angie += 40
    if wind_x_angie == WIDTH:
        wind_x_angie = -160
        wind_x_angie += 40

    angie_x = 0
    angie_y = 0

    # SCREEN FILL
    pygame.draw.rect(screen, (209, 215, 232), (angie_x, angie_y, angie_width, angie_height))

    # HILL POINTS
    hills1 = [
        (0, 104), 
        (0, 180),
        (70, 180)
    ]

    hills2 = [
        (32, 139),
        (70, 180),
        (146, 180)
    ]

    hills3 = [
        (70, 151),
        (128, 141),
        (176, 180),
        (65, 178)
    ]

    hills4 = [
        (12, 135),
        (124, 127),
        (233, 180),
        (72, 180)
    ]

    hills5 = [
        (4, 180),
        (0, 79),
        (192, 180),
        (227, 130),
        (361, 180),
        (436, 85),
        (538, 54),
        (538, 186)
    ]
    
    opposite_hills1 = [
        (539, 121),
        (435, 180),
        (640, 180)
    ]

    opposite_hills2 = [
        (499, 144),
        (424, 139),
        (403, 180),
        (499, 180)
    ]

    opposite_hills3 = [
        (415, 159),
        (329, 180),
        (416, 179)
    ]

    opposite_hills4 = [
        (286, 180),
        (363, 147),
        (448, 157),
        (489, 89),
        (539, 101),
        (539, 180)
    ]

    # CLOUDS
    clouds1 = [
        (0, 82),
        (1, 180),
        (36, 36),
        (235, 185),
        (29, 186)
    ]
   
    clouds2 = [
        (256, 165),
        (297, 179),
        (381, 103),
        (535, 1),
        (537, 180)
    ]

    clouds3 = [
        (63, 180),
        (159, 120),
        (280, 105),
        (392, 143),
        (263, 204)
    ]
    
    # CLOUDS
    pygame.draw.circle(screen, (255, 255, 255), (49, 79), 60)
    pygame.draw.circle(screen, (255, 255, 255), (39, 39), 60)
    pygame.draw.circle(screen, (255, 255, 255), (84, 36), 60)
    pygame.draw.circle(screen, (255, 255, 255), (99, 91), 60)
    pygame.draw.circle(screen, (255, 255, 255), (182, 129), 60)
    pygame.draw.circle(screen, (255, 255, 255), (220, 116), 60)
    pygame.draw.circle(screen, (255, 255, 255), (297, 129), 60)
    pygame.draw.circle(screen, (255, 255, 255), (414, 97), 60)
    pygame.draw.circle(screen, (255, 255, 255), (356, 124), 60)
    pygame.draw.circle(screen, (255, 255, 255), (444, 7), 60)
    pygame.draw.circle(screen, (255, 255, 255), (359, 161), 60)
    

    # CLOUD SHADOWS
    pygame.draw.polygon(screen, (196, 194, 185), clouds1)
    pygame.draw.polygon(screen, (196, 194, 185), clouds2)
    pygame.draw.polygon(screen, (196, 194, 185), clouds3)
    pygame.draw.circle(screen, (196, 194, 185), (151, 130), 30)
    pygame.draw.circle(screen, (196, 194, 185), (108, 92), 30)
    pygame.draw.circle(screen, (196, 194, 185), (50, 57), 30)
    pygame.draw.circle(screen, (196, 194, 185), (68, 88), 30)
    pygame.draw.circle(screen, (196, 194, 185), (224, 125), 30)
    pygame.draw.circle(screen, (196, 194, 185), (292, 123), 30)
    pygame.draw.circle(screen, (196, 194, 185), (12, 104), 30)
    pygame.draw.circle(screen, (196, 194, 185), (384, 107), 30)
    pygame.draw.circle(screen, (196, 194, 185), (445, 78), 30)
    pygame.draw.circle(screen, (196, 194, 185), (481, 15), 30)
    pygame.draw.circle(screen, (196, 194, 185), (525, 7), 30)
    pygame.draw.circle(screen, (196, 194, 185), (186, 131), 30)
    pygame.draw.circle(screen, (196, 194, 185), (320, 136), 30)
    pygame.draw.circle(screen, (196, 194, 185), (472, 59), 30)

    
    # HILLS
    pygame.draw.polygon(screen, (147, 152, 174), hills5)
    pygame.draw.polygon(screen, (100, 122, 117), hills4)
    pygame.draw.polygon(screen, (56, 70, 64), hills1)
    pygame.draw.polygon(screen, (56, 70, 64), hills2)
    pygame.draw.polygon(screen, (56, 70, 64), hills3)
    

    pygame.draw.polygon(screen, (100, 122, 117), opposite_hills4)
    pygame.draw.polygon(screen, (56, 70, 64), opposite_hills1)
    pygame.draw.polygon(screen, (56, 70, 64), opposite_hills2)
    pygame.draw.polygon(screen, (56, 70, 64), opposite_hills3)


    # LANDSCAPE
    pygame.draw.rect(screen, (104, 138, 92), (0, 180, angie_width, 120))
    pygame.draw.polygon(screen, (61, 84, 57), ((269, 180), (40, 270), (420, 270)))
    pygame.draw.polygon(screen, (30, 51, 27), ((269, 180), (110, 270), (380, 270)))
    pygame.draw.polygon(screen, (160, 178, 150), ((269, 180), (110, 270), (120, 270)))
    pygame.draw.polygon(screen, (139, 129, 94), ((269, 180), (0, 270), (55, 270)))

    # TREES
    tree_x_angie = 0
    tree_count = 26
    # DRAW 5 TREES + EACH TREE SHIFTS 28 PIXELS
    for tree_x_angie in range(tree_count):
        pygame.draw.polygon(screen, (33, 31, 25), ((28 + tree_x_angie * 28, 160), (47 + tree_x_angie * 28, 180), (10 + tree_x_angie * 28, 180)))

    # WIND
    pygame.draw.line(screen, (255, 255, 255), (-10 + wind_x_angie, 130), (80 + wind_x_angie, 130), width=4)
    pygame.draw.line(screen, (255, 255, 255), (-30 + wind_x_angie, 150), (150 + wind_x_angie, 150), width=4)
    pygame.draw.line(screen, (255, 255, 255), (0 + wind_x_angie, 26), (60 + wind_x_angie, 26), width=4)
    pygame.draw.line(screen, (255, 255, 255), (-60 + wind_x_angie, 85), (20 + wind_x_angie, 85), width=4)
    pygame.draw.line(screen, (255, 255, 255), (-50 + wind_x_angie, 95), (100 + wind_x_angie, 95), width=4)
    # ----------------------------------------------------------------------------------------
 

    # Must have these coordinates
    x = 1920
    y = 1440
    width = 640
    height = 480

    frames_gallo += 1
    text_scale_gallo = abs((math.sin(frames_gallo / 30) - 3) / 3)
    

    # Rather than screen.fill, draw a rectangle
    screen.blit(bg_gallo, (x, y))

    screen.blit(welcome_text_gallo, (x + width//2 - welcome_text_gallo.get_width()//2, y + height//3 - welcome_text_gallo.get_height()//2))
    scaled_text = pygame.transform.scale(text_gallo, (text_gallo.get_width() * text_scale_gallo, text_gallo.get_height() * text_scale_gallo))
    screen.blit(scaled_text, (x + width//2 - scaled_text.get_width()//2, y + height//2 - scaled_text.get_height()//2))
    


    # LEAVE HERE --------------------------------------------
    screen_width, screen_height = screen.get_size()
    scaled_screen = pygame.transform.scale(screen, (int(screen_width * scale), int(screen_height * scale)))
    window.blit(scaled_screen, (-camera_x*scale+WIDTH//2, -camera_y*scale+HEIGHT//2))

    pygame.display.flip()
    clock.tick(30)
    #---------------------------------------------------------


pygame.quit()
