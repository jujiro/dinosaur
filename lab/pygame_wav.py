import pygame
pygame.init()
#snd=pygame.mixer.Sound('./audio/sample.wav')
#pygame.mixer.music.load('./audio/sample.wav')
pygame.mixer.music.load('./audio/sample.mp3')
pygame.mixer.music.play()
#snd.play()
#pygame.time.wait(30000)
while True:
  if pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
  else:
    break
pygame.quit()
