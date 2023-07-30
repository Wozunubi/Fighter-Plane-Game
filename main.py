# Description: In the near future, the central computer controlling a cargo ship was hacked, and the e-waste contained within is being diverted to an alternate destination illegally. Your final goal is to temporarily disable the cargo ship and wipe the malicious code, thus regaining control. However, the enemy will throw their e-waste at you as they try to slow you down, but you can use your weapons to vaporize them.

# Import libraries
import pygame, math, random

#<------------------------------Constants------------------------------>

# Colour tuples
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
ELECTRIC_YELLOW = (255, 190, 0)
YELLOW_WHITE = (255, 255, 200)
ORANGE = (255, 165, 0)
BROWN = (145, 112, 43)
DARK_BROWN = (101, 78, 28)
BLUE = (0, 0, 255)
SEA_BLUE = (0, 51, 205)
LASER_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
LIGHT_GREY = (240, 240, 240)
GREY = (200, 200, 200)
DARK_GREY = (180, 180, 180)
DARKER_GREY = (150, 150, 150)
BLACK = (0, 0, 0)
ASPHALT_BLACK = (19, 10, 6)

# Screen parameters
LENGTH = 800
HEIGHT = 600
SIZE = (LENGTH, HEIGHT)

# Game constants
BOSS_LIVES = 15
BOSS_HP_BAR = 140
MAX_BOSS_WEAKNESS = 3
BOSS_SPAWN_TIME = 100
MAX_ENERGY = 140
MAX_HEALTH = 190
POWERUP_AMOUNT = 50
PLAYER_RADIUS = 20
WEAKNESS_RADIUS = 15
NORMAL_RADIUS = 10
BULLET_RADIUS = 2
SEEKING_RADIUS = 150

#<------------------------------Functions------------------------------>

#<-----Character functions----->

# Drawing main character
def drawCharacter(x, y, colour):
    # Drawing right wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-2, y-10, 24, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x, y-8, 20, 10))
    
    # Drawing left wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-22, y-10, 24, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-20, y-8, 20, 10))   
    
    # Drawing right stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+3, y+8, 14, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x+5, y+10, 10, 5))      
    
    # Drawing left stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-17, y+8, 14, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-15, y+10, 10, 5))   
    
    # Drawing fuselage
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-10, y-20, 20, 40))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-8, y-18, 16, 36))
    
    # Drawing rudder
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-5, y+7, 10, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-3, y+9, 6, 10))
    
    # Drawing cockpit
    pygame.draw.circle(screen, BLUE, (x, y-10), 4)
    
# Drawing main character turning left
def drawCharacterLeft(x, y, colour):    
    # Drawing left wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-18, y-10, 20, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-16, y-8, 16, 10))        
    
    # Drawing left stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-13, y+8, 10, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-11, y+10, 6, 5))   
    
    # Drawing fuselage
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-10, y-20, 20, 40))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-8, y-18, 16, 36))
    
    # Drawing rudder
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-4, y+7, 8, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-2, y+9, 4, 10))
    
    # Drawing right wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-2, y-10, 20, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x, y-8, 16, 10))    
    
    # Drawing right stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+3, y+8, 10, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x+5, y+10, 6, 5))     
    
    # Drawing cockpit
    pygame.draw.circle(screen, BLUE, (x-3, y-10), 4)
    
# Drawing main character turning right
def drawCharacterRight(x, y, colour): 
    # Drawing right wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-2, y-10, 20, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x, y-8, 16, 10))    
    
    # Drawing right stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+3, y+8, 10, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x+5, y+10, 6, 5))     
       
    # Drawing fuselage
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-10, y-20, 20, 40))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-8, y-18, 16, 36))
    
    # Drawing rudder
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-4, y+7, 8, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-2, y+9, 4, 10))
    
    # Drawing left wing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-18, y-10, 20, 14))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-16, y-8, 16, 10))        
    
    # Drawing left stabilizer
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-13, y+8, 10, 9))
    pygame.draw.ellipse(screen, colour, pygame.Rect(x-11, y+10, 6, 5))        
    
    # Drawing cockpit
    pygame.draw.circle(screen, BLUE, (x+3, y-10), 4)
    
# Drawing afterburner effect when player uses boost
def drawAfterburn(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y+26), 9)
    pygame.draw.circle(screen, ORANGE, (x, y+22), 5)
    
# Drawing shield effect when player uses shield
def drawShield(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 25)
    
# Drawing player, hp/energy bars
def drawBar(health, energy):
    # Drawing base of both bars
    pygame.draw.rect(screen, WHITE, pygame.Rect(325, 530, 150, 15))
    pygame.draw.rect(screen, WHITE, pygame.Rect(300, 550, 200, 30))
    
    # Filling space where the coloured bars will go
    pygame.draw.rect(screen, GREY, pygame.Rect(330, 535, 140, 5))
    pygame.draw.rect(screen, GREY, pygame.Rect(305, 555, 190, 20))      
    
    # Adding colour to the bars
    pygame.draw.rect(screen, YELLOW, pygame.Rect(330, 535, energy, 5))
    pygame.draw.rect(screen, RED, pygame.Rect(305, 555, health, 20))     
     
     
     
     
     
     
#<-----Boss functions----->  
      
# Drawing boss
def drawBoss(x, y):
    # Drawing main deck
    pygame.draw.ellipse(screen, DARK_GREY, pygame.Rect(x+200, y+360, 400, 80))
    pygame.draw.polygon(screen, DARK_GREY, ((x+200, y+400), (x+600, y+400), (x+650, y), (x+150, y)))
    pygame.draw.polygon(screen, BROWN, ((x+220, y+380), (x+580, y+380), (x+630, y), (x+170, y))) 
    
    # Drawing brown stripes to simulate wood planks
    i = 0
    while i <= 380:
        pygame.draw.line(screen, DARK_BROWN, (x+(i/8)+170, y+i), (x-(i/8)+630, y+i), 5)
        i += 10
    
    # Drawing bridge of the ship
    pygame.draw.rect(screen, GREY, pygame.Rect(x+300, y, 200, 200))
    
    # Drawing helicopter pad
    pygame.draw.circle(screen, WHITE, (x+400, y+290), 70)
    pygame.draw.circle(screen, DARK_GREY, (x+400, y+290), 65)
    pygame.draw.line(screen, WHITE, (x+335, y+290), (x+465, y+290), 3)
    pygame.draw.line(screen, WHITE, (x+400, y+245), (x+400, y+335), 3)
    
    # Drawing porthole
    pygame.draw.circle(screen, BLACK, (x+400, y+420), 10)
    pygame.draw.circle(screen, GREY, (x+400, y+420), 8)
    pygame.draw.circle(screen, BLACK, (x+300, y+410), 10)
    pygame.draw.circle(screen, GREY, (x+300, y+410), 8)
    pygame.draw.circle(screen, BLACK, (x+500, y+410), 10)
    pygame.draw.circle(screen, GREY, (x+500, y+410), 8)
          
# Drawing boss hp bar
def drawBossBar(x, y, bossDead):
    pygame.draw.rect(screen, WHITE, pygame.Rect(x+325, y+20, BOSS_HP_BAR+10, 15))
    pygame.draw.rect(screen, GREY, pygame.Rect(x+330, y+25, BOSS_HP_BAR, 5))  
    pygame.draw.rect(screen, RED, pygame.Rect(x+330, y+25, (BOSS_HP_BAR/BOSS_LIVES)*(BOSS_LIVES-bossDead), 5))    
 
# Drawing weakness for player to shoot at    
def drawWeakness(x, y, boolean):
    # Checking if boolean is true or false
    if boolean:
        # If true, draw a white circle with a red outline
        pygame.draw.circle(screen, RED, (x, y), 15)
        pygame.draw.circle(screen, WHITE, (x, y), 10)
    else:
        # If false, draw a red circle with a white outline
        pygame.draw.circle(screen, WHITE, (x, y), 15)
        pygame.draw.circle(screen, RED, (x, y), 10)        
        
        
        
        
        
        
#<-----Entity functions----->     

# Drawing runway
def drawRunway(x, y):
    # Drawing main runway
    pygame.draw.polygon(screen, GREY, ((x+100, y+600), (x+700, y+600), (x+600, y+100), (x+200, y+100)))
    pygame.draw.polygon(screen, ASPHALT_BLACK, ((x+110, y+600), (x+690, y+600), (x+590, y+100), (x+210, y+100)))
    
    # Looping through 4 times
    for i in range(4):
        # Drawing runway stripes at 140 pixel intervals
        pygame.draw.rect(screen, WHITE, pygame.Rect(x+390, y+150+(i*140), 20, 40))
        
    # Drawing runway number
    screen.blit(fontShipNum.render("76", 1, WHITE), pygame.Rect(x+355, y+190, 100, 100))

# Drawing waves
def drawWaves(x, y):
    pygame.draw.line(screen, BLUE, (x-10, y), (x-20, y+7), 5)
    pygame.draw.line(screen, BLUE, (x-10, y), (x, y+7), 5)
    pygame.draw.line(screen, BLUE, (x+10, y), (x, y+7), 5)
    pygame.draw.line(screen, BLUE, (x+10, y), (x+20, y+7), 5)
    
# Drawing normal enemy
def drawEnemyNormal(x, y):
    pygame.draw.circle(screen, (GREEN[0]+25, GREEN[1]-50, GREEN[2]+25), (x, y), 10)
    pygame.draw.circle(screen, GREEN, (x, y), 8)
    
# Drawing bomber enemy
def drawEnemyBomber(x, y):
    pygame.draw.circle(screen, (DARK_GREEN[0]+25, DARK_GREEN[1]-25, DARK_GREEN[2]+25), (x, y), 10)
    pygame.draw.circle(screen, DARK_GREEN, (x, y), 8)
    
# Drawing missle enemy
def drawEnemyMissle(x, y):
    pygame.draw.circle(screen, (YELLOW[0]-50, YELLOW[1]-50, YELLOW[2]), (x, y), 10)
    pygame.draw.circle(screen, YELLOW, (x, y), 8)
    
# Drawing player bullet
def drawBullet(x, y):
    pygame.draw.circle(screen, YELLOW_WHITE, (x, y), 2)
    
# Drawing health boost
def drawHealthBoost(x, y):
    # Drawing outline
    pygame.draw.circle(screen, BLACK, (x, y), 10)
    pygame.draw.circle(screen, WHITE, (x, y), 9)
    
    # Drawing red cross
    pygame.draw.rect(screen, RED, pygame.Rect(x-2, y-5, 4, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(x-5, y-2, 10, 4))
    
# Drawing energy boost
def drawEnergyBoost(x, y):
    # Drawing outline
    pygame.draw.circle(screen, BLACK, (x, y), 10)
    pygame.draw.circle(screen, WHITE, (x, y), 9)
    
    # Drawing electricity symbol
    pygame.draw.polygon(screen, ELECTRIC_YELLOW, ((x-1, y+1), (x-3, y+1), (x+1, y-7), (x+1, y-1), (x+3, y-1), (x-1, y+7)))
    
    
    
    
    
    
#<-----Button functions----->
    
# Drawing start game button
def drawStartButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, startButton)
    
    # Writes text onto screen
    startText = fontButton.render("Start", 1, WHITE)    
    screen.blit(startText, (startButton[0]+((startButton[2]-startText.get_width())/2), startButton[1], startButton[2], startButton[3])) # Centering the text based on length of text, and length of button
    
# Drawing view rules button
def drawRulesButton():
    # Drawing green rectangle as visual indicator of the button 
    pygame.draw.rect(screen, GREEN, rulesButton)
    
    # Writes text onto screen
    rulesText = fontButton.render("Rules", 1, WHITE)    
    screen.blit(rulesText, (rulesButton[0]+((rulesButton[2]-rulesText.get_width())/2), rulesButton[1], rulesButton[2], rulesButton[3])) # Centering the text based on length of text, and length of button
    
# Drawing open store button
def drawShopButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, shopButton)

    # Writes text onto screen
    shopText = fontButton.render("Store", 1, WHITE)    
    screen.blit(shopText, (shopButton[0]+((shopButton[2]-shopText.get_width())/2), shopButton[1], shopButton[2], shopButton[3])) # Centering the text based on length of text, and length of button 
    
# Drawing 'return to main menu from sub-menus button'
def drawBackButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, backButton)
    
    # Writes text onto screen
    rulesBackText = fontButton.render("OK", 1, WHITE)    
    screen.blit(rulesBackText, (backButton[0]+((backButton[2]-rulesBackText.get_width())/2), backButton[1], backButton[2], backButton[3])) # Centering the text based on length of text, and length of button

# Drawing 'return to main menu after dying/winning button'
def drawReturnButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, returnButton)

    # Writes text onto screen
    returnText = fontButton.render("Return", 1, WHITE)
    screen.blit(returnText, (returnButton[0]+((returnButton[2]-returnText.get_width())/2), returnButton[1], returnButton[2], returnButton[3])) # Centering the text based on length of text, and length of button      
    
# Drawing health upgrade button
def drawHealthPlusButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, upgradeButton[0])
    
    # Writes text onto screen
    healthPlusText = fontButton.render("Health+", 1, WHITE)
    screen.blit(healthPlusText, (upgradeButton[0][0]+((upgradeButton[0][2]-healthPlusText.get_width())/2), upgradeButton[0][1], upgradeButton[0][2], upgradeButton[0][3])) # Centering the text based on length of text, and length of button       
    
# Drawing energy upgrade button
def drawEnergyPlusButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, upgradeButton[1])
    
    # Writes text onto screen
    energyPlusText = fontButton.render("Energy+", 1, WHITE)
    screen.blit(energyPlusText, (upgradeButton[1][0]+((upgradeButton[1][2]-energyPlusText.get_width())/2), upgradeButton[1][1], upgradeButton[1][2], upgradeButton[1][3])) # Centering the text based on length of text, and length of button      
    
# Drawing bullet velocity upgrade button
def drawBulletVelocityButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, upgradeButton[2])
    
    # Writes text onto screen
    bulletVelocityText = fontButton.render("Velocity", 1, WHITE)
    screen.blit(bulletVelocityText, (upgradeButton[2][0]+((upgradeButton[2][2]-bulletVelocityText.get_width())/2), upgradeButton[2][1], upgradeButton[2][2], upgradeButton[2][3])) # Centering the text based on length of text, and length of button     
    
# Drawing bullet reload upgrade button
def drawBulletReloadButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, upgradeButton[3])
    
    # Writes text onto screen
    bulletReloadText = fontButton.render("Reload", 1, WHITE)
    screen.blit(bulletReloadText, (upgradeButton[3][0]+((upgradeButton[3][2]-bulletReloadText.get_width())/2), upgradeButton[3][1], upgradeButton[3][2], upgradeButton[3][3])) # Centering the text based on length of text, and length of button     
    
# Drawing triple shot upgrade button
def drawBulletShotgunButton():
    # Drawing green rectangle as visual indicator of the button
    pygame.draw.rect(screen, GREEN, upgradeButton[4])
    
    # Writes text onto screen
    bulletShotgunText = fontButton.render("Shotgun", 1, WHITE)
    screen.blit(bulletShotgunText, (upgradeButton[4][0]+((upgradeButton[4][2]-bulletShotgunText.get_width())/2), upgradeButton[4][1], upgradeButton[4][2], upgradeButton[4][3])) # Centering the text based on length of text, and length of button       





#<-----Misc functions----->

# Drawing results screen that shows when player dies/wins
def drawResultScreen():
    if win:
        # If win is true, draw win message
        winText = fontButton.render("You Win!", 1, LIGHT_GREY)
        screen.blit(winText, pygame.Rect((LENGTH-winText.get_width())/2, 90, 100, 100))        
        score = kills*(now//1000)*2
    else:
        # If win is false, therefore a loss, draw loss message
        deadText = fontButton.render("You Died", 1, LIGHT_GREY)
        screen.blit(deadText, pygame.Rect((LENGTH-deadText.get_width())/2, 90, 100, 100))          
        score = kills*(now//1000)
        
    # Drawing how many enemies the player has killed
    killText = fontButton.render("Killed: " + str(kills) + " Enemies", 1, LIGHT_GREY)
    screen.blit(killText, pygame.Rect((LENGTH-killText.get_width())/2, 165, 100, 100))
    
    # Drawing how long the player has survived for
    survivedTimeText = fontButton.render("Survived: " + str(now//1000) + " Seconds", 1, LIGHT_GREY)
    screen.blit(survivedTimeText, pygame.Rect((LENGTH-survivedTimeText.get_width())/2, 240, 100, 100))        
    
    # Drawing how much score the player has earned
    scoreText = fontButton.render("Earned: " + str(score) + " Score", 1, LIGHT_GREY)
    screen.blit(scoreText, pygame.Rect((LENGTH-scoreText.get_width())/2, 315, 100, 100))
    
    # Return score, where it can be added to an accumulator to calculate total score
    return score
    
# Draw how much e-waste the player has collected
def drawStorage():
    # E-waste collected is dependant on score
    screen.blit(fontButton.render("E-Waste: " + str(storage//1000) + " Pieces", 1, WHITE), pygame.Rect(10, 20, 100, 100))
    screen.blit(fontButton.render("(Note: Upgrades cost 1 e-waste, max 1 upgrade)", 1, WHITE), pygame.Rect(10, 70, 100, 100))
    
# Drawing a generic background for most menu screens
def drawBackground():
    # Drawing sea
    screen.fill(SEA_BLUE)
    
    # Drawing runway and player
    drawRunway(0, 0)
    drawCharacter(characterPos[0], characterPos[1], GREY)    






#<------------------------------Body------------------------------>

#<-----Initializing variables and other gameplay aspects----->

# Initializing pygame
pygame.init()
screen = pygame.display.set_mode(SIZE)
myClock = pygame.time.Clock()

# Creating variables for different fonts
fontShipNum = pygame.font.SysFont("Times New Roman", 90) 
fontButton = pygame.font.SysFont("Times New Roman", 40) 

# Creating variables for sound file types
fireSound = pygame.mixer.Sound("fanLaser.mp3") 
weaknessSound = pygame.mixer.Sound("fanPowerDown.mp3")
powerUpSound = pygame.mixer.Sound("fanPower-up.wav")
playerHitSound = pygame.mixer.Sound("fanPlayer-hit.wav")
takeOffSound = pygame.mixer.Sound("fanTake-off.wav")
backgroundMusic = pygame.mixer.Sound("fanRetroMusic.mp3")
destroySound = pygame.mixer.Sound("fanExplosion.wav")

# Changing sound volume
destroySound.set_volume(0.05)
playerHitSound.set_volume(0.05)
backgroundMusic.set_volume(0.05)
takeOffSound.set_volume(0.5)

# Creating variable for rules menu
rulesDisplay = pygame.image.load("fanISC3U Summative.png")

# Creating Rect for all buttons
startButton = pygame.Rect(325, 300, 150, 50)
rulesButton = pygame.Rect(325, 375, 150, 50)    
backButton = pygame.Rect(325, 540, 150, 50)
shopButton = pygame.Rect(325, 450, 150, 50)
returnButton = pygame.Rect(325, 450, 150, 50)
upgradeButton = [pygame.Rect(200, 200, 150, 50), pygame.Rect(450, 200, 150, 50), pygame.Rect(75, 300, 150, 50), pygame.Rect(325, 300, 150, 50), pygame.Rect(575, 300, 150, 50)] # Upgrade buttons are put into a list


# Initializing variables
# Setting bool variables to either true or false at the start of the game
keyLeft = keyRight = keyUp = keyDown = keySpace = keyShift = keyMouseLeft = dead = win = wobble = shield = boost = gameStart = rulesScreen = shopScreen = rulesButtonClicked = backButtonClicked = startButtonClicked = shopButtonClicked = returnButtonClicked = onceCheck = False 
onRunway = running = menuScreen = True

# Setting other variables to specific numbers
heading = lastShot = kills = bossDead = runwayPos = bossShake = score = storage = 0
characterSpeed = healthMultiplier = energyMultiplier = bulletVelocityMultiplier = bulletReloadMultiplier = 1  
shakeMagnitude = 2
energy = MAX_ENERGY
health = MAX_HEALTH

# Setting some lists to predefined values
upgradeButtonClicked = [False, False, False, False, False] # Each index represents one upgrade type
upgrade = [False, False, False, False, False] # Each index represents one upgrade type
characterPos = [LENGTH//2, (HEIGHT*4)//5]
mousePos = [LENGTH//2, (HEIGHT//2)-50]
bossPos = [0, -400]


# Initializing empty lists
# First axis is the entity number. Second axis, index 0 is xPos, 1 is yPos, 2 is direction, 3 is magnitude
enemyNormal = [] 
enemyBomber = [] # But index 4 is diving or not
enemyMissle = [] # But index 4 is locked on or not
bullet = []
energyBoost = []
healthBoost = []
# First axis is the entity number. Second axis, index 0 is xPos, 1 is yPos
bossWeakness = []
waves = []   

# Plays background music infinitely
backgroundMusic.play(-1)






#<-----Gameplay begins----->

# Start game loop
while running:

    #<-----Checking through events----->
    
    for event in pygame.event.get():
        # Checking if pygame should quit
        if event.type == pygame.QUIT:
            running = False
            
        # Check if any key has been pressed down
        if event.type == pygame.KEYDOWN:
            # Check which key has been pressed down
            if event.key == pygame.K_a:
                keyLeft = True
            if event.key == pygame.K_d:
                keyRight = True
            if event.key == pygame.K_w:
                keyUp = True
            if event.key == pygame.K_s:
                keyDown = True      
            if event.key == pygame.K_SPACE:
                keySpace = True
            if event.key == pygame.K_LSHIFT:
                keyShift = True
                
        # Check if any key has been released
        if event.type == pygame.KEYUP:
            # Check which key has been released
            if event.key == pygame.K_a:
                keyLeft = False
            if event.key == pygame.K_d:
                keyRight = False
            if event.key == pygame.K_w:
                keyUp = False
            if event.key == pygame.K_s:
                keyDown = False  
            if event.key == pygame.K_SPACE:
                keySpace = False        
            if event.key == pygame.K_LSHIFT:
                keyShift = False
        
        # Check if mouse button has been pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            keyMouseLeft = True
            
        # Check if mouse buton has been released
        if event.type == pygame.MOUSEBUTTONUP:
            keyMouseLeft = False
            
        # Check the position of the mouse cursor
        if event.type == pygame.MOUSEMOTION:
            mousePos[0], mousePos[1] = event.pos      
      
      
      
      
      
      
    #<-----Check if the player has won or lost the game----->
    
    if win or dead:
        # Set gameStart to false, pausing the game
        gameStart = False
        
        # Only perform this action the first time
        if not onceCheck:
            # Add player score to accumulator and draw results screen
            storage += drawResultScreen()
            onceCheck = True # Set to true, so this will not run again
        else:
            # Otherwise only draw the results screen
            drawResultScreen()
        
        # Drawing a return to main menu button
        drawReturnButton()
        
        # Checking if the mouse has been clicked inside of the 'return' button
        if keyMouseLeft and returnButton.collidepoint(mousePos[0], mousePos[1]):
            returnButtonClicked = True
        # If the mouse moves out of the 'return' button, the 'return' button is then set back to false
        elif not returnButton.collidepoint(mousePos[0], mousePos[1]):
            returnButtonClicked = False
            
        # If mouse is released within the 'return button', and also clicked within the 'return' button, perform the action
        if not keyMouseLeft and returnButton.collidepoint(mousePos[0], mousePos[1]) and returnButtonClicked:
            # Setting button clicked to false
            returnbuttonClicked = False
            
            # Setting menuScreen to true, because this button should navigate to the menu
            menuScreen = True
            
            # Setting win and loss to false, as after returning to the menu, the player has neither lost or won
            win = dead = False
      
      
      
      
      
      
    #<-----Checking if the player is on the menu screen----->
    
    if menuScreen:
        # Bringing player back to original position
        characterPos = [LENGTH//2, (HEIGHT*4)//5]
        
        # Drawing things
        drawBackground() # Drawing background
        drawStartButton() # Drawing start game button
        drawRulesButton() # Drawing view rules button
        drawShopButton() # Drawing open shop button
                
                
        # Checking if the mouse has been clicked inside of the 'start' button
        if keyMouseLeft and startButton.collidepoint(mousePos[0], mousePos[1]):
            startButtonClicked = True
        # If the mouse moves out of the 'start' button, the 'start' button is then set back to false
        elif not startButton.collidepoint(mousePos[0], mousePos[1]):
            startButtonClicked = False
            
        # Checking if the mouse has been clicked inside of the 'rules' button
        if keyMouseLeft and rulesButton.collidepoint(mousePos[0], mousePos[1]):
            rulesButtonClicked = True
        # If the mouse moves out of the 'rules' button, the 'rules' button is then set back to false
        elif not rulesButton.collidepoint(mousePos[0], mousePos[1]):
            rulesButtonClicked = False 
            
        # Checking if the mouse has been clicked inside of the 'shop' button
        if keyMouseLeft and shopButton.collidepoint(mousePos[0], mousePos[1]):
            shopButtonClicked = True
        # If the mouse moves out of the 'shop' button, the 'shop' button is then set back to false
        elif not shopButton.collidepoint(mousePos[0], mousePos[1]):
            shopButtonClicked = False 
          
          
        # If mouse is released within the 'start' button, and also clicked within the 'start' button, perform the action
        if not keyMouseLeft and startButton.collidepoint(mousePos[0], mousePos[1]) and startButtonClicked:
            startButtonClicked = menuScreen = False
            gameStart = True
            
            # Resetting all gameplay variables to their initial state, see Line 439
            startTime = pygame.time.get_ticks()
            keyLeft = keyRight = keyUp = keyDown = keySpace = keyShift = keyMouseLeft = wobble = shield = boost = onceCheck = False     
            onRunway = True
            heading = kills = bossDead = runwayPos = bossShake = lastShot = score = 0
            characterSpeed = 1  
            shakeMagnitude = 2
            energy = MAX_ENERGY
            health = MAX_HEALTH
            bossPos = [0, -400]   
            characterPos = [LENGTH//2, (HEIGHT*4)//5]
            enemyNormal = []
            enemyBomber = []
            enemyMissle = []
            bullet = []
            energyBoost = []
            healthBoost = []
            bossWeakness = []
            waves = []   
        
        # If mouse is released within the 'rules' button, and also clicked within the 'rules' button, perform the action
        if not keyMouseLeft and rulesButton.collidepoint(mousePos[0], mousePos[1]) and rulesButtonClicked:
            # Setting to false because the button is no longer pressed and the player is no longer on the menuScreen
            rulesButtonClicked = menuScreen = False
            
            # Setting to true, becuase they are now on the rulesScreen
            rulesScreen = True 
            
        # If mouse is released within the 'shop' button, and also clicked within the 'shop' button, perform the action
        if not keyMouseLeft and shopButton.collidepoint(mousePos[0], mousePos[1]) and shopButtonClicked:
            # Setting to false because the button is no longer pressed and the player is no longer on the menuScreen
            shopButtonClicked = menuScreen = False
            
            # Setting to true, becuase they are now on the shopScreen
            shopScreen = True
        
        
        
        
        
        
    #<-----Checking if the player is on the rules screen----->
    
    if rulesScreen:
        # Drawing things
        drawBackground() # Drawing background
        screen.blit(rulesDisplay, pygame.Rect(113, -30, 600, 400)) # Displaying rules 
        drawBackButton() # Drawing go back button
        
        # Checking if the mouse has been clicked inside of the 'back' button
        if keyMouseLeft and backButton.collidepoint(mousePos[0], mousePos[1]):
            backButtonClicked = True
        # If the mouse moves out of the 'back' button, the 'back' button is then set back to false
        elif not backButton.collidepoint(mousePos[0], mousePos[1]):
            backButtonClicked = False        
        
        # If mouse is released within the 'back' button, and also clicked within the 'back' button, perform the action
        if not keyMouseLeft and backButton.collidepoint(mousePos[0], mousePos[1]) and backButtonClicked:
            # Setting to false because the button is no longer pressed and the player is no longer on the rulesScreen
            backButtonClicked = rulesScreen = False
            
            # Setting to true, becuase they are now on the menuScreen
            menuScreen = True
            
            
            
            
            
            
    #<-----Checking if the player is on the shop screen----->  
    
    if shopScreen:
        # Drawing things
        drawBackground() # Drawing background
        drawBackButton() # Drawing 'back' button
        drawStorage() # Drawing storage  
        # Drawing all the upgrade buttons
        drawHealthPlusButton()
        drawEnergyPlusButton()
        drawBulletVelocityButton()
        drawBulletReloadButton()
        drawBulletShotgunButton()
              
        # Checking if the mouse has been clicked inside of the 'back' button
        if keyMouseLeft and backButton.collidepoint(mousePos[0], mousePos[1]):
            backButtonClicked = True
        # If the mouse moves out of the 'back' button, the 'back' button is then set back to false
        elif not backButton.collidepoint(mousePos[0], mousePos[1]):
            backButtonClicked = False  
            
        # If mouse is released within the 'back' button, and also clicked within the 'back' button, perform the action
        if not keyMouseLeft and backButton.collidepoint(mousePos[0], mousePos[1]) and backButtonClicked:
            # Setting to false because the button is no longer pressed and the player is no longer on the shopScreen
            backButtonClicked = shopScreen = False
            
            # Setting to true, becuase they are now on the menuScreen
            menuScreen = True
        
        # Looping 5 times
        for i in range(5):
            # Checking if the mouse has been clicked inside of the 'i' upgrade button
            if keyMouseLeft and upgradeButton[i].collidepoint(mousePos[0], mousePos[1]):
                upgradeButtonClicked[i] = True
            # If the mouse moves out of the 'i' upgrade button, the 'i' upgrade button is then set back to false
            elif not upgradeButton[i].collidepoint(mousePos[0], mousePos[1]):
                upgradeButtonClicked[i] = False 
                
            # If mouse is released within the 'i' upgrade button, and also clicked within the 'i' upgrade button, perform the action
            if not keyMouseLeft and upgradeButton[i].collidepoint(mousePos[0], mousePos[1]) and upgradeButtonClicked[i]:
                upgradeButtonClicked[i] = False
                
                # Checking if the upgrade has not been bought before, and if the player has enough e-waste
                if not upgrade[i] and storage//1000 >= 1:
                    # Setting that upgrade to true
                    upgrade[i] = True
                    
                    # Deducting cost
                    storage -= 1000
                    
                    # Depending on which upgrade was bought, change one of the multipliers
                    if i == 0:
                        healthMultiplier = 0.5 # Reduces health damage
                    if i == 1:
                        energyMultiplier = 0.5 # Reduces energy usage
                    if i == 2:
                        bulletVelocityMultiplier = 2 # Increases bullet velocity
                    if i == 3:
                        bulletReloadMultiplier = 0.5 # Reduces reload time
        
        
        
        
        
    #<-----Gameplay begins----->
    
    if gameStart:        
        # Setting 'now' to the tick the gameplay begins
        now = pygame.time.get_ticks() - startTime
        
        # Choosing a random number to generate enities from
        randomNum = random.randint(0, 1000)
        
        # By default set player colour to grey, and set player wobble to false
        colour = GREY
        wobble = False
        
        # Resetting the page
        screen.fill(SEA_BLUE)        
        
        
        
        
        
        
        #<-----Generating entities randomly----->
        
        # Check which conditions 'randomNum' fulfills, if multiple conditions are met, multiple entities are generated
        if randomNum >= 0 and randomNum < 50+(now//500): # Increase the range of which an enemy can generate every 0.5 seconds
            # Append a normal enemy
            enemyNormal.append([random.randint(0, 800), random.randint(-400, 0), 0, 1.5])       
            
        if randomNum >= 100 and randomNum < 103+((now-15000)//10000) and now > 15000: # Increase the range of which an enemy can generate every 10 seconds
            # Append a bomber enemy from the left
            enemyBomber.append([0, random.randint(0, 100), 90, 1.5, False])
                                
        if randomNum >= 200 and randomNum < 203+((now-15000)//10000) and now > 15000: # Increase the range of which an enemy can generate every 10 seconds
            # Append a bomber enemy from the right
            enemyBomber.append([800, random.randint(0, 100), 270, 1.5, False])
            
        if randomNum >= 300 and randomNum < 302+((now-30000)//5000) and now > 30000: # Increase the range of which an enemy can generate every 5 seconds
            # Append a missle enemy
            enemyMissle.append([random.randint(0, 800), random.randint(-400, 0), 0, 1.5, False])
            
        if randomNum >= 950 and randomNum < 999:
            # Append a wave
            waves.append([random.randint(0, 800), 0])
            
        if randomNum == 999:
            # Append a health boost
            healthBoost.append([random.randint(0, 800), 0, 0, 1])
                
        if randomNum == 1000:
            # Append an energy boost
            energyBoost.append([random.randint(0, 800), 0, 0, 1])
        
        # Simulating the movement of waves    
        i = 0
        while i < len(waves): # Loop through length of waves as long as waves remain
            waves[i][1] += 2 # Change y position by 2
            drawWaves(waves[i][0], waves[i][1]) # Drawing moving waves
            if waves[i][1] == 600: # If wave is on edge of screen, delete
                del waves[i]
            i += 1            
            
        # Simulating takeoff off of a runway
        if runwayPos == 0:
            # Play engine sounds
            takeOffSound.play()
        if runwayPos < 500:
            # Draw runway as long as it is visible
            drawRunway(0, runwayPos)
        if runwayPos > 350:
            # If runway is off the screen, allow player to start controlling the plane
            onRunway = False
        # Move runway down 2 pixels ever time
        runwayPos += 2        
        
        
        
        
        
        #<-----Boss----->
        
        # Checking if 100 seconds has passed, and if boss should spawn yet
        if now//1000 > BOSS_SPAWN_TIME:
            # As long as y position of boss is less than 0, keeping moving down by 2
            if bossPos[1] < 0:
                bossPos[1] += 2
                # Also move the weakpoints of the boss, if the boss itself is moving
                for i in range(len(bossWeakness)):
                    bossWeakness[i][1] += 2
                
            # Checking how much the boss should shake by
            if bossPos[0] < -150: # If too far to the left, move rightward
                bossShake = 10
            elif bossPos[0] > 150: # If too far to the right, move leftward
                bossShake = -10
            else: # Otherwise, shake in random directions, depending on number of weakpoints the player has hit
                if bossDead >= 12: # When boss is almost dead, shake violently
                    bossShake = random.randint(-8, 8)
                elif bossDead >= 9:
                    bossShake = random.randint(-5, 5)
                elif bossDead >= 6:
                    bossShake = random.randint(-3, 3)
                elif bossDead >= 3:
                    bossShake = random.randint(-2, 2)
                else: # Shake slowly when starting out
                    bossShake = random.randint(-1, 1)
                    
            # Change boss position by how much it shakes, then draw
            bossPos[0] += bossShake              
            drawBoss(bossPos[0], bossPos[1])   
            
            # Check if the player has rammed into the bridge of the ship
            if characterPos[0] > bossPos[0]+300 and characterPos[0] < bossPos[0]+500 and characterPos[1] < bossPos[1]+200:
                # If they still have hp, take consequnces of taking damage, shield and boost do not negate debuffs in this case
                if health > 0:
                    # Starting visual and audio cues of taking damage
                    wobble = True
                    playerHitSound.play()
                    
                    # Taking damage, and other debuffs
                    colour = RED
                    health -= 10*healthMultiplier # Multiplier can be upgraded to reduce damage     
                    characterSpeed = 1   
                # If no hp, set dead to true
                else:
                    dead = True                 
                    
            # Looping while length of bossWeakness is less than the maximum amount
            while len(bossWeakness) < MAX_BOSS_WEAKNESS:
                # Selecting a random location on the ship to be a weakness
                weaknessX = random.randint(210, 590)+bossPos[0]
                weaknessY = random.randint(10, 390)+bossPos[1]
                
                # Checking if the location on the ship is valid
                if not (weaknessX > bossPos[0]+300 and weaknessX < bossPos[0]+500 and weaknessY < bossPos[1]+200):
                    # Append a weakness if it is valid
                    bossWeakness.append([weaknessX, weaknessY])
                   
            # Looping through all of the boss weaknesses 
            i = 0
            while i < len(bossWeakness):
                # Change the position of the weakness with the direction the boss shakes
                bossWeakness[i][0] += bossShake
                
                # Check if value is even or odd, so we can have the boss weakness flash
                if (now//250) % 2 == 0:
                    drawWeakness(bossWeakness[i][0], bossWeakness[i][1], True)
                else:
                    drawWeakness(bossWeakness[i][0], bossWeakness[i][1], False)
                    
                # Checking if a bullet hits the weakness
                j = 0
                while j < len(bullet):
                    # If the distance between the two entities is less than their combined radii, then they must collide
                    if math.sqrt(((bossWeakness[i][0]-bullet[j][0])**2)+((bossWeakness[i][1]-bullet[j][1])**2)) <= WEAKNESS_RADIUS+BULLET_RADIUS:
                        # Temporarily setting bossWeakness to [-1, -1]
                        bossWeakness[i] = [-1, -1]
                        
                        # Delete bullet
                        del bullet[j]
                    j += 1
                # Checking if the bossWeakness was set to [-1, -1]
                if bossWeakness[i] == [-1, -1]:
                    # Delete weakness
                    del bossWeakness[i]
                    
                    # Audio sound confirming a hit
                    weaknessSound.play()
                    
                    # Increamenting how many weaknesses have been hit
                    bossDead += 1
                i += 1
                
            # If the number of weakness hits equals the boss total lives, player wins
            if bossDead == BOSS_LIVES:
                win = True
            
            # Drawing hp bar of the boss
            drawBossBar(bossPos[0], bossPos[1], bossDead)
            
            
            
            
            
            
        #<-----Bullets----->
        
        # Looping through all of the bullets on the screen
        i = 0
        while i < len(bullet):
            # Depending on the value of index 2, which is the heading in degrees, of the bullet, we can calulate the x and y position change
            if bullet[i][2] <= 90: # If less than 90
                bullet[i][0] += (math.cos(math.radians(90-bullet[i][2]))*bullet[i][3]) # Index 2 is the heading, index 3 is the magnitude
                bullet[i][1] -= (math.sin(math.radians(90-bullet[i][2]))*bullet[i][3])
            elif bullet[i][2] <= 180: # If between 90-180
                bullet[i][0] += (math.cos(math.radians(bullet[i][2]-90))*bullet[i][3])
                bullet[i][1] += (math.sin(math.radians(bullet[i][2]-90))*bullet[i][3])
            elif bullet[i][2] <= 270: # If between 90-270
                bullet[i][0] -= (math.cos(math.radians(270-bullet[i][2]))*bullet[i][3])
                bullet[i][1] += (math.sin(math.radians(270-bullet[i][2]))*bullet[i][3])
            else: # If greater than 270
                bullet[i][0] -= (math.cos(math.radians(bullet[i][2]-270))*bullet[i][3])
                bullet[i][1] -= (math.sin(math.radians(bullet[i][2]-270))*bullet[i][3])     
    
            # Drawing the bullet
            drawBullet(bullet[i][0], bullet[i][1])   
            
            # Checking if the bullet leaves the screen, or has hit the bridge of the boss
            if (bullet[i][0] > bossPos[0]+300 and bullet[i][0] < bossPos[0]+500 and bullet[i][1] < bossPos[1]+200) or (bullet[i][0] < 0 or bullet[i][0] > 800 or bullet[i][1] < 0 or bullet[i][1] > 600):
                # If so, delete the bullet
                del bullet[i]        
            i += 1          
    
    
    
    
    
        #<-----Enemy garbage----->
        
        # Looping through all normal enemies
        i = 0
        while i < len(enemyNormal):
            # Changing y coordinate by a constant rate
            enemyNormal[i][1] += enemyNormal[i][3]
            
            # Changing x coordinate by plugging in the y coordinate into a sine function
            enemyNormal[i][0] += math.sin(math.radians(enemyNormal[i][1]))
            
            # Drawing enemy
            drawEnemyNormal(enemyNormal[i][0], enemyNormal[i][1])
    
            # Looping through all bullets
            j = 0
            while j < len(bullet):
                # Checking if a bullet has hit the enemy
                if math.sqrt(((enemyNormal[i][0]-bullet[j][0])**2)+((enemyNormal[i][1]-bullet[j][1])**2)) <= BULLET_RADIUS+NORMAL_RADIUS:
                    # Send both the bullet and enemy out of bounds, so that a later function will delete it
                    enemyNormal[i][1] = 1000
                    bullet[j][0] = 1000
                    
                    # Add one kill
                    kills += 1
                    
                    # Play destroy sound
                    destroySound.play()
                j += 1
                  
            # Checking if the enemy has hit the player
            if math.sqrt(((enemyNormal[i][0]-characterPos[0])**2)+((enemyNormal[i][1]-characterPos[1])**2)) <= NORMAL_RADIUS+PLAYER_RADIUS:
                # If player has health, they take consequences of damage and debuffs
                if health > 0:
                    # Setting wobble to true
                    wobble = True
                    
                    # Audio cue, that player was hit
                    playerHitSound.play()
                    
                    # If shield, negate some debuffs
                    if not shield:
                        colour = RED
                        health -= 1*healthMultiplier
                        
                    # If boost, negate some debuffs
                    if not boost:
                        characterSpeed = 1
                # Otherwise, player dies
                else:
                    dead = True
                    break          
                
            # If enemy is out of bounds, delete
            if enemyNormal[i][1] > 620:
                del enemyNormal[i]             
            i += 1             
               
               
               
               
        # Looping through all bomber enemies 
        i = 0
        while i < len(enemyBomber):
            # If the x coordinate of the bomber is close to the x coordinate of the player, then it begins to dive
            if enemyBomber[i][0] > characterPos[0]-10 and enemyBomber[i][0] < characterPos[0]+10 and enemyBomber[i][1] < characterPos[1]:
                enemyBomber[i][4] = True # Index 4 is whether the bomber is diving or not
                
            # Checking if the bomber is diving
            if enemyBomber[i][4]:
                # Only travel straight downwards, at 5x speed
                enemyBomber[i][1] += enemyBomber[i][3]*5
            else:
                # Otherwise, check if the bomber is coming from the right or the left
                if enemyBomber[i][2] == 90:
                    # Move x position rightwards
                    enemyBomber[i][0] += enemyBomber[i][3] 
                elif enemyBomber[i][2] == 270:
                    # Move x position leftwards
                    enemyBomber[i][0] -= enemyBomber[i][3] 
                    
                # Change y position based on plugging in x position into a sin function
                enemyBomber[i][1] += math.sin(math.radians(enemyBomber[i][0]))             
            
            # Draw enemy bomber
            drawEnemyBomber(enemyBomber[i][0], enemyBomber[i][1])       
            
            # Looping through all bullets
            j = 0
            while j < len(bullet):
                # Checking if bullet hits the enemy
                if math.sqrt(((enemyBomber[i][0]-bullet[j][0])**2)+((enemyBomber[i][1]-bullet[j][1])**2)) <= BULLET_RADIUS+NORMAL_RADIUS:
                    # Send both the bullet and enemy out of bounds, so that a later function will delete it
                    enemyBomber[i][1] = 1000
                    bullet[j][0] = 1000
                    
                    # Add one kill
                    kills += 1
                    
                    # Play destory sound
                    destroySound.play()
                j += 1        
            
            # Checking if enemy has hit the player
            if math.sqrt(((enemyBomber[i][0]-characterPos[0])**2)+((enemyBomber[i][1]-characterPos[1])**2)) <= NORMAL_RADIUS+PLAYER_RADIUS:
                # If player has health, they take consequences of damage and debuffs
                if health > 0:
                    # Setting wobble to true
                    wobble = True
                    
                    # Audio cue, that player was hit
                    playerHitSound.play()
                    
                    # If shield, negate some debuffs
                    if not shield:
                        colour = RED
                        health -= 3*healthMultiplier
                        
                    # If boost, negate some debuffs
                    if not boost:
                        characterSpeed = 1      
                
            # Delete bomber if out of bounds
            if enemyBomber[i][1] > 620:
                del enemyBomber[i]          
            i += 1
        
        
        
        
        # Looping through all missle enemies
        i = 0
        while i < len(enemyMissle):
            # Checking if the player is within tracking distance of the missle
            if math.sqrt(((enemyMissle[i][0]-characterPos[0])**2)+((enemyMissle[i][1]-characterPos[1])**2)) <= SEEKING_RADIUS:
                # Move towards the player, depending the difference between the player and the missle enemy
                if enemyMissle[i][0] < characterPos[0]-15:
                    enemyMissle[i][0] += 1
                if enemyMissle[i][0] > characterPos[0]+15:
                    enemyMissle[i][0] -= 1
                if enemyMissle[i][1] < characterPos[1]-15:
                    enemyMissle[i][1] += 1
                if enemyMissle[i][1] > characterPos[1]+15:
                    enemyMissle[i][1] -= 1     
                
                # Drawing missle enemy
                drawEnemyMissle(enemyMissle[i][0], enemyMissle[i][1])
            else:
                # Changing y coordinate by a constant rate
                enemyMissle[i][0] += math.sin(math.radians(enemyMissle[i][1]))
                
                # Changing x coordinate by plugging in the y coordinate into a sine function                
                enemyMissle[i][1] += enemyMissle[i][3]
                
                # Drawing missle enemy
                drawEnemyMissle(enemyMissle[i][0], enemyMissle[i][1])
    
            # Looping through all bullets
            j = 0
            while j < len(bullet):
                # Checking if the bullet has hit the enemy
                if math.sqrt(((enemyMissle[i][0]-bullet[j][0])**2)+((enemyMissle[i][1]-bullet[j][1])**2)) <= BULLET_RADIUS+NORMAL_RADIUS:
                    # Send both the bullet and enemy out of bounds, so that a later function will delete it
                    enemyMissle[i][1] = 1000
                    bullet[j][0] = 1000
                    
                    # Add one kill
                    kills += 1
                    
                    # Play destory sound
                    destroySound.play()
                j += 1
                  
            # Checking if the enemy has hit a player
            if math.sqrt(((enemyMissle[i][0]-characterPos[0])**2)+((enemyMissle[i][1]-characterPos[1])**2)) <= NORMAL_RADIUS+PLAYER_RADIUS:
                # If player has health, they take consequences of damage and debuffs
                if health > 0:
                    # Setting wobble to true
                    wobble = True
                    
                    # Audio cue, that player was hit
                    playerHitSound.play()
                    
                    # If shield, negate some debuffs
                    if not shield:
                        colour = RED
                        health -= 1*healthMultiplier
                        
                    # If boost, negate some debuffs
                    if not boost:
                        characterSpeed = 1
                
            # Checking if missle is out of bounds
            if enemyMissle[i][1] > 620:
                del enemyMissle[i]             
            i += 1      
        
        # If wobble is true, cause the player to vibrate randomly
        if wobble:
            characterPos[0] += random.randint(-2, 2)
            characterPos[1] += random.randint(-2, 2)
        
        # Looping through all health boosts
        i = 0
        while i < len(healthBoost):
            # Increament the y value every time, to move it down the screen
            healthBoost[i][1] += healthBoost[i][3]
            
            # Draw the health boost
            drawHealthBoost(healthBoost[i][0], healthBoost[i][1])
            
            # If the health boost leaves the screen, then delete it
            if healthBoost[i][1] > 600:
                del healthBoost[i]
            # Otherwise, if it also hits the player, then the player gets a health boost
            elif math.sqrt(((healthBoost[i][0]-characterPos[0])**2)+((healthBoost[i][1]-characterPos[1])**2)) <= NORMAL_RADIUS+PLAYER_RADIUS:
                # Delete after being picked up
                del healthBoost[i]
                
                # Play power-up sound
                powerUpSound.play()
                
                # Healing 'POWERUP_AMOUNT', and capping it at 'MAX_HEALTH'
                if health + POWERUP_AMOUNT > MAX_HEALTH:
                    health = MAX_HEALTH
                else:
                    health += POWERUP_AMOUNT   
            i += 1
        
        # Looping through all energy boosts
        i = 0
        while i < len(energyBoost):
            # Increament the y value every time, to move it down the screen            
            energyBoost[i][1] += energyBoost[i][3]
            
            # Draw the energy boost
            drawEnergyBoost(energyBoost[i][0], energyBoost[i][1])
            
            # If the energy boost leaves the screen, then delete it
            if energyBoost[i][1] > 600:
                del energyBoost[i]
            # Otherwise, if it also hits the player, then the player gets a energy boost
            elif math.sqrt(((energyBoost[i][0]-characterPos[0])**2)+((energyBoost[i][1]-characterPos[1])**2)) <= 30:
                # Delete after being picked up
                del energyBoost[i]
                
                # Play power-up sound
                powerUpSound.play()
                
                # Healing 'POWERUP_AMOUNT', and capping it at 'MAX_ENERGY'
                if energy + POWERUP_AMOUNT > MAX_ENERGY:
                    energy = MAX_ENERGY
                else:
                    energy += POWERUP_AMOUNT 
            i += 1      
        
        
        
        
        
        
        #<-----Player----->
        
        # Checking if player is on runway, if true, they shouldn't be able to control the character
        if onRunway == False:
            # Checking if the player is still in the bounds of the screen, if yes, then they can continue to move
            if keyLeft and characterPos[0] > 0:
                characterPos[0] -= characterSpeed
            if keyRight and characterPos[0] < LENGTH:
                characterPos[0] += characterSpeed
            if keyUp and characterPos[1] > 0:
                characterPos[1] -= characterSpeed 
            if keyDown and characterPos[1] < HEIGHT:
                # Boost ability does not speed up backwards movement, so if the player is boosting, the backwards speeds does not change
                if keySpace:
                    characterPos[1] += 2
                else:
                    characterPos[1] += characterSpeed
                    
            # Checking if the player is using the shield ability
            if keyShift and energy > 0:
                # Drain energy
                energy -= 0.5*energyMultiplier
                
                # Give player a shield
                shield = True
                
                # Draw a shield
                drawShield(characterPos[0], characterPos[1])      
            else:
                # Otherwise, player gets no shield
                shield = False
                
            # Checking if the player is using the boost ability
            if keySpace and energy > 0:
                # Drain energy
                energy -= 0.5*energyMultiplier
                
                # Give player a boost
                characterSpeed = 3
                boost = True
                
                # Draw a afterburner effect
                drawAfterburn(characterPos[0], characterPos[1]) 
            else:
                # Otherwise, player gets no boost
                boost = False
                characterSpeed = 2
                
            # Checking if player is attempting to shoot a bullet
            if keyMouseLeft:
                # Calculate the distance between the mouse and the player, if mouse is straight above, set distance to 0.1, since division by 0 is invalid
                if math.sqrt((characterPos[0]-mousePos[0])**2+(characterPos[1]-mousePos[1])**2) != 0:
                    distance = math.sqrt((characterPos[0]-mousePos[0])**2+(characterPos[1]-mousePos[1])**2)
                else:
                    distance = 0.1
                
                # Find which quadrant the mouse is in, with the player model being the origin
                if mousePos[0] >= characterPos[0] and mousePos[1] <= characterPos[1]:
                    heading = math.degrees(math.asin((abs(mousePos[0]-characterPos[0]))/distance)) # Find the angle of the mouse, assuming 0 is straight up, like a compass
                elif mousePos[0] >= characterPos[0] and mousePos[1] >= characterPos[1]:
                    heading = 90 # If player tries to shoot behind them, the bullets are capped to shoot straight sideways only
                elif mousePos[0] <= characterPos[0] and mousePos[1] >= characterPos[1]:
                    heading = 270 # If player tries to shoot behind them, the bullets are capped to shoot straight sideways only
                elif mousePos[0] <= characterPos[0] and mousePos[1] <= characterPos[1]:
                    heading = math.degrees(math.asin((abs(mousePos[1]-characterPos[1]))/distance))+270   
                    
                # Checking if the time between the bullet shots has been long enough for the player to reload
                if now - lastShot >= (1000*bulletReloadMultiplier):
                    # Set the last shot, to the current tick
                    lastShot = now
                    
                    # Play the bullet fire sound
                    fireSound.play()
                    
                    # Checking if shotgun upgrade has been bought
                    if upgrade[4]:
                        # If so, shoot 2 extra bullets at 15 degrees angles, left and right of the main bullet
                        bullet.append([characterPos[0], characterPos[1], heading, 5*bulletVelocityMultiplier])
                        bullet.append([characterPos[0], characterPos[1], heading-15, 5*bulletVelocityMultiplier])
                        bullet.append([characterPos[0], characterPos[1], heading+15, 5*bulletVelocityMultiplier])        
                    else:
                        # Otherwise, shoot one bullet
                        bullet.append([characterPos[0], characterPos[1], heading, 5*bulletVelocityMultiplier])
            
            # If player is moving left, then draw moving left animation
            if keyLeft and not keyRight:
                drawCharacterLeft(characterPos[0], characterPos[1], colour)
            # If player is moving right, then drwa moving right animation
            elif keyRight and not keyLeft:
                drawCharacterRight(characterPos[0], characterPos[1], colour)
            # Otherwise, draw player in a neutral position
            else:
                drawCharacter(characterPos[0], characterPos[1], colour) 
        
        # If the player is still on the runway, draw the player in a neutral position, and do not allow player to control character
        else:
            drawCharacter(characterPos[0], characterPos[1], colour) 
         
        # Draw the health and energy bars
        drawBar(health, energy)
    
    # Flipping the drawings
    pygame.display.flip()
    
    # Setting framerate to 60fps
    myClock.tick(60)   

# Quit pygame
pygame.quit()    
