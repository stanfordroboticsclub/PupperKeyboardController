from UDPComms import Publisher
import pygame

def direction_helper(trigger, opt1, opt2):
    if trigger == opt1:
        return -1
    if trigger == opt2:
        return 1
    return 0

def direction_helper(opt1, opt2):
    if opt1:
        return -1
    if opt2:
        return 1
    return 0

if __name__ == "__main__":
    pub = Publisher(8830)

    pygame.init()
    pygame.display.init()
    MESSAGE_RATE = 20
    win = pygame.display.set_mode((500,250))

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    text_surface = font.render("Click to enable.", False, (220,0,0))
    win.fill((255,255,255))
    win.blit(text_surface, (40,100))


    rx_ = 0.0
    ry_ = 0.0
    lx_ = 0.0
    ly_ = 0.0
    l_alpha = 0.15
    r_alpha = 0.3

    while True:
        pygame.event.pump()
        
        msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 0,
            "L1": 0,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": MESSAGE_RATE,
        }
        if not pygame.key.get_focused():
            print("Application not in focus! Click the application window to re-enable control.")
        else:
            key = pygame.key.get_pressed()
            msg = {}
            lx_ = l_alpha * direction_helper(key[pygame.K_a], key[pygame.K_d]) + (1 - l_alpha) * lx_
            msg["lx"] = lx_
            ly_ = l_alpha * direction_helper(key[pygame.K_s], key[pygame.K_w]) + (1 - l_alpha) * ly_
            msg["ly"] = ly_
            rx_ = r_alpha * direction_helper(key[pygame.K_LEFT], key[pygame.K_RIGHT]) + (1 - r_alpha) * rx_
            msg["rx"] = rx_
            ry_ = r_alpha * direction_helper(key[pygame.K_DOWN], key[pygame.K_UP]) + (1 - r_alpha) * ry_
            msg["ry"] = ry_
            msg["x"] = 1 if key[pygame.K_x] else 0
            msg["square"] = 1 if key[pygame.K_u] else 0
            msg["circle"] = 1 if key[pygame.K_c] else 0
            msg["triangle"] = 1 if key[pygame.K_t] else 0
            msg["dpady"] = 1.0 * direction_helper(key[pygame.K_k], key[pygame.K_i])
            msg["dpadx"] = 1.0 * direction_helper(key[pygame.K_j], key[pygame.K_l])
            msg["L1"] = 1 if key[pygame.K_q] else 0
            msg["R1"] = 1 if key[pygame.K_e] else 0
            msg["L2"] = 0
            msg["R2"] = 0
            msg["message_rate"] = MESSAGE_RATE
            print(msg)
        
        pub.send(msg)
        pygame.display.flip()
        pygame.time.wait(int(1000/MESSAGE_RATE))



