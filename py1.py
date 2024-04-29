import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Display duration in seconds
    )

if __name__ == "__main__":
    title = "Whatsapp Notification"
    message = "This is a dummy notification."

    send_notification(title, message)