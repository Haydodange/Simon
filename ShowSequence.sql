BEGIN ShowSequence
    FOR each value in displaySequence
        IF x == 0 THEN
            Turn on red LED
        ELSE IF x == 1 THEN
            Turn on green LED
        ELSE IF x == 2 THEN
            Turn on blue LED
        ELSE IF x == 3 THEN
            Turn on yellow LED
        Turn off all LED
        END IF
    NEXT
END