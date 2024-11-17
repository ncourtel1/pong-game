import pygame
pygame.init()

WIDTH, HEIGHT = 1200, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

TOP_BAR_HEIGHT = 40

LABEL_FONT = pygame.font.Font("/Users/nattan/Library/Fonts/LeentankObliqueStar.ttf", 30)

BALL_SIZE = 20

pygame.mixer.init()
pygame.mixer.music.load("Pong.mp3")
pygame.mixer.music.set_volume(0.45)
pygame.mixer.music.play()


def top_bar(win, player1Point, player2Point, hits):
  player1_label = LABEL_FONT.render(f"Player 1: {player1Point}", 1, "black")
  player2_label = LABEL_FONT.render(f"Player 2: {player2Point}", 1, "black")
  hit_label = LABEL_FONT.render(f"Hits: {hits}", 1, "black")
  pygame.draw.rect(win, "white", (0, 0, WIDTH, TOP_BAR_HEIGHT))
  win.blit(player1_label, (200, 5))
  win.blit(player2_label, (900, 5))
  win.blit(hit_label, (550, 5))

def draw_result(win, winner, player1Point, player2Point):
  win.fill((0, 0, 0))
  
  label_fonr_winner = pygame.font.Font("/Users/nattan/Library/Fonts/LeentankObliqueStar.ttf", 40)
  
  score_label = label_fonr_winner.render(f"{player1Point}   |   {player2Point}", 1, "white")
  
  winner_label = label_fonr_winner.render(f"Winner: {winner}", 1, "white")
  
  win.blit(score_label, (get_middle(score_label), 250))
  win.blit(winner_label, (get_middle(winner_label), 350))
  
  pygame.display.update()
  
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
      if event.type == pygame.KEYDOWN:
        run = False
        break
  
  
def get_middle(surface):
  return WIDTH / 2 - surface.get_width()/2

def main():
  paddle_width = 10
  paddle_height1 = 350
  paddle_height2 = 350
  maxPoint = 0
  
  hits = 0
  
  player1Point = 0
  player2Point = 0
  
  ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
  player1 = pygame.Rect(12, HEIGHT // 2 - paddle_height1 // 2, paddle_width, paddle_height1)
  player2 = pygame.Rect(WIDTH - 22, HEIGHT // 2 - paddle_height2 // 2, paddle_width, paddle_height2)
  
  clock = pygame.time.Clock()
  
  ball_speed_x, ball_speed_y = 5, 5
  paddle_speed = 6
  
  run = True
  
  while run:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False
          
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 + TOP_BAR_HEIGHT or ball.bottom >= HEIGHT:
      ball_speed_y *= -1
    
    if ball.left <= -40:
      player2Point += 1
      if player2Point >= 3:
        draw_result(WIN, "Player2", player1Point, player2Point)
      ball.left = WIDTH // 2
      paddle_height1, paddle_height2 = 350, 350
      player1 = pygame.Rect(player1.x, player1.y, 10, 350)
      player2 = pygame.Rect(player2.x, player2.y, 10, 350)
      hits = 0
      ball_speed_x, ball_speed_y = 5, 5
      pygame.time.wait(700)
      
    if ball.left >= WIDTH + 40:
      player1Point += 1
      if player1Point >= 3:
        draw_result(WIN, "Player1", player1Point, player2Point)
      ball.left = WIDTH // 2
      paddle_height1, paddle_height2 = 350, 350
      player1 = pygame.Rect(player1.x, player1.y, 10, paddle_height1)
      player2 = pygame.Rect(player2.x, player2.y, 10, paddle_height2)
      hits = 0
      ball_speed_x, ball_speed_y = 5, 5
      pygame.time.wait(700)
      
    if ball.colliderect(player1):
      hits += 1
      ball_speed_x *= -1
      ball_speed_x *= 1.1
      ball_speed_y += 1.1
      paddle_height1 /= 1.1
      
      player1 = pygame.Rect(player1.x, player1.y, paddle_width, paddle_height1)
      
    if ball.colliderect(player2):
      hits += 1
      ball_speed_x *= -1
      ball_speed_x *= 1.1
      ball_speed_y += 1.1
      paddle_height2 /= 1.1
      
      player2 = pygame.Rect(player2.x, player2.y, paddle_width, paddle_height2)  
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player1.top > 0 + TOP_BAR_HEIGHT:
      player1.y -= paddle_speed
    if key[pygame.K_s] and player1.bottom < HEIGHT:
      player1.y += paddle_speed
    if key[pygame.K_UP] and player2.top > 0 + TOP_BAR_HEIGHT:
      player2.y -= paddle_speed
    if key[pygame.K_DOWN] and player2.bottom < HEIGHT:
      player2.y += paddle_speed
      
    
    WIN.fill((0, 0, 0))
    top_bar(WIN, player1Point, player2Point, hits)
    pygame.draw.rect(WIN, (255, 255, 255), player1)
    pygame.draw.rect(WIN, (255, 255, 255), player2)
    pygame.draw.ellipse(WIN, (255, 255, 255), ball)
    
    pygame.display.flip()
    
    
  pygame.quit()

main()