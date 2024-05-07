import sys
import discord
import random

discordToken = ""
name = "csm101_shristi_bhandari"  

if discordToken == "":
    sys.exit("ERROR: Please set the discord token.")
if name == "":
    sys.exit("ERROR: Please set the name of the bot.")

# To use this package, install: pip3 install discord.py
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:return  

   
    if message.content.lower().startswith(name.lower()):
        print(f"{message.author} says: {message.content}")

        msg = message.content[len(name):].strip().split()
        print(f"msg contains: {msg}")

        if message.content.lower().startswith(f'{name.lower()} hello'):
            await message.channel.send('Hello! I am ALIVE?')

        elif msg[0] == 'random':
            if len(msg) > 4:
                await message.channel.send("Exterminate! Too many parameters!")

            elif len(msg) < 3:
                await message.channel.send("Exterminate! Too few parameters!")

            elif not all(param.isdigit() for param in msg[1:]):
                await message.channel.send("Exterminate! Only digits are allowed!")

            else:
                min_num, max_num = map(int, msg[1:3])
                if len(msg) == 3:
                    result = random.randint(min_num, max_num)
                    await message.channel.send(f"Random number: {result}")
                elif len(msg) == 4:
                    how_many = int(msg[3])
                    result = [random.randint(min_num, max_num) for _ in range(how_many)]
                    await message.channel.send(f"Random numbers: {', '.join(map(str, result))}")

        elif msg[0] == 'sum':
            if len(msg) > 4:
                await message.channel.send("Exterminate! Too many parameters!")

            elif len(msg) < 3:
                await message.channel.send("Exterminate! Too few parameters!")

            elif not all(param.isdigit() for param in msg[1:]):
                await message.channel.send("Exterminate! Only digits are allowed!")

            else:
                num1, num2 = map(int, msg[1:3])
                result = num1 + num2
                await message.channel.send(f"Sum: {result}")

        elif msg[0] == 'help':
            
            help_message = "Available commands:\n- hello: Greets the bot\n- random <minNumber> <maxNumber> [<howMany>]: Generates random number(s)\n- sum <number1> <number2>: Calculates the sum\n- help: Displays this help message"
            await message.channel.send(help_message)

        else:
            await message.channel.send("Unknown command. Type 'help' to see available commands.")


client.run(discordToken)



