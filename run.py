import asyncio
from src.main import main

if __name__ == "__main__":
    # 🔑 Fix Windows shutdown bug
    if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
