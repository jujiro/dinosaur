import pygame
# Plays both MP3 and Wave files


pygame.init()
#snd=pygame.mixer.Sound('./audio/sample.wav')
#pygame.mixer.music.load('./audio/sample.wav')
pygame.mixer.music.load('./audio/1.mp3')
pygame.mixer.music.play()
#snd.play()
#pygame.time.wait(30000)
while True:
  if pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
  else:
    break
pygame.quit()
