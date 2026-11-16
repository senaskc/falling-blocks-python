from kepoco import display, buttonL, buttonR, buttonA

import random



SCREEN_W = 72

SCREEN_H = 40



player_x = SCREEN_W // 2

player_y = SCREEN_H - 4

player_speed = 2



obstacles = []

spawn_cooldown = 0

time_alive = 0

game_over = False

victory = False

high_score = 0



display.setFPS(30)

display.disableGrayscale()

# Add this near your drawing helpers

def draw_line(x0, y0, x1, y1, colour):

    dx = abs(x1 - x0)

    dy = -abs(y1 - y0)

    sx = 1 if x0 < x1 else -1

    sy = 1 if y0 < y1 else -1

    err = dx + dy

    while True:

        set_pixel_safe(x0, y0, colour)

        if x0 == x1 and y0 == y1:

            break

        e2 = 2 * err

        if e2 >= dy:

            err += dy

            x0 += sx

        if e2 <= dx:

            err += dx

            y0 += sy



def set_pixel_safe(x, y, colour):

    if 0 <= x < SCREEN_W and 0 <= y < SCREEN_H:

        display.setPixel(x, y, colour)



def draw_rect(x, y, w, h, colour):

    for dx in range(w):

        for dy in range(h):

            set_pixel_safe(x + dx, y + dy, colour)



def draw_stickman(cx, by, colour):

    # head (5 pixels)

    set_pixel_safe(cx, by - 5, colour)

    set_pixel_safe(cx - 1, by - 5, colour)

    set_pixel_safe(cx + 1, by - 5, colour)

    set_pixel_safe(cx, by - 6, colour)

    set_pixel_safe(cx, by - 4, colour)



    # body

    draw_line(cx, by - 4, cx, by - 1, colour)



    # arms

    draw_line(cx, by - 3, cx - 3, by - 1, colour)  # left arm

    draw_line(cx, by - 3, cx + 3, by - 1, colour)  # right arm



    # legs

    draw_line(cx, by - 1, cx - 2, by + 2, colour)  # left leg

    draw_line(cx, by - 1, cx + 2, by + 2, colour)  # right leg





def stickman_aabb(cx, by):

    return cx - 2, by - 6, cx + 2, by



def reset_game():

    global obstacles, spawn_cooldown, time_alive, game_over, victory, player_x

    obstacles = []

    spawn_cooldown = 0

    time_alive = 0

    game_over = False

    victory = False

    player_x = SCREEN_W // 2



def spawn_obstacle():

    w = random.randint(4, 10)

    h = random.randint(2, 4)

    x = random.randint(0, SCREEN_W - w)

    speed = min(2, 1 + (time_alive // 600))



    obstacles.append([x, -h, w, h, speed])



def update_obstacles():

    for ob in obstacles:

        ob[1] += ob[4]

    obstacles[:] = [ob for ob in obstacles if ob[1] < SCREEN_H]



def check_collision():

    pl_l, pl_t, pl_r, pl_b = stickman_aabb(player_x, player_y)

    for x, y, w, h, _ in obstacles:

        ob_l, ob_t = x, y

        ob_r, ob_b = x + w - 1, y + h - 1

        if not (pl_r < ob_l or pl_l > ob_r or pl_b < ob_t or pl_t > ob_b):

            return True

    return False



reset_game()

SCORE_TARGET = 800  



while True:

    if not game_over and not victory:

        if buttonL.pressed():

            player_x -= player_speed

        if buttonR.pressed():

            player_x += player_speed

        if buttonA.justPressed():

            player_x += 2



        player_x = max(0, min(SCREEN_W - 1, player_x))



        if spawn_cooldown <= 0:

            spawn_obstacle()

            spawn_cooldown = max(8, 30 - (time_alive // 60))

        else:

            spawn_cooldown -= 1



        update_obstacles()

        time_alive += 1



        if time_alive >= SCORE_TARGET:

            victory = True

            high_score = max(high_score, time_alive)

            print("VICTORY DETECTED")



        if check_collision():

            game_over = True

            high_score = max(high_score, time_alive)

            print("GAME OVER")



    display.fill(display.BLACK)



    for x, y, w, h, _ in obstacles:

        draw_rect(x, y, w, h, display.WHITE)



    draw_stickman(player_x, player_y, display.WHITE)



    

    bar_len = int((time_alive / SCORE_TARGET) * SCREEN_W)

    draw_rect(0, 0, bar_len, 1, display.WHITE)



    

    hs_len = int((high_score / SCORE_TARGET) * SCREEN_W)

    draw_rect(0, SCREEN_H - 1, hs_len, 1, display.WHITE)





    if game_over:

        display.drawFilledRectangle(8, 15, 55, 9, display.DARKGRAY)

        display.drawText("Game Over", 9, 16, display.WHITE)



    if victory:

        display.drawFilledRectangle(14, 15, 43, 9, display.DARKGRAY)

        display.drawText("Victory", 15, 16, display.WHITE)



    display.update()



    if (game_over or victory) and buttonA.justPressed():

        reset_game()