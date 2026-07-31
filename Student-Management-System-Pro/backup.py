import threading
import time
from export_json import export_json

def auto_backup():
    while True:
        export_json()
        print("Backup Completed")
        time.sleep(30)

backup_thread = threading.Thread(target=auto_backup)
backup_thread.daemon = True