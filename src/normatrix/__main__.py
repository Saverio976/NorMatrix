try:
    from normatrix.source.main import main
except ModuleNotFoundError:
    from src.normatrix.source.main import main

main()
