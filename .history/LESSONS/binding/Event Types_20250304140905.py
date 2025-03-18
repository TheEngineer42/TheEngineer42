"""
In Tkinter, events are always written inside < > (angle brackets).

For example:

<KeyPress> → Any key press
<Button-1> → Left mouse click
<Motion> → Mouse movement

root.bind("<Motion>", some_function)



🟢 Widget Activation & Deactivation
✅ Activate → Triggered when a widget (like a button) becomes active (e.g., selected in a listbox).
✅ Deactivate → Triggered when a widget becomes inactive (loses selection).

🖱️ Mouse Events
✅ MouseWheel → Triggered when you scroll the mouse wheel.
✅ ButtonPress → Triggered when any mouse button is pressed down.
✅ ButtonRelease → Triggered when a pressed mouse button is released.
✅ Motion → Triggered when the mouse is moved over the widget.

⌨️ Keyboard Events
✅ KeyPress → Triggered when a key is pressed down (<KeyPress-a> for "A", <KeyPress-Return> for Enter).
✅ KeyRelease → Triggered when a key is released after pressing.

📌 Window & Widget Events
✅ Configure → Triggered when a widget or window changes size or position.
✅ Destroy → Triggered when a widget or window is closed.

🔄 Focus & Hover Events
✅ FocusIn → Triggered when a widget gains focus (e.g., clicking inside an Entry box).
✅ FocusOut → Triggered when a widget loses focus (e.g., clicking outside an Entry box).
✅ Enter → Triggered when the mouse enters a widget area.
✅ Leave → Triggered when the mouse leaves a widget area.

🖱️ Mouse Button Events
✅ Button-1 → Left mouse button click.
✅ Button-2 → Middle mouse button click.
✅ Button-3 → Right mouse button click.
✅ Double-Button-1 → Double-click with the left mouse button.
✅ Motion → Tracks mouse movement inside a widget.


"""

"""
🟢 Widget Activation & Deactivation
✅ Activate → 1
✅ Deactivate → 2

🖱️ Mouse Events
✅ MouseWheel → 38 (on Windows) / 37 (on macOS) / 31 (on Linux)
✅ ButtonPress → 4
✅ ButtonRelease → 5
✅ Motion → 6

⌨️ Keyboard Events
✅ KeyPress → 2
✅ KeyRelease → 3

📌 Window & Widget Events
✅ Configure → 22
✅ Destroy → 17

🔄 Focus & Hover Events
✅ FocusIn → 9
✅ FocusOut → 10
✅ Enter → 7
✅ Leave → 8

🖱️ Mouse Button Events
✅ Button-1 (Left Click) → 4
✅ Button-2 (Middle Click) → 4
✅ Button-3 (Right Click) → 4
✅ Double-Button-1 → No specific integer (handled as two consecutive `Button-1` clicks)
✅ Motion → 6
"""