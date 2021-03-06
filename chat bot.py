import datetime
import wikipedia
import webbrowser
import pyjokes
import psutil


def time():
    t = datetime.datetime.now().strftime("%H:%M")
    print(f"Time:{t}")


def battery():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    print(f"CPU : {usage}\n Battery : {battery}")


def joke():
    j = pyjokes.get_jokes()
    print(j)


def wiki(command):
    command = command.replace("wiki", '')
    command = command.replace("wikipedia", '')
    result = wikipedia.summary(command, sentences=2)
    print(result)


def reminder():
    r = input("What you want me to remind?")
    rem = open("reminder.txt", "a")
    rem.write(f"\n {r}")
    rem.close()


def reminder1():
    reminder_file = open("reminder.txt", "r")
    y=reminder_file.read()
    print(y)
    reminder_file.close()

if __name__ == '__main__':

    while True:
        command = input("Input:\n")
        if 'time' == command:
            time()

        elif 'battery' in command or 'cpu' in command:
            battery()

        elif 'jokes' in command or 'joke' in command:
            joke()

        elif 'wikipedia' in command or 'wiki' in command:
            wiki(command)

        elif 'google' in command or 'open google' in command:
            webbrowser.open('google.com')

        elif 'open' in command:
            website = input("Enter your website here: ")
            webbrowser.open(website)

        elif 'reminder' in command  or 'remind' in  command:
            reminder()

        elif 'xyz' in command:
            reminder1()

        else:
            print("Sorry I'm not functioned for this program")