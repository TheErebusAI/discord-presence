#!/bin/bash

# Find and kill the bot process
if pgrep -f "python3 erebus_bot.py" > /dev/null; then
    pkill -f "python3 erebus_bot.py"
    echo "Bot stopped successfully!"
else
    echo "Bot was not running."
fi