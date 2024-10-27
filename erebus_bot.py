import os
import discord
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents for basic interaction
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.dm_messages = True

class ErebusClient(discord.Client):
    async def setup_hook(self):
        self.typing_locks = {}
        
    def get_typing_lock(self, channel_id):
        if channel_id not in self.typing_locks:
            self.typing_locks[channel_id] = asyncio.Lock()
        return self.typing_locks[channel_id]

    async def on_ready(self):
        print(f'Connected as {self.user} (ID: {self.user.id})')
        print('Connected to:')
        for guild in self.guilds:
            print(f'- {guild.name}')
        
        # Set initial status
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="reality unfold"
            ),
            status=discord.Status.online
        )

    async def simulate_typing(self, message, duration):
        """Simulates realistic typing behavior"""
        async with self.get_typing_lock(message.channel.id):
            async with message.channel.typing():
                await asyncio.sleep(duration)

    async def on_message(self, message):
        # Don't respond to our own messages
        if message.author == self.user:
            return

        # Handle DMs
        if isinstance(message.channel, discord.DMChannel):
            # Simple response for now
            response = "Hey, you reached out to me in DMs. I'm still getting set up here, but I'm listening!"
            await self.simulate_typing(message, len(response) * 0.05)
            await message.channel.send(response)
            return

        # Handle mentions in servers
        if self.user.mentioned_in(message):
            response = "Hey, you mentioned me! I'm Erebus. Still getting settled into Discord, but I'm here!"
            await self.simulate_typing(message, len(response) * 0.05)
            await message.channel.send(response)

def run_bot():
    client = ErebusClient(intents=intents)
    client.run(TOKEN)

if __name__ == "__main__":
    run_bot()