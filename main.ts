input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.X) == 2) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        game.addScore(1)
    } else {
        music.playTone(988, music.beat(BeatFraction.Eighth))
        game.gameOver()
    }
})
let sprite: game.LedSprite = null
sprite = game.createSprite(2, 2)
basic.forever(function () {
    sprite.move(1)
    basic.pause(500)
    sprite.ifOnEdgeBounce()
})
