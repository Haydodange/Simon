BEGIN ShowSequence
    FOR each value in displaySequence
        IF x == 0 THEN
            Turn on red LED
            Play sound for red
        ELSE IF x == 1 THEN
            Turn on green LED
            Play sound for green
        ELSE IF x == 2 THEN
            Turn on blue LED
            Play sound for blue
        ELSE IF x == 3 THEN
            Turn on yellow LED
            Play sound for yellow
        Turn off all LED
        Turn off Piezo
        END IF
    NEXT
END