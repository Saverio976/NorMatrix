try:
    from normatrix.source.main import main
except ModuleNotFoundError:
    from normatrix.normatrix.source.main import main

main()
