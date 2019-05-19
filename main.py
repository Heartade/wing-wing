import pygame as pg
import colors
import sys
import ui

import scene
import scene_main
import scene_teststage
import scene_intro
import scene_gameover
import scene_gameclear

if __name__ == "__main__":
  pg.init()
  pg.font.init()

  SCREEN = (360, 480)
  WINDOW = pg.display.set_mode(SCREEN)
  FPS = 60
  CLOCK = pg.time.Clock()
  SCENE_MAINMENU = scene_main.Scene_Main(WINDOW, CLOCK, 60, [])
  SCENE_INTRO = scene_intro.Scene_Intro(WINDOW, CLOCK, 60, [])
  SCENE_TIME = scene_teststage.Scene_TestStage(WINDOW, CLOCK, 60, [])
  SCENE_GAMEOVER = scene_gameover.Scene_Gameover(WINDOW, CLOCK, 60, [])
  SCENE_TIMECLEAR = scene_gameclear.Scene_GameClear(WINDOW, CLOCK, 60, [])
  SCENE = SCENE_MAINMENU
  while True:
    SCENE.loop_begin()
    next_scene = SCENE.loop()
    if next_scene != 0: # change scene according to loop return
      if SCENE == SCENE_MAINMENU and next_scene == 1:
        SCENE_INTRO = scene_intro.Scene_Intro(WINDOW,CLOCK,60,[])
        SCENE = SCENE_INTRO
      elif SCENE == SCENE_INTRO and next_scene == 1:
        SCENE_TIME = scene_teststage.Scene_TestStage(WINDOW,CLOCK,60,[])
        SCENE = SCENE_TIME
      elif SCENE == SCENE_TIME and next_scene == 2:
        SCENE_GAMEOVER = scene_gameover.Scene_Gameover(WINDOW,CLOCK,60,[])
        SCENE = SCENE_GAMEOVER
      elif SCENE == SCENE_TIME and next_scene == 1:
        SCENE_GAMECLEAR = scene_gameclear.Scene_GameClear(WINDOW,CLOCK,60,[],SCENE.score)
        SCENE = SCENE_GAMECLEAR
      elif SCENE == SCENE_GAMEOVER and next_scene == 1:
        SCENE_MAINMENU = scene_main.Scene_Main(WINDOW,CLOCK,60,[])
        SCENE = SCENE_MAINMENU
      elif SCENE == SCENE_GAMECLEAR and next_scene == 1:
        SCENE_MAINMENU = scene_main.Scene_Main(WINDOW,CLOCK,60,[])
        SCENE = SCENE_MAINMENU
    SCENE.loop_tick()
