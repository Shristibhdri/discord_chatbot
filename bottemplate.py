
import sys
import discord
import random

discordToken = ""  # Your bot token here (https://discord.com/developers/applications/ and tab Bot -> Token -> Reset Token -> Copy the token here)
name = ""  # Your bot name here

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
    if message.author == client.user:
        return  # We don't want to reply to ourselves

    # RULE: To not flood the channel with responses from multiple bots,
    # we only respond to messages that start with our name
    if message.content.lower().startswith(name.lower()):
        print(f"{message.author} says: {message.content}")

        msg = message.content[len(name):].strip().split()
        print(f"msg contains: {msg}")

        if message.content.startswith(f'{name} hello'):
            await message.channel.send('Hello! I am ALIVE?')

        elif msg[0] == 'random':
            if len(msg) == 3:
                min_num, max_num = map(int, msg[1:])
                result = random.randint(min_num, max_num)
                await message.channel.send(f"Random number: {result}")

            elif len(msg) == 4:
                min_num, max_num, how_many = map(int, msg[1:])
                result = [random.randint(min_num, max_num) for _ in range(how_many)]
                await message.channel.send(f"Random numbers: {', '.join(map(str, result))}")

            else:
                await message.channel.send("Invalid random command. Please use 'random <minNumber> <maxNumber>' or 'random <minNumber> <maxNumber> <howMany>'.")

        elif msg[0] == 'sum':
            if len(msg) == 3:
                num1, num2 = map(int, msg[1:])
                result = num1 + num2
                await message.channel.send(f"Sum: {result}")

            else:
                await message.channel.send("Invalid sum command. Please use 'sum <number1> <number2>'.")

        elif msg[0] == 'help':
            # Display help message
            help_message = "Available commands:\n- hello: Greets the bot\n- random <minNumber> <maxNumber> [<howMany>]: Generates random number(s)\n- sum <number1> <number2>: Calculates the sum\n- help: Displays this help message"
            await message.channel.send(help_message)

        else:
            await message.channel.send("Unknown command. Type 'help' to see available commands.")


client.run(discordToken)
