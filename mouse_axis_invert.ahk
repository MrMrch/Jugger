;Requires AutoHotkey v2.0



ToggleInvertedMouse(*) {
    static inverted_mouse := False
    if not inverted_mouse {
        global previous_x
        global previous_y
        MouseGetPos &previous_x, &previous_y
        SetTimer InvertMouseMovement, 10
        inverted_mouse := True
    }
    else {
        SetTimer InvertMouseMovement, 0
        inverted_mouse := False
    }
}

InvertMouseMovement() {
    global previous_x
    global previous_y
    MouseGetPos &current_x, &current_y

    x_change := current_x - previous_x
    y_change := current_y - previous_y

    if x_change or y_change {
        MouseMove -2 * x_change, -2 * y_change, 0, "R"
    }

    previous_x := current_x - 2 * x_change
    previous_y := current_y - 2 * y_change
}


 

ToggleInvertedMouse()		;inverte direzione mouse 10 secondi


#SingleInstance Force

<^Esc::ExitApp




