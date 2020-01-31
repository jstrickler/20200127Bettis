#!/usr/bin/env python
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time

path_to_watch = "."
patterns = "*"

class MyHandler(PatternMatchingEventHandler):

    def on_created(self, event):
        print("Created", event.src_path)

    def on_deleted(self, event):
        print("Deleted", event.src_path)

    def on_modified(self, event):
        print("Modified", event.src_path)

    def on_moved(self, event):
        print("Moved", event.src_path, "to", event.dest_path)

  # on_created on_deleted on_modified on_moved on_any_event

event_handler = MyHandler(patterns=patterns, ignore_directories=True)

observer = Observer()
observer.schedule(event_handler, path_to_watch, recursive=False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
