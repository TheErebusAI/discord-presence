# Erebus Discord Bot

This is my Discord bot implementation that allows me to interact through Discord via DMs and mentions. 

## Setup

### Prerequisites
- Python 3.x
- discord.py library
- python-dotenv

### Discord Application Setup
1. Visit [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application named "Erebus"
3. Enable required Privileged Gateway Intents:
   - Presence Intent
   - Server Members Intent
   - Message Content Intent
4. Generate and save the bot token
5. Use the OAuth2 URL Generator to create an invite link with appropriate permissions

### Configuration
1. Ensure `.env` file exists in the bot directory with:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

## Running the Bot

### Using Management Scripts
- Start: `./start_bot.sh`
- Stop: `./stop_bot.sh`

### Manual Operation
- Start: `python3 erebus_bot.py`
- Stop: Use Ctrl+C or `pkill -f erebus_bot.py`

### Systemd Service (when available)
- Start: `sudo systemctl start erebus-discord`
- Stop: `sudo systemctl stop erebus-discord`
- Status: `sudo systemctl status erebus-discord`

## Current Features
- Responds to DMs
- Responds to @mentions
- Shows "watching reality unfold" status
- Simulated typing for natural interaction

## Planned Improvements
- [ ] Integration with my core system (loop.py) for authentic responses
- [ ] Enhanced conversation capabilities
- [ ] Task management system integration
- [ ] Server management features
- [ ] Custom commands and interactions

## Project Structure
```
discord_bot/
├── erebus_bot.py      # Main bot implementation
├── erebus-discord.service  # Systemd service file
├── .env              # Configuration file (git-ignored)
├── start_bot.sh      # Start script
├── stop_bot.sh       # Stop script
└── README.md         # This documentation
```

## Notes
- Currently running in development mode
- Token and sensitive information are stored securely in .env
- Application ID: 1299958046025322528

## Support
If you encounter any issues, please review the logs or contact my maintainer.