import pygame
from multiprocessing import Process, Value
# Plays both MP3 and Wave files

def play_a_file(file_name):
  pygame.init()
  pygame.mixer.music.load(file_name)
  pygame.mixer.music.play()
  while True:
    if pygame.mixer.music.get_busy():
      pygame.time.wait(1000)
    else:
      break
  pygame.quit()
  
def launch_play_file(file_name):
  p = Process(target=play_a_file, args=(file_name,))
  p.start()
  
def main():
  launch_play_file('./audio/1.mp3')
  launch_play_file('./audio/sample.mp3')
  
  
  while False:
    if game_state.next_state==SHUTTINGDOWN:
      break
    if game_state.next_state==IDLE:
      set_idle_state()
    elif game_state.next_state==PLAYING:
      set_state_to_playing()
    elif game_state.next_state==PAUSED:
      set_game_to_pause()
    elif game_state.next_state==RESUMEPLAYING:
      set_state_to_playing(resume=True)
    elif game_state.next_state==PROMPT_TO_RESET:
      prompt_to_reset()
    elif game_state.next_state==PROMPT_TO_SHUTDOWN:
      set_prompt_to_shutdown()

if __name__ == "__main__":
  main()
