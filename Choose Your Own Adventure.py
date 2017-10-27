import turtle
import random
import time

'''
alpha = Character One, Warrior
beta = Character Two, Mage

gamma = Writes messages to user (excluding confused)
delta = Tells user when not recognized input is given
epsilon = Handles screen-fades
zeta = displays health during battle
eta = handles menu borders

omega = Boss

'''

def title_screen(alpha,beta,gamma,delta,eta,zeta,omega):
   # This screen gives the user an introduction into the program.

   treasure(beta)

   interface_1(gamma,eta)

   alpha.turtlesize(2,2,2)
   beta.turtlesize(2,2,2)
   omega.turtlesize(3,3,3)

   gamma.goto(-430,300)
   gamma.write("This is a simulation of a boss encounter from ",align="left",font=("Arial",30,"normal"))
   gamma.goto(-430, 250)
   gamma.write("the game 'Final Fantasy', a turn-based rpg.", align="left", font=("Arial", 30, "normal"))
   gamma.goto(-430, 150)
   gamma.write("The battle gives a lot of freedom with how you", align="left", font=("Arial", 30, "normal"))
   gamma.goto(-430, 100)
   gamma.write("can go about winning, so try your best.", align="left", font=("Arial", 30, "normal"))
   gamma.goto(-620, -320)
   gamma.write("Use the Console in Python to make choices.", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-600, -370)
   gamma.write("Type '1' to begin.", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-600, -420)
   gamma.write("Type '0' to cancel and quit the game.", align="left", font=("Arial", 24, "normal"))

   alpha.speed(3)
   beta.speed(3)
   omega.speed(3)

   alpha.goto(-300,-135)
   alpha.write("I'm Alpha!", align="center", font=("Arial", 24, "normal"))
   alpha.showturtle()
   alpha.goto(-300, -150)

   beta.setheading(180)
   beta.goto(300, -135)
   beta.write("I'm Beta!", align="center", font=("Arial", 24, "normal"))
   beta.showturtle()
   beta.goto(300, -150)

   while True:
       str1 = int(input("Ready for a response!"))
       if str1 == 1 or str1 == 0:
           beta.clear()
           gamma.clear()
           delta.clear()
           return str1
       else:
           confused(delta)

def treasure(beta):
   for loop in range(6):
       beta.tracer(20)
       beta.pensize(4)
       beta.fillcolor("gold")
       beta.begin_fill()
       beta.circle(15)
       beta.end_fill()
       beta.fillcolor("blue")

       beta.rt(60)
       beta.fd(25)

   beta.setheading(180)
   beta.tracer(1)

def interface_bat1(gamma,eta):
   # Battle interface for Alpha
   counter = 1

   gamma.clear()
   gamma.tracer(20)

   for lines in range(2):
       gamma.goto(-640+256*counter,-250)
       gamma.down()
       gamma.goto(-640+256*counter,-640)
       counter = counter + 1
       gamma.up()

   gamma.fillcolor("cornflowerblue")
   gamma.goto(-640, -250)
   gamma.begin_fill()
   gamma.down()
   gamma.goto(-640, -200)
   gamma.goto(-640 + 512, -200)
   gamma.goto(-640 + 512, -250)
   gamma.end_fill()
   gamma.up()
   gamma.goto(-620, -250)
   gamma.write("What should Alpha do?", align="left", font=("Arial", 24, "normal"))

   gamma.goto(-620,-300)
   gamma.write("'1' - Attack", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-600, -330)
   gamma.write("- Attacks Omega for", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-600, -360)
   gamma.write("  40-60 damage", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620+256,-300)
   gamma.write("'2' - Defend", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -330)
   gamma.write("- Blocks 50% of incoming", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -360)
   gamma.write("  damage (1 turn)", align="left", font=("Arial", 16, "normal"))

   gamma.tracer(1)


def interface_bat2(gamma, eta):
   # Battle interface for Beta
   counter = 1

   gamma.clear()
   gamma.tracer(20)

   for lines in range(2):
       gamma.goto(-640 + 256 * counter, -250)
       gamma.down()
       gamma.goto(-640 + 256 * counter, -640)
       counter = counter + 1
       gamma.up()

   gamma.fillcolor("cornflowerblue")
   gamma.goto(-640,-250)
   gamma.begin_fill()
   gamma.down()
   gamma.goto(-640,-200)
   gamma.goto(-640+512,-200)
   gamma.goto(-640+512,-250)
   gamma.end_fill()
   gamma.up()
   gamma.goto(-620,-250)
   gamma.write("What should Beta do?", align="left", font=("Arial", 24, "normal"))

   gamma.goto(-620, -300)
   gamma.write("'1' - Attack", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-600, -330)
   gamma.write("- Attacks Omega", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620 + 256, -300)
   gamma.write("'2' - Defend", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -330)
   gamma.write("- Blocks incoming damage", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -360)
   gamma.write("  (1 turn)", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620 + 256, -390)
   gamma.write("'3' - Cure A", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -420)
   gamma.write("- Heals Alpha", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620 + 256, -480)
   gamma.write("'4' - Cure B", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256, -510)
   gamma.write("- Heals Beta", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620 + 256*2, -300)
   gamma.write("'5' - Temper A", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256*2, -330)
   gamma.write("- Buffs Alpha's damage", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256 * 2, -360)
   gamma.write("  (entire fight)", align="left", font=("Arial", 16, "normal"))

   gamma.goto(-620 + 256*2, -390)
   gamma.write("'6' - Temper B", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256*2, -420)
   gamma.write("- Buffs Beta's damage", align="left", font=("Arial", 16, "normal"))
   gamma.goto(-620 + 256 * 2, -450)
   gamma.write("  (entire fight)", align="left", font=("Arial", 16, "normal"))

   gamma.tracer(1)

def interface_1(gamma,eta):
   # Basic interface

   gamma.clear()
   eta.tracer(20)

   eta.goto(-640, -250)
   eta.down()
   eta.fillcolor("cornflowerblue")
   eta.begin_fill()
   eta.goto(640, -250)
   eta.goto(640,-640)
   eta.goto(-640,-640)
   eta.goto(-640,-250)
   eta.end_fill()

   counter = 3

   for lines in range(2):
       eta.goto(-640 + 256 * counter, -250)
       eta.down()
       eta.goto(-640 + 256 * counter, -640)
       eta.up()
       counter = counter + 1

   eta.tracer(1)

def choice_1(alpha, beta, gamma, delta, epsilon, zeta, omega):
   # This function gives the user the option of deciding to approach the treasure.

   alpha.clear()
   beta.clear()
   epsilon.clear()

   quit_message(epsilon)

   gamma.goto(-430, 440)
   gamma.write("The world is in danger,", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-430, 400)
   gamma.write("and many people are sad.", align="left", font=("Arial", 24, "normal"))
   for joining in range(34):
       alpha.fd(3)
       beta.fd(3)

   gamma.goto(-430, 340)
   gamma.write("As the King requested, your", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-430, 300)
   gamma.write("party goes on an adventure.", align="left", font=("Arial", 24, "normal"))
   for joining in range(33):
       alpha.fd(3)
       beta.fd(3)

   gamma.goto(-430, 240)
   gamma.write("During your journey, you", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-430, 200)
   gamma.write("stumble upon some treasure", align="left", font=("Arial", 24, "normal"))
   gamma.goto(-430, 160)
   gamma.write("in a cave.", align="left", font=("Arial", 24, "normal"))
   for joining in range(33):
       alpha.fd(3)
       beta.fd(3)

   beta.hideturtle()
   beta.goto(0, 570)
   treasure(beta)

   alpha.lt(90)
   alpha.fd(70)

   gamma.goto(-620, -330)
   gamma.write("What do you want to do?", align="left", font=("Arial", 24, "normal"))
   time.sleep(1)
   gamma.goto(-600, -380)
   gamma.write("'1' - Sure, I'll approach the treasure.", align="left", font=("Arial", 24, "normal"))
   time.sleep(0.5)
   gamma.goto(-600, -430)
   gamma.write("'2' - Nah, there's probably a forced encounter.", align="left", font=("Arial", 24, "normal"))

   while True:
       str1 = int(input("Ready for a response!"))
       if str1 == 1 or str1 == 2 or str1 == 0:
           gamma.clear()
           delta.clear()
           return str1
       else:
           confused(delta)

def choice_2(alpha, beta, gamma, delta, epsilon, zeta, eta, omega):
   # This function asks if the user is ready to start the battle.

   alpha.fd(300)

   omega.goto(0,380)
   omega.setheading(270)
   omega.showturtle()

   gamma.goto(0,450)
   gamma.write("Foolish adventurers, this is not your treasure!", align="center", font=("Arial", 24, "normal"))
   time.sleep(1)
   gamma.goto(0, 410)
   gamma.write("Prepare to face my wrath!", align="center", font=("Arial", 24, "normal"))
   time.sleep(3)

   screen_fade(alpha,beta,epsilon,omega)

   gamma.clear()
   epsilon.clear()

   alpha.tracer(10)

   alpha.showturtle()
   alpha.goto(300, 300)
   alpha.setheading(180)

   beta.showturtle()
   beta.goto(300, -100)
   beta.setheading(180)

   omega.showturtle()
   omega.goto(-300, 100)
   omega.setheading(0)

   alpha.tracer(1)

   gamma.goto(300, 330)
   gamma.write("This is Alpha; he's your Warrior.", align="center", font=("Arial", 20, "normal"))
   gamma.goto(300, -70)
   gamma.write("This is Beta; she's your Support Mage.", align="center", font=("Arial", 20, "normal"))
   gamma.goto(-300, 130)
   gamma.write("This is Omega. Defeat him!", align="center", font=("Arial", 20, "normal"))

   gamma.goto(-620, -330)
   gamma.write("Ready to start the battle?", align="left", font=("Arial", 24, "normal"))
   time.sleep(1)
   gamma.goto(-600, -380)
   gamma.write("'1' - Yes, now start!", align="left", font=("Arial", 24, "normal"))
   time.sleep(0.5)
   gamma.goto(-600, -430)
   gamma.write("'2' - Too hard, I quit!", align="left", font=("Arial", 24, "normal"))

   while True:
       str1 = int(input("Ready for a response!"))
       if str1 == 1 or str1 == 2 or str1 == 0:
           gamma.clear()
           delta.clear()
           return str1
       else:
           confused(delta)


def battle(alpha,beta,gamma,delta,epsilon,zeta,eta,omega):
   # This function sets up the battle, and it also interprets the results given by the battle_turn function.

   quit_message(epsilon)

   gamma.goto(400,-300)

   battle_result = battle_turn(alpha,beta,gamma,delta,zeta,eta,omega)

   if battle_result == 1:
       return 1
   elif battle_result == 2:
       return 2
   else:
       return 0

def battle_turn(alpha,beta,gamma,delta,zeta,eta,omega):
   # This function deals with player and boss health, while also regulating the turns taken.
   # The function does not return a value until one side is completely wiped out.
   alpha_health = 200
   beta_health = 125
   omega_health = 300

   alpha_attack_min = 40
   alpha_attack_max = 60

   beta_attack_min = 20
   beta_attack_max = 40

   omega_attack_min = 50
   omega_attack_max = 65

   alpha_temper = False
   beta_temper = False

   while omega_health > 0:
       # Inputs are received at the start of each turn.
       # Inputs are not asked of when a character is downed.
       omega_output = omega_input()
       if alpha_health > 0:
           interface_bat1(gamma,eta)
           alpha_output = alpha_input(delta)
           if alpha_output == 0:
               return 0
       if beta_health > 0:
           interface_bat2(gamma,eta)
           beta_output = beta_input(delta)
           if beta_output == 0:
               return 0

       interface_1(gamma, eta)

       # If the user signals to defend for either character, it is executed before damage is dealt.
       if alpha_output == 2:
           alpha_defend = True
           print("Alpha is defending")
       else:
           alpha_defend = False

       if beta_output == 2:
           beta_defend = True
           print("Beta is defending")
       else:
           beta_defend = False

       # Attack values are calculated
       alpha_attack = random.randrange(alpha_attack_min, alpha_attack_max+1)
       beta_attack = random.randrange(beta_attack_min, beta_attack_max + 1)
       omega_attack = random.randrange(omega_attack_min, omega_attack_max + 1)

       # Alpha's turn
       if alpha_health > 0:
           if alpha_output == 1:
               # Attack: Deals damage to omega (base 50)
               alpha.fd(40)
               alpha.rt(360)
               omega_health = omega_health - alpha_attack

               gamma.goto(-300,130)
               gamma.write(-alpha_attack, align="left", font=("Arial", 16, "normal"))

               omega.rt(30)
               omega.lt(30)

               alpha.bk(40)
               gamma.clear()

       health_check(alpha_health, beta_health, omega_health)

       health(alpha_health, beta_health, omega_health, zeta)

       # Beta's turn
       if beta_health > 0:
           if beta_output == 1:
               # Attack: Deals damage to omega (base 30)
               beta.fd(40)
               beta.rt(360)
               omega_health = omega_health - beta_attack

               gamma.goto(-300, 130)
               gamma.write(-beta_attack, align="left", font=("Arial", 16, "normal"))

               omega.rt(30)
               omega.lt(30)
               beta.bk(40)
               gamma.clear()

           elif beta_output == 3:
               # CureA: Heals Alpha for 35 health, if he is alive
               beta.fd(40)
               gamma.goto(300, -70)
               gamma.write("Cure A!", align="left", font=("Arial", 16, "normal"))
               beta.rt(360)
               gamma.clear()
               beta.bk(40)

               if alpha_health > 0:
                   alpha_health = alpha_health + 35
                   gamma.goto(300, 330)
                   gamma.write("+35", align="left", font=("Arial", 16, "normal"))
                   alpha.rt(360)
                   gamma.clear()
               else:
                   gamma.goto(300, 330)
                   gamma.write("No effect, Alpha is down!", align="left", font=("Arial", 16, "normal"))
                   time.sleep(2)
                   gamma.clear()
                   print("No effect, Alpha is down!")

           elif beta_output == 4:
               # CureB: Heals Beta for 35 health, if she is alive
               beta.fd(40)
               gamma.goto(300, -70)
               gamma.write("Cure B", align="left", font=("Arial", 16, "normal"))
               beta.rt(360)
               gamma.clear()
               beta.bk(40)

               beta_health = beta_health + 35
               gamma.goto(300, -70)
               gamma.write("+35", align="left", font=("Arial", 16, "normal"))
               beta.rt(360)
               gamma.clear()

           elif beta_output == 5:
               # TemperA: Buff Alpha's damage by 50%
               print("Beta casts 'Temper' on Alpha!")
               beta.fd(40)
               gamma.goto(300, -70)
               gamma.write("Temper A!", align="left", font=("Arial", 16, "normal"))
               beta.rt(360)
               gamma.clear()
               beta.bk(40)

               if alpha_health > 0:
                   if alpha_temper == False:
                       alpha_attack = alpha_attack * 1.5
                       gamma.goto(300, 330)
                       gamma.write("Tempered!", align="left", font=("Arial", 16, "normal"))
                       print("    Alpha is now Tempered!")
                       alpha.rt(360)
                       gamma.clear()
                       alpha_temper = True
                   else:
                       gamma.goto(300, 330)
                       gamma.write("No effect, Alpha is already tempered!", align="left", font=("Arial", 16, "normal"))
                       time.sleep(2)
                       gamma.clear()
                       print("    No effect, Alpha is already tempered!")
               else:
                   gamma.goto(330)
                   gamma.write("No effect, Alpha is already tempered!", align="left", font=("Arial", 16, "normal"))
                   time.sleep(2)
                   gamma.clear()
                   print("    No effect, Alpha is down!")

           elif beta_output == 6:
               # TemperB: Buff Beta's damage by 50%
               print("Beta casts 'Temper' on Beta!")

               beta.fd(40)
               gamma.goto(300, -70)
               gamma.write("Temper B!", align="left", font=("Arial", 16, "normal"))
               beta.rt(360)
               gamma.clear()
               beta.bk(40)

               if beta_temper == False:
                   beta_attack = beta_attack*1.5
                   gamma.goto(300, -70)
                   gamma.write("Tempered!", align="left", font=("Arial", 16, "normal"))
                   print("    Beta is now Tempered!")
                   beta.rt(360)
                   beta.clear()
                   beta_temper = True
               else:
                   gamma.goto(300, -70)
                   gamma.write("No effect, Beta is already tempered!", align="left", font=("Arial", 16, "normal"))
                   time.sleep(2)
                   beta.clear()
                   print("    No effect, Beta is already tempered!")
               gamma.clear()

       health_check(alpha_health, beta_health, omega_health)

       health(alpha_health, beta_health, omega_health, zeta)

       # Omega's turn
       if omega_output == 1:
           omega.fd(40)
           omega.rt(360)
           # Omega attacks Alpha (or Beta if Alpha is down)
           if alpha_health > 0:
               alpha.rt(30)
               alpha.lt(30)
               if alpha_defend == False:
                   alpha_health = alpha_health - omega_attack
                   gamma.goto(300, 330)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   alpha_health = alpha_health - omega_attack*0.5
                   gamma.goto(300,330)
                   gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))
           else:
               beta.rt(30)
               beta.lt(30)
               if beta_defend == False:
                   beta_health = beta_health - omega_attack
                   gamma.goto(300, -70)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   beta_health = beta_health - omega_attack * 0.5
                   gamma.goto(300, -70)
                   gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))
           omega.clear()
           omega.bk(40)
           gamma.clear()

       elif omega_output == 2:
           omega.fd(40)
           omega.rt(360)
           # Omega attacks Beta (or Alpha if Beta is down)
           if beta_health > 0:
               beta.rt(30)
               beta.lt(30)
               if beta_defend == False:
                   beta_health = beta_health - omega_attack
                   gamma.goto(300, -70)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   beta_health = beta_health - omega_attack*0.5
                   gamma.goto(300, -70)
                   gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))
           else:
               alpha.rt(30)
               alpha.lt(30)
               if alpha_defend == False:
                   alpha_health = alpha_health - omega_attack
                   gamma.goto(300, 330)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   alpha_health = alpha_health - omega_attack*0.5
                   gamma.goto(300, 330)
                   gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))
           omega.bk(40)
           gamma.clear()

       elif omega_output == 3:
           omega.fd(40)
           gamma.goto(-300, 0)
           gamma.write("Fira!", align="left", font=("Arial", 16, "normal"))
           omega.rt(360)
           gamma.clear()
           # Fira - Damages both allies with normal attack damage
           alpha.rt(30)
           alpha.lt(30)

           beta.rt(30)
           beta.lt(30)
           if alpha_defend == False:
               alpha_health = alpha_health - omega_attack
               gamma.goto(300, 330)
               gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
           else:
               alpha_health = alpha_health - omega_attack*0.5
               gamma.goto(300, 330)
               gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))

           if beta_defend == False:
               beta_health = beta_health - omega_attack
               gamma.goto(300, -70)
               gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
           else:
               beta_health = beta_health - omega_attack * 0.5
               gamma.goto(300, -70)
               gamma.write(-0.5*omega_attack, align="left", font=("Arial", 16, "normal"))
           omega.bk(40)
           gamma.clear()

       elif omega_output == 4:
           omega.fd(40)
           omega.rt(360)
           # Omega attacks Alpha (or Beta if Alpha is down)
           if alpha_health > 0:
               alpha.rt(30)
               alpha.lt(30)
               if alpha_defend == False:
                   alpha_health = alpha_health - omega_attack
                   gamma.goto(300, 330)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   alpha_health = alpha_health - omega_attack * 0.5
                   gamma.goto(300, 330)
                   gamma.write(-0.5 * omega_attack, align="left", font=("Arial", 16, "normal"))
           else:
               beta.rt(30)
               beta.lt(30)
               if beta_defend == False:
                   beta_health = beta_health - omega_attack
                   gamma.goto(300, -70)
                   gamma.write(-omega_attack, align="left", font=("Arial", 16, "normal"))
               else:
                   beta_health = beta_health - omega_attack * 0.5
                   gamma.goto(300, -70)
                   gamma.write(-0.5 * omega_attack, align="left", font=("Arial", 16, "normal"))
           omega.clear()
           omega.bk(40)
           gamma.clear()

       health_check(alpha_health, beta_health, omega_health)

       health(alpha_health, beta_health, omega_health, zeta)

       # If both of the player's characters are downed, end game.
       if alpha_health <= 0 and beta_health <= 0:
           return 2

   health_check(alpha_health, beta_health, omega_health)

   return 1

def health_check(alpha_health,beta_health,omega_health):
   if alpha_health < 0:
       alpha_health = 0
   if beta_health < 0:
       beta_health = 0
   if omega_health < 0:
       omega_health = 0

def health(alpha_health,beta_health,omega_health,zeta):
   # During battle, turtle Zeta writes the health of all three characters.
   zeta.clear()

   zeta.speed(20)

   zeta.goto(404, -300)
   zeta.write("Alpha:", align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -330)
   zeta.write(alpha_health, align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -330)
   zeta.write(alpha_health, align="left", font=("Arial", 16, "normal"))

   zeta.goto(404, -360)
   zeta.write("Beta:", align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -390)
   zeta.write(beta_health, align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -390)
   zeta.write(beta_health, align="left", font=("Arial", 16, "normal"))

   zeta.goto(404, -420)
   zeta.write("Omega:", align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -450)
   zeta.write(omega_health, align="left", font=("Arial", 16, "normal"))
   zeta.goto(424, -450)
   zeta.write(omega_health, align="left", font=("Arial", 16, "normal"))

def alpha_input(delta):
   # This function receives a player input and interprets it to an action in-game.

       # Alpha
   # 1 - Attack for 50 damage
   # 2 - Defend to reduce incoming damage by 50 % (1 turn)

   while True:
       str1 = int(input("What should Alpha do?"))
       if str1 == 1 or str1 == 2 or str1 == 0:
           delta.clear()
           return str1
       else:
           confused(delta)


def beta_input(delta):
   # This function receives a player input and interprets it to an action in-game.

       # Beta
   # 1 - Attack for 30 damage
   # 2 - Defend to reduce incoming damage by 50 % (1 turn)
   # 3 - CureA - Heal Alpha ally for 35 health (3 energy)
   # 4 - CureB - Heal Beta ally for 35 health (3 energy)
   # 5 - TemperA - Increase damage of Alpha by 50 % (5 energy, rest of battle)
   # 6 - TemperB - Increase damage by Beta by 50 % (5 energy, rest of battle)


   while True:
       str1 = int(input("What should Beta do?"))
       if str1 == 1 or str1 == 2 or str1 == 3 or str1 == 4 or str1 == 5 or str1 == 6 or str1 == 0:
           delta.clear()
           return str1
       else:
           confused(delta)

def omega_input():
   # This function receives a random input and interprets it to a boss action in-game.

   boss_action = random.randrange(1,5)

   return boss_action

def confused(delta):
   # This runs if an input isn't recognized by the program.

   delta.pensize(7)
   delta.fillcolor("cornflowerblue")

   delta.goto(180,525)
   delta.down()
   delta.begin_fill()
   delta.goto(180, 575)
   delta.goto(535, 575)
   delta.goto(535, 525)
   delta.goto(180,525)
   delta.up()
   delta.end_fill()

   delta.goto(200, 532)
   delta.write("Sorry, didn't understand that.", align="left", font=("Arial", 24, "normal"))
   print("Sorry, didn't understand that.")

def quit_message(epsilon):
   epsilon.goto(-640+256*3+20, -300)
   epsilon.write("Type '0' to quit the", align="left", font=("Arial", 16, "normal"))
   epsilon.goto(-640+256*3+20, -330)
   epsilon.write("game at any time.", align="left", font=("Arial", 16, "normal"))

def screen_fade(alpha,beta,epsilon,omega):
   # This function provides a screen fade transition between scenes.
   for turtles in [alpha,beta,omega]:
       turtles.hideturtle()
       turtles.clear()

   epsilon.pensize(10)
   epsilon.setheading(270)
   epsilon.tracer(15)

   ult_counter = 0
   counter = 0
   for fade in range(4):
       x_start = -640 + ult_counter*10
       for fade_bar in range(32):
           epsilon.goto(x_start+40*counter,640)
           epsilon.down()
           epsilon.fd(640+250)
           epsilon.up()
           counter = counter + 1
       counter = 0
       ult_counter = ult_counter + 1

   epsilon.tracer(1)
   time.sleep(1)

def run_game(alpha,beta,gamma,delta,epsilon,zeta,eta,omega):
   # This runs the title screen
   title_num = title_screen(alpha,beta,gamma,delta,eta,zeta,omega)
   if title_num == 1:
       print("You decide to continue.")
   else:
       return 0

   # Runs the first choice
   choice_1_num = choice_1(alpha, beta, gamma, delta, epsilon, zeta, omega)
   if choice_1_num == 1:
       print("You approach the treasure.")
   elif choice_1_num == 2:
       print("You move on.")
       return 2
   else:
       return 0

   # Runs the second choice
   choice_2_num = choice_2(alpha, beta, gamma, delta, epsilon, zeta, eta, omega)
   if choice_2_num == 1:
       print("You agree to start.")
   elif choice_2_num == 2:
       print("You give up.")
       return 2
   else:
       return 0

   # Runs the battle simulation, with the number of turns determined by how well the user plays.
   battle_result = battle(alpha,beta,gamma,delta,epsilon,zeta,eta,omega)
   if battle_result == 1:
       print("You defeated Omega and claimed his treasure!")
   elif battle_result == 2:
       print("You were defeated by Omega.")
       return 2
   else:
       return 0



   return 1

def outcome(alpha,beta,gamma,delta,epsilon,zeta,eta,omega,list):
   # This function determines the final output, or the ending screen of the game.
   outcome_num = run_game(alpha,beta,gamma,delta,epsilon,zeta,eta,omega)

   if outcome_num == 0:
       for turtles in [alpha,beta,gamma,delta,epsilon,omega]:
           turtles.clear()
           turtles.hideturtle()
       screen_fade(alpha, beta, epsilon, omega)
       epsilon.clear()
       gamma.goto(0,100)
       gamma.write("Game ended.", align="center",font=("Arial", 40, "normal"))
       print("Game ended.")
   elif outcome_num == 1:
       for turtles in [alpha,beta,gamma,delta,epsilon,omega]:
           turtles.clear()
       screen_fade(alpha, beta, epsilon, omega)
       epsilon.clear()
       gamma.goto(0,350)
       gamma.write("Congratulations, you won the game.", align="center",font=("Arial", 40, "normal"))
       gamma.goto(0,300)
       gamma.write("You still do not know if you can save the world.", align="center",font=("Arial", 40, "normal"))
       gamma.goto(0,250)
       gamma.write("But, at least you got some treasure.", align="center",font=("Arial", 40, "normal"))
       print("Congratulations, you won the game.")

       alpha.goto(-300, -100)
       alpha.showturtle()

       beta.goto(300, -100)
       beta.showturtle()


   elif outcome_num == 2:
       for turtles in [alpha,beta,gamma,delta,epsilon,omega]:
           turtles.clear()
           turtles.hideturtle()
       screen_fade(alpha, beta, epsilon, omega)
       epsilon.clear()
       gamma.goto(0, 250)
       gamma.write("Game Over, You Failed.", align="center", font=("Arial", 40, "normal"))
       print("Game Over, You Failed.")

       alpha.goto(-300,-100)
       alpha.setheading(0)
       alpha.showturtle()

       beta.goto(300,-100)
       beta.setheading(180)
       beta.showturtle()


def main():
   wn = turtle.Screen()
   wn.setworldcoordinates(-640,-640,640,640)
   wn.bgcolor("lightslategrey")

   alpha = turtle.Turtle()
   beta = turtle.Turtle()

   gamma = turtle.Turtle()
   delta = turtle.Turtle()
   epsilon = turtle.Turtle()
   zeta = turtle.Turtle()
   eta = turtle.Turtle()

   omega = turtle.Turtle()

   list = [alpha, beta, gamma, delta, epsilon, zeta, eta, omega]

   for running_speed in list:
       running_speed.speed(10)
       running_speed.hideturtle()
       running_speed.up()

   alpha.speed(1)
   alpha.color("red")
   alpha.shape("turtle")

   beta.speed(1)
   beta.color("blue")
   beta.shape("turtle")

   omega.speed(1)
   omega.color("green")
   omega.shape("turtle")

   gamma.pensize(7)
   eta.pensize(7)

   outcome(alpha,beta,gamma,delta,epsilon,zeta,eta,omega,list)

   wn.exitonclick()

main()

