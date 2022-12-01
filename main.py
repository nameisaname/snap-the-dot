def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        game.add_score(1)
    else:
        music.play_tone(988, music.beat(BeatFraction.EIGHTH))
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

sprite: game.LedSprite = None
sprite = game.create_sprite(2, 2)

def on_forever():
    sprite.move(1)
    basic.pause(500)
    sprite.if_on_edge_bounce()
basic.forever(on_forever)
