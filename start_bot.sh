#!/bin/bash

# Check if bot is already running
if pgrep -f "python3 erebus_bot.py" > /dev/null; then
    echo "Bot is already running!"
    exit 1
fi

# Start the bot
cd "$(dirname "$0")"
python3 erebus_bot.py &
echo "Bot started! PID: $!"