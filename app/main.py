from app.application import Application, create_app


def main() -> None:
    app: Application = create_app()

    app.run()


if __name__ == "__main__":
    main()
