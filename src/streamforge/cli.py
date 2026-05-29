import uvicorn


def main() -> None:
    uvicorn.run(
        "streamforge.main:app",
        host="0.0.0.0",
        port=8001,
        workers=1,
        log_level="info",
    )
    
if __name__ == "__main__":
    main()