import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎵 Simple Music Player")

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]  # Replace with your own files
current_index = 0
is_paused = False

def load_and_play(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    print(f"Now playing: {playlist[index]}")

load_and_play(current_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_paused = True
                    print("Paused")
                elif is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                    print("Resumed")
                else:
                    load_and_play(current_index)

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_paused = False
                print("Stopped")

            elif event.key == pygame.K_n:
                current_index = (current_index + 1) % len(playlist)
                load_and_play(current_index)

            elif event.key == pygame.K_p:
                current_index = (current_index - 1) % len(playlist)
                load_and_play(current_index)

    pygame.display.flip()

# Quit properly
pygame.quit()
