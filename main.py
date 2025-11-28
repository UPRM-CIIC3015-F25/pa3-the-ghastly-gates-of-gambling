import pygame
from states.core.StateClass import State
from states.menus.TitleState import StartState
from states.GameState import GameState
from states.menus.GameWinState import GameWinState
from states.core.RunInfoState import RunInfoState
from states.core.PlayerInfo import PlayerInfo
from states.menus.ShopState import ShopState
from states.menus.LevelSelectState import LevelSelectState

if __name__ == "__main__":
    # --- Pygame setup ---
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("graphics/sounds/mainTheme.mp3")
    pygame.display.set_caption("Balatro")
    screen = pygame.display.set_mode((1300, 750))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    State.set_screen(screen)
    
    # --- Initial states ---
    startScreen = StartState()
    player = PlayerInfo()
    gameScreen = GameState(player=player)
    curScreen = startScreen

    # --- Main loop ---
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                if curScreen == gameScreen:
                    curScreen.nextState = "StartState"
                curScreen.isFinished = True
            curScreen.userInput(event)              # Pass all events to both current screen and debug overlay

        if curScreen.isFinished:                    # Handle state transitions
            if curScreen.nextState == "GameState":
                # If we come from GameWinState, recreate player/game instances
                # U guys can google what isinstance does :)
                if isinstance(curScreen, GameWinState):
                    player = PlayerInfo()
                    gameScreen = GameState(player=player)
                    curScreen.isFinished = False
                    curScreen.nextState = ""
                    curScreen = gameScreen
                else:
                    # Otherwise, just continue with existing player/game instances
                    curScreen.isFinished = False
                    curScreen.nextState = ""
                    curScreen = gameScreen
            elif curScreen.nextState == "GameWinState":
                curScreen.isFinished = False
                curScreen = GameWinState()
            elif curScreen.nextState == "StartState":
                curScreen.isFinished = False
                curScreen = startScreen
            elif curScreen.nextState == "RunInfoState":
                curScreen.isFinished = False
                curScreen = RunInfoState(curScreen.playedHandNameList)
            elif curScreen.nextState == "ShopState":
                curScreen.isFinished = False
                curScreen = ShopState(game_state=curScreen)
            elif curScreen.nextState == "LevelSelectState":
                curScreen.isFinished = False
                curScreen = LevelSelectState(playerInfo=player, deckManager=State.deckManager)
            else:
                exit()

        curScreen.update()
        pygame.display.update()
         