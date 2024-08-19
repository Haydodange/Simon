BEGIN GetSequence
    button1 = 0
    button2 = 1
    button3 = 2
    button4 = 3

    GET order buttons pressed
    APPEND order
    
    IF order == sequence THEN
        next level
    ELSE THEN
        you lose
    END IF

END
