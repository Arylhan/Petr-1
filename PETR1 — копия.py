import arcade as ar
import random as ran

WIDTH = 1024
HEIGHT = 750
TITLE = "PETR 1"



class Petya2(ar.Sprite):
    def __init__(self): 
        super().__init__()
        self.texture = ar.load_texture("Resourse\шаг__вправо_1[1].png")

       


        self.scale = 0.25
        self.center_x = 20
        self.center_y = 150



    def update(self ):

        self.center_x += self.change_x 
        self.center_y += self.change_y

class orel(ar.Sprite):
    def __init__(self): 
       super().__init__()
       self.scale = 0.3
       img = ar.load_texture("Resourse\орёл.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\орёл.png")
       self.textures.append(img)
       self.set_texture(ran.randint(0, 1))
       self.center_x = ran.randint(WIDTH,WIDTH+1000 )
       self.center_y = ran.randint(HEIGHT-570,HEIGHT-570)

       self.change_x = ran.randint(-3, -2)

    def update(self):
        self.center_x += self.change_x

class Potatob(ar.Sprite):
    def __init__(self): 
       super().__init__()
       self.scale = 0.5
       img = ar.load_texture("Resourse\золотая картошка.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\золотая картошка.png")
       self.textures.append(img)
       self.set_texture(ran.randint(0, 1))
       self.center_x = ran.randint(0, WIDTH)
       self.center_y = ran.randint(HEIGHT, HEIGHT+250)

       self.change_y = ran.randint(-5, -1)
    def update(self):
        self.center_y += self.change_y
       
class Potatou(ar.Sprite):    
    def __init__(self): 
       super().__init__()
       self.scale = 0.5   
       img = ar.load_texture("Resourse\золотая картошка.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\золотая картошка.png")
       self.textures.append(img) 
       self.set_texture(ran.randint(0, 1))
       self.center_x = ran.randint(0, WIDTH)
       self.center_y = ran.randint(HEIGHT, HEIGHT+250)

       self.change_y = ran.randint(-5, -1)
    def update(self):
        self.center_y += self.change_y

class gPotato(ar.Sprite):
    def __init__(self): 
       super().__init__()
       self.scale = 0.5
       img = ar.load_texture("Resourse\гнилая картошка.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\гнилая картошка.png")
       self.textures.append(img)
       self.set_texture(ran.randint(0, 1))
       self.center_x = ran.randint(0, WIDTH)
       self.center_y = ran.randint(HEIGHT, HEIGHT+250)

       self.change_y = ran.randint(-5, -1)

    def update(self):
        self.center_y += self.change_y

class Potato(ar.Sprite):
    def __init__(self): 
       super().__init__()
       self.scale = 0.5
       img = ar.load_texture("Resourse\картошка.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\картошка.png")
       self.textures.append(img)
       img = ar.load_texture("Resourse\картошка.png")
       self.textures.append(img)
       self.set_texture(ran.randint(0, 2))
       self.center_x = ran.randint(0, WIDTH)
       self.center_y = ran.randint(HEIGHT, HEIGHT+250)

       self.change_y = ran.randint(-5, -1)

    def update(self):
        self.center_y += self.change_y

class Petya(ar.Sprite):
    def __init__(self): 
        super().__init__()
        self.texture = ar.load_texture("Resourse\петр 1.png")

       


        self.scale = 0.25
        self.center_x = 500
        self.center_y = 150



    def update(self ):

        self.center_x += self.change_x 
        self.center_y += self.change_y

class Menu2(ar.View):
    def __init__(self):
        super().__init__()

        self.start = ar.SpriteList()
        button = ar.Sprite("Resourse\lvl1 (1).png")
        button.scale = 1.5
        button.center_x = 150
        button.center_y = 350
    
        self.start2 = ar.SpriteList()
        button2 = ar.Sprite("Resourse\lvl2.png")
        button2.scale = 1.5
        button2.center_x = 150
        button2.center_y = 170

        self.start3 = ar.SpriteList()
        button3 = ar.Sprite("Resourse\lvl3.png")
        button3.scale = 1.5
        button3.center_x = 530
        button3.center_y = 310


        self.start4 = ar.SpriteList()
        button4 = ar.Sprite("Resourse\lvl4.png")
        button4.scale = 1.5
        button4.center_x = 880
        button4.center_y = 350
    
        self.start5 = ar.SpriteList()
        button5 = ar.Sprite("Resourse\lvl5.png")
        button5.scale = 1.5
        button5.center_x = 880
        button5.center_y = 170

        self.close = ar.SpriteList()
        but = ar.Sprite("Resourse\exit.png")
        but.scale = 0.8
        but.center_x = 530
        but.center_y = -150


        self.close.append(but)
        self.start.append(button)
        self.start2.append(button2)
        self.start3.append(button3)
        self.start5.append(button5)
        self.start4.append(button4)
       
    def on_show(self):
        ar.set_background_color(ar.color.WHITE)
    
    def on_draw(self):
        ar.start_render()
        fon = ar.load_texture("Resourse\меню.png")
        ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT,fon)
        fon = ar.load_texture("Resourse\логотип.png")
        ar.draw_texture_rectangle(WIDTH/2+30, HEIGHT/2+250, WIDTH, HEIGHT,fon)
               


        self.start.draw()
        self.start3.draw()
        self.start2.draw()
        self.close.draw()
        self.start5.draw()
        self.start4.draw() 



  

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == ar.MOUSE_BUTTON_LEFT and ar.get_sprites_at_point((x,y), self.start):
            view = Instruction1()
            self.window.show_view(view)
        if button == ar.MOUSE_BUTTON_LEFT and ar.get_sprites_at_point((x,y), self.start2):
            view = Instruction2()
            self.window.show_view(view)
     

        if button == ar.MOUSE_BUTTON_LEFT and ar.get_sprites_at_point((x,y) , self.close):
            ar.close_window()

class Instruction1(ar.View):
    def on_show(self):
        ar.set_background_color(ar.color.ORANGE_PEEL)

    def on_draw(self):
        ar.start_render()
        fon = ar.load_texture("Resourse\инструкция.png")
        ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT,fon)

    def on_mouse_press(self, x, y, button, modifiers):
        # Переход в игру 
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

class Instruction2(ar.View):
    def on_show(self):
        ar.set_background_color(ar.color.ORANGE_PEEL)

    def on_draw(self):
        ar.start_render()
        fon = ar.load_texture("Resourse\инструкция2.png")
        ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT,fon)

    def on_mouse_press(self, x, y, button, modifiers):
        # Переход в игру 
        game_view = Game2()
        game_view.setup()
        self.window.show_view(game_view)

class Game(ar.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.view_left = 0 
        self.view_bottom = 0
        self.hp = None
        self.score = None



        
        self.potato_list = ar.SpriteList()
        self.gpotato_list = ar.SpriteList()
        self.potatob_list = ar.SpriteList()
        self.potatou_list = ar.SpriteList()
        self.bg_sound = ar.Sound("Resourse\e4c1fdca51422a9.mp3")
    

    def setup(self):
        ar.set_background_color(ar.color.WHITE)
        self.hp = 3
        self.score = 0 
        self.player = Petya()
        self.bg_sound.play(0.2, loop=True)

        for i in range(7):
            p = Potato()
            self.potato_list.append(p)

        for i in range(5):
            g = gPotato()
            self.gpotato_list.append(g)


        for i in range(1):
            g = Potatob()
            self.potatob_list.append(g)
        

        for i in range(1):
            g = Potatou()
            self.potatou_list.append(g)
    
        
    def on_draw(self):
        ar.start_render()
        fon = ar.load_texture("Resourse\лес.png")
        ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT,fon)
        self.player.draw()
        ar.draw_text(f"здоровье: {self.hp}", self.view_left+50, self.view_bottom+700, ar.color.RED, 40 )
        ar.draw_text(f"картошка: {self.score}", self.view_left+50, self.view_bottom+650, ar.color.RED_BROWN, 40 )
        self.potato_list.draw()
        self.gpotato_list.draw()
        self.potatou_list.draw()
        self.potatob_list.draw()
        

        if self.score >= 10:
            ar.start_render()
            fon = ar.load_texture("Resourse\меню.png")
            ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, fon)
            ar.draw_text("ТЫ ПРОШЕЛ", WIDTH/2-200, HEIGHT/2, ar.color.RED_ORANGE, 40 )
            ar.draw_text("нажмите пробел чтобы пройти дальше", WIDTH/2-230, HEIGHT/2-30, ar.color.GRAY,15)

            img = ar.load_texture("Resourse\ему хорошо.png")
            ar.draw_texture_rectangle(WIDTH/2-350, HEIGHT/2,WIDTH, HEIGHT, img)
        if self.hp <= 0:
            ar.start_render()
            fon = ar.load_texture("Resourse\меню.png")
            ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, fon)
            ar.draw_text("ИГРА НЕ ПРОЙДЕНА", WIDTH/2-200, HEIGHT/2, ar.color.BLUE, 40 )
            ar.draw_text("нажмите пробел чтобы начать заново", WIDTH/2-200, HEIGHT/2-30, ar.color.GRAY, 15)
            img = ar.load_texture("Resourse\ему плохо.png")
            ar.draw_texture_rectangle(WIDTH/2-300, HEIGHT/2,WIDTH, HEIGHT, img)

        


    def on_update(self, delta_time):
        self.player.update()
        self.potato_list.update()
        self.gpotato_list.update()
        self.potatou_list.update()
        self.potatob_list.update()


        ar.set_viewport(self.view_left, self.view_left+WIDTH, self.view_bottom, self.view_bottom+HEIGHT)
        if self.score == 5:
            b = Potatob()
            b.center_x = ran.randint(self.view_left+WIDTH, self.view_left+WIDTH+200)
            b.center_y = ran.randint(200, HEIGHT-100)
            b.change_y = -2
            self.potatob_list.append(b)
            self.score = 6



        if self.score == 5:
            u = Potatou()
            u.center_x = ran.randint(self.view_left+WIDTH, self.view_left+WIDTH+200)
            u.center_y = ran.randint(900, 100)
            u.change_y = -2
            self.potatou_list.append(u)
            self.score = 6
        


        for potato in self.potato_list:
            if ar.check_for_collision(self.player, potato):
                potato.kill()
                self.score += 1
                p = Potato() 
                self.potato_list.append(p)
            

        for gpotato in self.gpotato_list:
            if ar.check_for_collision(self.player, gpotato):
                gpotato.kill()
                self.hp -= 1
                g = gPotato()
                self.gpotato_list.append(g)
                
        for potatob in self.potatob_list:
            if ar.check_for_collision(self.player, potatob):
                potatob.kill()
                self.score += 4
                b = Potatob() 
                self.potatob_list.append(b)

        for potatou in self.potatou_list:
            if ar.check_for_collision(self.player, potatou):
                potatou.kill()
                self.score -= 5
                u = Potatou() 
                self.potatou_list.append(u)
    
        



        
    
 
    
    # метод управления клавиатурой
    def on_key_press(self,key,modifiers):
        if key == ar.key.A:
            self.player.change_x = -5
        elif key == ar.key.D:
            self.player.change_x = 5
        if key == ar.key.SPACE:


   
            menu_view = Menu2()
            self.window.show_view(menu_view)
 
            
      
            
   

    # метод для остановки игрока если нет нажатия
    def on_key_release(self,key,modifiers):
        if key == ar.key.A:
            self.player.change_x = 0
        elif key == ar.key.D:
            self.player.change_x = 0
       
class Game2(ar.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.view_left = 0 
        self.view_bottom = 0
        self.hp = None
        self.orel_list = ar.SpriteList()
    def setup(self):
        ar.set_background_color(ar.color.WHITE)
        self.hp = 1 
        self.player = Petya2()

        for i in range(5):
            p = orel()
            self.orel_list.append(p)

    def on_draw(self):
        ar.start_render()
        fon = ar.load_texture("Resourse\поле.png")
        ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT,fon)
        self.player.draw()
        ar.draw_text(f"здоровье: {self.hp}", self.view_left+50, self.view_bottom+700, ar.color.RED, 40 )
        if self.hp <= 0:
            ar.start_render()
            fon = ar.load_texture("Resourse\меню.png")
            ar.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, fon)
            ar.draw_text("ИГРА НЕ ПРОЙДЕНА", WIDTH/2-200, HEIGHT/2, ar.color.BLUE, 40 )
            ar.draw_text("нажмите пробел чтобы начать заново", WIDTH/2-200, HEIGHT/2-30, ar.color.GRAY, 15)

    
        self.orel_list.draw()

    def on_update(self, delta_time):
        self.player.update()
        self.orel_list.update()


        for orel in self.orel_list:
            if ar.check_for_collision(self.player, orel):
                orel.kill()
                self.hp -= 1
                g = orel()
                self.orel_list.append(g)


    def on_key_press(self,key,modifiers):
        if key == ar.key.E:
            self.player.change_y = 15
        if key == ar.key.D:
            self.player.change_x = 5
        if key == ar.key.SPACE:

            menu_view = Menu2()
            self.window.show_view(menu_view)
                  
    # метод для остановки игрока если нет нажатия
    def on_key_release(self,key,modifiers):
        

        if key == ar.key.D:
            self.player.change_x = 0
        if key == ar.key.E:
            self.player.change_y = 0
       
def main():
    window = ar.Window(WIDTH, HEIGHT, TITLE)
    menu_view = Menu2()
    window.show_view(menu_view)

    ar.run()
main()