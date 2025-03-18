"""
In Tkinter, events are always written inside < > (angle brackets).

For example:

<KeyPress> → Any key press
<Button-1> → Left mouse click
<Motion> → Mouse movement

root.bind("<Motion>", some_function)



🔵 Basic Events
✅ Activate → When a widget (like a button) becomes active (clicked or focused).
✅ Deactivate → When a widget becomes inactive (loses focus).

🖱️ Mouse Events
✅ MouseWheel → Triggered when you scroll the mouse wheel.
✅ ButtonPress → When any mouse button is clicked (<Button-1> for left-click, <Button-2> for middle, <Button-3> for right).
✅ ButtonRelease → When the pressed mouse button is released.
✅ Motion → When the mouse moves over a widget (<Motion> for continuous tracking).

⌨️ Keyboard Events
✅ KeyPress → When a key is pressed (<KeyPress-a> for "A", <KeyPress-Return> for Enter).
✅ KeyRelease → When a key is released.

📌 Window & Widget Events
✅ Configure → When a widget or window is resized or moved.
✅ Destroy → When a widget or the main window is closed.

🔄 Focus & Hover Events
✅ FocusIn → When a widget gains focus (e.g., clicking inside an Entry box).
✅ FocusOut → When a widget loses focus (e.g., clicking outside an Entry box).
✅ Enter → When the mouse enters a widget area.
✅ Leave → When the mouse leaves a widget area.


"""

